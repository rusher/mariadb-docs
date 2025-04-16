
# OLD_MODE

The [old_mode](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old_mode) system variable was introduced in [MariaDB 5.5.35](../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5535-release-notes.md) to replace the [old](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old) variable with a new one with better granularity.



MariaDB supports several different modes which allow you to tune it to suit your needs.


The most important ways for doing this are with [SQL_MODE](sql-mode.md) and `OLD_MODE`.


[SQL_MODE](sql-mode.md) is used for getting MariaDB to emulate behavior from other SQL servers, while `OLD_MODE` is used for emulating behavior from older MariaDB or MySQL versions.


`OLD_MODE` is a string with different options separated by commas ('`,`') without spaces. The options are case insensitive.


Normally `OLD_MODE` should be empty. It's mainly used to get old behavior when switching to MariaDB or to a new major version of MariaDB, until you have time to fix your application.


Between major versions of MariaDB various options supported by `OLD_MODE` may be removed. This is intentional as we assume that the application will be fixed to conform with the new MariaDB behavior between releases.


In other words, `OLD_MODE` options are by design deprecated from the day they were added and will eventually be removed [as any other deprecated feature](../../../release-notes/mariadb-feature-deprecation-policy.md).


You can check the variable's local and global value with:


```
SELECT @@OLD_MODE, @@GLOBAL.OLD_MODE;
```

You can set the `<span class="n">OLD_MODE</span>
` either from the
[command line](../getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) (option `--old-mode`) or by setting the [old_mode](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old_mode) system variable.


Non-default old mode features are deprecated by design, and from [MariaDB 11.3](../../../release-notes/mariadb-community-server/what-is-mariadb-113.md), a warning will be issued when set.


## Modes


The different values of `OLD_MODE` are:


### COMPAT_5_1_CHECKSUM


From [MariaDB 10.9](../../../release-notes/mariadb-community-server/what-is-mariadb-109.md), the [--old option](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old) is deprecated. This option allows behaviour of the --old option for enabling the old-style checksum for `CHECKSUM TABLE` that MySQL 5.1 supports


### IGNORE_INDEX_ONLY_FOR_JOIN


From [MariaDB 10.9](../../../release-notes/mariadb-community-server/what-is-mariadb-109.md), the [--old option](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old) is deprecated. This option allows behaviour of the --old option for disabling the index only for joins, but allow it for ORDER BY.


### LOCK_ALTER_TABLE_COPY


From [MariaDB 11.2](../../../release-notes/mariadb-community-server/what-is-mariadb-112.md). The non-locking copy ALTER introduced in [MDEV-16329](https://jira.mariadb.org/browse/MDEV-16329) should be beneficial in the vast majority of cases, but scenarios can exist which significantly impact performance. For example, RBR on tables without a primary key. When non-locking ALTER is performed on such a table, and DML affecting a large number of records is run in parallel, the ALTER can become extremely slow, and further DML can also be affected. If there is a chance of such scenarios (and no possibility of improving the schema by immediately adding primary keys), ALTER should be performed with the explicit LOCK=SHARED clause. If this is also impossible, then LOCK_ALTER_TABLE_COPY flag should be added to the old_mode variable until the schema can be improved.


### NO_DUP_KEY_WARNINGS_WITH_IGNORE


Don't print duplicate key warnings when using INSERT [IGNORE](../../reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/ignore.md).


### NO_NULL_COLLATION_IDS


A compatibility setting to support connectors (in particular MySQL Connector/NET) that give an exception when collation ids returned by [SHOW COLLATION](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-collation.md) are NULL. It is automatically set when a MySQL Connector/NET connection is determined. From [MariaDB 10.11.7](../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-7-release-notes.md), [MariaDB 11.0.5](../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes.md), [MariaDB 11.1.4](../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes.md), [MariaDB 11.2.3](../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes.md).


### NO_PROGRESS_INFO


Don't show progress information in [SHOW PROCESSLIST](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-processlist.md).


### OLD_FLUSH_STATUS


From [MariaDB 11.5](../../../release-notes/mariadb-community-server/what-is-mariadb-115.md), restores the pre-[MariaDB 11.5](../../../release-notes/mariadb-community-server/what-is-mariadb-115.md) behavior of [FLUSH STATUS](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md#flush-status).


### SESSION_USER_IS_USER


From [MariaDB 11.7](../../../release-notes/mariadb-community-server/what-is-mariadb-117.md), restores the pre-[MariaDB 11.7](../../../release-notes/mariadb-community-server/what-is-mariadb-117.md) behavior of [SESSION_USER](../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/session_user.md).


### UTF8_IS_UTF8MB3


From [MariaDB 10.6.1](../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md), the main name of the previous 3 byte `utf` [character set](../../reference/data-types/string-data-types/character-sets/README.md) has been changed to `utf8mb3`. If set, the default, `utf8` is an alias for `utf8mb3`. If not set, `utf8` would be an alias for `utf8mb4`.


### ZERO_DATE_TIME_CAST


When a [TIME](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/time_ms-column-in-information_schemaprocesslist.md) value is cast to a [DATETIME](../../reference/data-types/date-and-time-data-types/datetime.md), the date part will be `0000-00-00`, not [CURRENT_DATE](../../reference/sql-statements-and-structure/sql-statements/built-in-functions/date-time-functions/curdate.md) (as dictated by the SQL standard).


## OLD_MODE and Stored Programs


In contrast to [SQL_MODE](sql-mode.md), [stored programs](../../server-usage/programming-customizing-mariadb/stored-routines/README.md) use the current user's `OLD_MODE`value.


Changes to `OLD_MODE` are not sent to replicas.


## Examples


This example shows how to get a readable list of enabled OLD_MODE flags:


```
SELECT REPLACE(@@OLD_MODE, ',', '\n');
+---------------------------------------------------+
| REPLACE(@@OLD_MODE, ',', '\n')                    |
+---------------------------------------------------+
| NO_DUP_KEY_WARNINGS_WITH_IGNORE                   |
| NO_PROGRESS_INFO                                  |
+---------------------------------------------------+
```

Adding a new flag:


```
SET @@OLD_MODE = CONCAT(@@OLD_MODE, ',NO_PROGRESS_INFO');
```

If the specified flag is already ON, the above example has no effect but does not produce an error.


How to unset a flag:


```
SET @@OLD_MODE = REPLACE(@@OLD_MODE, 'NO_PROGRESS_INFO', '');
```

How to check if a flag is set:


```
SELECT @@OLD_MODE LIKE '%NO_PROGRESS_INFO';
+------------------------------------+
| @@OLD_MODE LIKE '%NO_PROGESS_INFO' |
+------------------------------------+
|                                  1 |
+------------------------------------+
```

From [MariaDB 11.3](../../../release-notes/mariadb-community-server/what-is-mariadb-113.md):


```
SET @@OLD_MODE = CONCAT(@@OLD_MODE, ',NO_PROGRESS_INFO');
Query OK, 0 rows affected, 1 warning (0.000 sec)

SHOW WARNINGS;
+---------+------+--------------------------------------------------------------------------+
| Level   | Code | Message                                                                  |
+---------+------+--------------------------------------------------------------------------+
| Warning | 1287 | 'NO_PROGRESS_INFO' is deprecated and will be removed in a future release |
+---------+------+--------------------------------------------------------------------------+
```
