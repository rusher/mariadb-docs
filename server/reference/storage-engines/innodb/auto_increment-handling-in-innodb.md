
# AUTO_INCREMENT Handling in InnoDB


## AUTO_INCREMENT Lock Modes


The [innodb_autoinc_lock_mode](innodb-system-variables.md#innodb_autoinc_lock_mode) system variable determines the lock mode when generating [AUTO_INCREMENT](auto_increment-handling-in-innodb.md) values for [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) tables. These modes allow [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) to make significant performance optimizations in certain circumstances.


The [innodb_autoinc_lock_mode](innodb-system-variables.md#innodb_autoinc_lock_mode) system variable may be removed in a future release. See [MDEV-19577](https://jira.mariadb.org/browse/MDEV-19577) for more information.


### Traditional Lock Mode


When [innodb_autoinc_lock_mode](innodb-system-variables.md#innodb_autoinc_lock_mode) is set to `<code>0</code>`, [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) uses the traditional lock mode.


In this mode, [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) holds a table-level lock for all [INSERT](../../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/insert-function.md) statements until the statement completes.


### Consecutive Lock Mode


When [innodb_autoinc_lock_mode](innodb-system-variables.md#innodb_autoinc_lock_mode) is set to `<code>1</code>`, [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) uses the consecutive lock mode.


In this mode, [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) holds a table-level lock for all bulk [INSERT](../../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/insert-function.md) statements (such as [LOAD DATA](../../sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) or [INSERT ... SELECT](../../sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert-select.md)) until the end of the statement. For simple [INSERT](../../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/insert-function.md) statements, no table-level lock is held. Instead, a lightweight mutex is used which scales significantly better. This is the default setting.


### Interleaved Lock Mode


When [innodb_autoinc_lock_mode](innodb-system-variables.md#innodb_autoinc_lock_mode) is set to `<code>2</code>`, [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) uses the interleaved lock mode.


In this mode, [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) does not hold any table-level locks at all. This is the fastest and most scalable mode, but is not safe for [statement-based](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based) replication.


## Setting AUTO_INCREMENT Values


The [AUTO_INCREMENT](auto_increment-handling-in-innodb.md) value for an [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) table can be set for a table by executing the [ALTER TABLE](../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md) statement and specifying the [AUTO_INCREMENT](../../sql-statements-and-structure/vectors/create-table-with-vectors.md#auto_increment) table option. For example:


```
ALTER TABLE tab AUTO_INCREMENT=100;
```

However, in [MariaDB 10.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md) and before, [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) stores the table's [AUTO_INCREMENT](auto_increment-handling-in-innodb.md) counter in memory. In these versions, when the server restarts, the counter is re-initialized to the highest value found in the table. This means that the above operation can be undone if the server is restarted before any rows are written to the table.


In [MariaDB 10.2.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1024-release-notes.md) and later, the [AUTO_INCREMENT](auto_increment-handling-in-innodb.md) counter is persistent, so this restriction is no longer present. Persistent, however, does not mean transactional. Gaps may still occur in some cases, such as if a [INSERT IGNORE](../../sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert-ignore.md) statement fails, or if a user executes [ROLLBACK](../../sql-statements-and-structure/sql-statements/transactions/rollback.md) or [ROLLBACK TO SAVEPOINT](../../sql-statements-and-structure/sql-statements/transactions/savepoint.md).


For example:


```
CREATE TABLE t1 (pk INT AUTO_INCREMENT PRIMARY KEY, i INT, UNIQUE (i)) ENGINE=InnoDB;

INSERT INTO t1 (i) VALUES (1),(2),(3);
INSERT IGNORE INTO t1 (pk, i) VALUES (100,1);
Query OK, 0 rows affected, 1 warning (0.099 sec)

SELECT * FROM t1;
+----+------+
| pk | i    |
+----+------+
|  1 |    1 |
|  2 |    2 |
|  3 |    3 |
+----+------+

SHOW CREATE TABLE t1\G
*************************** 1. row ***************************
       Table: t1
Create Table: CREATE TABLE `t1` (
  `pk` int(11) NOT NULL AUTO_INCREMENT,
  `i` int(11) DEFAULT NULL,
  PRIMARY KEY (`pk`),
  UNIQUE KEY `i` (`i`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1
```

If the server is restarted at this point, then the [AUTO_INCREMENT](auto_increment-handling-in-innodb.md) counter will revert to `<code>101</code>`, which is the persistent value set as part of the failed [INSERT IGNORE](../../sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert-ignore.md).


```
# Restart server
SHOW CREATE TABLE t1\G
*************************** 1. row ***************************
       Table: t1
Create Table: CREATE TABLE `t1` (
  `pk` int(11) NOT NULL AUTO_INCREMENT,
  `i` int(11) DEFAULT NULL,
  PRIMARY KEY (`pk`),
  UNIQUE KEY `i` (`i`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=latin1
```

## See Also


* [AUTO_INCREMENT](auto_increment-handling-in-innodb.md)
* [AUTO_INCREMENT FAQ](../../data-types/auto_increment-faq.md)
* [LAST_INSERT_ID](../../sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/last_insert_id.md)
* [Sequences](../../sql-statements-and-structure/sequences/README.md) - an alternative to auto_increment available from [MariaDB 10.3](../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md)

