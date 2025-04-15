
# LevelDB Storage Engine MS1

This page describes what will be implemented for milestone#1 of [LevelDB Storage Engine](leveldb-storage-engine-ms2.md). *For development after MS1, see [LevelDB Storage Engine Development](leveldb-storage-engine-development.md)*



# Feature Description


## How the data is stored in LevelDB


### One leveldb instance


We will use one LevelDB instance for mysqld process. LevelDB keys will be 
prefixed with 'dbname.table_name.PRIMARY' for the table itself, and
'dbname.table_name.index_name' for the secondary indexes. This allows to 
store arbitrary number of tables/indexes in one LevelDB instance.


### Data encoding


We will rely on LevelDB's compression to make the storage compact.
Data that goes into LevelDB's key will be stored in KeyTupleFormat (which 
allows mysql's lookup/index ordering functions to work).


Data that goes into LevelDB's value will be stored in table->record[0] format, 
except blobs. (Blobs will require special storage convention because they 
store a char* pointer in table->record[0]).


We will need to support blobs because table `<code>nodetable</code>` has a `<code>mediumtext</code>` field.


### Secondary indexes


Non-unique secondary indexes will be supported.


LevelDB stores {KEY->VALUE} mappings. Non-unique index will need to have some unique values for KEY. This can be arranged by using this mapping:


```
KEY = {index_columns, primary_key_columns}.   
VALUE = {nothing}
```

Using primary key as suffix will make DB::Get() useless. Instead, we will have to do lookups with:


```
get(secondary_index_key_val)
{
  open cursor for (secondary_index_key_val)
  read the first record
  if (record > secondary_index_key_val)
    return NOT_FOUND;
  else
    return FOUND;
}
```

*TODO: we will not support unique secondary indexes in MS1. ALTER/CREATE TABLE statements attempting to add a unique index will fail. Is this ok?*


## Concurrency handling


We will use what was discussed in the "Pessimistic locking proposal".


Basic idea is: LevelDB's operations do blind overwrites. In order to make sure we're not overwriting anything, we will use this pattern:


```
acqure record lock;
  read;
  modify as necessary;
  write;
  release record lock;
```

record locks can be obtained for {table_name, primary_key}. Locks are
exclusive, for a given record, only one lock can obtained at a time. A lock can
be obtained when its record doesn't exist (see INSERT below)


### C1. UPDATE


UPDATE will use the above scheme. It will get row locks for the keys it is
reading in order to prevent concurrent updates.


### C.2 INSERT


INSERT will use a row lock to make sure the record of interest does not exist.


### C.3 DELETE


If a DELETE statement has a form of


```
DELETE FROM tbl WHERE tbl.primary_key=const
```

then it theoretically can be translated into a DB::Delete() call, that is, into a write-without-read. In other cases, we will need to do reads and put locks on the rows that we want to delete.


MS1 will only implement the variant with locking DELETE.


### C.4 SELECT


SELECT statements will use a read snapshot. They will not put (or check) whether there are any locks for records they are reading. This is similar to the definition of `<code>read-committed</code>` isolation level.


We will also support `<code>SELECT FOR UPDATE</code>`. In this mode, the read records will be locked with a write lock until the end of the transaction.


### C.5 Locking mechanism


As specified in previous sections, we will be employing locks on the values of {dbname, tablename, primary_key_value}. Locks will be exclusive: only one transaction can hold a lock at a time.


Locks are acquired one-by-one, which allows for deadlocks. There will be no deadlock detection or deadlock prevention systems. Instead, lock waits will time out after @@leveldb_lock_wait_timeout milliseconds. When @@leveldb_lock_wait_timeout==0, lock system will not wait at all, attempt to acquire a lock that's occupied will result in an immediate transaction abort.


Locks will be stored in a highly-concurrent hashtable. Current candidate for it is mysys/lf_hash.


### C.6 Applying transaction changes


The changes made by transaction will be accumulated as a LevelDB batch operation, and applied at transaction commit. This has a consequence:


**the transaction is unable to see its own changes until it commits**


We'll call the above CANT-SEE-OWN-CHANGES property. The property is contrary to the SQL's semantics. In SQL, one expects to see the changes they've made in preceding statements. However, the set of transactions we're targeting can live with CANT-SEE-OWN-CHANGES, so we'll live with the property for MS1.


After MS1, LevelDB SE will make sure that CANT-SEE-OWN changes is not observed. It will use the following approach:


* keep track of what records have been modified by this transaction in a buffer $R.
* If SQL layer makes a request to read a row, then

  * Consult $R if the record was INSERTed. If yes, return what was inserted.
  * Consult $R if the record was modified. if yes, return what was recorded to be the result of modification
  * Consult $R if the record was deleted. If yes, return "record not found".
  * Finally, try reading the row from the LevelDB.


## Table Access methods


MS1 will support:


* Full table scan.
* index lookups and range scans over primary and secondary indexes.


### Optimizer statistics


* Estimate of #records in the table will be obtained from DB::GetApproximateSizes() (see below for details)
* Estimate of #records-in-range will be obtained from DB::GetApproximateSizes()
* There is no acceptable estimate for #rec_per_key of secondary indexes (or for prefixes of the primary key). MS1 will perform some trivial guesswork.


Note: DB::GetApproximateSizes() returns amount of disk space occupied by the data. The number cannot be directly translated to #rows, because


* We do not always know average record length
* Disk data is compressed.


Because of this, optimizer will have very imprecise input. It is expected to be still sufficient for MS1.


## Write-optimized INSERTs


We will need to do fast bulk data loads. During the bulk load, writes-without-reads are ok: the user knows he's not overwriting data, he doesn't care about @@rows_affected.


These will be achieved as follows:


* there will be a thread-local @@leveldb_bulk_load variable.
* Its default value is FALSE.
* When it is set to true, INSERTS (which make ha_leveldb::write() calls) will work in bulk-loading mode.


Bulk-loading mode means:


* INSERTs will be done in batches of @@leveldb_bulk_load_size each
* INSERTs will take no locks, and do no-read-writes. In other words, they will silently overwrite data
* @@affected_rows will return the value that will show that all records were successfully inserted.


## What will not be supported


* Non-blocking schema changes will not be supported at all in the first milestone. All DDL-modifying operations will use pump all the data from the original table to the table with the new DDL.
* Binlog XA on the master will not be supported.
* Crash-proof slave will not be supported.
* Building server packages (*.rpm, *.deb, etc) will not be supported (leveldb dependency may be challenging).


## Other details


* The patch will be against mysql-5.6
* TODO: How to run DROP TABLE The only way we implement DROP TABLE is to delete record by record. The size of changes may become too big to be in RAM. If we split into multiple transactions, we'll have to handle crashes in the middle of DROP TABLE.
Q: can we avoid that for the first milestone?
* TODO: There is no efficient way to run TRUNCATE TABLE. Is this ok?
* TODO: In the above spec, nothing is said about max. transaction size. Is it ok not to have it for MS1?

