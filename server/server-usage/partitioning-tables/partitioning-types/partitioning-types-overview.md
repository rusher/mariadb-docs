# Partitioning Types Overview

A partitioning type determines how a partitioned table's rows are distributed across partitions. Some partition types require the user to specify a partitioning expression that determines in which partition a row will be stored.

The size of individual partitions depends on the partitioning type. Read and write performance are affected by the partitioning expression. Therefore, these choices should be made carefully.

MariaDB supports the following partitioning types:

* [RANGE](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/partitioning-tables/partitioning-types/broken-reference/README.md)
* [LIST](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/partitioning-tables/partitioning-types/broken-reference/README.md)
* [RANGE COLUMNS and LIST COLUMNS](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/partitioning-tables/partitioning-types/broken-reference/README.md)
* [HASH](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/partitioning-tables/partitioning-types/broken-reference/README.md)
* [LINEAR HASH](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/partitioning-tables/partitioning-types/broken-reference/README.md)
* [KEY](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/partitioning-tables/partitioning-types/broken-reference/README.md)
* [LINEAR KEY](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/partitioning-tables/partitioning-types/broken-reference/README.md)
* [SYSTEM\_TIME](../../../reference/sql-structure/temporal-tables/system-versioned-tables.md)

### See Also

* [Partitioning Overview](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/partitioning-tables/partitioning-types/broken-reference/README.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
