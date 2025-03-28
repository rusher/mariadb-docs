# PROCEDURE

The `PROCEDURE` clause of [SELECT](../../../../../server-usage/replication-cluster-multi-master/standard-replication/selectively-skipping-replication-of-binlog-events.md) passes the whole result set to a Procedure which will process it. These Procedures are not [Stored Procedures](/kb/en/stored-procedures/), and can only be written in the C language, so it is necessary to recompile the server.

Currently, the only available procedure is [ANALYSE](../../built-in-functions/secondary-functions/information-functions/procedure-analyse.md), which examines the resultset and suggests the optimal datatypes for each column. It is defined in the `sql/sql_analyse.cc` file, and can be used as an example to create more Procedures.

This clause cannot be used in a [view](/kb/en/views/)'s definition.

#

# See Also

* [SELECT](../../../../../server-usage/replication-cluster-multi-master/standard-replication/selectively-skipping-replication-of-binlog-events.md)
* [Stored Procedures](/kb/en/stored-procedures/)