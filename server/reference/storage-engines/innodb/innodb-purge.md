
# InnoDB Purge


When a transaction updates a row in an InnoDB table, InnoDB's MVCC implementation keeps old versions of the row in the [InnoDB undo log](innodb-undo-log.md). The old versions are kept at least until all transactions older than the transaction that updated the row are no longer open. At that point, the old versions can be deleted. InnoDB has purge process that is used to delete these old versions.


## Optimizing Purge Performance


### Configuring the Purge Threads


The number of purge threads can be set by configuring the [innodb_purge_threads](innodb-system-variables.md#innodb_purge_threads) system variable. This system variable can be specified as a command-line argument to [mysqld](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
innodb_purge_threads = 6
```

### Configuring the Purge Batch Size


The purge batch size is defined as the number of [InnoDB redo log](innodb-redo-log.md) records that must be written before triggering purge. The purge batch size can be set by configuring the [innodb_purge_batch_size](innodb-system-variables.md#innodb_purge_batch_size) system variable. This system variable can be specified as a command-line argument to [mysqld](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
innodb_purge_batch_size = 50
```

### Configuring the Max Purge Lag


If purge operations are lagging on a busy server, then this can be a tough situation to recover from. As a solution, InnoDB allows you to set the max purge lag. The max purge lag is defined as the maximum number of [InnoDB undo log](innodb-undo-log.md) that can be waiting to be purged from the history until InnoDB begins delaying DML statements.


The max purge lag can be set by configuring the [innodb_max_purge_lag](innodb-system-variables.md#innodb_max_purge_lag) system variable. This system variable can be changed dynamically with [SET GLOBAL](../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md#global-session). For example:


```
SET GLOBAL innodb_max_purge_lag=1000;
```

This system variable can also be specified as a command-line argument to [mysqld](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
innodb_max_purge_lag = 1000
```

The maximum delay can be set by configuring the [innodb_max_purge_lag_delay](innodb-system-variables.md#innodb_max_purge_lag_delay) system variable. This system variable can be changed dynamically with [SET GLOBAL](../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md#global-session). For example:


```
SET GLOBAL innodb_max_purge_lag_delay=100;
```

This system variable can also be specified as a command-line argument to [mysqld](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
innodb_max_purge_lag_delay = 100
```

### Configuring the Purge Rollback Segment Truncation Frequency


The purge rollback segment truncation frequency is defined as the number of purge loops that are run before unnecessary rollback segments are truncated. The purge rollback segment truncation frequency can be set by configuring the [innodb_purge_rseg_truncate_frequency](innodb-system-variables.md#innodb_purge_rseg_truncate_frequency) system variable. This system variable can be changed dynamically with [SET GLOBAL](../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md#global-session). For example:


```
SET GLOBAL innodb_purge_rseg_truncate_frequency=64;
```

This system variable can also be specified as a command-line argument to [mysqld](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
innodb_purge_rseg_truncate_frequency = 64
```

### Configuring the Purge Undo Log Truncation


Purge undo log truncation occurs when InnoDB truncates an entire [InnoDB undo log](innodb-undo-log.md) tablespace, rather than deleting individual [InnoDB undo log](innodb-undo-log.md) records.


Purge undo log truncation can be enabled by configuring the [innodb_undo_log_truncate](innodb-system-variables.md#innodb_undo_log_truncate) system variable. This system variable can be changed dynamically with [SET GLOBAL](../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md#global-session). For example:


```
SET GLOBAL innodb_undo_log_truncate=ON;
```

This system variable can also be specified as a command-line argument to [mysqld](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
innodb_undo_log_truncate = ON
```

An [InnoDB undo log](innodb-undo-log.md) tablespace is truncated when it exceeds the maximum size that is configured for [InnoDB undo log](innodb-undo-log.md) tablespaces. The maximum size can be set by configuring the [innodb_max_undo_log_size](innodb-system-variables.md#innodb_max_undo_log_size) system variable. This system variable can be changed dynamically with [SET GLOBAL](../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md#global-session). For example:


```
SET GLOBAL innodb_max_undo_log_size='64M';
```

This system variable can also be specified as a command-line argument to [mysqld](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
[mariadb]
...
innodb_max_undo_log_size = 64M
```

## Purge's Effect on Row Metadata


An InnoDB table's clustered index has three hidden system columns that are automatically generated. These hidden system columns are:


* `<code>DB_ROW_ID</code>` - If the table has no other `<code>PRIMARY KEY</code>` or no other `<code>UNIQUE KEY</code>` defined as `<code>NOT NULL</code>` that can be promoted to the table's `<code>PRIMARY KEY</code>`, then InnoDB will use a hidden system column called `<code>DB_ROW_ID</code>`. InnoDB will automatically generated the value for the column from a global InnoDB-wide 48-bit sequence (instead of being table-local).
* `<code>DB_TRX_ID</code>` - The transaction ID of either the transaction that last changed the row or the transaction that currently has the row locked.
* `<code>DB_ROLL_PTR</code>` - A pointer to the [InnoDB undo log](innodb-undo-log.md) that contains the row's previous record. The value of `<code>DB_ROLL_PTR</code>` is only valid if `<code>DB_TRX_ID</code>` belongs to the current read view. The oldest valid read view is the purge view.


If a row's last [InnoDB undo log](innodb-undo-log.md) record is purged, this can obviously effect the value of the row's `<code>DB_ROLL_PTR</code>` column, because there would no longer be any [InnoDB undo log](innodb-undo-log.md) record for the pointer to reference.


In [MariaDB 10.2](../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md) and before, the purge process wouldn't touch the value of the row's `<code>DB_TRX_ID</code>` column.


However, in [MariaDB 10.3](../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md) and later, the purge process will set a row's `<code>DB_TRX_ID</code>` column to `<code>0</code>` after all of the row's associated [InnoDB undo log](innodb-undo-log.md) records have been deleted. This change allows InnoDB to perform an optimization: if a query wants to read a row, and if the row's `<code>DB_TRX_ID</code>` column is set to `<code>0</code>`, then it knows that no other transaction has the row locked. Usually, InnoDB needs to lock the transaction system's mutex in order to safely check whether a row is locked, but this optimization allows InnoDB to confirm that the row can be safely read without any heavy internal locking.


This optimization can speed up reads, but it come at a noticeable cost at other times. For example, it can cause the purge process to use more I/O after inserting a lot of rows, since the value of each row's `<code>DB_TRX_ID</code>` column will have to be reset.

