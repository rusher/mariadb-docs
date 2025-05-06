
# MariaDB Enterprise ColumnStore Backup and Restore with Shared Local Storage


# Overview


MariaDB Enterprise ColumnStore supports backup and restore. If Enterprise ColumnStore uses shared local storage for the DB Root directories, the DB Root directories and the MariaDB data directory must be backed up separately.


# Recovery Planning


MariaDB Enterprise ColumnStore supports multiple [storage options](mariadb-enterprise-columnstore-storage-architecture/#storage-options).


This page discusses how to backup and restore Enterprise ColumnStore when it uses [shared local storage](mariadb-enterprise-columnstore-storage-architecture/#shared-local-storage) (such as NFS) for the [DB Root directories](mariadb-enterprise-columnstore-storage-architecture/#db-root-directories).


Any file can become corrupt due to hardware issues, crashes, power loss, and other reasons. If the Enterprise ColumnStore data or metadata were to become corrupt, Enterprise ColumnStore could become unusable, and data loss could occur.


If Enterprise ColumnStore is your [system of record](backup-and-restore-with-mariadb-enterprise-columnstore.md#system-of-record), it should be backed up regularly.


If Enterprise ColumnStore uses [shared local storage](mariadb-enterprise-columnstore-storage-architecture/#shared-local-storage) for the [DB Root directories](mariadb-enterprise-columnstore-storage-architecture/#db-root-directories), the following items must be backed up:


* The MariaDB Data directory is backed up using [MariaDB Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariabackup/)
* The [Storage Manager directory](mariadb-enterprise-columnstore-storage-architecture/#storage-manager-directory) must be backed up
* Each [DB Root directories](mariadb-enterprise-columnstore-storage-architecture/#db-root-directories) must be backed up


See the instructions below for more details.


# Backup


Use the following process to take a backup:


1. Determine which node is the primary server using curl to send the status command to the CMAPI Server:


```
$ curl -k -s https://mcs1:8640/cmapi/0.4.0/cluster/status \
   --header 'Content-Type:application/json' \
   --header 'x-api-key:93816fa66cc2d8c224e62275bd4f248234dd4947b68d4af2b29671dd7d5532dd' \
   | jq .
```

The output will show "dbrm_mode": "master" for the primary server:


```
{
  "timestamp": "2020-12-15 00:40:34.353574",
  "192.0.2.1": {
    "timestamp": "2020-12-15 00:40:34.362374",
    "uptime": 11467,
    "dbrm_mode": "master",
    "cluster_mode": "readwrite",
    "dbroots": [
      "1"
    ],
    "module_id": 1,
    "services": [
      {
        "name": "workernode",
        "pid": 19202
      },
      {
        "name": "controllernode",
        "pid": 19232
      },
      {
        "name": "PrimProc",
        "pid": 19254
      },
      {
        "name": "ExeMgr",
        "pid": 19292
      },
      {
        "name": "WriteEngine",
        "pid": 19316
      },
      {
        "name": "DMLProc",
        "pid": 19332
      },
      {
        "name": "DDLProc",
        "pid": 19366
      }
    ]
  }
```

2. Connect to the primary server using MariaDB Client as a user account that has privileges to lock the database:


```
$ mariadb --host=192.0.2.1 \
   --user=root \
   --password
```

3. Lock the database with the [FLUSH TABLES WITH READ LOCK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush) statement:


```
FLUSH TABLES WITH READ LOCK;
```

Ensure that the client remains connected to the primary server, so that the lock is held for the remaining steps.


4. Make a copy or snapshot of the [Storage Manager directory](mariadb-enterprise-columnstore-storage-architecture/#storage-manager-directory). By default, it is located at `/var/lib/columnstore/storagemanager`.


For example, to make a copy of the directory with rsync:


```
$ sudo mkdir -p /backups/columnstore/202101291600/
$ sudo rsync -av /var/lib/columnstore/storagemanager /backups/columnstore/202101291600/
```

5. Make a copy or snapshot of the [DB Root directories](mariadb-enterprise-columnstore-storage-architecture/#db-root-directories). By default, they are located at `/var/lib/columnstore/dataN`, where the N in dataN represents a range of integers that starts at 1 and stops at the number of nodes in the deployment.


For example, to make a copy of the directories with rsync in a 3-node deployment:


```
$ sudo rsync -av /var/lib/columnstore/data1 /backups/columnstore/202101291600/
$ sudo rsync -av /var/lib/columnstore/data2 /backups/columnstore/202101291600/
$ sudo rsync -av /var/lib/columnstore/data3 /backups/columnstore/202101291600/
```

6. Use [MariaDB Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariabackup/) to backup the [Storage Manager directory](mariadb-enterprise-columnstore-storage-architecture/#storage-manager-directory):


```
$ sudo mkdir -p /backups/mariadb/202101291600/
$ sudo mariadb-backup --backup \
   --target-dir=/backups/mariadb/202101291600/ \
   --user=mariabackup \
   --password=mbu_passwd
```

7. Use [MariaDB Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariabackup/) to prepare the backup:


```
$ sudo mariadb-backup --prepare \
   --target-dir=/backups/mariadb/202101291600/
```

8. Ensure that all previous operations are complete.


9. In the original client connection to the primary server, unlock the database with the [UNLOCK TABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/transactions/transactions-unlock-tables) statement:


```
UNLOCK TABLES;
```

# Restore


Use the following process to restore a backup:


1. [Deploy Enterprise ColumnStore](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-differences/deployment), so that you can restore the backup to an empty deployment.


2. Ensure that all services are stopped on each node:


```
$ sudo systemctl stop mariadb-columnstore-cmapi
$ sudo systemctl stop mariadb-columnstore
$ sudo systemctl stop mariadb
```

3. Restore the backup of the [Storage Manager directory](mariadb-enterprise-columnstore-storage-architecture/#storage-manager-directory). By default, it is located at `/var/lib/columnstore/storagemanager`.


For example, to restore the backup with rsync:


```
$ sudo rsync -av /backups/columnstore/202101291600/storagemanager/ /var/lib/columnstore/storagemanager/
$ sudo chown -R mysql:mysql /var/lib/columnstore/storagemanager
```

4. Restore the backup of the DB Root directories. By default, they are located at `/var/lib/columnstore/dataN`, where the N in dataN represents a range of integers that starts at 1 and stops at the number of nodes in the deployment.


For example, to restore the backup with rsync in a 3-node deployment:


```
$ sudo rsync -av /backups/columnstore/202101291600/data1/ /var/lib/columnstore/data1/
$ sudo rsync -av /backups/columnstore/202101291600/data2/ /var/lib/columnstore/data2/
$ sudo rsync -av /backups/columnstore/202101291600/data3/ /var/lib/columnstore/data3/
$ sudo chown -R mysql:mysql /var/lib/columnstore/data1
$ sudo chown -R mysql:mysql /var/lib/columnstore/data2
$ sudo chown -R mysql:mysql /var/lib/columnstore/data3
```

5. Use [MariaDB Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariabackup/) to restore the backup of the MariaDB data directory:


```
$ sudo mariadb-backup --copy-back \
   --target-dir=/backups/mariadb/202101291600/
$ sudo chown -R mysql:mysql /var/lib/mysql
```

6. Start the services on each node:


```
$ sudo systemctl start mariadb
$ sudo systemctl start mariadb-columnstore-cmapi
```


Copyright © 2025 MariaDB

