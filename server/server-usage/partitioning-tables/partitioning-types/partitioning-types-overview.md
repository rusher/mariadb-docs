# Partitioning Types Overview

A partitioning type determines how a partitioned table's rows are distributed across partitions. Some partition types require the user to specify a partitioning expression that determines in which partition a row will be stored.

The size of individual partitions depends on the partitioning type. Read and write performance are affected by the partitioning expression. Therefore, these choices should be made carefully.

MariaDB supports the following partitioning types:

* [RANGE](broken-reference)
* [LIST](broken-reference)
* [RANGE COLUMNS and LIST COLUMNS](broken-reference)
* [HASH](broken-reference)
* [LINEAR HASH](broken-reference)
* [KEY](broken-reference)
* [LINEAR KEY](broken-reference)
* [SYSTEM\_TIME](../../../reference/sql-structure/temporal-tables/system-versioned-tables.md)

### See Also

* [Partitioning Overview](broken-reference)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
