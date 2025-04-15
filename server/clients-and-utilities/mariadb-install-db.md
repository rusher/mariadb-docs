
# mariadb-install-db

**This page is for the `<code>mariadb-install-db</code>` script for Linux/Unix only**
For the Windows specific tool of similar name and purpose see [mysql_install_db.exe](../server-management/getting-installing-and-upgrading-mariadb/mariadb-install-db-exe.md).
The Windows version shares the common theme (creating system tables), yet has a lot of functionality specific to Windows systems, for example creating a Windows service. The Windows version does *not* share command line parameters with the Unix shell script.



`<code>mariadb-install-db</code>` initializes the MariaDB data directory and creates the
[system tables](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/README.md) in the [mysql](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md) database, if they do not exist.


Prior to [MariaDB 10.5](../../release-notes/mariadb-community-server/what-is-mariadb-105.md), the client was called `<code>mysql_install_db</code>`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.


MariaDB uses these tables to manage [privileges](../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#privilege-levels), [roles](../security/user-account-management/roles/roles_overview.md), and [plugins](../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/general-development-information/development-plans/old-plans/plugins-storage-engines-summit-for-mysqlmariadbdrizzle-2011.md). It also uses them to provide the data for the [help](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/help-command.md) command in the [mariadb](mariadb-client/mariadb-command-line-client.md) client.


`<code>mariadb-install-db</code>` works by starting MariaDB Server's `<code>mariadbd</code>` process in [--bootstrap](../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-bootstrap) mode and sending commands to create the [system tables](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/README.md) and their content.


## Using mariadb-install-db


To invoke `<code>mariadb-install-db</code>`, use the following syntax:


```
$ mariadb-install-db [options]
```

Because the MariaDB server, `<code>mariadbd</code>`, needs to access the data directory
when it runs later, you should either run `<code>mariadb-install-db</code>` from the same
account that will be used for running `<code>mariadbd</code>` or run it as root and use the
`<code>--user</code>` option to indicate the user name that `<code>mariadbd</code>` will run
as. It might be necessary to specify other options such as
`<code>--basedir</code>` or `<code>--datadir</code>` if
`<code>mariadb-install-db</code>` does not use the correct locations for the installation
directory or data directory. For example:


```
$ scripts/mariadb-install-db --user=mysql \
   --basedir=/opt/mysql/mysql \
   --datadir=/opt/mysql/mysql/data
```

### Options


`<code>mariadb-install-db</code>` supports the following options:



| Option | Description |
| --- | --- |
| Option | Description |
| --auth-root-authentication-method={normal | socket} | If set to normal, it creates a root@localhost account that authenticates with the [mysql_native_password](../reference/plugins/authentication-plugins/authentication-plugin-mysql_native_password.md) authentication plugin and that has no initial password set, which can be insecure. If set to socket, it creates a root@localhost account that authenticates with the [unix_socket](../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) authentication plugin. Set to socket by default (see [Authentication from MariaDB 10.4](../security/user-account-management/authentication-from-mariadb-10-4.md)), or normal by default in earlier versions. |
| --auth-root-socket-user=USER | Used with --auth-root-authentication-method=socket. It specifies the name of the second account to create with [SUPER](../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md#global-privileges) privileges in addition to root, as well as of the system account allowed to access it. Defaults to the value of --user. |
| --basedir=path | The path to the MariaDB installation directory. |
| --builddir=path | If using --srcdir with out-of-directory builds, you will need to set this to the location of the build directory where built files reside. |
| --catalogs=["list"] | Initialize MariaDB for [catalogs](../security/user-account-management/catalogs/catalogs-overview.md). Argument is a list, separated with space or ',', of the catalogs to create. The def catalog is created automatically. Likely added in [MariaDB 11.7](../../release-notes/mariadb-community-server/what-is-mariadb-117.md). |
| --catalog-user=user | User when adding [catalogs](../security/user-account-management/catalogs/catalogs-overview.md) to running server. Likely added in [MariaDB 11.7](../../release-notes/mariadb-community-server/what-is-mariadb-117.md). |
| --catalog-password[=password] | Password for [catalog-user](../security/user-account-management/catalogs/catalogs-overview.md). Likely added in [MariaDB 11.7](../../release-notes/mariadb-community-server/what-is-mariadb-117.md). |
| --catalog-client-arg=arg | Other arguments to 'mariadb' when adding new [catalogs](../security/user-account-management/catalogs/catalogs-overview.md). Likely added in [MariaDB 11.7](../../release-notes/mariadb-community-server/what-is-mariadb-117.md). |
| --cross-bootstrap | For internal use. Used when building the MariaDB system tables on a different host than the target. |
| --datadir=path, --ldata=path | The path to the MariaDB data directory. |
| --client-debug | Write commands to-be executed in '/tmp/mariadb_install_db.log'. Added in [MariaDB 11.6](../../release-notes/mariadb-community-server/what-is-mariadb-116.md). |
| --server-debug | Start mariadbd (server) with --debug. |
| --defaults-extra-file=name | Read this file after the global files are read. Must be given as the first option. |
| --defaults-file=name | Only read default options from the given file name Must be given as the first option. |
| --defaults-group-suffix=name | In addition to the given groups, read also groups with this suffix. |
| --force | Causes mariadb-install-db to run even if DNS does not work. In that case, grant table entries that normally use host names will use IP addresses. |
| --no-defaults | Don't read default options from any option file. Must be given as the first option. |
| --print-defaults | Print the program argument list and exit. Must be given as the first option. |
| --rpm | For internal use. This option is used by RPM files during the MariaDB installation process. |
| --skip-name-resolve | Uses IP addresses rather than host names when creating grant table entries. This option can be useful if your DNS does not work. |
| --skip-test-db | Don't install the test database |
| --srcdir=path | For internal use. The path to the MariaDB source directory. This option uses the compiled binaries and support files within the source tree, useful for if you don't want to install MariaDB yet and just want to create the system tables. The directory under which mariadb-install-db looks for support files such as the error message file and the file for populating the help tables. |
| --user=user_name | The login user name to use for running mariadbd. Files and directories created by mariadbd will be owned by this user. You must be root to use this option. By default, mariadbd runs using your current login name and files and directories that it creates will be owned by you. |
| --verbose | Verbose mode. Print more information about what the program does. |
| --windows | For internal use. This option is used for creating Windows distributions. |



### Option Files


In addition to reading options from the command-line, `<code>mariadb-install-db</code>` can also read options from [option files](../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). If an unknown option is provided to `<code>mariadb-install-db</code>` in an option file, then it is ignored.


The following options relate to how MariaDB command-line tools handles option files. They must be given as the first argument on the command-line:



| Option | Description |
| --- | --- |
| Option | Description |
| --print-defaults | Print the program argument list and exit. |
| --no-defaults | Don't read default options from any option file. |
| --defaults-file=# | Only read default options from the given file #. |
| --defaults-extra-file=# | Read this file after the global files are read. |
| --defaults-group-suffix=# | In addition to the default option groups, also read option groups with this suffix. |



#### Option Groups


`<code>mariadb-install-db</code>` reads options from the following [option groups](../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md):



| Group | Description |
| --- | --- |
| Group | Description |
| [mysql_install_db] | Options read by mysqld_safe, which includes both MariaDB Server and MySQL Server. |



`<code>mariadb-install-db</code>` also reads options from the following server [option groups](../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md):



| Group | Description |
| --- | --- |
| Group | Description |
| [mysqld] | Options read by mysqld, which includes both MariaDB Server and MySQL Server. |
| [server] | Options read by MariaDB Server. |
| [mysqld-X.Y] | Options read by a specific version of mysqld, which includes both MariaDB Server and MySQL Server. For example, [mysqld-5.5]. |
| [mariadb] | Options read by MariaDB Server. |
| [mariadb-X.Y] | Options read by a specific version of MariaDB Server. |
| [client-server] | Options read by all MariaDB [client programs](/kb/en/clients-utilities/) and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. |
| [galera] | Options read by a galera-capable MariaDB Server. Available on systems compiled with Galera support. |



## Installing System Tables


### Installing System Tables From a Source Tree


If you have just [compiled MariaDB from source](../server-management/getting-installing-and-upgrading-mariadb/compiling-mariadb-from-source/compiling-mariadb-from-source-mariadb-source-configuration-options.md), and if you want to use `<code>mariadb-install-db</code>` from your source tree, then that can be done without having to actually install MariaDB. This is very useful if you want to test your changes to MariaDB without disturbing any existing installations of MariaDB.


To do so, you would have to provide the `<code>--srcdir</code>` option. For example:


```
./scripts/mariadb-install-db --srcdir=. --datadir=path-to-temporary-data-dir
```

### Installing System Tables From a Binary Tarball


If you install a [binary tarball](../server-management/getting-installing-and-upgrading-mariadb/binary-packages/installing-mariadb-binary-tarballs.md) package in a non standard path, like your home directory, and if you already have a MariaDB / MySQL package installed, then you may get conflicts
with the default `<code>/etc/my.cnf</code>`. This often results in permissions
errors.


One possible solution is to use the `<code>--no-defaults</code>` option, so that it does not read any [option files](../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
./scripts/mariadb-install-db --no-defaults --basedir=. --datadir=data
```

Another possible solution is to use the `<code>defaults-file</code>` option, so that you can specify your own [option file](../server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files.md). For example:


```
./scripts/mariadb-install-db --defaults-file=~/.my.cnf
```

## User Accounts Created by Default


`<code>mariadb-install-db</code>` sets `<code>--auth-root-authentication-method=socket</code>` by default. When this is set, the default `<code>root@localhost</code>` user account is created with the ability to use two [authentication plugins](../reference/plugins/authentication-plugins/README.md):


* First, it is configured to try to use the [unix_socket](../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) authentication plugin. This allows the the `<code>root@localhost</code>` user to login without a password via the local Unix socket file defined by the [socket](../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#socket) system variable, as long as the login is attempted from a process owned by the operating system `<code>root</code>` user account.
* Second, if authentication fails with the [unix_socket](../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) authentication plugin, then it is configured to try to use the [mysql_native_password](../reference/plugins/authentication-plugins/authentication-plugin-mysql_native_password.md) authentication plugin.


The definition of the default `<code>root@localhost</code>` user account is:


```
CREATE USER 'root'@'localhost' IDENTIFIED VIA unix_socket 
  OR mysql_native_password USING 'invalid';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
GRANT PROXY ON ''@'%' TO 'root'@'localhost' WITH GRANT OPTION;
```

Since `<code>mariadb-install-db</code>` sets `<code>--auth-root-authentication-method=socket</code>` by default, the following additional user accounts are **not** created by default:


* `<code>root@127.0.0.1</code>`
* `<code>root@::1</code>`
* `<code>root@${current_hostname}</code>`


However, an additional user account that is defined by the `<code>--auth-root-socket-user</code>` option is created. If this option is not set, then the value defaults to the value of the `<code>--user</code>` option. On most systems, the `<code>--user</code>` option will use the value of `<code>mysql</code>` by default, so this additional user account would be called `<code>mysql@localhost</code>`.


The definition of this `<code>mysql@localhost</code>` user account is similar to the `<code>root@localhost</code>` user account:


```
CREATE USER 'mysql'@'localhost' IDENTIFIED VIA unix_socket 
  OR mysql_native_password USING 'invalid';
GRANT ALL PRIVILEGES ON *.* TO 'mysql'@'localhost' WITH GRANT OPTION;
```

An invalid password is initially set for both of these user accounts. This means that before a password can be used to authenticate as either of these user accounts, the accounts must first be given a valid password by executing the `<code>[SET PASSWORD](../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/set-password.md)</code>` statement.


For example, here is an example of setting the password for the `<code>root@localhost</code>` user account immediately after installation:


```
$ sudo yum install MariaDB-server
$ sudo systemctl start mariadb
$ sudo mariadb
...
MariaDB> SET PASSWORD = PASSWORD('XH4VmT3_jt');
```

You may notice in the above example that the [mariadb](mariadb-client/mariadb-command-line-client.md) command-line client is executed via [sudo](https://linux.die.net/man/8/sudo). This allows the `<code>root@localhost</code>` user account to successfully authenticate via the [unix_socket](../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) authentication plugin.
<</product>>


## Troubleshooting Issues


### Checking the Error Log


If `<code>mariadb-install-db</code>` fails, you should examine the [error log](../server-management/server-monitoring-logs/error-log.md) in the
data directory, which is the directory specified with `<code>--datadir</code>` option. This should provide a clue about what went wrong.


### Testing With mariadbd


You can also test that this is not a general fault of MariaDB Server by trying to start the `<code>mariadbd</code>` process. The [-skip-grant-tables](../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-skip-grant-tables) option will tell it to ignore the [system tables](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/README.md). Enabling the [general query log](../server-management/server-monitoring-logs/general-query-log.md) can help you determine what queries are being run on the server. For example:


```
mariadbd --skip-grant-tables --general-log
```

At this point, you can use the [mariadb](mariadb-client/mariadb-command-line-client.md) client to connect to the [mysql](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md) database and look at the [system tables](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/README.md). For example:


```
$ /usr/local/mysql/bin/mysql -u root mysql
MariaDB [mysql]> show tables
```

## Using a Server Compiled With --disable-grant-options


The following only apply in the exceptional case that you are using a mariadbd server which is configured with the `<code class="fixed" style="white-space:pre-wrap">--disable-grant-options</code>` option:


`<code>mariadb-install-db</code>` needs to invoke `<code>mariadbd</code>` with the
`<code class="fixed" style="white-space:pre-wrap">--bootstrap</code>` and `<code class="fixed" style="white-space:pre-wrap">--skip-grant-tables</code>` options.
A MariaDB configured with the `<code class="fixed" style="white-space:pre-wrap">--disable-grant-options</code>`
option has `<code class="fixed" style="white-space:pre-wrap">--bootstrap</code>` and `<code class="fixed" style="white-space:pre-wrap">--skip-grant-tables</code>`
disabled. To handle this case, set the `<code>MYSQLD_BOOTSTRAP</code>` environment
variable to the full path name of a mariadbd server that is configured without `<code class="fixed" style="white-space:pre-wrap">--disable-grant-options</code>`. `<code>mariadb-install-db</code>` will use that server.


## The test and test_% Databases


When calling the `<code>mariadb-install-db</code>` script, a new folder called `<code>test</code>` is created in the data directory.
It only has the single `<code>db.opt</code>` file, which sets the client options `<code>default-character-set</code>` and `<code>default-collation</code>` only.


If you run `<code>mysql</code>` as an anonymous user, `<code class="fixed" style="white-space:pre-wrap"> mysql -u''@localhost</code>`, and look for the grants and databases you are able to work with, you will get the following:


```
SELECT current_user;
+--------------+
| current_user |
+--------------+
| @localhost   |
+--------------+

SHOW GRANTS FOR current_user;
+--------------------------------------+
| Grants for @localhost                |
+--------------------------------------+
| GRANT USAGE ON *.* TO ``@`localhost` |
+--------------------------------------+

SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| test               |
+--------------------+
```

Shown are the `<code>information_schema</code>` as well as `<code>test</code>` databases that are built in databases.
But looking from [SHOW GRANTS](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-grants.md) appears to be a paradox; how can the current user see something if they don't have privileges for that?


Let's go a step further.
Now, use the `<code>root</code>`/`<code>unix</code>` user, which has all rights, in order to create a new database with the prefix `<code>test_</code>` , something like:


```
CREATE DATABASE test_electricity;
```

With the above change, a new directory will be created in the data directory.
Now login again with the anonymous user and run [SHOW DATABASES](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-databases.md):


```
SHOW DATABASES
+--------------------+
| Database           |
+--------------------+
| information_schema |
| test               |
| test_electricity   |
+--------------------+
```

Again we are able to see the newly created database, without any rights?
We have an anonymous user that has no privileges, but still can see the `<code>test</code>` and `<code>test_electricity</code>` databases.
**Where does this come from?**



Login with the `<code>root</code>`/`<code>unix</code>` user to find out all privileges that the anonymous user has:


```
SELECT * FROM mysql.user WHERE user='' AND host='localhost'\G
*************************** 1. row ***************************
                  Host: localhost
                  User: 
              Password: 
           Select_priv: N
           Insert_priv: N
           Update_priv: N
           Delete_priv: N
           Create_priv: N
             Drop_priv: N
           Reload_priv: N
         Shutdown_priv: N
          Process_priv: N
             File_priv: N
            Grant_priv: N
       References_priv: N
            Index_priv: N
            Alter_priv: N
          Show_db_priv: N
            Super_priv: N
 Create_tmp_table_priv: N
      Lock_tables_priv: N
          Execute_priv: N
       Repl_slave_priv: N
      Repl_client_priv: N
      Create_view_priv: N
        Show_view_priv: N
   Create_routine_priv: N
    Alter_routine_priv: N
      Create_user_priv: N
            Event_priv: N
          Trigger_priv: N
Create_tablespace_priv: N
   Delete_history_priv: N
              ssl_type: 
            ssl_cipher: 
           x509_issuer: 
          x509_subject: 
         max_questions: 0
           max_updates: 0
       max_connections: 0
  max_user_connections: 0
                plugin: 
 authentication_string: 
      password_expired: N
               is_role: N
          default_role: 
    max_statement_time: 0.000000
```

As seen above from the [mysql.user](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-user-table.md) table, the anonymous user doesn't have any global privileges.
Still, the anonymous user can see databases, so there must be a way so that anonymous user can see the `<code>test</code>` and `<code>test_electricity</code>` databases.


Let's check for grants on the database level. That information can be found in the [mysql.db](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-db-table.md) table.
Looking at the `<code>mysql.db</code>` table, it already contains 2 rows created when the `<code>mariadb-install-db</code>` script was invoked.


The anonymous user has database privileges (without `<code>grant</code>`, `<code>alter_routine</code>` and `<code>execute</code>`) on `<code>test</code>` and `<code>test_%</code>` databases:


```
SELECT * FROM mysql.db\G
*************************** 1. row ***************************
                 Host: %
                   Db: test
                 User: 
          Select_priv: Y
          Insert_priv: Y
          Update_priv: Y
          Delete_priv: Y
          Create_priv: Y
            Drop_priv: Y
           Grant_priv: N
      References_priv: Y
           Index_priv: Y
           Alter_priv: Y
Create_tmp_table_priv: Y
     Lock_tables_priv: Y
     Create_view_priv: Y
       Show_view_priv: Y
  Create_routine_priv: Y
   Alter_routine_priv: N
         Execute_priv: N
           Event_priv: Y
         Trigger_priv: Y
  Delete_history_priv: Y
*************************** 2. row ***************************
                 Host: %
                   Db: test\_%
                 User: 
          Select_priv: Y
          Insert_priv: Y
          Update_priv: Y
          Delete_priv: Y
          Create_priv: Y
            Drop_priv: Y
           Grant_priv: N
      References_priv: Y
           Index_priv: Y
           Alter_priv: Y
Create_tmp_table_priv: Y
     Lock_tables_priv: Y
     Create_view_priv: Y
       Show_view_priv: Y
  Create_routine_priv: Y
   Alter_routine_priv: N
         Execute_priv: N
           Event_priv: Y
         Trigger_priv: Y
  Delete_history_priv: Y
```

The first row is reserved for explicit usage for the `<code>test</code>` database, which is automatically created with `<code>mariadb-install-db</code>`.


Since database `<code>test_electricity</code>` satisfies the `<code>test_%</code>` pattern where `<code>test_</code>` is a prefix, we can understand why the user has the right to work with the newly-created database.


As long as records in `<code>mysql.db</code>` for the anonymous user exists, each new user created will have the privileges for the `<code>test</code>` and `<code>test_%</code>` databases.


Other databases privileges **are not automatically granted** for the newly created user. We have to grant privileges, which will be visible in `<code>mysql.db</code>` table.


### Not Creating the test Database and Anonymous User


If you run `<code>mariadb-install-db</code>` with the `<code>--skip-test-db</code>` option, no `<code>test</code>` database will be created, which we can see as follows:


```
SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
+--------------------+

SELECT * FROM mysql.db;
Empty set (0.001 sec)
```

Also, no anonymous user is created (only `<code>unix</code>`/`<code>mariadb.sys</code>`/`<code>root</code>` users):


```
SELECT user,host FROM mysql.user;
+-------------+-----------+
| User        | Host      |
+-------------+-----------+
| anel        | localhost |
| mariadb.sys | localhost |
| root        | localhost |
+-------------+-----------+
```

## See Also


* [Configure MariaDB with catalog support](../security/user-account-management/catalogs/starting-with-catalogs.md)
* [Installing system tables (mariadb-install-db)](../server-management/getting-installing-and-upgrading-mariadb/installing-system-tables-mariadb-install-db.md)
* The Windows version of `<code>mariadb-install-db</code>`: `<code>[mysql_install_db.exe](../server-management/getting-installing-and-upgrading-mariadb/mariadb-install-db-exe.md)</code>`

