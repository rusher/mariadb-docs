# Setting Up Replication

The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.

Getting [replication](broken-reference) working involves steps on both the master server/s and steps on the replica server/s.

### Setting up a Replication Replica with MariaDB-Backup

If you would like to use [Mariabackup](../../server-management/backing-up-and-restoring-databases/mariabackup/) to set up a replication slave, then you might find the information at [Setting up a Replication Replica with MariaDB-Backup](../../server-management/backing-up-and-restoring-databases/mariabackup/setting-up-a-replica-with-mariabackup.md) helpful.

### Versions

In general, when replicating across different versions of MariaDB, it is best that the master is an older version than the slave. MariaDB versions are usually backward compatible, while of course older versions cannot always be forward compatible. See also [Replicating from MySQL Master to MariaDB Replica](setting-up-replication.md#replicating-from-mysql-master-to-mariadb-slave).

### Configuring the Master

* Enable binary logging if it's not already enabled. See [Activating the Binary Log](../../server-management/server-monitoring-logs/binary-log/activating-the-binary-log.md) and [Binary log formats](../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) for details.
* Give the master a unique [server\_id](replication-and-binary-log-system-variables.md#server_id). All slaves must also be given a server\_id. This can be a number from 1 to 232-1, and must be unique for each server in the replicating group.
* Specify a unique name for your replication logs with [--log-basename](../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md). If this is not specified your host name will be used and there will be problems if the hostname ever changes.
* Slaves will need permission to connect and start replicating from a server. Usually this is done by creating a dedicated slave user, and granting that user permission only to replicate (REPLICATION SLAVE permission).

#### Example Enabling Replication for MariaDB

Add the following into your [my.cnf](../../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md) file and restart the database.

```
[mariadb]
log-bin
server_id=1
log-basename=master1
binlog-format=mixed
```

The server id is a unique number for each MariaDB/MySQL server in your network.[binlog-format](../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) specifies how your statements are logged. This mainly affects the size of the [binary log](../../server-management/server-monitoring-logs/binary-log/) that is sent between the Master and the Replicas.

Then execute the following SQL with the [mysql](../../clients-and-utilities/mariadb-client/mysql-command-line-client.md) command line client:

```
CREATE USER 'replication_user'@'%' IDENTIFIED BY 'bigs3cret';
GRANT REPLICATION SLAVE ON *.* TO 'replication_user'@'%';
```

#### Example Enabling Replication for MySQL

If you want to enable replication from MySQL 5.7 or earlier to MariaDB, you can do it in almost the same way as between MariaDB servers. The main difference is that MySQL doesn't support `log-basename`.

```
[mysqld]
log-bin
server_id=1
```

For replication from MySQL 8.0 to MariaDB [requires slight more configurations](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/mariadb-vs-mysql-compatibility#mysql-80).

### Settings to Check

There are a number of options that may impact or break replication. Check the following settings to avoid problems.

* [skip-networking](../optimization-and-tuning/system-variables/server-system-variables.md#skip_networking). If `skip-networking=1`, the server will limit connections to localhost only, and prevent all remote slaves from connecting.
* [bind-address](../optimization-and-tuning/system-variables/server-system-variables.md#bind_address). Similarly, if the address the server listens for TCP/IP connections is 127.0.0.1 (localhost), remote slaves connections will fail.

### Configuring the Replica

* Give the slave a unique [server\_id](replication-and-binary-log-system-variables.md). All servers, whether masters or replicas, are given a server\_id. This can be a number from 1 to 232-1, and must be unique for each server in the replicating group. The server will need to be restarted in order for a change in this option to take effect.

### Getting the Master's Binary Log Co-ordinates

Now you need prevent any changes to the data while you view the binary log position. You'll use this to tell the slave at exactly which point it should start replicating from.

* On the master, flush and lock all tables by running `FLUSH TABLES WITH READ LOCK`. Keep this session running - exiting it will release the lock.
* Get the current position in the binary log by running `[SHOW MASTER STATUS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-binlog-status.md)`:

```
SHOW MASTER STATUS;
+--------------------+----------+--------------+------------------+
| File               | Position | Binlog_Do_DB | Binlog_Ignore_DB |
+--------------------+----------+--------------+------------------+
| master1-bin.000096 |      568 |              |                  |
+--------------------+----------+--------------+------------------+
```

* Record the File and Position details. If binary logging has just been enabled, these will be blank.
* Now, with the lock still in place, copy the data from the master to the slave. See [Backup, Restore and Import](../../clients-and-utilities/backup-restore-and-import-clients/) for details on how to do this.
* Note for live databases: You just need to make a local copy of the data, you don't need to keep the master locked until the slave has imported the data.
* Once the data has been copied, you can release the lock on the master by running [UNLOCK TABLES](../../reference/sql-statements/transactions/lock-tables.md).

```
UNLOCK TABLES;
```

### Start the Slave

* Once the data has been imported, you are ready to start replicating. Begin by running a [CHANGE MASTER TO](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md), making sure that MASTER\_LOG\_FILE matches the file and MASTER\_LOG\_POS the position returned by the earlier SHOW MASTER STATUS. For example:

```
CHANGE MASTER TO
  MASTER_HOST='master.domain.com',
  MASTER_USER='replication_user',
  MASTER_PASSWORD='bigs3cret',
  MASTER_PORT=3306,
  MASTER_LOG_FILE='master1-bin.000096',
  MASTER_LOG_POS=568,
  MASTER_CONNECT_RETRY=10;
```

If you are starting a slave against a fresh master that was configured for replication from the start, then you don't have to specify `MASTER_LOG_FILE` and `MASTER_LOG_POS`.

#### Use Global Transaction Id (GTID)

It is generally recommended to use (GTIDs), as it has a number of benefits. All that is needed is to add the `MASTER_USE_GTID` option to the `CHANGE MASTER` statement, for example:

```
CHANGE MASTER TO MASTER_USE_GTID = slave_pos
```

See [Global Transaction ID](gtid.md) for a full description.\
<>

* Now start the slave with the [START SLAVE](../../reference/sql-statements/administrative-sql-statements/replication-statements/start-replica.md) command:

```
START SLAVE;
```

* Check that the replication is working by executing the [SHOW SLAVE STATUS](../../reference/sql-statements/administrative-sql-statements/show/show-replica-status.md) command:

```
SHOW SLAVE STATUS \G
```

* If replication is working correctly, both the values of `Slave_IO_Running` and `Slave_SQL_Running` should be `Yes`:

```
Slave_IO_Running: Yes
Slave_SQL_Running: Yes
```

### Replicating from MySQL Master to MariaDB Replica

* Replicating from MySQL 5.5 to MariaDB should just work. When using a MariaDB as a replica, it may be necessary to set [binlog\_checksum](replication-and-binary-log-system-variables.md) to NONE.
* Replicating from MySQL 5.6 without GTID to MariaDB 10+ should work.
* Replication from MySQL 5.6 with GTID, binlog\_rows\_query\_log\_events and ignorable events works. In this case MariaDB will remove the MySQL GTIDs and other unneeded events and instead adds its own GTIDs.
* \[Replication from MySQL 8.

## to MariaDB]\(https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/mariadb-vs-mysql-compatibility#mysql-80) requires [MariaDB 11.4.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-11-4-series/mariadb-11-4-5-release-notes) or newer.

### See Also

* [Differences between Statement-based, mixed and row logging](../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md)
* [Replication and Foreign Keys](replication-and-foreign-keys.md)
* [Replication as a Backup Solution](../../server-management/backing-up-and-restoring-databases/replication-as-a-backup-solution.md)
* [Multi-source Replication](multi-source-replication.md)
* [Global Transaction ID](gtid.md)
* [Parallel Replication](parallel-replication.md)
* [Replication and Binary Log System Variables](replication-and-binary-log-system-variables.md)
* [Replication and Binary Log Status Variables](replication-and-binary-log-status-variables.md)
* [Semisynchronous Replication](semisynchronous-replication.md)
* [Delayed Replication](delayed-replication.md)
* [Replication Compatibility Between MariaDB and MySQL](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/replication-compatibility-between-mariadb-and-mysql)

CC BY-SA / Gnu FDL
