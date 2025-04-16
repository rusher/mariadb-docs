
# Flashback


Flashback is a feature that allows instances, databases or tables to be rolled back to an old snapshot.


Flashback is currently supported only over DML statements ([INSERT](../../../ref/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/insert-function.md), [DELETE](../../../ref/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/delete.md), [UPDATE](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md)). An upcoming version of MariaDB will add support for flashback over DDL statements ([DROP](../../../ref/sql-statements-and-structure/sql-statements/data-definition/drop/drop-tablespace.md), [TRUNCATE](../../../ref/sql-statements-and-structure/sql-statements/table-statements/truncate-table.md), [ALTER](../../../ref/sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md), etc.) by copying or moving the current table to a reserved and hidden database, and then copying or moving back when using flashback. See [MDEV-10571](https://jira.mariadb.org/browse/MDEV-10571).


Flashback is achieved in MariaDB Server using existing support for full image format binary logs ([binlog_row_image=FULL](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#binlog_row_image)), so it supports all engines.


The real work of Flashback is done by [mariadb-binlog](../../../../connectors/mariadb-connector-c/mariadb-binlogreplication-api-reference.md) with `--flashback`. This causes events to be translated: INSERT to DELETE, DELETE to INSERT, and for UPDATEs, the before and after images are swapped.


When executing `mariadb-binlog` with `--flashback`, the Flashback events will be stored in memory. You should make sure your server has enough memory for this feature.


## Arguments


* [mariadb-binlog](../../../../connectors/mariadb-connector-c/mariadb-binlogreplication-api-reference.md) has the option `--flashback` or `-B` that will let it work in flashback mode.
* [mariadbd](../../getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) has the option [--flashback](../../getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-flashback) that enables the binary log and sets `binlog_format=ROW`. It is not mandatory to use this option if you have already enabled those options directly.


Do not use `-v` `-vv` options, as this adds verbose information to the binary log which can cause problems when importing. See [MDEV-12066](https://jira.mariadb.org/browse/MDEV-12066) and [MDEV-12067](https://jira.mariadb.org/browse/MDEV-12067).


## Example


With a table "mytable" in database "test", you can compare the output with `--flashback` and without.


```
mariadb-binlog /var/lib/mysql/mysql-bin.000001 -vv -d test -T mytable \
    --start-datetime="2013-03-27 14:54:00" > review.sql
```

```
mariadb-binlog /var/lib/mysql/mysql-bin.000001 -vv -d test -T mytable \
    --start-datetime="2013-03-27 14:54:00" --flashback > flashback.sql
```

If you know the exact position, `--start-position` can be used instead of `--start-datetime`.


Then, by importing the output file (`mariadb < flashback.sql`), you can flash your database/table back to the specified time or position.


## Common Use Case


A common use case for Flashback is the following scenario:


* You have one primary and two replicas, one started with `--flashback` (i.e. with binary logging enabled, using [binlog_format=ROW](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#binlog_format), and [binlog_row_image=FULL](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#binlog_row_image)).
* Something goes wrong on the primary (like a wrong update or delete) and you would like to revert to a state of the database (or just a table) at a certain point in time.
* Remove the flashback-enabled replica from replication.
* Invoke [mariadb-binlog](../../../../connectors/mariadb-connector-c/mariadb-binlogreplication-api-reference.md) to find the exact log position of the first offending operation after the state you want to revert to.
* Run `mariadb-binlog --flashback --start-position=xyz | mariadb` to pipe the output of `mariadb-binlog` directly to the `mariadb` client, or save the output to a file and then direct the file to the command-line client.

