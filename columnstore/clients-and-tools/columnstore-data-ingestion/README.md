# Data Ingestion Methods & Tools

ColumnStore provides several mechanisms to ingest data:

* [cpimport](columnstore-bulk-data-loading.md) provides the fastest performance for inserting data and ability to route data to particular PM nodes. Normally this should be the default choice for loading data .
* [LOAD DATA INFILE](../../columnstore-sql-structure-and-commands/columnstore-data-manipulation-statements/columnstore-load-data-infile.md) provides another means of bulk inserting data.
  * By default with autocommit on it will internally stream the data to an instance of the cpimport process. This requires some memory overhead on the UM server so may be less reliable than cpimport for very large imports.
  * In transactional mode DML inserts are performed which will be significantly slower plus it will consume both binlog transaction files and ColumnStore VersionBuffer files.
* DML, i.e. INSERT, UPDATE, and DELETE, provide row level changes. ColumnStore is optimized towards bulk modifications and so these operations are slower than they would be in say InnoDB.
  * Currently ColumnStore does not support operating as a replication slave target.
  * Bulk DML operations will in general perform better than multiple individual statements.
    * [INSERT INTO SELECT](columnstore-batch-insert-mode.md) with autocommit behaves similarly to LOAD DATE INFILE in that internally it is mapped to cpimport for higher performance.
    * Bulk update operations based on a join with a small staging table can be relatively fast especially if updating a single column.
* Using [ColumnStore Bulk Write SDK](columnstore-bulk-write-sdk.md) or [ColumnStore Streaming Data Adapters](columnstore-streaming-data-adapters.md)
