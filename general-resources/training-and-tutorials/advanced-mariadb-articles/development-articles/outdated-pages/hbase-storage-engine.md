
# HBase Storage Engine

Data mapping from HBase to SQL


The Jira task for this is [MDEV-122](https://jira.mariadb.org/browse/MDEV-122)


Nobody is working on this feature ATM. See [Cassandra Storage Engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/legacy-storage-engines/cassandra/cassandra-storage-engine-overview) for a related development that has reached the release stage.


This page describes a feature that's under development. The feature has not been released (even in beta), its interface and function may change, etc.



## Hbase data model and operations


### 1.1 HBase data model


* An HBase table consists of rows, which are identified by row key.
* Each row has an arbitrary (potentially, very large) number of columns.
* Columns are split into column groups, column groups define how the columns 
 are stored (not reading some column groups is an optimization).
* Each (row, column) combination can have multiple versions of the data,
 identified by timestamp.


### 1.2 Hbase read operations


HBase API defines two ways to read data:


* Point lookup: get record for a given row_key.


* Point scan: read all records in [startRow, stopRow) range.


Both kinds of scans allow to specify:


* A column family we're interested in
* A particular column we're interested in


The default behavior for versioned columns is to return only the most recent
version. HBase API also allows to ask for


* versions of columns that were valid at some specific timestamp value;
* all versions that were valid within a specifed [minStamp, maxStamp)
 interval.
* N most recent versions
We'll refer to the above as [VersionedDataConds].


One can see two ways to map HBase tables to SQL tables:


* Per-cell mapping
* Per-row mapping


## 2. Per-cell mapping


HBase shell has 'scan' command, here's an example of its output:


```
hbase(main):007:0> scan 'testtable'
 ROW COLUMN+CELL
  myrow-1 column=colfam1:q1, timestamp=1297345476469, value=value-1
  myrow-2 column=colfam1:q2, timestamp=1297345495663, value=value-2
  myrow-2 column=colfam1:q3, timestamp=1297345508999, value=value-3
```

Here, one HBase row produces multiple rows in the query output. Each 
output row represents one (row_id, column) combination, so rows with 
multiple columns (and multiple revisions of column data) can be easily 
represented.


### 2.1 Table definition


Mapping could be defined as follows:


```
CREATE TABLE hbase_tbl_cells (
  row_id binary(MAX_HBASE_ROWID_LEN),
  column_family binary(MAX_HBASE_COLFAM_LEN),
  column_name binary(MAX_HBASE_NAME_LEN),
  timestamp TIMESTAMP,
  value BLOB,
  PRIMARY KEY (row_id, column_family, column_name, timestamp)
) ENGINE=hbase_cell;
```

There is no need for dynamic columns in this mapping.


* NOTE: It is nice to have SQL table DDLs independent of the content of
 the backend hbase table. This saves us from the need to synchronize
 table DDLs between hbase and mysql (NDB cluster had to do this and they
 have ended up implementing a very complex system to do this).


### 2.2 Queries in per-cell mapping


```
# Point-select:
SELECT value 
FROM hbase_cell
WHERE 
  row_id='hbase_row_id' AND 
  column_family='hbase_column_family' AND column_name='hbase_column'
  ...
```

```
#  Range select:
#   (the example uses BETWEEN but we will support arbitrary predicates)
SELECT value 
FROM hbase_cell
WHERE 
  row_id BETWEEN 'hbase_row_id1' AND 'hbase_row_id2' AND 
  column_family='hbase_column_family' AND column_name='hbase_column'
```

```
# Update a value for {row, column}
UPDATE hbase_cell SET value='value' 
WHERE row_id='hbase_row' AND 
      column_family='col_family' AND column_name='col_name'
```

```
# Add a column into row
INSERT INTO hbase_cell values ('hbase_row', 'col_family','col_name','value');
```

Note that


* accessing versioned data is easy: one can read some particular version, versions within a date range, etc
* it is also easy to select all columns from a certain column family.


### 2.3 Mapping of SQL statements


#### Mapping for SELECT


The table is defined as having a


```
PRIMARY KEY (row_id, column_family, column_name, timestamp)
```

which allows to make use of range optimizer to get ranges on


* rowid
* rowid, column_family
* rowid, column_family, column_name
* ...


If a range specifies one row, we can read it with HTable.get(), otherwise we'll have to use HTable.getScanner() and make use of the obtained scanner.


##### Multiple non-equality conditions


HBase API allows to scan a range of rows, retrieving only certain column name
or certain column families. In our SQL mapping, this can be written as:


```
SELECT value
FROM hbase_cell
WHERE
  row_id BETWEEN 'hbase_row_id1' AND 'hbase_row_id2' AND
  column_family='hbase_column_family'                           (*)
```

If we feed this into the range optimizer, it will produce a range:


```
('hbase_row_id1', 'hbase_column_family') <= (row_id, column_family) <=
  ('hbase_row_id2', 'hbase_column_family')
```

which includes all column families for records which satisfy


```
'hbase_row_id1' < rowid < 'hbase_row_id2'
```

This will cause extra data to be read.


Possible solutions:


* Extend multi-range-read interface to walk the 'SEL_ARG graph' instead of
 list of ranges. This will allow to capture the exact form of conditions 
 like (*).
* Implement table condition pushdown and and perform independent condition analysis.
* Define more indexes, so that ranges are "dense".
 what about (row_id BETWEEN $X AND $Y) AND (timestamp BETWEEN $T1 AND
 $T2) ? No matter which index you define, the range list will not be
 identical to the WHERE clause.


#### Mapping for INSERT


INSERT will be translated into HTable.checkAndPut(..., value=NULL) call. That way, attempt to insert a {rowid, column} that already exists will fail.


#### Mapping for DELETE


MySQL/MariaDB's storage engine API handles DELETEs like this:


* Use some way to read the record that should be deleted
* call handler->ha_delete_row(). It will delete the row that was last read.


ha_hbase_cell can remember {rowid, column_name} of the record, and then use HBase.checkAndDelete() call, so that we're sure we're deleting what we've read.


If we get a statement in form of


```
DELETE FROM hbase_cell 
WHERE rowid='hbase_row_id' AND column_family='...' AND column_name='...';
```

then reading the record is redundant (we could just make one HBase.checkAndDelete() call). This will require some form of query pushdown, though.


#### Mapping for UPDATE


UPDATEs are similar to deletes as long as row_id, column_family, and column_name fields are not changed (that is, only column_value changes). Like with DELETEs:


* HBase.checkAndPut() call can be used to make sure we're updating what we've read
* one-point UPDATEs may need a shortcut so that we don't have to read the value before we make an update.


If UPDATE statement changes row_id, column_family, or column_name field, it becomes totally different. HBase doesn't allow to change rowid of a record. We can only remove the record with old rowid, and insert a record with the new rowid. HBase doesn't support multi-row transactions, so we'll want to insert the new variant of the record before we have deleted the old one (I assume that data duplication is better than data loss).


For first milestone, we could disallow UPDATEs that change row_id, column_family or column_name.


## 3. Per-row mapping


Let each row in HBase table be mapped into a row from SQL point of view:


```
SELECT * FROM hbase_table;

row-id column1 column2  column3  column4  ...
------ ------- -------  -------  -------  
row1    data1   data2
row2                     data3    
row3    data4                      data5
```

The problem is that the set of columns in a HBase table is not fixed and is
potentially is very large. The solution is to put all columns into one blob column
and use Dynamic Columns ([dynamic-columns](https://kb.askmonty.org/en/dynamic-columns)) functions
to pack/extract values of individual columns:


```
row-id dyn_columns
------ ------------------------------
row1   {column1=data1,column2=data2}
row2   {column3=data3}
row3   {column1=data4,column4=data5}
```

### 3.2 Mapping definition


Table DDL could look like this:


```
CREATE TABLE hbase_tbl_rows (
  row_id BINARY(MAX_HBASE_ROWID_LEN),
  columns BLOB,  -- All columns/values packed in dynamic column format
  PRIMARY KEY (row_id)
) ENGINE=hbase_row;
```

(TODO: Does Hbase have MAX_HBASE_ROWID_LEN limit? What is it? We can ignore
this. Let the user define 'row_id' column with whatever limit he desires; don't do operations with rows that have row_id longer than the limit)


Functions for reading data:


```
COLUMN_GET(dynamic_column, column_nr as type)
  COLUMN_EXISTS(dynamic_column, column_nr);
  COLUMN_LIST(dynamic_column);
```

Functions for data modification:


```
COLUMN_ADD(dynamic_column, column_nr,  value [as type], ...)
  COLUMN_DELETE(dynamic_column, column_nr, column_nr, ...);
```

### 3.2.1 Required improvements in Dynamic Columns


Dynamic column functions cannot be used as-is:


* HBase columns have string names, Dynamic Columns have numbers (see column_nr parameter for the above functions). The set of column names in HBase is potentially very large, there is no way to get a list of all names: we won't be able to solve this with enum-style mapping, we'll need real support for string names.


* HBase has column families, Dynamic Columns do not . Column family is not just a ':' in the column name. For example, HBase API allows to request "all columns from within a certain column family".


* HBase supports versioned data, Dynamic Columns do not. A possible limited solution is to have global/session @@hbase_timestamp variable which will globally specify the required data version.


* (See also note below about efficient execution)


Names for dynamic columns are covered in [MDEV-377](https://jira.mariadb.org/browse/MDEV-377)


### 3.3 Queries in per-row mapping


```
# Point-select, get value of one column
SELECT COLUMN_GET(hbase_tbl.columns, 'column_name' AS INTEGER)
FROM hbase_tbl
WHERE 
  row_id='hbase_row_id';
```

```
#  Range select:
#   (the example uses BETWEEN but we will support arbitrary predicates)
SELECT COLUMN_GET(hbase_tbl.columns, 'column_name' AS INTEGER)
FROM hbase_tbl
WHERE 
  row_id BETWEEN 'hbase_row_id1' AND 'hbase_row_id2';
```

```
# Update or add a column for a row
UPDATE hbase_tbl SET columns=COLUMN_ADD(columns, 'column_name', 'value') WHERE row_id='hbase_row_id1';
```

Use of COLUMN_ADD like above will make no check whether column_name=X already
existed for that row. If it did, it will be silently overwritten.


ATTENTION: There seems to be no easy way to do something that would be like
SQL's INSERT statement, i.e. which would fail if the data you're changing
already exists.


One can write a convoluted IF(..., ....) expression will do the
store-if-not-exist operation, but it's bad when basic operations require
convoluted expressions.


ATTENTION: One could also question whether a statement with semantics of 
"store this data irrespectively of what was there before" has any value for
"remote" storage engine, where you're not the only one who's modifying the
data.


```
# Set all columns at once, overwriting the content that was there
UPDATE hbase_tbl SET columns=... WHERE row_id='hbase_row_id1';

UPDATE hbase_tbl SET columns=COLUMN_CREATE('column1', 'foo') WHERE row_id='row1';
```

Note that the lsat statement will cause all columns except for 'column1' to be
deleted for row 'row1'. This seems logical for SQL but there is no such
operation in HBase.


```
# Insert a new row with column(s)
INSERT INTO hbase_tbl (row_id, columns) VALUES
  ('hbase_row_id', COLUMN_CREATE('column_name', 'column-value'));
```

Q: It's not clear how to access versioned data? Can we go without versioned 
 data for the first milestone? 
 (and then, use @@hbase_timestamp for the second milestone?)


Q: It's not clear how to select "all columns from column family X".


### 3.4 Efficient execution for per-row mapping


#### 3.4.1 Predicate analysis


The table declares:


```
row_id BINARY(MAX_HBASE_ROWID_LEN),
  ...
  PRIMARY KEY (row_id)
```

which allows to use range/ref optimizer to extract ranges over the row_id
column.


One can also imagine a realistic query which uses conditions on hbase column
names:


```
SELECT column_get(columns, 'some_data') FROM hbase_tbl 
WHERE 
  row_id BETWEEN 'first_interesting_row' and 'last_interesting_row' AND 
  column_get(columns, 'attribute' as string)='eligible';
```

Range optimizer is unable to catch conditions in form of


```
column_get(columns, 'attribute' as string)='eligible'
```

We'll need to either extend it, or create another condition analyzer.


#### 3.4.2 Dynamic columns optimizations


Currently, MariaDB works with Dynamic Columns with this scenario:


1. When the record is read, the entire blob (=all columns) is read into memory
1. The query operates on the blob with Dynamic Columns Functions (reads and updates values for some columns, etc)
1. [If this is an UPDATE] the entire blob is written back to the table


If we use this approach with HBase, we will cause a lot of overhead with
reading/writing of unneeded data.


#### Solution #1: on-demand reads


* When table record is read, don't read any columns, return a blob handle.
* Dynamic Column functions will use the handle to read particular columns. The column is read from HBase only when its value is requested.


This scheme ensures there are no redundant data reads, at the cost making extra mysqld<->HBase roundtrips (which are likely to be expensive)


#### Solution #2: List of reads


* Walk through the query and find all references to hbase_table.columns.
* Collect the names of columns that are read, and retrieve only these columns.


This may cause redundant data reads, for example for


```
SELECT COLUMN_GET(hbase_tbl, 'column1' AS INTEGER) 
  FROM hbase_tbl
  WHERE 
    row_id BETWEEN 'hbase_row_id1' AND 'hbase_row_id2' AND 
    COLUMN_GET(hbase_tbl, 'column2' AS INTEGER)=1
```

column1 will be read for rows which have column2!=1. This still seems to 
be better than making extra roundtrips.


There is a question of what should be done when the query has references like


```
COLUMN_GET(hbase_tbl, {non-const-item} AS ...)
```

where it is not possible to tell in advance which columns must be read. Possible approaches are


* retrieve all columns
* fetch columns on demand
* stop the query with an error.


### 3.5 Mapping of SQL statements


#### SELECT


See above sections: we'll be able to analyze condition on row_id, and a list of columns we need to read. That will give sufficient info to do either an HTable.get() call, or call HTable.getScanner() and use the scanner.


#### INSERT


INSERT should make sure it actually creates the row, it should not overwrite existing rows. This is not trivial in HBase. The closest we can get is to make a number of 
HTable.checkAndPut() calls, with the checks that we're not overwriting the data.


This will cause INSERT ('row_id', COLUMN_CREATE('column1', 'data')) to succeed even if the table already had a row with ('row_id', COLUMN_CREATE('column2', 'data')).


Another possible problem is that INSERT can fail mid-way (we will insert only some columns of the record).


#### DELETE


DELETE seems to be ok: we can delete all {rowid, column_name} combinations for the given row_id. I'm not sure, perhaps this will require multiple HBase calls.


#### UPDATE


Just like with per-cell mapping, UPDATEs that change the row_id are actually deletions followed by inserts. We can disallow them in the first milestone.


The most frequent form of UPDATE is expected to be one that changes the value of a column:


```
UPDATE hbase_tbl SET columns=COLUMN_ADD(columns, 'column_name', 'value') 
WHERE 
  row_id='hbase_row_id1' AND COLUMN_GET(columns, 'column_name')='foo';
```

For that one, we need modified Dynamic Column Functions that will represent *changes* in the set of columns (and not *state*), so that we can avoid reading columns and writing them back.


## 4. Select-columns mapping


This is a simplification of the per-row mapping. Suppose, the user is only interested in particular columns with names `column1` and `column2`. They create a table with this definition:


```
CREATE TABLE hbase_tbl_cells (
  row_id binary(MAX_HBASE_ROWID_LEN),
  column1  TYPE,
  column2  TYPE,
  PRIMARY KEY (row_id),
  KEY(column1),
  KEY(column2)
) ENGINE=hbase_columns;
```

and then access it. Access is done like in per-row mapping, but without use of dynamic columns.


This mapping imposes lots of restrictions: it is only possible to select a fixed set of columns, there is no way to specify version of the data, etc.


## 5. Comparison of the mappings


If we select two columns from a certain row, per-cell mapping produces
"vertical" result, while per-row mapping produces "horizontal" result.


```
# Per-cell:
SELECT column_name, value 
FROM hbase_cell
WHERE 
  row_id='hbase_row_id1' AND 
  column_family='col_fam' AND column_name IN ('column1','column2')
+-------------+-------+
| column_name | value |
+-------------+-------+
| column1     | val1  |
| column2     | val2  |
+-------------+-------+
```

```
# Per row:
SELECT 
  COLUMN_GET(columns, 'col_fam:column1') as column1,  
  COLUMN_GET(columns, 'col_fam:column2') as column2,
FROM hbase_row
WHERE 
  row_id='hbase_row_id1' 
+---------+---------+
| column1 | column2 |
+---------+---------+
| val1    | val2    |
+---------+---------+
```

Per-cell mapping:


* Allows a finer control over selection of versioned data (easy to specify
 [range of] versions to select), column families, etc.
* Is more suitable for cases when one needs to select an arbitrarily-long list
 of columns.


Per-row (or select-columns) mapping is easier when:


* one is accessing a limited set of columns
* one needs to access multiple columns from multiple rows (in per-cell mapping
 this will require an [inefficient?] self-join).


## 6. Interfacing with HBase


HBase is in Java, and its native client API is a java library. We need to
interface with it from C++ storage engine code. Possible options are:


### 6.1 Use Thrift


This requires HBase installation to run a Thrift server


### 6.2 Re-implement HBase's network protocol


* It seems to be a custom-made RPC protocol.
* There is an independent re-implementation here: [asynchbase](https://github.com/stumbleupon/asynchbase). It is 10K lines of Java code, which gives an idea about HBase's protocol complexity

  * It seems to support only a subset of features? I.e. I was unable to find mention of pushed down conditions support?
  * Look in `HBaseRpc.java` for `"Unofficial Hadoop / HBase RPC protocol documentation"`


### 6.3 Use JNI+HBase client protocol


* not sure how complex this is
* Mark has mentioned this has an unacceptable overhead?


## 7. Consistency, transactions, etc


* HBase has single-record transactions. Does this mean that HBase storage
 engine will have MyISAM-like characteristics? e.g. if we fail in the
 middle of a multi-row UPDATE, there is no way to go back.


* Q: Are the writes important at all? (e.g. if we've had the first version with
 provide read-only access, would that be useful?) 
 A: Yes?


## 8. Batching


Q: will we need joins, i.e. do I need to implement Multi-Range-Read and
support Batched Key Access right away?


## 9. Results of discussion with Monty


* Per-row mapping seems to be much more useful than per-cell mapping, because a lot of users have queries that retrieve lots of columns for lots of rows (is this so?)
* Dynamic column format will support string column names (see [MDEV-377](https://jira.mariadb.org/browse/MDEV-377))
* For the first milestone, forget about dynamic column concerns mentioned in "Efficient execution for per-row mapping". It is sufficient that all columns are returned as one blob that physically contains all columns.


CC BY-SA / Gnu FDL

