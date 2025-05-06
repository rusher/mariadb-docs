
# LevelDB Storage Engine

## Basic feature list


* single-statement transactions
* secondary indexes
* HANDLER implementation with extensions to support atomic multi-put (kind of like multi-statement transactions)
* binlog XA on the master to be crash safe
* crash-proof slave replication state
* (almost) non blocking schema change
* full test coverage via mysql-test-run
* hot backup
* possible options are to have LevelDB instance per mysqld, per schema or per table



## Implementation overview


### One leveldb instance


We consider using one LevelDB instance for mysqld process. LevelDB keys will be 
prefixed with 'dbname.table_name', 'dbname.table_name.index_name' (or their shorter equivalents). This will allow to store arbitrary number of tables/indexes in one
LevelDB instance.


### Transaction support


LevelDB supports


* read snapshots
* batch updates


when you have just those, there is no easy way to support full transactional
semantics in the way it is required from MySQL table engine.


If we limit ourselves to single-statement transactions which touch limited numbers of rows, they could be implemented as follows:


* updates done by the statement are accumulated in a batch
* if the statement is committed, the batch is applied. LevelDB guarantees this will be an atomic operation
* if the statement is rolled back, the batch is simply discarded.


(Note: the "Test implementation" uses exactly this approach. It presents itself to MySQL as a non-transactional engine which is able to roll back a statement)


(Note: According to Serg: Storage Engine API does not specify whether the changes made to table data should be immediately visible, or remain invisible until the end of the statement. Both kinds of behavior are allowed).


*TODO: what if two transactions attempt to make conflicting changes? Will one of them get a conflict? A: NO, because LevelDB's operations cannot get in conflict. Delete() means "delete if exists" and Put() means "write, or overwrite". Therefore, no conflicts possible. TODO: is this ok? (more on this below)*


### Data formats


LevelDB compresses data with something called SnappyCompressor.


We will rely on it to make the storage compact. Data that goes into LevelDB's key will be stored in KeyTupleFormat (which allows mysql's lookup/index ordering functions to work). Data that goes into LevelDB's value will be stored in table->record[0] format, except blobs. (Blobs will require special storage convention because they store a char* pointer in table->record[0]).


(TODO: is it okay not to support blobs in the first milestone?)


(note: datatypes in the provided benchmark are: composite primary/secondary keys, INTs and VARCHARs (are they latin1 or utf-8?)).


### Secondary Indexes


#### Unique secondary indexes


Unique secondary index is stored in a {KEY->VALUE} mapping in LevelDB, where index
columns are used as KEY, and Primary Key columns are used as VALUE. This way,


* "index-only" scans are possible
* non-"index-only" scan is a two step process (access the index, access the primary index).


We need to support unique indexes, but not in the first milestone.


Note: unique indexes may prevent read-before-write optimization. There is a @@unique_checks variable (used at least by InnoDB) which can be used to offer no-guarantees fast execution.


#### Non-unique secondary indexes


LevelDB stores {KEY->VALUE} mappings. Non-unique index will need to have some unique values for KEY. This is possible if we do


```
KEY = {index_columns, primary_key_columns}.   
VALUE = {nothing}
```

(todo: check if leveldb allows zero-sized values).


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

### Non-blocking schema changes


* There is a requirement that doing schema changes does not block other queries
 from running.


* Reclaiming space immediately after some parts of data were dropped is not
 important.


Possible approaches we could use:


* Record format that support multiple versions. That way, adding/modifying/
 dropping a non-indexed column may be instant. Note that this is applicable
 for records, not keys.


* Background creation/dropping of indexes.


### Hot backup


Hot backup will be made outside of this project. The idea is to hard-link the 
files so that they can't be deleted by compaction process, and then copy them over.


## SQL Command mapping for LevelDB


### INSERT


There will be two kinds of INSERTs


1. No-reads INSERT-or-UPDATE, with semantics like in LevelDB's DB::Put() operation.
1. a "real" INSERT with SQL semantics


#### INSERT-or-UPDATE (low priority)


SergeiG has pointed out that SQL layer already has support for write-optimized INSERTs (it was implemented for NDB Cluster).


When the table has no triggers, REPLACE command will call
handler->extra(HA_EXTRA_WRITE_CAN_REPLACE), after which
handler->write_row() calls are allowed to silently overwrite rows.


The number of affected rows returned by the statement is actually upper bound.


(note: TokuDB documentation mentions they have something similar with INSERTs.
They allow no-reads REPLACE and INSERT IGNORE, when the table has no triggers,
there is no RBR binary logging, etc - the same conditions as we will have)


##### Batching


It is possible to batch multi-line REPLACE commands. (TODO: Can no-read REPLACEs fail at all? If not, we can limit batch size and use multiple batches if necessary. If yes, we'll have to document that big REPLACEs may fail in the middle of a statement/ Q: is this OK?)


#### Regular INSERT


Regular INSERT will do a read before write and will use "gap locking" to 
make sure its DB::Put() call doesn't overwrite somebody's data.


### UPDATE


UPDATE will do a read before write and will use record locking to make sure it's not overwriting somebody else's changes (or not updating a row that has just been deleted).


*Note: mysql-5.6 has [WL#5906](https://askmonty.org/worklog/?tid=5906) (see link at the bottom)read before write removal (RBWR). It is not exactly what we need, but is similar (and ugly)*


### DELETE


Currently, a DELETE statement has to do a read. Records are deleted through
handler->delete_row() call of the Storage Engine API, which has the meaning
"delete the row that was just read".


There will be two kinds of DELETE statement:


* Write-optimized DELETE IF_EXISTS
* Regular DELETE


#### DELETE IF_EXISTS (low priority)


This is a write-optimized version. It will have semantics close to LevelDB's 
DB::Delete() call. We will have to modify the SQL layer to support it.


The syntax will be


<<code lang='sql'>
DELETE NO_READ FROM tbl WHERE ...
<</code>>


the option NO_READ will be supported only for single-table DELETEs, and will 
require that
- the WHERE clause refers to primary key columns only
- the WHERE clause allows to construct a list of primary keys to be deleted.
- there ORDER BY clause


if the above conditions are not met, the statement will fail with an error.
if they are met, the statement translate into handler->delete_row() calls, without any read calls.


mysql_affected_rows() will return an upper bound of how many rows could be deleted.


#### Regular DELETE


Regular DELETE will have to use locking.


### SELECT


#### Will use snapshot


SELECTs will allocate/use a snapshot for reading data. This way, sql layer will not
get non-repeatable reads within a statement.


Q: is this needed? Using snapshots has some cost?


#### Range scans


* LevelDB cursors can be used for range scans.
* DB::GetApproximateSizes() can be used to implement handler::records_in_range()
* There is nothing for rec_per_key (index statistics)


### ALTER TABLE


MySQL 5.6 should support online ALTER TABLE operations (as InnoDB now supports them).


TODO: what does the storage engine needs to do to inform the SQL layer that it is running a long DDL change which does not prevent other selects/updates from running?


## Binlog XA on Master


This is about keeping binlog and LevelDB in sync on the master. MySQL does it as follows:


* prepare transaction in the storage engine
* write it into the binlog
* commit it in the engine


If transactions are grouped, they are committed in the same order as they were written into the binary log.


Recovery proceeds as follows:


* Read the last binlog file and note XIDs of transactions that are there.
* for each storage engine, 

  * scan the committed transactions and compare their XIDs to those we've found in the binlog.
  * If transaction is the binlog - commit, otherwise - roll it back)


(note that the order the transactions are applied in is determined from the engine, not from the binlog)


TODO: suggestions about how PREPARE/COMMIT/recovery should work for LevelDB. (got some ideas after discussion with Kristian, need to write them down)


## Crash-proof slave


MySQL 5.6 stores information that used to be in relay_log.info
in InnoDB. That way, InnoDB and relay_log.info (aka binlog position) are always in sync.


It seems, switching to storing relay_log.info in a LevelDB table is sufficient for 
crash-proof slave. (note: this implies that semantics of operations over LevelDB table is sufficiently close to that of a regular MySQL storage engine, like innodb).


## Other details


* The target version is MySQL 5.6 (good, because LevelDB API uses STL and
 5.6-based versions support compiling with STL).
* It is ok to make changes to LevelDB itself


* There is a "Test implementation" at [tbleveldb](https://github.com/tbdingqi/tbleveldb).


* Task tracking for this is done here: [MDEV-3841](https://jira.mariadb.org/browse/MDEV-3841)


* We may want to check out this: [?id=5906](https://dev.mysql.com/worklog/task/?id=5906). It is pushed into 5.6


## Milestones


* Milestone #1 is described at [leveldb-storage-engine-ms1](leveldb-storage-engine-ms1.md)
* Subsequent development is described at [leveldb-storage-engine-development](leveldb-storage-engine-development.md)


* Milestone #2 is described at [leveldb-storage-engine-ms2](leveldb-storage-engine-ms2.md)


CC BY-SA / Gnu FDL

