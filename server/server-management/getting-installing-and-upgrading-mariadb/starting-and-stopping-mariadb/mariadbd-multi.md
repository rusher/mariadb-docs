
# mariadbd-multi

Before using mariadbd-multi be sure that you understand the meanings of the options that are passed to the mariadbd servers and why you would want to have separate mariadbd processes. Beware of the dangers of using multiple mariadbd servers with the same data directory. Use separate data directories, unless you know what you are doing. Starting multiple servers with the same data directory does not give you extra performance in a threaded system.



The `<code>mariadbd-multi</code>` startup script is in MariaDB distributions on Linux and Unix. It is a wrapper that is designed to manage several `<code>mariadbd</code>` processes running on the same host.


Prior to [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), the client was called `<code>mysqld_multi</code>`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.


In order for multiple `<code>mariadbd</code>` processes to work on the same host, these processes must:


* Use different Unix socket files for local connections.
* Use different TCP/IP ports for network connections.
* Use different data directories.
* Use different process ID files (specified by the `<code>--pid-file</code>` option) if using `<code>[mariadbd-safe](mariadbd-safe.md)</code>` to start `<code>mariadbd</code>`.


`<code>mariadbd-multi</code>` can start or stop servers, or report their current status.


## Using mariadbd-multi


The command to use `<code>mariadbd-multi</code>` and the general syntax is:


```
mariadbd-multi [options] {start|stop|report} [GNR[,GNR] ...]
```

`<code>start</code>`, `<code>stop</code>`, and `<code>report</code>` indicate which operation to perform.


You can specify which servers to perform the operation on by providing one or more `<code>GNR</code>` values. `<code>GNR</code>` refers to an option group number, and it is explained more in the [option groups](#option-groups) section below. If there is no `<code>GNR</code>` list, then `<code>mariadbd-multi</code>` performs the operation for all `<code>GNR</code>` values found in its option files.


Multiple `<code>GNR</code>` values can be specified as a comma-separated list. `<code>GNR</code>` values can also be specified as a range by separating the numbers by a dash. There must not be any whitespace characters in the `<code>GNR</code>` list.


For example:


This command starts a single server using option group `<code>[mariadbd17]</code>`:


```
mariadbd-multi start 17
```

This command stops several servers, using option groups `<code>[mariadbd8]</code>` and `<code>[mariadbd10]</code>` through `<code>[mariadbd13]</code>`:


```
mariadbd-multi stop 8,10-13
```

### Options


`<code>mariadbd-multi</code>` supports the following options:



| Option | Description |
| --- | --- |
| Option | Description |
| --example | Give an example of a config file with extra information. |
| --help | Display help and exit. |
| --log=filename | Specify the path and name of the log file. If the file exists, log output is appended to it. |
| --mysqladmin=prog_name | The [mariadb-admin](../../../clients-and-utilities/mariadb-admin.md) binary to be used to stop servers. Can be given within groups [mariadbd#]. |
| --mariadbd=prog_name | The mariadbd binary to be used. Note that you can also specify [mariadbd-safe](mariadbd-safe.md) as the value for this option. If you use mariadbd-safe to start the server, you can include the mariadbd or ledir options in the corresponding [mariadbdN] option group. These options indicate the name of the server that mariadbd-safe should start and the path name of the directory where the server is located. Example:[mariadbd38]mariadbd = mariadbd-debugledir = /opt/local/mysql/libexec. |
| --no-log | Print to stdout instead of the log file. By default the log file is turned on. |
| --password=password | The password of the MariaDB account to use when invoking [mariadb-admin](../../../clients-and-utilities/mariadb-admin.md). Note that the password value is not optional for this option, unlike for other MariaDB programs. |
| --silent | Silent mode; disable warnings. |
| --tcp-ip | Connect to the MariaDB server(s) via the TCP/IP port instead of the UNIX socket. This affects stopping and reporting. If a socket file is missing, the server may still be running, but can be accessed only via the TCP/IP port. By default connecting is done via the UNIX socket. This option affects stop and report operations. |
| --user=username | The user name of the MariaDB account to use when invoking [mariadb-admin](../../../clients-and-utilities/mariadb-admin.md). |
| --verbose | Be more verbose. |
| --version | Display version information and exit. |
| --wsrep-new-cluster | Bootstrap a cluster. Added in [MariaDB 10.1.15](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10115-release-notes.md). |



### Option Files


In addition to reading options from the command-line, `<code>mariadbd-multi</code>` can also read options from [option files](../configuring-mariadb-with-option-files.md). If an unknown option is provided to `<code>mariadbd-multi</code>` in an option file, then it is ignored.


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


`<code>mariadbd-multi</code>` reads options from the following [option groups](../configuring-mariadb-with-option-files.md#option-groups) from [option files](../configuring-mariadb-with-option-files.md):



| Group | Description |
| --- | --- |
| Group | Description |
| [mysqld_multi] | Options read by mysqld_multi, which includes both MariaDB Server and MySQL Server. |



`<code>mariadbd-multi</code>` also searches [option files](../configuring-mariadb-with-option-files.md) for [option groups](../configuring-mariadb-with-option-files.md#option-groups) with names like `<code>[mariadbdN]</code>`, where `<code>N</code>` can be any positive integer. This number is referred to in the following discussion as the option group number, or `<code>GNR</code>`:



| Group | Description |
| --- | --- |
| Group | Description |
| [mysqldN] | Options read by a mysqld instance managed by mysqld_multi, which includes both MariaDB Server and MySQL Server. The N refers to the instance's GNR. |



`<code>GNR</code>` values distinguish option groups from one another and are used as arguments to `<code>mariadbd-multi</code>` to specify which servers you want to start, stop, or obtain a status report for. The `<code>GNR</code>` value should be the number at the end of the option group name in the option file. For example, the `<code>GNR</code>` for an option group named `<code>[mariadbd17]</code>` is `<code>17</code>`.


Options listed in these option groups are the same that you would use in the regular server option groups used for configuring `<code>mariadbd</code>`. However, when using multiple servers, it is necessary that each one use its own value for options such as the Unix socket file and TCP/IP port number.


The `<code>[mariadbd-multi]</code>` option group can be used for options that are needed for `<code>mariadbd-multi</code>` itself. `<code>[mariadbdN]</code>` option groups can be used for options passed to specific `<code>mariadbd</code>` instances.


The regular server [option groups](../configuring-mariadb-with-option-files.md#option-groups) can also be used for common options that are read by all instances:



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



For an example of how you might set up an option file, use this command:


```
mariadbd-multi --example
```

### Authentication and Privileges


Make sure that the MariaDB account used for stopping the `<code>mariadbd</code>` processes (with the [mariadb-admin](../../../clients-and-utilities/mariadb-admin.md) utility) has the same user name and password for each server. Also, make sure that the account has the `<code>SHUTDOWN</code>` privilege. If the servers that you want to manage have different user names or passwords for the administrative accounts, you might want to create an account on each server that has the same user name and password. For example, you might set up a common `<code>multi_admin</code>` account by executing the following commands for each server:


```
shell> mysql -u root -S /tmp/mysql.sock -p
Enter password:
mysql> GRANT SHUTDOWN ON *.*
 -> TO ´multi_admin´@´localhost´ IDENTIFIED BY ´multipass´;
```

Change the connection parameters appropriately when connecting to each one. Note that the host name part of the account name must allow you to connect as `<code>multi_admin</code>` from the host where you want to run `<code>mariadbd-multi</code>`.


## User Account


Make sure that the data directory for each server is fully accessible to the Unix account that the specific `<code>mariadbd</code>` process is started as. If you run the `<code>mariadbd-multi</code>` script as the Unix `<code>root</code>` account, and if you want the `<code>mariadbd</code>` process to be started with another Unix account, then you can use use the `<code>--user</code>` option with `<code>mariadbd</code>`. If you specify the `<code>--user</code>` option in an option file, and if you did not run the `<code>mariadbd-multi</code>` script as the Unix `<code>root</code>` account, then it will just log a warning and the `<code>mariadbd</code>` processes are started under the original Unix account.


Do not run the `<code>mariadbd</code>` process as the Unix `<code>root</code>` account, unless you know what you are doing.


## Example


The following example shows how you might set up an option file for use with mariadbd-multi. The order in which the mariadbd programs are started or stopped depends on the order in which they appear in the option file. Group numbers need not form an unbroken sequence. The first and fifth [mariadbdN] groups were intentionally omitted from the example to illustrate that you can have “gaps” in the option file. This gives you more flexibility.


```
# This file should probably be in your home dir (~/.my.cnf)
           # or /etc/my.cnf
           # Version 2.1 by Jani Tolonen
           [mariadbd-multi]
           mariadbd     = /usr/local/bin/mariadbd-safe
           mysqladmin = /usr/local/bin/mysqladmin
           user       = multi_admin
           password   = multipass
           [mariadbd2]
           socket     = /tmp/mysql.sock2
           port       = 3307
           pid-file   = /usr/local/mysql/var2/hostname.pid2
           datadir    = /usr/local/mysql/var2
           language   = /usr/local/share/mysql/english
           user       = john
           [mariadbd3]
           socket     = /tmp/mysql.sock3
           port       = 3308
           pid-file   = /usr/local/mysql/var3/hostname.pid3
           datadir    = /usr/local/mysql/var3
           language   = /usr/local/share/mysql/swedish
           user       = monty
           [mariadbd4]
           socket     = /tmp/mysql.sock4
           port       = 3309
           pid-file   = /usr/local/mysql/var4/hostname.pid4
           datadir    = /usr/local/mysql/var4
           language   = /usr/local/share/mysql/estonia
           user       = tonu
           [mariadbd6]
           socket     = /tmp/mysql.sock6
           port       = 3311
           pid-file   = /usr/local/mysql/var6/hostname.pid6
           datadir    = /usr/local/mysql/var6
           language   = /usr/local/share/mysql/japanese
           user       = jani
```
