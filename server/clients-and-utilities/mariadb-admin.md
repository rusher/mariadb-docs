---
icon: question
---

# mariadb-admin

## mariadb-admin

`mariadb-admin` is an administration program for the mariadbd daemon. It can be used to:

* Monitor what the MariaDB clients are doing (processlist)
* Get usage statistics and variables from the MariaDB server
* Create/drop databases
* Flush (reset) logs, statistics and tables
* Kill running queries.
* Stop the server (shutdown)
* Start/stop replicas
* Check if the server is alive (ping)

Prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105), the client was called `mysqladmin`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.

### Using mariadb-admin

The command to use `mariadb-admin` and the general syntax is:

```
mariadb-admin [options] command [command-arg] [command [command-arg]] ...
```

#### Options

`mariadb-admin` supports the following options:

| Option | Description |
| - | - |
| --character-sets-dir=name    | Directory where the [character set](../reference/data-types/string-data-types/character-sets/) files are located. |
| -C, --compress               | Compress all information sent between the client and the server if both support compression.  |
| --connect\_timeout=val       | Maximum time in seconds before connection timeout. The default value is 43200 (12 hours). |
| -c val, --count=val          | Number of iterations to make. This works with -i (--sleep) only. |
| --debug\[=debug\_options], - |  |
|[debug\_options] | Write a debugging log. A typical debug\_options string is d:t:o,file\_name. The default is d:t:o,/tmp/mysqladmin.trace. |
| --debug-check | Check memory and open file usage at exit. |
| --debug-info | Print debugging information and memory and CPU usage statistics when the program exits. |
| --default-auth=plugin | Default authentication client-side plugin to use. |
| --default-character-set=name | Set the default character set. |
| -f, --force | Don't ask for confirmation on drop database; with multiple commands, continue even if an error occurs. |
| -?, --help | Display this help and exit. |
| -h name, --host=name | Hostname to connect to. |
| -l, --local | Suppress the SQL command(s) from being written to the [binary log](../server-management/server-monitoring-logs/binary-log/) by enabling [sql\_log\_bin=0](../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) for the session, or, from [MariaDB 10.2.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1027-release-notes) and [MariaDB 10.1.24](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10124-release-notes), for flush commands only, using FLUSH LOCAL rather than SET sql\_log\_bin=0, so the privilege requirement is RELOAD rather than SUPER. |
| -b, --no-beep | Turn off beep on error. |
| -p\[password], --password\[=password] | Password to use when connecting to server. If password is not given it's asked from the terminal. |
| --pipe, -W | On Windows, connect to the server via a named pipe. This option applies only if the server supports named-pipe connections. |
| -P portnum, --port=portnum | Port number to use for connection, or 0 for default to, in order of preference, my.cnf, $MYSQL\_TCP\_PORT, /etc/services, built-in default (3306). |
| --protocol=name | The protocol to use for connection (tcp, socket, pipe, memory). |
| -r, --relative | Show difference between current and previous values when used with -i. Currently only works with extended-status. |
| -O value, --set-variable=vaue | Change the value of a variable. Please note that this option is deprecated; you can set variables directly with --variable-name=value. |
| --shutdown\_timeout=val | Maximum number of seconds to wait for server shutdown. The default value is 3600 (1 hour). |
| -s, --silent | Silently exit if one can't connect to server. |
| -i delay, --sleep=delay | Execute commands repeatedly, sleeping for delay seconds in between. The --count option determines the number of iterations. If --count is not given, mariadb-admin executes commands indefinitely until interrupted. |
| -S name, --socket=name | For connections to localhost, the Unix socket file to use, or, on Windows, the name of the named pipe to use. |
| --ssl | Enables [TLS](../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). TLS is also enabled even without setting this option when certain other TLS options are set. The --ssl option will not enable [verifying the server certificate](../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification) by default. In order to verify the server certificate, the user must specify the --ssl-verify-server-cert option. |
| --ssl-ca=name | Defines a path to a PEM file that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for [TLS](../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Authorities (CAs)](../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information. This option implies the --ssl option. |
| --ssl-capath=name | Defines a path to a directory that contains one or more PEM files that should each contain one X509 certificate for a trusted Certificate Authority (CA) to use for [TLS](../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Authorities (CAs)](../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information. This option is only supported if the client was built with OpenSSL or yaSSL. If the client was built with GnuTLS or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms. This option implies the --ssl option. |
| --ssl-cert=name | Defines a path to the X509 certificate file to use for [TLS](../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. This option implies the --ssl option. |
| --ssl-cipher=name | List of permitted ciphers or cipher suites to use for [TLS](../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option implies the --ssl option. |
| --ssl-crl=name | Defines a path to a PEM file that should contain one or more revoked X509 certificates to use for [TLS](../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information. This option is only supported if the client was built with OpenSSL or Schannel. If the client was built with yaSSL or GnuTLS, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms. |\
| --ssl-crlpath=name | Defines a path to a directory that contains one or more PEM files that should each contain one revoked X509 certificate to use for [TLS](../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information. This option is only supported if the client was built with OpenSSL. If the client was built with yaSSL, GnuTLS, or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms. |
| --ssl-key=name | Defines a path to a private key file to use for [TLS](../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. This option implies the --ssl option. |
| --ssl-verify-server-cert | Enables [server certificate verification](../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification). This option is disabled by default. |
| --tls-version=name | This option accepts a comma-separated list of TLS protocol versions. A TLS protocol version will only be enabled if it is present in this list. All other TLS protocol versions will not be permitted. See [Secure Connections Overview: TLS Protocol Versions](../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#tls-protocol-versions) for more information. |
| -u, --user=name | User for login if not current user. |\
| -v, --verbose | Write more information. |\
| -V, --version | Output version information and exit. |\
| -E, --vertical | Print output vertically. Is similar to '--relative', but prints output vertically. |\
| -w\[count], --wait\[=count] | If the connection cannot be established, wait and retry instead of aborting. If a count value is given, it indicates the number of times to retry. The default is one time. |\
| --wait-for-all-slaves | Wait for the last binlog event to be sent to all connected replicas before shutting down. This option is off by default. |

#### Option Files

In addition to reading options from the command-line, `mariadb-admin` can also read options from [option files](../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). If an unknown option is provided to `mariadb-admin` in an option file, then it is ignored.

The following options relate to how MariaDB command-line tools handles option files. They must be given as the first argument on the command-line:

| Option                    | Description                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------- |
| Option                    | Description                                                                         |
| --print-defaults          | Print the program argument list and exit.                                           |
| --no-defaults             | Don't read default options from any option file.                                    |
| --defaults-file=#         | Only read default options from the given file #.                                    |
| --defaults-extra-file=#   | Read this file after the global files are read.                                     |
| --defaults-group-suffix=# | In addition to the default option groups, also read option groups with this suffix. |

`mariadb-admin` is linked with [MariaDB Connector/C](../../kb/en/about-mariadb-connector-c/). However, MariaDB Connector/C does not yet handle the parsing of option files for this client. That is still performed by the server option file parsing code. See [MDEV-19035](https://jira.mariadb.org/browse/MDEV-19035) for more information.

**Option Groups**

`mariadb-admin` reads options from the following [option groups](../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

| Group             | Description                                                                                                                                                                                                                               |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Group             | Description                                                                                                                                                                                                                               |
| \[mysqladmin]     | Options read by mysqladmin, which includes both MariaDB Server and MySQL Server.                                                                                                                                                          |
| \[mariadb-admin]  | Options read by mariadb-admin. Available starting with [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes). |
| \[client]         | Options read by all MariaDB and MySQL [client programs](../../kb/en/clients-utilities/), which includes both MariaDB and MySQL clients. For example, mysqldump.                                                                           |
| \[client-server]  | Options read by all MariaDB [client programs](../../kb/en/clients-utilities/) and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients.                                |
| \[client-mariadb] | Options read by all MariaDB [client programs](../../kb/en/clients-utilities/).                                                                                                                                                            |

### mariadb-admin Variables

Variables can be set with `--variable-name=value`.

| Variables and boolean options | Value                           |
| ----------------------------- | ------------------------------- |
| Variables and boolean options | Value                           |
| count                         | 0                               |
| debug-check                   | FALSE                           |
| debug-info                    | FALSE                           |
| force                         | FALSE                           |
| compress                      | FALSE                           |
| character-sets-dir            | (No default value)              |
| default-character-set         | (No default value)              |
| host                          | (No default value)              |
| no-beep                       | FALSE                           |
| port                          | 3306                            |
| relative                      | FALSE                           |
| socket                        | /var/run/mariadbd/mariadbd.sock |
| sleep                         | 0                               |
| ssl                           | FALSE                           |
| ssl-ca                        | (No default value)              |
| ssl-capath                    | (No default value)              |
| ssl-cert                      | (No default value)              |
| ssl-cipher                    | (No default value)              |
| ssl-key                       | (No default value)              |
| ssl-verify-server-cert        | FALSE                           |
| user                          | (No default value)              |
| verbose                       | FALSE                           |
| vertical                      | FALSE                           |
| connect\_timeout              | 43200                           |
| shutdown\_timeout             | 3600                            |

### mariadb-admin Commands

```
mariadb-admin [options] command [command-arg] [command [command-arg]] ...
```

_Command_ is one or more of the following. Commands may be shortened to a unique prefix.

| Command                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Command                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| create databasename       | Create a new database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| debug                     | Instruct server to write debug information to log.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| drop databasename         | Delete a database and all its tables.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| extended-status           | Return all [status variables](../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md) and their values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| flush-all-statistics      | Flush all statistics tables                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| flush-all-status          | Flush status and statistics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| flush-binary-log          | Flush [binary log](../server-management/server-monitoring-logs/binary-log/).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| flush-client-statistics   | Flush client statistics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| flush-engine-log          | Flush engine log.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| flush-error-log           | Flush [error log](../server-management/server-monitoring-logs/error-log.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| flush-general-log         | Flush [general query log](../server-management/server-monitoring-logs/general-query-log.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| flush-hosts               | Flush all cached hosts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| flush-index-statistics    | Flush index statistics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| flush-logs                | Flush all logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| flush-privileges          | Reload grant tables (same as reload).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| flush-relay-log           | Flush [relay log](../server-management/server-monitoring-logs/binary-log/relay-log.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| flush-slow-log            | Flush slow query log.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| flush-ssl                 | Flush SSL certificates. Added in [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| flush-status              | Clear [status variables](../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| flush-table-statistics    | Clear table statistics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| flush-tables              | Flush all tables.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| flush-threads             | Flush the thread cache.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| flush-user-resources      | Flush user resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| flush-user-statistics     | Flush user statistics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| kill id,id,...            | Kill mysql threads.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| password new-password     | Change old password to new-password. The new password can be passed on the commandline as the next argument (for example, mariadb-admin password "new\_password", or can be omitted (as long as no other command follows), in which case the user will be prompted for a password. If the password contains special characters, it needs to be enclosed in quotation marks. In Windows, the quotes can only be double quotes, as single quotes are assumed to be part of the password. If the server was started with the [--skip-grant-tables](../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-skip-grant-tables) option, changing the password in this way will have no effect. |
| old-password new-password | Change old password to new-password using the old pre-MySQL 4.1 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ping                      | Check if mariadbd is alive. Return status is 0 if the server is running (even in the case of an error such as access denied), 1 if it is not.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| processlist               | Show list of active threads in server, equivalent to [SHOW PROCESSLIST](../reference/sql-statements/administrative-sql-statements/show/show-processlist.md). With --verbose, equivalent to [SHOW FULL PROCESSLIST](../reference/sql-statements/administrative-sql-statements/show/show-processlist.md).                                                                                                                                                                                                                                                                                                                                                                                                   |
| reload                    | Reload grant tables.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| refresh                   | Flush all tables and close and open log files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| shutdown                  | Take server down by executing the [SHUTDOWN](../reference/sql-statements/administrative-sql-statements/shutdown.md) command on the server. If connected to a local server using a Unix socket file, mariadb-admin waits until the server's process ID file has been removed to ensure that the server has stopped properly. See also the --wait-for-all-slaves option.                                                                                                                                                                                                                                                                                                                                    |
| status                    | Gives a short status message from the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| start-all-slaves          | Start all replicas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| start-slave               | Start replication on a replica server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| stop-all-slaves           | Stop all replicas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| stop-slave                | Stop replication on a replica server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| variables                 | Prints variables available.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| version                   | Returns version as well as status info from the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

### The shutdown Command and the --wait-for-all-slaves Option

The `--wait-for-all-slaves` option was first added in [MariaDB 10.4.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1044-release-notes). When a primary server is shutdown and it goes through the normal shutdown process, the primary kills client threads in random order. By default, the primary also considers its binary log dump threads to be regular client threads. As a consequence, the binary log dump threads can be killed while client threads still exist, and this means that data can be written on the primary during a normal shutdown that won't be replicated. This is true even if [semi-synchronous replication](../ha-and-performance/standard-replication/semisynchronous-replication.md) is being used.

In [MariaDB 10.4](broken-reference) and later, this problem can be solved by shutting down the server with the mariadb-admin utility and by providing the `--wait-for-all-slaves` option to the utility and by executing the `shutdown` command with the utility. For example:

```
mariadb-admin --wait-for-all-slaves shutdown
```

When the `--wait-for-all-slaves` option is provided, the server only kills its binary log dump threads after all client threads have been killed, and it only completes the shutdown after the last [binary log](../server-management/server-monitoring-logs/binary-log/) has been sent to all connected replicas.

See [Replication Threads: Binary Log Dump Threads and the Shutdown Process](../ha-and-performance/standard-replication/replication-threads.md#binary-log-dump-threads-and-the-shutdown-process) for more information.

### Examples

Quick check of what the server is doing:

```
shell> mariadb-admin status
Uptime: 8023 Threads: 1 Questions: 14 Slow queries: 0 Opens: 15 Flush tables: 1 Open tables: 8 Queries per second avg: 0.1
shell> mariadb-admin processlist
+----+-------+-----------+----+---------+------+-------+------------------+
| Id | User | Host | db | Command | Time | State | Info |
+----+-------+-----------+----+---------+------+-------+------------------+
....
+----+-------+-----------+----+---------+------+-------+------------------+
```

More extensive information of what is happening 'just now' changing\
(great for troubleshooting a slow server):

```
shell> mariadb-admin --relative --sleep=1 extended-status | grep -v " 0 "
```

Check the variables for a running server:

```
shell> mariadb-admin variables | grep datadir
| datadir | /my/data/ |
```

Using a shortened prefix for the `version` command:

```
shell> mariadb-admin ver
mariadb-admin from 11.1.0-preview-MariaDB, client 9.1 for linux-systemd (x86_64)
Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Server version		11.1.0-preview-MariaDB
Protocol version	10
Connection		localhost via TCP/IP
TCP port		11100
Uptime:			3 min 21 sec

Threads: 1  Questions: 1  Slow queries: 0  Opens: 17  Open tables: 10  Queries per second avg: 0.004
```

#### Other Ways To Stop mariadbd (Unix)

If you get the error:

```
mariadb-admin: shutdown failed; error: 'Access denied; you need (at least one of) the SHUTDOWN privilege(s) for this operation'
```

It means that you didn't use `mariadb-admin` with a user that has the SUPER or SHUTDOWN privilege.

If you don't know the user password, you can still take the mariadbd process down with a system `kill` command:

```
kill -SIGTERM pid-of-mariadbd-process
```

The above is identical to `mariadb-admin shutdown`.

On windows you should use:

```
NET STOP MySQL
```

You can use the [SHUTDOWN](../reference/sql-statements/administrative-sql-statements/shutdown.md) command from any client.

### See Also

* [SHUTDOWN command](../reference/sql-statements/administrative-sql-statements/shutdown.md)
* [mytop](https://www.mysqlfanboy.com/mytop-3/), a 'top' like program for\
  MariaDB/MySQL that allows you to see what the server is doing. A mytop\
  optimized for MariaDB is included in [MariaDB 5.3](broken-reference)

CC BY-SA / Gnu FDL
