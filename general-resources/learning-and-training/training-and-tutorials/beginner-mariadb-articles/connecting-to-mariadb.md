
# Connecting to MariaDB

This article covers connecting to MariaDB and the basic connection parameters. If you are completely new to MariaDB, take a look at [A MariaDB Primer](a-mariadb-primer.md) first.


In order to connect to the MariaDB server, the client software must provide the correct connection parameters. The client software will most often be the [mariadb client](../../../../server/clients-and-utilities/mariadb-client/README.md), used for entering statements from the command line, but the same concepts apply to any client, such as a [graphical client](../../../../server/clients-and-utilities/graphical-and-enhanced-clients/graphical-and-enhanced-clients-omnidb.md), a client to run backups such as [mariadb-dump](../../../../server/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md), etc. The rest of this article assumes that the mariadb command line client is used.


If a connection parameter is not provided, it will revert to a default value.


For example, to connect to MariaDB using only default values with the mariadb client, enter the following from the command line:


```
mariadb
```

In this case, the following defaults apply:


* The host name is `<code>localhost</code>`.
* The user name is either your Unix login name, or `<code>ODBC</code>` on Windows.
* No password is sent.
* The client will connect to the server with the default socket, but not any particular database on the server.


These defaults can be overridden by specifying a particular parameter to use. For example:


```
mariadb -h 166.78.144.191 -u username -ppassword database_name
```

In this case:


* `<code>-h</code>` specifies a host. Instead of using `<code>localhost</code>`, the IP `<code>166.78.144.191</code>` is used.
* `<code>-u</code>` specifies a user name, in this case `<code>username</code>`
* `<code>-p</code>` specifies a password, `<code>password</code>`. Note that for passwords, unlike the other parameters, there cannot be a space between the option (`<code>-p</code>`) and the value (`<code>password</code>`). It is also not secure to use a password in this way, as other users on the system can see it as part of the command that has been run. If you include the `<code>-p</code>` option, but leave out the password, you will be prompted for it, which is more secure.
* The database name is provided as the first argument after all the options, in this case `<code>database_name</code>`.
* It will connect with the default tcp_ip port, 3306


## Connection Parameters


### host


```
--host=name
-h name
```

Connect to the MariaDB server on the given host. The default host is `<code>localhost</code>`. By default, MariaDB does not permit remote logins - see [Configuring MariaDB for Remote Client Access](../basic-mariadb-articles/configuring-mariadb-for-remote-client-access.md).


### password


```
--password[=passwd]
-p[passwd]
```

The password of the MariaDB account. It is generally not secure to enter the password on the command line, as other users on the system can see it as part of the command that has been run. If you include the `<code>-p</code>` or `<code>--password</code>` option, but leave out the password, you will be prompted for it, which is more secure.


### pipe


```
--pipe
-W
```

On Windows systems that have been started with the `<code>--enable-named-pipe</code>` option, use this option to connect to the server using a named pipe.


### port


```
--port=num
-P num
```

The TCP/IP port number to use for the connection. The default is `<code>3306</code>`.


### protocol


```
--protocol=name
```

Specifies the protocol to be used for the connection for the connection. It can be one of `<code>TCP</code>`, `<code>SOCKET</code>`, `<code>PIPE</code>` or `<code>MEMORY</code>` (case-insensitive). Usually you would not want to change this from the default. For example on Unix, a Unix socket file (`<code>SOCKET</code>`) is the default protocol, and usually results in the quickest connection.


* `<code>TCP</code>`: A TCP/IP connection to a server (either local or remote). Available on all operating systems.
* `<code>SOCKET</code>`: A Unix socket file connection, available to the local server on Unix systems only. If socket is not specified with --socket, in a config file or with the environment variable `<code>MYSQL_UNIX_PORT</code>` then the default `<code>/tmp/mysql.sock</code>` will be used.
* `<code>PIPE</code>`. A named-pipe connection (either local or remote). Available on Windows only.
* `<code>MEMORY</code>`. Shared-memory connection to the local server on Windows systems only.


### shared-memory-base-name


```
--shared-memory-base-name=name
```

Only available on Windows systems in which the server has been started with the `<code>--shared-memory</code>` option, this specifies the shared-memory name to use for connecting to a local server. The value is case-sensitive, and defaults to `<code>MARIADB</code>`.


### socket


```
--socket=name
-S name
```

For connections to localhost, this specifies either the Unix socket file to use (default `<code>/tmp/mysql.sock</code>`), or, on Windows where the server has been started with the `<code>--enable-named-pipe</code>` option, the name (case-insensitive) of the named pipe to use (default `<code>MARIADB</code>`).


### TLS Options


A brief listing is provided below. See [Secure Connections Overview](../../../../server/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md) and [TLS System Variables](../../../../server/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md) for more detail.


#### ssl


```
--ssl
```

Enable TLS for connection (automatically enabled with other TLS flags). Disable with '`<code>--skip-ssl</code>`'


#### ssl-ca


```
--ssl-ca=name
```

CA file in PEM format (check OpenSSL docs, implies `<code>--ssl</code>`).


#### ssl-capath


```
--ssl-capath=name
```

|   |
| --- |
| CA directory (check OpenSSL docs, implies --ssl). |


#### ssl-cert


```
--ssl-cert=name
```

X509 cert in PEM format (implies `<code>--ssl</code>`).


#### ssl-cipher


```
--ssl-cipher=name
```

TLS cipher to use (implies `<code>--ssl</code>`).


#### ssl-key


```
--ssl-key=name
```

X509 key in PEM format (implies `<code>--ssl</code>`).


#### ssl-crl


```
--ssl-crl=name
```

Certificate revocation list (implies `<code>--ssl</code>`).


#### ssl-crlpath


```
--ssl-crlpath=name
```

Certificate revocation list path (implies `<code>--ssl</code>`).


#### ssl-verify-server-cert


```
--ssl-verify-server-cert
```

Verify server's "Common Name" in its cert against hostname used when connecting. This option is disabled by default.


### user


```
--user=name
-u name
```

The MariaDB user name to use when connecting to the server. The default is either your Unix login name, or `<code>ODBC</code>` on Windows. See the [GRANT](../../../../server/reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md) command for details on creating MariaDB user accounts.


## Option Files


It's also possible to use option files (or configuration files) to set these options. Most clients read option files. Usually, starting a client with the `<code>--help</code>` option will display which files it looks for as well as which option groups it recognizes.


## See Also


* [A MariaDB Primer](a-mariadb-primer.md)
* [mariadb client](../../../../server/clients-and-utilities/mariadb-client/README.md)
* [Clients and Utilities](../../../../server/clients-and-utilities/README.md)
* [Configuring MariaDB for Remote Client Access](../basic-mariadb-articles/configuring-mariadb-for-remote-client-access.md)
* [--skip-grant-tables](../../../../server/server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) allows you to start MariaDB without `<code>GRANT</code>`. This is useful if you lost your root password.

