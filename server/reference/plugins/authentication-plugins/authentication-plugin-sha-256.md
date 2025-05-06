
# Authentication Plugin - SHA-256


MySQL 5.6 added support for the `[sha256_password](https://dev.mysql.com/doc/refman/5.6/en/sha256-pluggable-authentication.html)` authentication plugin, and MySQL 8.0 also added support for the `[caching_sha2_password](https://dev.mysql.com/doc/refman/8.0/en/caching-sha2-pluggable-authentication.html)` authentication plugin.


The `caching_sha2_password` plugin is now the default authentication plugin in MySQL 8.0.4 and above, based on the value of the `[default_authentication_plugin](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_default_authentication_plugin)` system variable.


## Support in MariaDB Server


MariaDB Server does not currently support either the `[sha256_password](https://dev.mysql.com/doc/refman/5.6/en/sha256-pluggable-authentication.html)` or the `[caching_sha2_password](https://dev.mysql.com/doc/refman/8.0/en/caching-sha2-pluggable-authentication.html)` authentication plugins. See [MDEV-9804](https://jira.mariadb.org/browse/MDEV-9804) for more information. The majority of this article is about how to use MariaDB clients and connectors to connect to a MySQL server!


MariaDB Server does not support either of these authentication plugins. This is mainly because:


* To use the protocol, one has to distribute the server's public key to all MariaDB users, which can be cumbersome and impractical.
* The server gets the password in clear text which can cause problems if the user is convinced to connect to a malicious server.


If you are replacing a MySQL instance, that is using SHA-256 authentication, with MariaDB, you should start by changing SHA-256 authentication to use mysql_native_authentication.


```
ALTER USER user_name IDENTIFIED WITH mysql_native_password BY  'new_password'
```

## Support in Client Libraries


### Client Authentication Plugins


For clients that use the [MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/) library, MariaDB provides two client authentication plugins that are compatible with MySQL's SHA-256 authentication plugins:


* `sha256_password`
* `caching_sha256_password`


When connecting with a [client or utility](/kb/en/clients-utilities/) to a server as a user account that authenticates with the `sha256_password` or `caching_sha256_password` authentication plugin, you may need to tell the client where to find the relevant client authentication plugin by specifying the `--plugin-dir` option. For example:


```
mysql --plugin-dir=/usr/local/mysql/lib64/mysql/plugin --user=alice
```

For clients that use MariaDB's `libmysqlclient` library instead of [MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/), these client authentication plugins are not supported.


#### `sha256_password`


The `sha256_password` client authentication plugin is compatible with MySQL's `[sha256_password](https://dev.mysql.com/doc/refman/5.6/en/sha256-pluggable-authentication.html)` authentication plugin, which was added in MySQL 5.6.


#### `caching_sha256_password`


The `caching_sha256_password` client authentication plugin is compatible with MySQL's `[caching_sha2_password](https://dev.mysql.com/doc/refman/8.0/en/caching-sha2-pluggable-authentication.html)` authentication plugin, which was added in MySQL 8.0.


The `caching_sha2_password` plugin is now the default authentication plugin in MySQL 8.0.4 and above, based on the value of the `[default_authentication_plugin](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_default_authentication_plugin)` system variable.


### Using the Plugin with MariaDB Connector/C


[MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/) supports `sha256_password` and `caching_sha2_password` authentication using the [client authentication plugins](https://mariadb.com/kb/en/client-authentication-plugins) mentioned in the previous section.


It has supported the `sha256_password` client authentication plugin since MariaDB Connector/C 3.0.2. See [CONC-229](https://jira.mariadb.org/browse/CONC-229) for more information.


It has supported the `caching_sha256_password` client authentication plugin since MariaDB Connector/C 3.0.8 and MariaDB Connector/C 3.1.0. See [CONC-312](https://jira.mariadb.org/browse/CONC-312) for more information.


### Using Plugins with MariaDB Connector/ODBC


[MariaDB Connector/ODBC](/kb/en/about-mariadb-connector-odbc/) supports `sha256_password` and `caching_sha2_password` authentication using the [client authentication plugins](client-authentication-plugins) mentioned in the previous section.


It has supported `sha256_password` and `caching_sha2_password` authentication since MariaDB Connector/ODBC 3.1.4. See [ODBC-241](https://jira.mariadb.org/browse/ODBC-241) for more information.


### Using Plugins with MariaDB Connector/J


[MariaDB Connector/J](/kb/en/about-mariadb-connector-j/) supports `sha256_password` and `caching_sha2_password` authentication since MariaDB Connector/J 2.5.0. See [CONJ-327](https://jira.mariadb.org/browse/CONJ-327) and [CONJ-663](https://jira.mariadb.org/browse/CONJ-663) for more information.


note: The version 3.x being a rewrite of the connector, only caching_sha2_password is implemented, since sha256_password is only implemented on EOL version.


### Using Plugins with MariaDB Connector/Node.js


[MariaDB Connector/Node.js](/kb/en/nodejs-connector/) supports `sha256_password` and `caching_sha2_password` authentication since MariaDB Connector/Node.js 2.5.0. See [CONJS-76](https://jira.mariadb.org/browse/CONJS-76) and [CONJS-77](https://jira.mariadb.org/browse/CONJS-77) for more information.


## See Also


* [MDEV-9804](https://jira.mariadb.org/browse/MDEV-9804) contains the plans to use if we ever decide to support these protocols.
* [History of MySQL and MariaDB authentication protocols](https://mariadb.org/history-of-mysql-mariadb-authentication-protocols)


CC BY-SA / Gnu FDL

