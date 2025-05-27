# FLUSH QUERY CACHE

## Description

You can defragment [the query cache](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache.md) to better utilize its memory with\
the `FLUSH QUERY CACHE` statement. The statement does not remove any queries from the cache.

The [RESET QUERY CACHE](../reset.md) statement removes all query results from the query cache.\
The [FLUSH TABLES](flush.md) statement also does this.

GPLv2 fill\_help\_tables.sql
