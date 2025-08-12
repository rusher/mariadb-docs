# Migration from MySQL to MariaDB Cluster using Replication

This guide migrates a live database from a MySQL Galera Cluster to a MariaDB Galera Cluster. The migration strategy requires setting up a new MariaDB Cluster and using asynchronous replication to sync it with the existing MySQL Cluster. The method includes a reliable failback route.

{% hint style="info" %}
This document focuses on the migration process itself. For detailed comparisons between the two database systems, please refer to [Incompatibilities and Feature Differences Between MariaDB and MySQL](https://mariadb.com/docs/release-notes/community-server/about/compatibility-and-differences/incompatibilities-and-feature-differences-between-mariadb-rolling-and-mysql).
{% endhint %}

### I. Prerequisites

* **MySQL Server**: A running MySQL Galera Cluster (version 8.0 or 8.4) to migrate.
* **MariaDB Server**: The target MariaDB version that supports Galera Cluster. This guide assumes the latest stable version.
* **`mysqldump`**: A command-line utility by MySQL to create initial database backup.&#x20;

{% hint style="warning" %}
Due to changes in MySQL 8.0+, `mariadb-dump` may not be compatible for this initial step.
{% endhint %}

* **Root or Sudo Access**: Administrative privileges are required on all servers involved in the migration.

### II. Migration Steps

#### Step 1: Check for Incompatibilities

{% hint style="warning" %}
While MariaDB maintains a high degree of compatibility with MySQL, it is crucial to review any differences that could impact your applications.
{% endhint %}

* **Version Compatibility**: Select a MariaDB version compatible with your MySQL version for replication.
* **Feature Differences**: Review the [Incompatibilities and Feature Differences](https://mariadb.com/docs/release-notes/community-server/about/compatibility-and-differences/incompatibilities-and-feature-differences-between-mariadb-rolling-and-mysql) to identify any deprecated features or changes in system tables, user accounts, and authentication that might affect your setup.

**Replication Compatibility**

| MySQL Version | Compatible MariaDB Version                  |
| ------------- | ------------------------------------------- |
| 5.7           | 10.2 and newer                              |
| 8.0           | 10.6.21, 10.11.11, 11.4.5, 11.7.2 and newer |

For more details, see MySQL to MariaDB Replication Compatibility.

#### Step 2: Install and Configure a New MariaDB Galera Cluster

Set up a new, empty MariaDB Galera Cluster that will become the target for the migration.

**2.1. Install MariaDB Server and Galera Provider**

Install MariaDB Server package and Galera wsrep provider library on each node of the new cluster. Refer [Install and Upgrade MariaDB](../../upgrading/) for detailed instructions.

**2.2. Configure Each MariaDB Node**

Create a configuration file at `/etc/mysql/conf.d/galera.cnf` on each node. The configuration will be mostly identical across nodes, except for node-specific details like `wsrep_node_name` and `wsrep_node_address`.

**Example `galera.cnf`:**

```ini
[mysqld]
# MariaDB settings
binlog_format=ROW
default_storage_engine=InnoDB
innodb_autoinc_lock_mode=2
bind-address=0.0.0.0

# Galera Provider Configuration
wsrep_on=ON
wsrep_provider=/usr/lib/galera/libgalera_smm.so # Adjust path if necessary

# Galera Cluster Configuration
wsrep_cluster_name="new_mariadb_cluster"
wsrep_cluster_address="gcomm://node1_ip,node2_ip,node3_ip"

# Node-specific Configuration
wsrep_node_name="mariadb_node1"
wsrep_node_address="node1_ip"

# SST Configuration
wsrep_sst_method=mariadb-backup

```

{% hint style="info" %}
It is recommended to set `wsrep_sst_method` on all nodes to ensure consistency during State Snapshot Transfers (SST).
{% endhint %}

#### Step 3: Back Up the MySQL Database

A full logical backup of the MySQL database is required to seed the new MariaDB Cluster.

**3.1. Enable Binary Logging on MySQL**

Asynchronous replication requires the binary log to be enabled on the MySQL source. If not enabled, enable it on at least one node in your MySQL cluster.

1. **Edit `my.cnf`**: In the `[mysqld]` section of your MySQL configuration file, add `log-bin=mysql-bin`.
2. **Restart MySQL**: A server restart is required for the change to take effect.&#x20;

{% hint style="danger" %}
Restarting MySQL will cause a brief outage for the node.
{% endhint %}

**3.2. Create the Backup with `mysqldump`**

Use `mysqldump` from the source MySQL server to create a full backup. Using `--all-databases` and `--master-data` will include all databases and the binary log position needed to start replication.

```bash
mysqldump --user=backup_user --password --all-databases --master-data=2 > /path/to/backup.sql

```

> This above command generates a backup file and logs the source's binary log file name and position in the output.

#### Step 4: Bootstrap the MariaDB Cluster and Restore Data

Start the first node of the MariaDB cluster and load the MySQL backup.

**4.1. Bootstrap the First Node**

Start the first MariaDB node with the `--wsrep-new-cluster` option. This initializes the cluster.

```bash
sudo galera_new_cluster

```

**4.2. Load the Backup File**

Transfer the `backup.sql` file to the first MariaDB node and import it:'

```bash
mariadb -u root -p < /path/to/backup.sql

```

**4.3. Start Subsequent Nodes**

Start the MariaDB service normally on the remaining nodes. They will connect to the first node, and a State Snapshot Transfer (SST) will automatically sync their data.

```bash
sudo systemctl start mariadb

```

**4.4. Verify the Cluster**

Connect to any node and check the cluster size to ensure all nodes have joined successfully.

```sql
SHOW STATUS LIKE 'wsrep_cluster_size';

```

The value should match the number of nodes in your cluster.

#### Step 5: Set Up Asynchronous Replication

Configure one of the MariaDB nodes to act as a replica of the source MySQL cluster.

**5.1. Create a Replication User on MySQL**

On the MySQL source node where binlogging is enabled, create a dedicated user for replication.

```sql
CREATE USER 'repl_user'@'mariadb_node_ip' IDENTIFIED BY 'your_password';
GRANT REPLICATION SLAVE ON *.* TO 'repl_user'@'mariadb_node_ip';

```

**5.2. Configure the MariaDB Replica**

On one of the MariaDB nodes, configure and start the replication process. Use the binary log file and position noted from the `mysqldump` output (`MASTER_LOG_FILE` and `MASTER_LOG_POS`) or use GTID-based replication.

```sql
CHANGE MASTER TO
  MASTER_HOST='mysql_source_ip',
  MASTER_PORT=3306,
  MASTER_USER='repl_user',
  MASTER_PASSWORD='your_password',
  MASTER_USE_GTID=slave_pos;

START SLAVE;

```

#### Step 6: Monitor and Failover

With replication running, the MariaDB cluster will catch up with any changes made to the MySQL cluster since the backup was taken.

**6.1. Monitor Replication Lag**

Check the replica status on the MariaDB node to ensure it is synchronized.

```sql
SHOW SLAVE STATUS\G

```

Look for `Slave_IO_Running: Yes`, `Slave_SQL_Running: Yes`, and `Seconds_Behind_Master: 0`. Once the replica has caught up, `Seconds_Behind_Master` will be 0.

**6.2. Perform the Failover**

Once the MariaDB cluster is fully synchronized, follow these steps:

1. Stop application traffic to the MySQL cluster.
2. Verify final synchronization: Ensure the MariaDB replica has processed all remaining events from the MySQL binary log.
3. Promote MariaDB: Stop the replication on the MariaDB node (`STOP SLAVE;`) and reconfigure your application to connect to the new MariaDB Galera Cluster.
4. Start application traffic on the MariaDB cluster.
5. Decommission MySQL: Once you have verified that your application is running correctly on the new cluster, you can decommission the old MySQL cluster.
