
# PERFORMANCE_SCHEMA Storage Engine

If you run [SHOW ENGINES](../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-engines.md), you'll see the following storage engine listed.


```
SHOW ENGINES\G
...
      Engine: PERFORMANCE_SCHEMA
     Support: YES
     Comment: Performance Schema
Transactions: NO
          XA: NO
  Savepoints: NO
...
```

The PERFORMANCE_SCHEMA is not a regular storage engine for storing data, it's a mechanism for implementing the [Performance Schema](../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/README.md) feature.


The [SHOW ENGINE PERFORMANCE_SCHEMA STATUS](../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-engine.md#show-engine-performance_schema-status) statement is also available, which shows how much memory is used by the tables and internal buffers.


See [Performance Schema](../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/README.md) for more details.


CC BY-SA / Gnu FDL

