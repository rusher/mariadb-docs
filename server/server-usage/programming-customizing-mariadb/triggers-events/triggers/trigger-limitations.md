
# Trigger Limitations

The following restrictions apply to [triggers](README.md).


* All of the restrictions listed in [Stored Routine Limitations](../../stored-routines/stored-routine-limitations.md).
* All of the restrictions listed in [Stored Function Limitations](../../stored-routines/stored-functions/stored-function-limitations.md).
* Until [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes), each table can have only one trigger for each timing/event combination (ie: you can't define two BEFORE INSERT triggers for the same table).
* Triggers are always executed for each row. The standard `FOR EACH STATEMENT` option is not supported in MariaDB,
* Triggers cannot operate on any tables in the mysql, information_schema or performance_schema database.
* Cannot return a resultset.
* The [RETURN](../../programmatic-compound-statements/return.md) statement is not permitted, since triggers don't return any values. Use [LEAVE](../../programmatic-compound-statements/leave.md) to immediately exit a trigger.
* Triggers are not activated by [foreign key](../../../replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/foreign-keys.md) actions.
* If a trigger is loaded into cache, it is not automatically reloaded when the table metadata changes. In this case a trigger can operate using the outdated metadata.
* By default, with row-based replication, triggers run on the master, and the effects of their executions are replicated to the slaves. However, starting from [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes), it is possible to run triggers on the slaves. See [Running triggers on the slave for Row-based events](../../../replication-cluster-multi-master/standard-replication/running-triggers-on-the-replica-for-row-based-events.md).


## See Also


* [Trigger Overview](trigger-overview.md)
* [CREATE TRIGGER](create-trigger.md)
* [DROP TRIGGER](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-trigger.md)
* [Information Schema TRIGGERS Table](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-triggers-table.md)
* [SHOW TRIGGERS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-triggers.md)
* [SHOW CREATE TRIGGER](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-trigger.md)

