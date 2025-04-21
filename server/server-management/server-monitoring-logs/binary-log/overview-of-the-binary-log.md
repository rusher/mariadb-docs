
# Overview of the Binary Log

The binary log contains a record of all changes to the databases, both data and structure, as well as how long each statement took to execute. It consists of a set of binary log files and an index.


This means that statements such as [CREATE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/README.md), [ALTER](../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/README.md), [INSERT](../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert.md), [UPDATE](../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/update.md) and [DELETE](../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/delete.md) will be logged, but statements that have no effect on the data, such as SELECT and SHOW, will not be logged. If you want to log these (at a cost in performance), use the [general query log](../general-query-log.md).


If a statement may potentially have an effect, but doesn't, such as an UPDATE or DELETE that returns no rows, it will still be logged (this applies to the default statement-based logging, not to row-based logging - see [Binary Log Formats](binary-log-formats.md)).


The purpose of the binary log is to allow [replication](../../../server-usage/replication-cluster-multi-master/README.md), where data is sent from one or more masters to one or more slave servers based on the contents of the binary log, as well as assisting in backup operations.


A MariaDB server with the binary log enabled will run slightly more slowly.


It is important to protect the binary log, as it may contain sensitive information, including passwords.


Binary logs are stored in a binary, not plain text, format, and so are not viewable with a regular editor. However, MariaDB includes [mariadb-binlog](../../../clients-and-utilities/mariadb-binlog/README.md), a commandline tool for plain text processing of binary logs.

