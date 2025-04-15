
# LevelDB Storage Engine MS2


## Remove the need for a second database


MS1 code needs to use two databases, because


* `<code>leveldb</code>` database uses type-aware key comparison. This means, one must have knowledge about types of values in indexes before the database can be opened.


* `<code>leveldb-ddl</code>` stores information about 

  * datatypes used by various indexes.
  * Mapping from `<code>dbname.tablename.index_no</code>` to `<code>index_number</code>`.


The database itself uses default key comparison function, so one can open it without any knowledge.


It is possible to switch to having one database, if the keys can use the default key comparison function, memcmp(). The database will store


* table/index data
* Mapping from `<code>dbname.tablename.index_no</code>` to `<code>index_number</code>`.


It seems, it is possible to convert MySQL field values into values comparable with memcmp() by using Field::make_sort_key() function.


### Index-only scans


Index-only scans require that it is possible to restore key value from its memcmp()'able form.


In general, it is not possible. For some particular datatypes, it is possible. We want to target the following types:


* `<code>INT</code>`, `<code>BIGINT</code>`, `<code>TINYINT</code>`, and their `<code>UNSIGNED</code>` variants (i.e., all INT-based types)
* `<code>CHAR(n) COLLATE latin1_bin</code>`, `<code>VARCHAR(n) COLLATE latin1_bin</code>`, possibly support `<code>utf8_bin</code>`.


#### INT-based types


For INT-based types, mem-comparable form is the integer stored in most-significant-bytes-first order. For SIGNED types, one needs to make negative values precede positive ones (memcmp() assumes all bytes are unsigned). This can be achieved by adding MAX_VALUE/2 to the number.


It is apparent that one can restore integer values back from their mem-comparable form.


#### String-based types


For string-based types, getting the value back from its mem-comparable form is harder.


##### Problem#1: case-insensitivity


For case-insensitive collations, conversion to mem-comparable form is, roughly speaking, conversion of all characters to upper case (it's actually more complex, but that's the idea)


For example, for column='foo' and column='FOO' the mem-comparable form is 'FOO', and there is no way to get the original case back.


##### Problem#2: VARCHAR and end-spaces


Consider a [VAR]CHAR(n) type. The mem-comparable form must have the same length for all values. If some values have different length, we won't be able to support multi-part keys.


In MySQL charset functions, mem-comparable form does have a fixed length. Fixed length is achieved by end-padding the value with spaces (more precisely, with mem-comparable images of spaces). This raises a question of, how do we get rid of these spaces when we're decoding the value back?


For `<code>CHAR(n)</code>` fields, the problem doesn't exist, because MySQL strips all trailing spaces:


```
create table t10 (a char(10) primary key); 
insert into t10 values ('abc   ');
select a, length(a) from t10;
+-----+-----------+
| a   | length(a) |
+-----+-----------+
| abc |         3 |
+-----+-----------+
```

(@@sql_mode has a PAD_CHAR_TO_FULL_LENGTH flag which will make MySQL to pad strings with as many spaces as possible instead of stripping. But either way, we don't have to care about how many end-spaces are in a CHAR(n) value).


For VARCHAR fields, end-spaces are not removed:


```
create table t11 (a varchar(10) primary key);
insert into t11 values ('abc   ');
select a, length(a) from t11;
+--------+-----------+
| a      | length(a) |
+--------+-----------+
| abc    |         6 |
+--------+-----------+
```

When we try to decode a string from its mem-comparable form, we will not know how many end-spaces were in the original value. We need to store the length somewhere.


##### Solution for case-insensitivity


We will avoid the problem of upper-casing by supporting index-only reads when used collations do not map two different characters to the same mem-comparable value. The following collations are ok:


* `<code>BINARY</code>` - characters are not transformed
* `<code>latin1_bin</code>` - characters are not transformed
* `<code>utf8_bin</code>` - characters are transformed into 2-byte images with `<code>my_utf8_uni()</code>` and can be restored with `<code>my_uni_utf8()</code>`. The functions are stored in `<code>cs->cset->mb_wc</code>` and `<code>cs->cset->wc_mb</code>`.
* `<code>utf8mb4_bin</code>` - characters are transformed into 3-byte images with `<code>my_mb_wc_utf8mb4()</code>` and can be restored with `<code>my_wc_mb_utf8mb4()</code>`


##### Solution for end-spaces


We need to store the original length of the value somewhere. There is no way we could put it into a mem-comparable form. If we put it there, we would have


```
memcmp(mem_comparable('abc'), mem_comparable('abc  '), len) != 0
```

which would make equal values be compared as non equal.


The solution is: don't store length in leveldb key.


* For PRIMARY KEY, length is stored in leveldb's Value (we have entire table->record[0] there, with special encoding for blobs).
* For secondary indexes, we will store length in the leveldb's Value (which is currently empty).


## Fix CANT-SEE-OWN-CHANGES


The property is described at [leveldb-storage-engine-ms1](leveldb-storage-engine-ms1.md) page. A solution is also described there:


 After MS1, LevelDB SE will make sure that CANT-SEE-OWN changes is not observed. It will use the following approach:

* keep track of what records have been modified by this transaction in a buffer $R.
* If SQL layer makes a request to read a row, then

  * Consult $R if the record was INSERTed. If yes, return what was inserted.
  * Consult $R if the record was modified. if yes, return what was recorded as the result of modification
  * Consult $R if the record was deleted. If yes, return "record not found".
  * Finally, try reading the row from the LevelDB.




Note: this allows us to keep only the last update if the transaction has made multiple updates in the same row. (as long as we didn't use to store both transaction and statement's changes together. In that case, we need to keep both transaction's and statement's changes)


## More test coverage


Adopt a storage-engine-independent testsuite to be used together with leveldb.


## Statement rollback inside a transaction


A truly transactional MySQL engine needs to support two kinds of rollback


1. Rollback a statement
1. Rollback a transaction


If a statement fails inside a transaction, the engine will need to rollback the statement, but not the transaction. Currently, leveldb SE is unable to do so, because transaction's changes and statement's changes are stored in a single `<code>leveldb::WriteBatch</code>` object.


The solution will be to keep transaction's changes and statement's changes separate, and put statement's changes into transaction's changes on statement end.


Another way: when we maintain a hashtable of changes, remember query_id of every change. If we need to roll back a statement, go through the changes and remove those that have query_id equal to the last query (TODO: is statement the same as query here, or not?)


## Fix the build process


[MDEV-4154](https://jira.mariadb.org/browse/MDEV-4154): Currently, leveldb SE hardcodes paths to leveldb library. Lift this limitation.


## @@leveldb_max_row_locks


Transaction locks are held in memory. Hence, there is an idea: prevent transactions from getting too big - have a variable that explicitly limits how many locks a transaction can take. (there was a similar variable in BDB storage engine). If a transaction attempts to take more locks than allowed, an error will be returned.


## Tasks


### Remove the need for a second database


* Store mem-comparable values as keys (no index-only support)
* Switch rowlock table to use the same hash value?


### Index-only scans


* Analyze index definition and set HA_KEYREAD_ONLY only when appropriate
* Unpack functions for integer columns
* Unpack function for CHAR(n)
* Storage an unpack for VARCHAR(n)


### Fix CANT-SEE-OWN-CHANGES


* Maintain a hash table of changes made by the transaction
* Have read functions consult the hashtable before reading actual data


### Statement rollback inside a transaction


* Maintain transaction's changes and last statement's changes separately.

  * Roll back the right set of changes on statement/transaction abort.


### More test coverage


* Adopt the engine-independent testsuite to be used with leveldb


## Misc


* (from skype discussion)_Currently max. auto_increment value is loaded every time a TABLE is opened. Make it to be loaded only when TABLE_SHARE is opened.

