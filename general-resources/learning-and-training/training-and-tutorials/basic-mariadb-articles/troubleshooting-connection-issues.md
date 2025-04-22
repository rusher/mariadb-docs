
# Troubleshooting Connection Issues

If you are completely new to MariaDB and relational databases, you may want to start with the [MariaDB Primer](../beginner-mariadb-articles/a-mariadb-primer.md). Also, make sure you understand the connection parameters discussed in the [Connecting to MariaDB](../beginner-mariadb-articles/connecting-to-mariadb.md) article.

There are a number of common problems that can occur when connecting to MariaDB.


### Server Not Running in Specified Location


If the error you get is something like:


```
mariadb -uname -p -uname -p
ERROR 2002 (HY000): Can't connect to local MySQL server through 
  socket '/var/run/mysqld/mysqld.sock' (2 "No such file or directory")
```

or


```
mariadb -uname -p --port=3307 --protocol=tcp
ERROR 2003 (HY000): Can't connect to MySQL server on  'localhost' 
  (111 "Connection refused")
```

the server is either not running, or not running on the specified port, socket or pipe. Make sure you are using the correct [host](../beginner-mariadb-articles/connecting-to-mariadb.md#host), [port](../beginner-mariadb-articles/connecting-to-mariadb.md#port), [pipe](../beginner-mariadb-articles/connecting-to-mariadb.md#pipe), [socket](../beginner-mariadb-articles/connecting-to-mariadb.md#socket) and [protocol](../beginner-mariadb-articles/connecting-to-mariadb.md#protocol) options, or alternatively, see [Getting, Installing and Upgrading MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/), [Starting and Stopping MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/) or [Troubleshooting Installation Issues](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/troubleshooting-installation-issues/).


The socket file can be in a non-standard path. In this case, the `socket` option is probably written in the my.cnf file. Check that its value is identical in the [mysqld] and [client] sections; if not, the client will look for a socket in a wrong place.


If unsure where the Unix socket file is running, it's possible to find this out, for example:


```
netstat -ln | grep mysqld
unix  2      [ ACC ]     STREAM     LISTENING     33209505 /var/run/mysqld/mysqld.sock
```

### Unable to Connect from a Remote Location


Usually, the MariaDB server does not by default accept connections from a remote client or connecting with tcp and a hostname and has to be configured to permit these.


```
(/my/maria-10.4) ./client/mysql --host=myhost --protocol=tcp --port=3306 test
ERROR 2002 (HY000): Can't connect to MySQL server on 'myhost' (115)
(/my/maria-10.4) telnet myhost 3306
Trying 192.168.0.11...
telnet: connect to address 192.168.0.11: Connection refused
(/my/maria-10.4) perror 115
OS error code 115:  Operation now in progress
```

To solve this, see [Configuring MariaDB for Remote Client Access](configuring-mariadb-for-remote-client-access.md)


### Authentication Problems


Note that from [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes), the [unix_socket authentication plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-unix-socket) is enabled by default on Unix-like systems. This uses operating system credentials when connecting to MariaDB via the local Unix socket file. See [unix_socket authentication plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-unix-socket) for instructions on connecting and on switching to password-based authentication as well as [Authentication from MariaDB 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/user-account-management/authentication-from-mariadb-10-4) for an overview of the [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104) changes..


Authentication is granted to a particular username/host combination. `user1'@'localhost'`, for example, is not the same as `user1'@'166.78.144.191'`. See the [GRANT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant) article for details on granting permissions.


Passwords are hashed with [PASSWORD](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/encryption-hashing-and-compression-functions/password) function. If you have set a password with the [SET PASSWORD](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/set-password) statement, the [PASSWORD](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/encryption-hashing-and-compression-functions/password) function must be used at the same time. For example, `SET PASSWORD FOR 'bob'@'%.loc.gov' = PASSWORD('newpass')` rather than just `SET PASSWORD FOR 'bob'@'%.loc.gov' = 'newpass'`;


#### Problems Exporting Query Results


If you can run regular queries, but get an authentication error when running the [SELECT ... INTO OUTFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/select-into-outfile), [SELECT ... INTO DUMPFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/select-into-dumpfile) or [LOAD DATA INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) statements, you do not have permission to write files to the server. This requires the FILE privilege. See the [GRANT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant) article.


#### Access to the Server, but not to a Database


If you can connect to the server, but not to a database, for example:


```
USE test;
ERROR 1044 (42000): Access denied for user 'ian'@'localhost' to database 'test'
```

or can connect to a particular database, but not another, for example
`mariadb -uname -p -u name db1` works but not `mariadb -uname -p -u name db2`, you have not been granted permission for the particular database. See the [GRANT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant) article.


#### Option Files and Environment Variables


It's possible that option files or environment variables may be providing incorrect connection parameters. Check the values provided in any option files read by the client you are using (see [mariadbd Configuration Files and Groups](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/configuring-mariadb-with-option-files) and the documentation for the particular client you're using - see [Clients and Utilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/)).


Option files can usually be suppressed with `no-defaults` option, for example:


```
mariadb-import --no-defaults ...
```

#### Unable to Connect to a Running Server / Lost root Password


If you are unable to connect to a server, for example because you have lost the root password, you can start the server without using the privilege tables by running the [--skip-grant-tables](mariadb-options/#-skip-grant-tables) option, which gives users full access to all tables. You can then run [FLUSH PRIVILEGES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush) to resume using the grant tables, followed by [SET PASSWORD](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/set-password) to change the password for an account.


#### localhost and %


You may have created a user with something like:


```
CREATE USER melisa identified by 'password';
```

This creates a user with the '%' wildcard host.


```
select user,host from mysql.user where user='melisa';
+--------+------+
| user   | host |
+--------+------+
| melisa | %    |
+--------+------+
```

However, you may still be failing to login from localhost. Some setups create anonymous users, including localhost. So the following records exist in the user table:


```
select user,host from mysql.user where user='melisa' or user='';
+--------+-----------+
| user   | host      |
+--------+-----------+
| melisa | %         |
|        | localhost |
+--------+-----------+
```

Since you are connecting from localhost, the anonymous credentials, rather than those for the 'melisa' user, are used. The solution is either to add a new user specific to localhost, or to remove the anonymous localhost user.


### See Also


* [CREATE USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user)
* [GRANT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant)
* [Authentication from MariaDB 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/user-account-management/authentication-from-mariadb-10-4)
* [Authentication from MariaDB 10 4 video tutorial](https://www.youtube.com/watch?v=aWFG4uLbimM)
* [Error 1698: Access denied for user](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-1600-to-1699/e1698)

