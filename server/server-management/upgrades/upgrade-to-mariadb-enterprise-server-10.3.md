# Upgrade to MariaDB Enterprise Server 10.3

These instructions detail the **upgrade** from a previous version of **MariaDB Enterprise Server** to **MariaDB Enterprise Server 10.3** on a range of [supported Operating Systems](https://mariadb.com/docs/server/deploy/compatibility/).

When [MariaDB Enterprise Server](https://mariadb.com/docs/server/products/mariadb-enterprise-server/) is upgraded, the old version needs to be uninstalled, and the new version needs to be installed.

See [What's New in MariaDB Enterprise Server 10.3](https://mariadb.com/docs/server/whats-new/prior-series/mariadb-enterprise-server-10-3/).

### Data Backup

Occasionally, issues can be encountered during upgrades. These issues can even potentially corrupt the database's data files, preventing you from easily reverting to the old installation. Therefore, it is generally best to perform a backup prior to upgrading. If an issue is encountered during the upgrade, you can use the backup to restore your MariaDB Server database to the old version. If the upgrade finishes without issue, then the backup can be deleted.

The instructions below show how to perform a backup using [MariaDB Backup](https://mariadb.com/docs/server/ref/es10.3/cli/mariabackup/). For more information about backing up and restoring the database, please see the [Recovery Guide](https://mariadb.com/docs/server/data-operations/backups/enterprise-server/).

1.  Take a full backup.

    On MariaDB Enterprise Server 10.4 and later:

    ```
    $ sudo mariadb-backup --backup \
          --user=mariabackup_user \
          --password=mariabackup_passwd \
          --target-dir=/data/backup/preupgrade_backup
    ```

    Confirm successful completion of the backup operation.
2.  The backup must be prepared.

    On MariaDB Enterprise Server 10.4 and later:

    ```
    $ sudo mariadb-backup --prepare \
          --target-dir=/data/backup/preupgrade_backup
    ```

    Confirm successful completion of the prepare operation.
3. Backups should be tested before they are trusted.

### Audit Plugin Considerations

If you have the [MariaDB Audit Plugin](https://mariadb.com/docs/server/ref/mdb/plugins/SERVER_AUDIT,server_audit.so/) installed and if you are upgrading to MariaDB Enterprise Server 10.4 or later, then the audit plugin should be removed prior to the upgrade to prevent conflict with the [MariaDB Enterprise Audit Plugin](https://mariadb.com/docs/server/security/audit/enterprise-audit/) that is present in MariaDB Enterprise Server 10.4 or later.

It can be removed by using the [UNINSTALL SONAME](https://mariadb.com/docs/server/ref/mdb/sql-statements/UNINSTALL_SONAME/) statement:

```
UNINSTALL SONAME 'server_audit';
```

And if you load the plugin in a configuration file using the `plugin_load_add` option, then the option should also be removed.

The [MariaDB Enterprise Audit Plugin](https://mariadb.com/docs/server/security/audit/enterprise-audit/) will automatically be installed after installing MariaDB Enterprise Server 10.4 or later.

### Uninstall the Old Version

When upgrading to a new major release of MariaDB Enterprise Server, it is necessary to remove the existing installation of MariaDB Enterprise Server, before installing the new version of MariaDB Enterprise Server. Otherwise, the package manager will refuse to install the new version of MariaDB Enterprise Server.

#### Stop the MariaDB Server Process

Before the old version can be uninstalled, we first need to stop the current MariaDB Server process.

1.  Set the [innodb\_fast\_shutdown](https://mariadb.com/docs/server/ref/mdb/system-variables/innodb_fast_shutdown/) system variable to `1`:

    ```
    SET GLOBAL innodb_fast_shutdown = 1;
    ```
2.  Use [XA RECOVER](https://mariadb.com/docs/server/ref/mdb/sql-statements/XA_RECOVER/) to confirm that there are no external XA transactions in a prepared state:

    ```
    XA RECOVER;
    ```

    Commit or rollback any open XA transactions before stopping the node for upgrade.
3.  Stop the server process:

    For distributions that use systemd (most supported OSes), you can manage the Server process using the `systemctl` command:

    ```
    $ sudo systemctl stop mariadb
    ```

#### Uninstall via YUM (RHEL, AlmaLinux, CentOS, Rocky Linux)

1.  Uninstall all of the MariaDB Enterprise Server packages. Note that a wildcard character is used to ensure that all MariaDB Enterprise Server packages are uninstalled:

    ```
    $ sudo yum remove "MariaDB-*"
    ```

    Be sure to check that this wildcard does not unintentionally refer to any of your custom applications:
2.  Uninstall the Galera package as well.

    The name of the package depends on the specific version of MariaDB Enterprise Server.

    When upgrading from MariaDB Enterprise Server 10.4 or later, the package is called `galera-enterprise-4`:

    ```
    $ sudo yum remove galera-enterprise-4
    ```
3.  Before proceeding, verify that all MariaDB Enterprise Server packages are uninstalled. The following command should not return any results:

    ```
    $ rpm --query --all | grep -i -E "mariadb|galera"
    ```

#### Uninstall via APT (Debian, Ubuntu)

1.  Uninstall all of the MariaDB Enterprise Server packages. Note that a wildcard character is used to ensure that all MariaDB Enterprise Server packages are uninstalled:

    ```
    $ sudo apt-get remove "mariadb-*"
    ```

    Be sure to check that this wildcard does not unintentionally refer to any of your custom applications.
2.  Uninstall the Galera package as well.

    The name of the package depends on the specific version of MariaDB Enterprise Server.

    When upgrading from MariaDB Enterprise Server 10.4 or later, the package is called `galera-enterprise-4`:

    ```
    $ sudo apt remove galera-enterprise-4
    ```
3.  Before proceeding, verify that all MariaDB Enterprise Server packages are uninstalled. The following command should not return any results:

    ```
    $ apt list --installed | grep -i -E "mariadb|galera"
    ```

#### Uninstall via ZYpp (SLES)

1.  Uninstall all of the MariaDB Enterprise Server packages. Note that a wildcard character is used to ensure that all MariaDB Enterprise Server packages are uninstalled:

    ```
    $ sudo zypper remove "MariaDB-*"
    ```

    Be sure to check that this wildcard does not unintentionally refer to any of your custom applications.
2.  Uninstall the Galera package as well.

    The name of the package depends on the specific version of MariaDB Enterprise Server.

    When upgrading from MariaDB Enterprise Server 10.4 or later, the package is called `galera-enterprise-4`:

    ```
    $ sudo zypper remove galera-enterprise-4
    ```
3.  Before proceeding, verify that all MariaDB Enterprise Server packages are uninstalled. The following command should not return any results:

    ```
    $ rpm --query --all | grep -i -E "mariadb|galera"
    ```

### Install the New Version

MariaDB Corporation provides package repositories for YUM (RHEL, AlmaLinux, CentOS, Rocky Linux), APT (Debian, Ubuntu), and ZYpp (SLES).

#### Install via YUM (RHEL, AlmaLinux, CentOS, Rocky Linux)

1. Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.
2.  Configure the YUM package repository. Installable versions of MariaDB Enterprise Server are `11.4`, `10.6`, `10.5`, `10.4`, and `10.3`. Pass the version to install using the `--mariadb-server-version` flag to [mariadb\_es\_repo\_setup](https://mariadb.com/docs/server/ref/mariadb_es_repo_setup/). The following directions reference `10.3`.

    To configure YUM package repositories:

    ```
    $ sudo yum install curl
    ```

    ```
    $ curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
    ```

    ```
    $ echo "4d483b4df193831a0101d3dfa7fb3e17411dda7fc06c31be4f9e089c325403c0  mariadb_es_repo_setup" \
        | sha256sum -c -
    ```

    ```
    $ chmod +x mariadb_es_repo_setup
    ```

    ```
    $ sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
       --mariadb-server-version="10.3"
    ```
3.  Install MariaDB Enterprise Server and package dependencies:

    ```
    $ sudo yum install MariaDB-server MariaDB-backup
    ```

    Installation of additional packages may be required for some plugins.
4.  Configure MariaDB.

    Installation only loads MariaDB Enterprise Server to the system. MariaDB Enterprise Server requires configuration before the database server is ready for use.

#### Install via APT (Debian, Ubuntu)

1. Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.
2.  Configure the APT package repository.

    Installable versions of MariaDB Enterprise Server are `11.4`, `10.6`, `10.5`, `10.4`, and `10.3`. Pass the version to install using the `--mariadb-server-version` flag to [mariadb\_es\_repo\_setup](https://mariadb.com/docs/server/ref/mariadb_es_repo_setup/). The following directions reference `10.3`.

    To configure APT package repositories:

    ```
    $ sudo apt install curl
    ```

    ```
    $ curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
    ```

    ```
    $ echo "4d483b4df193831a0101d3dfa7fb3e17411dda7fc06c31be4f9e089c325403c0  mariadb_es_repo_setup" \
        | sha256sum -c -
    ```

    ```
    $ chmod +x mariadb_es_repo_setup
    ```

    ```
    $ sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
       --mariadb-server-version="10.3"
    ```

    ```
    $ sudo apt update
    ```
3.  Install MariaDB Enterprise Server and package dependencies:

    ```
    $ sudo apt install mariadb-server mariadb-backup
    ```

    Installation of additional packages may be required for some plugins.
4.  Configure MariaDB.

    Installation only loads MariaDB Enterprise Server to the system. MariaDB Enterprise Server requires configuration before the database server is ready for use.

#### Install via ZYpp (SLES)

1. Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.
2.  Configure the ZYpp package repository.

    Installable versions of MariaDB Enterprise Server are `11.4`, `10.6`, `10.5`, `10.4`, and `10.3`. Pass the version to install using the `--mariadb-server-version` flag to [mariadb\_es\_repo\_setup](https://mariadb.com/docs/server/ref/mariadb_es_repo_setup/). The following directions reference `10.3`.

    To configure ZYpp package repositories:

    ```
    $ sudo zypper install curl
    ```

    ```
    $ curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
    ```

    ```
    $ echo "4d483b4df193831a0101d3dfa7fb3e17411dda7fc06c31be4f9e089c325403c0  mariadb_es_repo_setup" \
        | sha256sum -c -
    ```

    ```
    $ chmod +x mariadb_es_repo_setup
    ```

    ```
    $ sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
       --mariadb-server-version="10.3"
    ```
3.  Install MariaDB Enterprise Server and package dependencies:

    ```
    $ sudo zypper install MariaDB-server MariaDB-backup
    ```

    Installation of additional packages may be required for some plugins.
4.  Configure MariaDB.

    Installation only loads MariaDB Enterprise Server to the system. MariaDB Enterprise Server requires configuration before the database server is ready for use.

### Configuration

For platforms that use YUM or ZYpp as a package manager:

MariaDB Enterprise Server's packages bundle several configuration files:

* `/etc/my.cnf`
* `/etc/my.cnf.d/client.cnf`
* `/etc/my.cnf.d/mariadb-enterprise.cnf`
* `/etc/my.cnf.d/mysql-clients.cnf`
* `/etc/my.cnf.d/server.cnf`

If your version of any of these configuration files contained any custom edits, then the package manager may save your edited version with the `.rpmsave` extension during the upgrade process. If you want to continue using your version with the custom edits, then you may need to move it back. For example, to move `server.cnf` back in place:

```
$ sudo mv /etc/my.cnf.d/server.cnf /etc/my.cnf.d/server.cnf.original
```

```
$ sudo mv /etc/my.cnf.d/server.cnf.rpmsave /etc/my.cnf.d/server.cnf
```

### Starting the Server

MariaDB Enterprise Server includes configuration to start, stop, restart, enable/disable on boot, and check the status of the Server using the operating system default process management system.

For distributions that use systemd, you can manage the Server process using the `systemctl` command:

| **Operation**          | **Command**                      |
| ---------------------- | -------------------------------- |
| Start                  | `sudo systemctl start mariadb`   |
| Stop                   | `sudo systemctl stop mariadb`    |
| Restart                | `sudo systemctl restart mariadb` |
| Enable during startup  | `sudo systemctl enable mariadb`  |
| Disable during startup | `sudo systemctl disable mariadb` |
| Status                 | `sudo systemctl status mariadb`  |

### Upgrading the Data Directory

MariaDB Enterprise Server ships with a utility that can be used to identify and correct compatibility issues in the new version. After you upgrade your Server and start the server process, run this utility to upgrade the data directory.

The utility is called [mariadb-upgrade](https://mariadb.com/docs/server/ref/es10.3/cli/mysql_upgrade/) in MariaDB Enterprise Server 10.4 and later:

```
$ sudo mariadb-upgrade
```

### Testing

When MariaDB Enterprise Server is up and running on your system, you should test that it is working and there weren't any issues during startup.

1.  Connect to the server using MariaDB Client using the `root@localhost` user account.

    MariaDB Client is called [mariadb](https://mariadb.com/docs/server/ref/es10.3/cli/mysql/) (ES10.4 and later):

    ```
    $ sudo mysql
    ```

    ```
    Welcome to the MariaDB monitor.  Commands end with ; or \g.
    Your MariaDB connection id is 9
    Server version: 10.3.39-20-MariaDB-Enterprise MariaDB Enterprise Server

    Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    MariaDB [(none)]>
    ```
2.  You can also verify the server version by checking the value of the [version](https://mariadb.com/docs/server/ref/mdb/system-variables/version/) system variable with the [SHOW GLOBAL STATUS](https://mariadb.com/docs/server/ref/mdb/sql-statements/SHOW_STATUS/) statement:

    ```
    SHOW GLOBAL VARIABLES LIKE 'version';
    ```

    ```
    +---------------+-------------------------------+
    | Variable_name | Value                         |
    +---------------+-------------------------------+
    | version       | 10.3.39-20-MariaDB-Enterprise |
    +---------------+-------------------------------+
    ```
3.  You can also verify the server version by calling the [VERSION()](https://mariadb.com/docs/server/ref/mdb/functions/VERSION/) function:

    ```
    SELECT VERSION();
    ```

    ```
    +-------------------------------+
    | VERSION()                     |
    +-------------------------------+
    | 10.3.39-20-MariaDB-Enterprise |
    +-------------------------------+
    ```

***

© 2025 MariaDB. All rights reserved.
