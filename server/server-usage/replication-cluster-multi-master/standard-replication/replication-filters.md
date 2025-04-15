# Replication Filters

The terms *master* and *slave* have historically been used in replication, and MariaDB has begun the process of adding *primary* and *replica* synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.

Replication filters allow users to configure [replicas](replication-overview.md) to intentionally skip certain events.

#

# Binary Log Filters for Replication Primaries

MariaDB provides options that can be used on a [replication primary](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) to restrict local changes to specific databases from getting written to the [binary log](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md), which also determines whether any replicas replicate those changes.

#

## Binary Log Filter Options

The following options are available, and they are evaluated in the order that they are listed below. If there are conflicting settings, *binlog_do_db* prevails. Before [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes), they are only available as options; from [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes) they are also available as system variables.

#

### `binlog_do_db`

The [binlog_do_db](/kb/en/mysqld-options/#-binlog-do-db) option allows you to configure a [replication primary](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) to write statements and transactions affecting databases that match a specified name into its [binary log](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md). Since the filtered statements or transactions will not be present in the [binary log](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md), its replicas will not be able to replicate them.

This option will **not** work with cross-database updates with [statement-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](#statement-based-logging) section for more information.

This option can **not** be set dynamically.

When setting it on the command-line or in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), the option does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the option multiple times. For example:

```
[mariadb]
...
binlog_do_db=db1
binlog_do_db=db2
```

This will tell the primary to do the following:

* Write statements and transactions affecting the database named db1 into the [binary log](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md).
* Write statements and transactions affecting the database named db2 into the [binary log](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md).
* Don't write statements and transactions affecting any other databases into the [binary log](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md).

#

### `binlog_ignore_db`

The [binlog_ignore_db](/kb/en/mysqld-options/#-binlog-ignore-db) option allows you to configure a [replication primary](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) to **not** write statements and transactions affecting databases that match a specified name into its [binary log](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md). Since the filtered statements or transactions will not be present in the [binary log](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md), its replicas will not be able to replicate them.

This option will **not** work with cross-database updates with [statement-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](#statement-based-logging) section for more information.

This option can **not** be set dynamically.

When setting it on the command-line or in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), the option does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the option multiple times. For example:

```
[mariadb]
...
binlog_ignore_db=db1
binlog_ignore_db=db2
```

This will tell the primary to do the following:

* Don't write statements and transactions affecting the database named db1 into the [binary log](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md).
* Don't write statements and transactions affecting the database named db2 into the [binary log](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md).
* Write statements and transactions affecting any other databases into the [binary log](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md).

The [binlog_ignore_db](#binlog_ignore_db) option is effectively ignored if the [binlog_do_db](#binlog_do_db) option is set, so those two options should not be set together.

#

# Replication Filters for Replicas

MariaDB provides options and system variables that can be used on used on a [replicas](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) to filter events replicated in the [binary log](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md).

#

## Replication Filter Options

The following options and system variables are available, and they are evaluated in the order that they are listed below. If there are conflicting settings, the respective *replicate_do_* prevails.

#

### `replicate_rewrite_db`

The [replicate_rewrite_db](replication-and-binary-log-system-variables.md#replicate_rewrite_db) option (and, from [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-1011), system variable), allows you to configure a [replica](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) to rewrite database names. It uses the format `primary_database->replica_database`. If a replica encounters a [binary log](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) event in which the default database (i.e. the one selected by the [USE](../../../security/user-account-management/user-password-expiry.md) statement) is `primary_database`, then the replica will apply the event in `replica_database` instead.

This option will **not** work with cross-database updates with [statement-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](#statement-based-logging) section for more information.

This option only affects statements that involve tables. This option does not affect statements involving the database itself, such as [CREATE DATABASE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-database.md), [ALTER DATABASE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-database.md), and [DROP DATABASE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-database.md).

This option's rewrites are evaluated *before* any other replication filters configured by the `replicate_*` system variables.

Statements that use table names qualified with database names do not work with other replication filters such as [replicate_do_table](#replicate_do_table).

Until [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-1011), this option could not be set dynamically.

When setting it on the command-line or in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), the option does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the option multiple times. For example:

```
[mariadb]
...
replicate_rewrite_db=db1->db3
replicate_rewrite_db=db2->db4
```

This will tell the replica to do the following:

* If a [binary log](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) event is encountered in which the default database was db1, then apply the event in db3 instead.
* If a [binary log](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) event is encountered in which the default database was db2, then apply the event in db4 instead.

See [Configuring Replication Filter Options with Multi-Source Replication](#configuring-replication-filter-options-with-multi-source-replication) for how to configure this system variable with [multi-source replication](multi-source-replication.md).

#

### `replicate_do_db`

The [replicate_do_db](/kb/en/replication-and-binary-log-server-system-variables/#replicate_do_db) system variable allows you to configure a [replica](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) to apply statements and transactions affecting databases that match a specified name.

This system variable will **not** work with cross-database updates with [statement-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging) or when using [mixed-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging) and the statement is logged statement based. For statement-based replication, only the default database (that is, the one selected by USE) is considered, not any explicitly mentioned tables in the query.
See the [Statement-Based Logging](#statement-based-logging) section for more information.

When setting it dynamically with [SET GLOBAL](setting-up-replication.md#global-session), the system variable accepts a comma-separated list of filters.

When setting it dynamically, it is not possible to specify database names that contain commas. If you need to specify database names that contain commas, then you will need to specify them by either providing the command-line options or configuring them in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) when the server is [started](/kb/en/starting-and-stopping-mariadb-starting-and-stopping-mariadb/).

When setting it dynamically, the [replica threads](replication-threads.md#threads-on-the-slave) must be stopped. For example:

```
STOP SLAVE;
SET GLOBAL replicate_do_db='db1,db2';
START SLAVE;
```

When setting it on the command-line or in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), the system variable does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the system variable multiple times. For example:

```
[mariadb]
...
replicate_do_db=db1
replicate_do_db=db2
```

This will tell the replica to do the following:

* Replicate statements and transactions affecting the database named db1.
* Replicate statements and transactions affecting the database named db2.
* Ignore statements and transactions affecting any other databases.

See [Configuring Replication Filter Options with Multi-Source Replication](#configuring-replication-filter-options-with-multi-source-replication) for how to configure this system variable with [multi-source replication](multi-source-replication.md).

#

### `replicate_ignore_db`

The [replicate_ignore_db](/kb/en/replication-and-binary-log-server-system-variables/#replicate_ignore_db) system variable allows you to configure a [replica](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) to ignore statements and transactions affecting databases that match a specified name.

This system variable will **not** work with cross-database updates with [statement-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging) or when using [mixed-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging) and the statement is logged statement based. For statement-based replication, only the default database (that is, the one selected by USE) is considered, not any explicitly mentioned tables in the query.
See the [Statement-Based Logging](#statement-based-logging) section for more information.

When setting it dynamically with [SET GLOBAL](setting-up-replication.md#global-session), the system variable accepts a comma-separated list of filters.

When setting it dynamically, it is not possible to specify database names that contain commas. If you need to specify names or patterns that contain commas, then you will need to specify them by either providing the command-line options or configuring them in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) when the server is [started](/kb/en/starting-and-stopping-mariadb-starting-and-stopping-mariadb/).

When setting it dynamically, the [replica threads](replication-threads.md#threads-on-the-slave) must be stopped. For example:

```
STOP SLAVE;
SET GLOBAL replicate_ignore_db='db1,db2';
START SLAVE;
```

When setting it on the command-line or in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), the system variable does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the system variable multiple times. For example:

```
[mariadb]
...
replicate_ignore_db=db1
replicate_ignore_db=db2
```

This will tell the replica to do the following:

* Ignore statements and transactions affecting databases named db1.
* Ignore statements and transactions affecting databases named db2.
* Replicate statements and transactions affecting any other databases.

The [replicate_ignore_db](#replicate_ignore_db) system variable is effectively ignored if the [replicate_do_db](#replicate_do_db) system variable is set, so those two system variables should not be set together.

See [Configuring Replication Filter Options with Multi-Source Replication](#configuring-replication-filter-options-with-multi-source-replication) for how to configure this system variable with [multi-source replication](multi-source-replication.md).

#

### `replicate_do_table`

The [replicate_do_table](/kb/en/replication-and-binary-log-server-system-variables/#replicate_do_table) system variable allows you to configure a [replica](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) to apply statements and transactions that affect tables that match a specified name. The table name is specified in the format: `dbname.tablename`.

This system variable will **not** work with cross-database updates with [statement-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](#statement-based-logging) section for more information.

This option only affects statements that involve tables. This option does not affect statements involving the database itself, such as [CREATE DATABASE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-database.md), [ALTER DATABASE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-database.md), and [DROP DATABASE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-database.md).

When setting it dynamically with [SET GLOBAL](setting-up-replication.md#global-session), the system variable accepts a comma-separated list of filters.

When setting it dynamically, it is not possible to specify database or table names
or patterns that contain commas. If you need to specify database or table names that contain commas, then you will need to specify them by either providing the command-line options or configuring them in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) when the server is [started](/kb/en/starting-and-stopping-mariadb-starting-and-stopping-mariadb/).

When setting it dynamically, the [replica threads](replication-threads.md#threads-on-the-slave) must be stopped. For example:

```
STOP SLAVE;
SET GLOBAL replicate_do_table='db1.tab,db2.tab';
START SLAVE;
```

When setting it on the command-line or in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), the system variable does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the system variable multiple times. For example:

```
[mariadb]
...
replicate_do_table=db1.tab
replicate_do_table=db2.tab
```

This will tell the replica to do the following:

* Replicate statements and transactions affecting tables in databases named db1 and which are named tab.
* Replicate statements and transactions affecting tables in databases named db2 and which are named tab.
* Ignore statements and transactions affecting any other tables.

See [Configuring Replication Filter Options with Multi-Source Replication](#configuring-replication-filter-options-with-multi-source-replication) for how to configure this system variable with [multi-source replication](multi-source-replication.md).

#

### `replicate_ignore_table`

The [replicate_ignore_table](/kb/en/replication-and-binary-log-server-system-variables/#replicate_ignore_table) system variable allows you to configure a [replica](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) to ignore statements and transactions that affect tables that match a specified name. The table name is specified in the format: `dbname.tablename`.

This system variable will **not** work with cross-database updates with [statement-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](#statement-based-logging) section for more information.

When setting it dynamically with [SET GLOBAL](setting-up-replication.md#global-session), the system variable accepts a comma-separated list of filters.

When setting it dynamically, it is not possible to specify database or table names that contain commas. If you need to specify database or table names that contain commas, then you will need to specify them by either providing the command-line options or configuring them in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) when the server is [started](/kb/en/starting-and-stopping-mariadb-starting-and-stopping-mariadb/).

When setting it dynamically, the [replica threads](replication-threads.md#threads-on-the-slave) must be stopped. For example:

```
STOP SLAVE;
SET GLOBAL replicate_ignore_table='db1.tab,db2.tab';
START SLAVE;
```

When setting it on the command-line or in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), the system variable does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the system variable multiple times. For example:

```
[mariadb]
...
replicate_ignore_table=db1.tab
replicate_ignore_table=db2.tab
```

This will tell the replica to do the following:

* Ignore statements and transactions affecting tables in databases named db1 and which are named tab.
* Ignore statements and transactions affecting tables in databases named db2 and which are named tab.
* Replicate statements and transactions affecting any other tables.

The [replicate_ignore_table](#replicate_ignore_table) system variable is effectively ignored if either the [replicate_do_table](#replicate_do_table) system variable or the [replicate_wild_do_table](#replicate_wild_do_table) system variable is set, so the [replicate_ignore_table](#replicate_ignore_table) system variable should not be used with those two system variables.

See [Configuring Replication Filter Options with Multi-Source Replication](#configuring-replication-filter-options-with-multi-source-replication) for how to configure this system variable with [multi-source replication](multi-source-replication.md).

#

### `replicate_wild_do_table`

The [replicate_wild_do_table](/kb/en/replication-and-binary-log-server-system-variables/#replicate_wild_do_table) system variable allows you to configure a [replica](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) to apply statements and transactions that affect tables that match a specified wildcard pattern.

The wildcard pattern uses the same semantics as the [LIKE](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/like.md) operator. This means that the the following characters have a special meaning:

* `_` - The `_` character matches any single character.
* `%` - The `%` character matches zero or more characters.
* `\` - The `\` character is used to escape the other special characters in cases where you need the literal character.

This system variable will work with cross-database updates with [statement-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](#statement-based-logging) section for more information.

The system variable does filter databases, tables, [views](/kb/en/views/) and [triggers](../../programming-customizing-mariadb/triggers-events/triggers/triggers-and-implicit-locks.md).

The system variable does not filter [stored procedures](/kb/en/stored-procedures/), [stored functions](/kb/en/stored-functions/), and [events](/kb/en/stored-programs-and-views-events/). The [replicate_do_db](/kb/en/replication-and-binary-log-server-system-variables/#replicate_do_db) system variable will need to be used to filter those.

If the table name pattern for a filter is just specified as `%`, then all tables in the database will be matched. In this case, the filter will also affect certain database-level statements, such as [CREATE DATABASE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-database.md), [ALTER DATABASE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-database.md) and [DROP DATABASE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-database.md).

When setting it dynamically with [SET GLOBAL](setting-up-replication.md#global-session), the system variable accepts a comma-separated list of filters.

When setting it dynamically, it is not possible to specify database or table names or patterns that contain commas. If you need to specify database or table names or patterns that contain commas, then you will need to specify them by either providing the command-line options or configuring them in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) when the server is [started](/kb/en/starting-and-stopping-mariadb-starting-and-stopping-mariadb/).

When setting it dynamically, the [replica threads](replication-threads.md#threads-on-the-slave) must be stopped. For example:

```
STOP SLAVE;
SET GLOBAL replicate_wild_do_table='db%.tab%,app1.%';
START SLAVE;
```

When setting it on the command-line or in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), the system variable does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the system variable multiple times. For example:

```
[mariadb]
...
replicate_wild_do_table=db%.tab%
replicate_wild_do_table=app1.%
```

This will tell the replica to do the following:

* Replicate statements and transactions affecting tables in databases that start with db and whose table names start with tab.
* Replicate statements and transactions affecting the database named app1.
* Ignore statements and transactions affecting any other tables and databases.

See [Configuring Replication Filter Options with Multi-Source Replication](#configuring-replication-filter-options-with-multi-source-replication) for how to configure this system variable with [multi-source replication](multi-source-replication.md).

#

### `replicate_wild_ignore_table`

The [replicate_wild_ignore_table](/kb/en/replication-and-binary-log-server-system-variables/#replicate_wild_ignore_table) system variable allows you to configure a [replica](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) to ignore statements and transactions that affect tables that match a specified wildcard pattern.

The wildcard pattern uses the same semantics as the [LIKE](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/like.md) operator. This means that the the following characters have a special meaning:

* `_` - The `_` character matches any single character.
* `%` - The `%` character matches zero or more characters.
* `\` - The `\` character is used to escape the other special characters in cases where you need the literal character.

This system variable will work with cross-database updates with [statement-based logging](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based-logging). See the [Statement-Based Logging](#statement-based-logging) section for more information.

The system variable does filter databases, tables, [views](/kb/en/views/) and [triggers](../../programming-customizing-mariadb/triggers-events/triggers/triggers-and-implicit-locks.md).

The system variable does not filter [stored procedures](/kb/en/stored-procedures/), [stored functions](/kb/en/stored-functions/), and [events](/kb/en/stored-programs-and-views-events/). The [replicate_ignore_db](/kb/en/replication-and-binary-log-server-system-variables/#replicate_ignore_db) system variable will need to be used to filter those.

If the table name pattern for a filter is just specified as `%`, then all tables in the database will be matched. In this case, the filter will also affect certain database-level statements, such as [CREATE DATABASE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-database.md), [ALTER DATABASE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-database.md) and [DROP DATABASE](../../../reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-database.md).

When setting it dynamically with [SET GLOBAL](setting-up-replication.md#global-session), the system variable accepts a comma-separated list of filters.

When setting it dynamically, it is not possible to specify database or table names or patterns that contain commas. If you need to specify database or table names or patterns that contain commas, then you will need to specify them by either providing the command-line options or configuring them in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) when the server is [started](/kb/en/starting-and-stopping-mariadb-starting-and-stopping-mariadb/).

When setting it dynamically, the [replica threads](replication-threads.md#threads-on-the-slave) must be stopped. For example:

```
STOP SLAVE;
SET GLOBAL replicate_wild_ignore_table='db%.tab%,app1.%';
START SLAVE;
```

When setting it on the command-line or in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), the system variable does not accept a comma-separated list. If you would like to specify multiple filters, then you need to specify the system variable multiple times. For example:

```
[mariadb]
...
replicate_wild_ignore_table=db%.tab%
replicate_wild_ignore_table=app1.%
```

This will tell the replica to do the following:

* Ignore statements and transactions affecting tables in databases that start with db and whose table names start with tab.
* Ignore statements and transactions affecting all the tables in the database named app1.
* Replicate statements and transactions affecting any other tables and databases.

The [replicate_ignore_table](#replicate_wild_ignore_table) system variable is effectively ignored if either the [replicate_do_table](#replicate_do_table) system variable or the [replicate_wild_do_table](#replicate_wild_do_table) system variable is set, so the [replicate_ignore_table](#replicate_wild_ignore_table) system variable should not be used with those two system variables.

See [Configuring Replication Filter Options with Multi-Source Replication](#configuring-replication-filter-options-with-multi-source-replication) for how to configure this system variable with [multi-source replication](multi-source-replication.md).

#

### Configuring Replication Filter Options with Multi-Source Replication

How you configure replication filters with [multi-source replication](multi-source-replication.md) depends on whether you are configuring them dynamically or whether you are configuring them in a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md).

#

#### Setting Replication Filter Options Dynamically with Multi-Source Replication

The usage of dynamic replication filters changes somewhat when [multi-source replication](multi-source-replication.md) is in use. By default, the variables are addressed to the default connection, so in a multi-source environment, the required connection needs to be specified. There are two ways to do this.

#

##### Prefixing the Replication Filter Option with the Connection Name

One way to change a replication filter for a multi-source connection is to explicitly specify the name when changing the filter. For example:

```
STOP SLAVE 'gandalf';
SET GLOBAL gandalf.replicate_do_table='database1.table1,database1.table2,database1.table3';
START SLAVE 'gandalf';
```

#

##### Changing the Default Connection

Alternatively, the default connection can be changed by setting the [default_master_connection](/kb/en/replication-and-binary-log-server-system-variables/#default_master_connection) system variable, and then the replication filter can be changed in the usual fashion. For example:

```
SET default_master_connection = 'gandalf';
STOP SLAVE; 
SET GLOBAL replicate_do_table='database1.table1,database1.table2,database1.table3';
START SLAVE;
```

#

#### Setting Replication Filter Options in Option Files with Multi-Source Replication

If you are using [multi-source replication](multi-source-replication.md) and if you would like to make this filter persist server restarts by adding it to a server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md), then the option file can also include the connection name that each filter would apply to. For example:

```
[mariadb]
...
gandalf.replicate_do_db=database1
saruman.replicate_do_db=database2
```

#

## CHANGE MASTER Options

The [CHANGE MASTER](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-commands/change-master-to.md) statement has a few options that can be used to filter certain types of [binary log](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) events.

#

### `IGNORE_SERVER_IDS`

The [IGNORE_SERVER_IDS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-commands/change-master-to.md#ignore_server_ids) option for `CHANGE MASTER` can be used to configure a [replica](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) to ignore [binary log](binary_log) events that originated from certain servers. Filtered [binary log](binary_log) events will not get logged to the replica’s [relay log](../../../server-management/server-monitoring-logs/binary-log/relay-log.md), and they will not be applied by the replica.

#

### `DO_DOMAIN_IDS`

The [DO_DOMAIN_IDS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-commands/change-master-to.md#do_domain_ids) option for `CHANGE MASTER` can be used to configure a [replica](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) to only apply [binary log](binary_log) events if the transaction's [GTID](/kb/en/global-transaction-id/) is in a specific [gtid_domain_id](../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md#gtid_domain_id) value. Filtered [binary log](binary_log) events will not get logged to the replica’s [relay log](../../../server-management/server-monitoring-logs/binary-log/relay-log.md), and they will not be applied by the replica.

#

### `IGNORE_DOMAIN_IDS`

The [IGNORE_DOMAIN_IDS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-commands/change-master-to.md#ignore_domain_ids) option for `CHANGE MASTER` can be used to configure a [replica](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) to ignore [binary log](binary_log) events if the transaction's [GTID](/kb/en/global-transaction-id/) is in a specific [gtid_domain_id](../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/gtid_event.md#gtid_domain_id) value. Filtered [binary log](binary_log) events will not get logged to the replica’s [relay log](../../../server-management/server-monitoring-logs/binary-log/relay-log.md), and they will not be applied by the replica.

#

# Replication Filters and Binary Log Formats

The way that a replication filter is interpreted can depend on the [binary log format](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md).

#

## Statement-Based Logging

When an event is logged in its statement-based format, many replication filters that affect a database will test the filter against the default database (i.e. the one selected by the [USE](../../../security/user-account-management/user-password-expiry.md) statement). This applies to the following replication filters:

* [binlog_do_db](#binlog_do_db)
* [binlog_ignore_db](#binlog_ignore_db)
* [replicate_rewrite_db](#replicate_rewrite_db)
* [replicate_do_db](#replicate_do_db)
* [replicate_ignore_db](#replicate_ignore_db)

When an event is logged in its statement-based format, many replication filters that affect a table will test the filter against the table in the default database (i.e. the one selected by the [USE](../../../security/user-account-management/user-password-expiry.md) statement). This applies to the following replication filters:

* [replicate_do_table](#replicate_do_table)
* [replicate_ignore_table](#replicate_ignore_table)

This means that cross-database updates **not** work with replication filters and statement-based binary logging. For example, if [replicate_do_table=db2.tab](replicate_do_table%3Ddb2.tab) were set, then the following would not replicate with statement-based binary logging:

```
USE db1;
INSERT INTO db2.tab VALUES (1);
```

If you need to be able to support cross-database updates with replication filters and statement-based binary logging, then you should use the following replication filters:

* [replicate_wild_do_table](#replicate_wild_do_table)
* [replicate_wild_ignore_table](#replicate_wild_ignore_table)

#

## Row-Based Logging

When an event is logged in its row-based format, many replication filters that affect a database will test the filter against the database that is actually affected by the event.

Similarly, when an event is logged in its row-based format, many replication filters that affect a table will test the filter against the table in the the database that is actually affected by the event.

This means that cross-database updates work with replication filters and statement-based binary logging.

Keep in mind that DDL statements are always logged to the [binary log](../../programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) in statement-based format, even when the [binlog_format](replication-and-binary-log-system-variables.md#binlog_format) system variable is set to `ROW`. This means that the notes mentioned in [Statement-Based Logging](#statement-based-logging) always apply to DDL.

#

# Replication Filters and Galera Cluster

When using Galera cluster, replication filters should be used with caution. See [Configuring MariaDB Galera Cluster: Replication Filters](../galera-cluster/configuring-mariadb-galera-cluster.md#replication-filters) for more details.

#

# See Also

* [Dynamic replication filters — our wheel will be square!](https://mariadb.org/dynamic-replication-filters-our-wheel-will-be-square/)