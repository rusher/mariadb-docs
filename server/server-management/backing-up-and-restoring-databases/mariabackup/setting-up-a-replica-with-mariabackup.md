
# Setting up a Replica with Mariabackup

The terms *master* and *slave* have historically been used in replication, and MariaDB has begun the process of adding *primary* and *replica* synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.




Mariabackup makes it very easy to set up a [replica](../../../server-usage/replication-cluster-multi-master/standard-replication/README.md) using a [full backup](full-backup-and-restore-with-mariabackup.md). This page documents how to set up a replica from a backup.


If you are using [MariaDB Galera Cluster](../../../server-usage/replication-cluster-multi-master/galera-cluster/README.md), then you may want to try one of the following pages instead:


* [Configuring MariaDB Replication between MariaDB Galera Cluster and MariaDB Server](/kb/en/using-mariadb-replication-with-mariadb-galera-cluster-configuring-mariadb-r/)
* [Configuring MariaDB Replication between Two MariaDB Galera Clusters](../../../server-usage/replication-cluster-multi-master/galera-cluster/using-mariadb-replication-with-mariadb-galera-cluster/configuring-mariadb-replication-between-two-mariadb-galera-clusters.md)


## Backup the Database and Prepare It


The first step is to simply take and prepare a fresh [full backup](full-backup-and-restore-with-mariabackup.md) of a database server in the [replication topology](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-overview.md#common-replication-setups). If the source database server is the desired replication primary, then we do not need to add any additional options when taking the full backup. For example:


```
$ mariabackup --backup \
   --target-dir=/var/mariadb/backup/ \
   --user=mariabackup --password=mypassword
```

If the source database server is a [replica](../../../server-usage/replication-cluster-multi-master/standard-replication/README.md) of the desired primary, then we should add the [--slave-info](mariabackup-options.md#-slave-info) option, and possibly the [--safe-slave-backup](mariabackup-options.md#-safe-slave-backup) option. For example:


```
$ mariabackup --backup \
   --slave-info --safe-slave-backup \
   --target-dir=/var/mariadb/backup/ \
   --user=mariabackup --password=mypassword
```

And then we would prepare the backup as you normally would. For example:


```
$ mariabackup --prepare \
   --target-dir=/var/mariadb/backup/
```

## Copy the Backup to the New Replica


Once the backup is done and prepared, we can copy it to the new replica. For example:


```
$ rsync -avP /var/mariadb/backup dbserver2:/var/mariadb/backup
```

## Restore the Backup on the New Replica


At this point, we can restore the backup to the [datadir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#datadir), as you normally would. For example:


```
$ mariabackup --copy-back \
   --target-dir=/var/mariadb/backup/
```

And adjusting file permissions, if necessary:


```
$ chown -R mysql:mysql /var/lib/mysql/
```

## Create a Replication User on the Primary


Before the new replica can begin replicating from the primary, we need to [create a user account](../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user.md) on the primary that the replica can use to connect, and we need to [grant](../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md) the user account the [REPLICATION SLAVE](../../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#global-privileges) privilege. For example:


```
CREATE USER 'repl'@'dbserver2' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.*  TO 'repl'@'dbserver2';
```

## Configure the New Replica


Before we start the server on the new replica, we need to configure it. At the very least, we need to ensure that it has a unique [server_id](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#server_id) value. We also need to make sure other replication settings are what we want them to be, such as the various [GTID system variables](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md#system-variables-for-global-transaction-id), if those apply in the specific environment.


Once configuration is done, we can [start the MariaDB Server process](https://mariadb.com/kb/en/) on the new replica.


## Start Replication on the New Replica


At this point, we need to get the replication coordinates of the primary from the original backup directory.


If we took the backup on the primary, then the coordinates will be in the [xtrabackup_binlog_info](files-created-by-mariabackup.md#xtrabackup_binlog_info) file. If we took the backup on another replica and if we provided the [--slave-info](mariabackup-options.md#-slave-info) option, then the coordinates will be in the file [xtrabackup_slave_info](files-created-by-mariabackup.md#xtrabackup_slave_info) file.


Mariabackup dumps replication coordinates in two forms: [GTID](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md) coordinates and [binary log](../../server-monitoring-logs/binary-log/README.md) file and position coordinates, like the ones you would normally see from [SHOW MASTER STATUS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-binlog-status.md) output. We can choose which set of coordinates we would like to use to set up replication.


For example:


```
mariadb-bin.000096 568 0-1-2
```

Regardless of the coordinates we use, we will have to set up the primary connection using [CHANGE MASTER TO](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) and then start the replication threads with [START SLAVE](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/start-replica.md).


### GTIDs


If we want to use GTIDs, then we will have to first set [gtid_slave_pos](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md#gtid_slave_pos) to the [GTID](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md) coordinates that we pulled from either the [xtrabackup_binlog_info](files-created-by-mariabackup.md#xtrabackup_binlog_info) file or the [xtrabackup_slave_info](files-created-by-mariabackup.md#xtrabackup_slave_info) file in the backup directory. For example:


```
$ cat xtrabackup_binlog_info
mariadb-bin.000096 568 0-1-2
```

And then we would set `MASTER_USE_GTID=slave_pos` in the [CHANGE MASTER TO](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) command. For example:


```
SET GLOBAL gtid_slave_pos = "0-1-2";
CHANGE MASTER TO 
   MASTER_HOST="dbserver1", 
   MASTER_PORT=3306, 
   MASTER_USER="repl",  
   MASTER_PASSWORD="password", 
   MASTER_USE_GTID=slave_pos;
START SLAVE;
```

### File and Position


If we want to use the [binary log](../../server-monitoring-logs/binary-log/README.md) file and position coordinates, then we would set `MASTER_LOG_FILE` and `MASTER_LOG_POS` in the [CHANGE MASTER TO](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) command to the file and position coordinates that we pulled; either the [xtrabackup_binlog_info](files-created-by-mariabackup.md#xtrabackup_binlog_info) file or the [xtrabackup_slave_info](files-created-by-mariabackup.md#xtrabackup_slave_info) file in the backup directory, depending on whether the backup was taken from the primary or from a replica of the primary. For example:


```
CHANGE MASTER TO 
   MASTER_HOST="dbserver1", 
   MASTER_PORT=3306, 
   MASTER_USER="repl",  
   MASTER_PASSWORD="password", 
   MASTER_LOG_FILE='mariadb-bin.000096',
   MASTER_LOG_POS=568;
START SLAVE;
```

## Check the Status of the New Replica


We should be done setting up the replica now, so we should check its status with [SHOW SLAVE STATUS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-replica-status.md). For example:


```
SHOW SLAVE STATUS\G
```
