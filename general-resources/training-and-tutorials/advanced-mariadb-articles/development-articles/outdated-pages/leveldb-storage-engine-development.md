
# LevelDB Storage Engine Development

Items that are considered for development of [LevelDB Storage Engine](leveldb.md) after [Milestone #1](leveldb-storage-engine-ms1.md) is complete.



## [DONE] AUTO_INCREMENT


See [MDEV-4110](https://jira.mariadb.org/browse/MDEV-4110).


## [DONE] Use table/index numbers as prefixes


(The Jira entry for this task is [MDEV-4122](https://jira.mariadb.org/browse/MDEV-4122))


Currently, keys are prefixed with


```
dbname.table_name$INDEX_NO\0
```

where INDEX_NO is one byte with the number of index, counting from 1.


With this:


* Renaming a table is very slow. This is a problem, because ALTER TABLE assumes table rename is a fast, O(1) operation.
* DROP TABLE needs to delete every row, it is not possible to do the deletions later in the background. If one wants to run `DROP TABLE t; CREATE TABLE t; ...` then CREATE TABLE will have to wait until DROP has truly finished.
* Dropping a table and creating another table with a different DDL causes deleted records of the first table to be compared with DDL of the second. This particular issue (but not others) can be avoided if we switch to keys that are compared with memcmp().


### Proposed solution


LevelDB keys should look like this (for both table records and secondary indexes):


```
[indexnr] key_data
```

where `indexnr` is an index number, which is assigned sequentially, and is not a function of dbname.tablename.


The "data dictionary" will need to have two mappings:


```
index2ddl
  index_no -> index_ddl_data

table2indexes
  dbname.tablename -> (index_no, index_no, ...)
```

index2ddl will be used to make comparisons when LevelDB requests them.


table2indexes will tell us what to read when SQL layer requests to read (or write) records for dbname.tablename.


DROP TABLE will remove table's entry from table2indexes. Actual record deletion can be done in the background. index2ddl entries can remain forever, so we will not face potential crashes when LevelDB tries to compare long-deleted records.


RENAME TABLE will modify the entry in table2indexes. This is an O(1) operation.


TRUNCATE TABLE will remove the entry in table2indexes and add another one, with different values of index_no. Actual row deletion can be done in the background.


## memcmp'able keys


Current way to compare keys (find the table DDL in the hash, then use ha_key_cmp()) is likely to be slow.


The advantages of current scheme are


* It is possible to restore field values from index tuple, which means index-only scans are always possible.
* Keys are "packed" - for example, endspace is removed from CHAR(n) fields.


*not that these matter much. In the benchmark of interest, most of indexed values are integers. There is a VARCHAR column with charset=latin1*.


If we switched to keys that were comparable with memcmp(), one could expect comparisons to become faster.


### Making keys comparable


#### Falcon SE


Falcon did use memcmp() to compare index tuples. Looking into the source (it is available for download still), one can see the comparison being somewhere around:


```
void Index::makeKey(Field *field, Value *value, int segment, IndexKey *indexKey, bool highKey)
void Index::makeMultiSegmentKey(int count, Value **values, IndexKey *indexKey, bool highKey)
...
void IndexKey::appendNumber(double number)
^^ makes double numbers memcmp'able...
```

unfortunately, there is no single, isolated part of code that we could copy. (Or may be there is, but we were not able to find it yet).


#### Field::make_sort_key


Found this in the source:


```
/**
    Writes a copy of the current value in the record buffer, suitable for
    sorting using byte-by-byte comparison. Integers are always in big-endian
    regardless of hardware architecture. At most length bytes are written
    into the buffer.

    @param buff The buffer, assumed to be at least length bytes.

    @param length Number of bytes to write.
  */
  virtual void make_sort_key(uchar *buff, uint length) = 0;
```

Looks like this is exactly what we needed?


## Fewer mutexes


Current code initializes/uses a mutex for every row lock taken. According to Monty, having lots of mutexes that are spread out all over the memory will slow things down, and we should switch to fewer mutexes (this is a basic description).


Maybe, it makes sense to use mutex/condition from waiter's struct st_my_thread_var.


## Not included in MS2


### Improve AUTO_INCREMENT handling


If there is no replication, then nothing is missing? The effect of


```
ALTER TABLE tbl AUTO_INCREMENT=nnn
```

does not survive the server restart for leveldb tables. But neither it does for InnoDB (at least, when replication is not in use).


To our best knowledge, AUTO_INCREMENT handling is adequate for non-replication use cases.


### Partial indexes


Currently, leveldb doesn't support indexes that cover a part of the column, e.g.


```
CREATE TABLE t1 (
 pk int primary key,
 col1 varchar(100),
 INDEX i1 (col1(10))
);
```

Adding them is just a question of careful coding/testing.


CC BY-SA / Gnu FDL

