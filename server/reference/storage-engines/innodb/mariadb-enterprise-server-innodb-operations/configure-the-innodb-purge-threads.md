
# Configure the InnoDB Purge Threads


# Overview


In MariaDB Enterprise Server, the InnoDB storage engine uses Purge Threads to perform garbage collection in the background. The Purge Threads are related to multi-version concurrency control (MVCC).


The Purge Threads perform garbage collection of various items:


The Purge Threads perform garbage collection of the [InnoDB Undo Log](../innodb-undo-log.md). When a row is updated in the clustered index, InnoDB updates the values in the clustered index, and the old row version is added to the Undo Log. The Purge Threads scan the Undo Log for row versions that are not needed by open transactions and permanently delete them.


The Purge Threads perform garbage collection of index records. When an indexed column is updated, InnoDB creates a new index record for the updated value in each affected index, and the old index records are delete-marked. When the primary key column is updated, InnoDB creates a new index record for the updated value in every index, and each old index record is delete-marked. The Purge Threads scan for delete-marked index records and permanently delete them.


The Purge Threads perform garbage collection of freed overflow pages. [BLOB](data-types-blob), [CHAR](data-types-char), [TEXT](data-types-text), [VARCHAR](data-types-varchar), [VARBINARY](data-types-varbinary), and related types are sometimes stored on overflow pages. When the value on the overflow page is deleted or updated, the overflow page is no longer needed. The Purge Threads delete these freed overflow pages.


For additional information, see "[InnoDB Purge Threads](mariadb-enterprise-server-innodb-purge-threads)".


This page describes how to configure the InnoDB Purge Threads.


# Configure the Number of InnoDB Purge Threads


The number of the InnoDB Purge Threads is configurable. If your server deletes or updates rows at a very high frequency, then you may need to increase the number of purge threads.


The method to configure the number of Purge Threads depends on the server version and whether a server restart will be performed:



| Product Versions | Server Restart? | Method |
| --- | --- | --- |
| Product Versions | Server Restart? | Method |
| ES 10.5 and Later | No | [Configure maximum number of asynchronous I/O requests with SET GLOBAL](configure-the-innodb-io-threads.md#configure-the-number-of-innodb-io-threads-in-a-configuration-file) |
| Any ES Any CS | Yes. | [Configure number of I/O threads in configuration file](configure-the-innodb-io-threads.md#configure-the-number-of-innodb-io-threads) |



# Configure the Number of InnoDB Purge Threads with SET GLOBAL (ES 10.5) and Later


Starting in MariaDB Enterprise Server 10.5, the number of InnoDB purge threads can be changed dynamically by setting the [innodb_purge_threads](../innodb-system-variables.md#innodb_purge_threads) system variable using the [SET GLOBAL](../../../sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set.md) statement. The [SET GLOBAL](../../../sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set.md) statement requires the SUPER privilege.


To ensure that the change survives server restarts, the [innodb_purge_threads](../innodb-system-variables.md#innodb_purge_threads) system variable should also be set in a configuration file.


To configure the number of InnoDB Purge threads with the [SET GLOBAL](../../../sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set.md) statement, use the following procedure:


1. Connect to the server using [MariaDB Client](../../../../clients-and-utilities/mariadb-client/README.md) as the `root@localhost` user account or another user account with the SUPER privilege:


```
$ mariadb --user=root
```

2. Set the [innodb_purge_threads](../innodb-system-variables.md#innodb_purge_threads) system variable to the new size using the [SET GLOBAL](../../../sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set.md) statement.


For example:


```
SET GLOBAL innodb_purge_threads=8;
```

3. Choose a configuration file for custom changes to system variables and options.
It is not recommended to make custom changes to Enterprise Server's default configuration files, because your custom changes can be overwritten by other default configuration files that are loaded after.


Ensure that your custom changes will be read last by creating a custom configuration file in one of the included directories. Configuration files in included directories are read in alphabetical order. Ensure that your custom configuration file is read last by using the `z-` prefix in the file name.


Some example configuration file paths for different distributions are shown in the following table:



| Distributions | Example configuration file path |
| --- | --- |
| Distributions | Example configuration file path |
| CentOS RHEL Rocky Linux SLES | /etc/my.cnf.d/z-custom-mariadb.cnf |
| Debian Ubuntu | /etc/mysql/mariadb.conf.d/z-custom-mariadb.cnf |



4. Set the [innodb_purge_threads](../innodb-system-variables.md#innodb_purge_threads) system variable in the configuration file.
It needs to be set in a group that will be read by MariaDB Server, such as [mariadb] or [server].


For example:


```
[mariadb]
...
innodb_purge_threads=8
```

# Configure the Number of InnoDB Purge Threads in a Configuration File


The number of InnoDB Purge Threads can be configured by setting the [innodb_purge_threads](../innodb-system-variables.md#innodb_purge_threads) system variable in a configuration file.


To configure the number of [innodb_purge_threads](../innodb-system-variables.md#innodb_purge_threads) in a configuration file, use the following procedure:


1. Choose a configuration file for custom changes to system variables and options.
It is not recommended to make custom changes to Enterprise Server's default configuration files, because your custom changes can be overwritten by other default configuration files that are loaded after.


Ensure that your custom changes will be read last by creating a custom configuration file in one of the included directories. Configuration files in included directories are read in alphabetical order. Ensure that your custom configuration file is read last by using the `z-` prefix in the file name.


Some example configuration file paths for different distributions are shown in the following table:



| Distributions | Example configuration file path |
| --- | --- |
| Distributions | Example configuration file path |
| CentOS RHEL Rocky Linux SLES | /etc/my.cnf.d/z-custom-mariadb.cnf |
| Debian Ubuntu | /etc/mysql/mariadb.conf.d/z-custom-mariadb.cnf |



2. Set the innodb_purge_threads system variable in the configuration file.
It needs to be set in a group that will be read by MariaDB Server, such as [mariadb] or [server].


For example:


```
[mariadb]
...
innodb_purge_threads=8
```

3. Restart the server:


```
$ sudo systemctl restart mariadb
```

Starting in MariaDB Enterprise Server 10.5, the server can use the configuration change without a restart if you use [SET GLOBAL](../../../sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set.md).


Copyright © 2025 MariaDB

