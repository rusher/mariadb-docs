# CREATE USER

### Syntax <a href="#syntax" id="syntax"></a>

```
CREATE [OR REPLACE] USER [IF NOT EXISTS] 
 user_specification [,user_specification ...] 
  [REQUIRE {NONE | tls_option [[AND] tls_option ...] }]
  [WITH resource_option [resource_option ...] ]
  [lock_option] [password_option] 

user_specification:
  username [authentication_option]

authentication_option:
  IDENTIFIED BY 'password' 
  | IDENTIFIED BY PASSWORD 'password_hash'
  | IDENTIFIED {VIA|WITH} authentication_rule [OR authentication_rule  ...]

authentication_rule:
    authentication_plugin
  | authentication_plugin {USING|AS} 'authentication_string'
  | authentication_plugin {USING|AS} PASSWORD('password')

tls_option:
  SSL 
  | X509
  | CIPHER 'cipher'
  | ISSUER 'issuer'
  | SUBJECT 'subject'

resource_option:
  MAX_QUERIES_PER_HOUR count
  | MAX_UPDATES_PER_HOUR count
  | MAX_CONNECTIONS_PER_HOUR count
  | MAX_USER_CONNECTIONS count
  | MAX_STATEMENT_TIME time

password_option:
  PASSWORD EXPIRE
  | PASSWORD EXPIRE DEFAULT
  | PASSWORD EXPIRE NEVER
  | PASSWORD EXPIRE INTERVAL N DAY

lock_option:
    ACCOUNT LOCK
  | ACCOUNT UNLOCK
}
```

### Description <a href="#description" id="description"></a>

The `CREATE USER` statement creates new MariaDB accounts. To use it, you must have the global [CREATE USER](https://mariadb.com/kb/en/grant/#create-user) privilege or the [INSERT](https://mariadb.com/kb/en/grant/#table-privileges) privilege for the [mysql](https://mariadb.com/kb/en/the-mysql-database-tables/) database. For each account, `CREATE USER` creates a new row in [mysql.user](https://mariadb.com/kb/en/mysqluser-table/) (until [MariaDB 10.3](https://mariadb.com/kb/en/what-is-mariadb-103/) this is a table, from [MariaDB 10.4](https://mariadb.com/kb/en/what-is-mariadb-104/) it's a view) or [mysql.global\_priv\_table](https://mariadb.com/kb/en/mysqlglobal_priv-table/) (from [MariaDB 10.4](https://mariadb.com/kb/en/what-is-mariadb-104/)) that has no privileges.

If any of the specified accounts, or any permissions for the specified accounts, already exist, then the server returns `ERROR 1396 (HY000)`. If an error occurs, `CREATE USER` will still create the accounts that do not result in an error. Only one error is produced for all users which have not been created:

```
ERROR 1396 (HY000): 
  Operation CREATE USER failed for 'u1'@'%','u2'@'%'
```

`CREATE USER`, [DROP USER](https://mariadb.com/kb/en/drop-user/), [CREATE ROLE](https://mariadb.com/kb/en/create-role/), and [DROP ROLE](https://mariadb.com/kb/en/drop-role/) all produce the same error code when they fail.

See [Account Names](https://mariadb.com/kb/en/create-user/#account-names) below for details on how account names are specified.

One can also create users with [GRANT](https://mariadb.com/kb/en/grant/) if [SQL\_MODE](https://mariadb.com/kb/en/sql-mode/) does not have [NO\_AUTO\_CREATE\_USER](https://mariadb.com/kb/en/sql-mode/#no_auto_create_user) set. `NO_AUTO_CREATE_USER` is set by default.

### OR REPLACE <a href="#or-replace" id="or-replace"></a>

If the optional `OR REPLACE` clause is used, it is basically a shortcut for:

```
DROP USER IF EXISTS name;
CREATE USER name ...;
```

For example:

```
CREATE USER foo2@test IDENTIFIED BY 'password';
ERROR 1396 (HY000): Operation CREATE USER failed for 'foo2'@'test'

CREATE OR REPLACE USER foo2@test IDENTIFIED BY 'password';
Query OK, 0 rows affected (0.00 sec)
```

### IF NOT EXISTS <a href="#if-not-exists" id="if-not-exists"></a>

When the `IF NOT EXISTS` clause is used, MariaDB will return a warning instead of an error if the specified user already exists.

For example:

```
CREATE USER foo2@test IDENTIFIED BY 'password';
ERROR 1396 (HY000): Operation CREATE USER failed for 'foo2'@'test'

CREATE USER IF NOT EXISTS foo2@test IDENTIFIED BY 'password';
Query OK, 0 rows affected, 1 warning (0.00 sec)

SHOW WARNINGS;
+-------+------+----------------------------------------------------+
| Level | Code | Message                                            |
+-------+------+----------------------------------------------------+
| Note  | 1973 | Can't create user 'foo2'@'test'; it already exists |
+-------+------+----------------------------------------------------+
```

### Authentication Options <a href="#authentication-options" id="authentication-options"></a>

If more than one authentication mechanism is declared using the `OR` keyword, the mechanisms are attempted in the order they are declared in the `CREATE USER` statement. As soon as one of the authentication mechanisms is successful, authentication is complete. If none of them is successful, the authentication has failed.

#### IDENTIFIED BY 'password' <a href="#identified-by-password" id="identified-by-password"></a>

The optional `IDENTIFIED BY` clause can be used to provide an account with a password. The password should be specified in plain text. It will be hashed by the [PASSWORD](https://mariadb.com/kb/en/password/) function prior to being stored in the [mysql.user](https://mariadb.com/kb/en/mysqluser-table/)/[mysql.global\_priv\_table](https://mariadb.com/kb/en/mysqlglobal_priv-table/) table.

For example, if our password is `mariadb`, then we can create the user with:

```
CREATE USER foo2@test IDENTIFIED BY 'mariadb';
```

If you do not specify a password with the `IDENTIFIED BY` clause, the user will be able to connect without a password. A blank password is not a wildcard to match any password. The user must connect without providing a password if no password is set.

The only [authentication plugins](https://mariadb.com/kb/en/authentication-plugins/) that this clause supports are [mysql\_native\_password](https://mariadb.com/kb/en/authentication-plugin-mysql_native_password/) and [mysql\_old\_password](https://mariadb.com/kb/en/authentication-plugin-mysql_old_password/).

#### IDENTIFIED BY PASSWORD 'password\_hash' <a href="#identified-by-password-password_hash" id="identified-by-password-password_hash"></a>

The optional `IDENTIFIED BY PASSWORD` clause can be used to provide an account with a password that has already been hashed. The password should be specified as a hash that was provided by the [PASSWORD](https://mariadb.com/kb/en/password/) function. It will be stored in the [mysql.user](https://mariadb.com/kb/en/mysqluser-table/)/[mysql.global\_priv\_table](https://mariadb.com/kb/en/mysqlglobal_priv-table/) table as-is.

For example, if our password is `mariadb`, then we can find the hash with:

```
SELECT PASSWORD('mariadb');
+-------------------------------------------+
| PASSWORD('mariadb')                       |
+-------------------------------------------+
| *54958E764CE10E50764C2EECBB71D01F08549980 |
+-------------------------------------------+
1 row in set (0.00 sec)
```

And then we can create a user with the hash:

```
CREATE USER foo2@test IDENTIFIED BY PASSWORD '*54958E764CE10E50764C2EECBB71D01F08549980';
```

If you do not specify a password with the `IDENTIFIED BY` clause, the user will be able to connect without a password. A blank password is not a wildcard to match any password. The user must connect without providing a password if no password is set.

The only [authentication plugins](https://mariadb.com/kb/en/authentication-plugins/) that this clause supports are [mysql\_native\_password](https://mariadb.com/kb/en/authentication-plugin-mysql_native_password/) and [mysql\_old\_password](https://mariadb.com/kb/en/authentication-plugin-mysql_old_password/).

#### IDENTIFIED {VIA|WITH} authentication\_plugin <a href="#identified-viawith-authentication_plugin" id="identified-viawith-authentication_plugin"></a>

The optional `IDENTIFIED VIA authentication_plugin` allows you to specify that the account should be authenticated by a specific [authentication plugin](https://mariadb.com/kb/en/authentication-plugins/). The plugin name must be an active authentication plugin as per [SHOW PLUGINS](https://mariadb.com/kb/en/show-plugins/). If it doesn't show up in that output, then you will need to install it with [INSTALL PLUGIN](https://mariadb.com/kb/en/install-plugin/) or [INSTALL SONAME](https://mariadb.com/kb/en/install-soname/).

`VIA` and `WITH` are synonyms.

For example, this could be used with the [PAM authentication plugin](https://mariadb.com/kb/en/authentication-plugin-pam/):

```
CREATE USER foo2@test IDENTIFIED VIA pam;
```

Some authentication plugins allow additional arguments to be specified after a `USING` or `AS` keyword. For example, the [PAM authentication plugin](https://mariadb.com/kb/en/authentication-plugin-pam/) accepts a [service name](https://mariadb.com/kb/en/authentication-plugin-pam/#configuring-the-pam-service):

```
CREATE USER foo2@test IDENTIFIED VIA pam USING 'mariadb';
```

The exact meaning of the additional argument would depend on the specific authentication plugin.

The `USING` or `AS` keyword can also be used to provide a plain-text password to a plugin if it's provided as an argument to the [PASSWORD()](https://mariadb.com/kb/en/password/) function. This is only valid for [authentication plugins](https://mariadb.com/kb/en/authentication-plugins/) that have implemented a hook for the [PASSWORD()](https://mariadb.com/kb/en/password/) function. For example, the [ed25519](https://mariadb.com/kb/en/authentication-plugin-ed25519/) authentication plugin supports this:

```
CREATE USER safe@'%' IDENTIFIED VIA ed25519 USING PASSWORD('secret');
```

One can specify many authentication plugins, they all work as alternatives ways of authenticating a user:

```
CREATE USER safe@'%' IDENTIFIED VIA ed25519 USING PASSWORD('secret') OR unix_socket;
```

By default, when you create a user without specifying an authentication plugin, MariaDB uses the [mysql\_native\_password](https://mariadb.com/kb/en/authentication-plugin-mysql_native_password/) plugin.

### TLS Options <a href="#tls-options" id="tls-options"></a>

By default, prior to [MariaDB 11.4](https://mariadb.com/kb/en/what-is-mariadb-114/), MariaDB transmits data between the server and clients without encrypting it. This is generally acceptable when the server and client run on the same host or in networks where security is guaranteed through other means. However, in cases where the server and client exist on separate networks or they are in a high-risk network, the lack of encryption does introduce security concerns as a malicious actor could potentially eavesdrop on the traffic as it is sent over the network between them.

To mitigate this concern, MariaDB allows you to encrypt data in transit between the server and clients using the Transport Layer Security (TLS) protocol. TLS was formerly known as Secure Socket Layer (SSL), but strictly speaking the SSL protocol is a predecessor to TLS and, that version of the protocol is now considered insecure. The documentation still uses the term SSL often and for compatibility reasons TLS-related server system and status variables still use the prefix ssl\_, but internally, MariaDB only supports its secure successors.

See [Secure Connections Overview](https://mariadb.com/kb/en/secure-connections-overview/) for more information about how to determine whether your MariaDB server has TLS support.

You can set certain TLS-related restrictions for specific user accounts. For instance, you might use this with user accounts that require access to sensitive data while sending it across networks that you do not control. These restrictions can be enabled for a user account with the [CREATE USER](https://mariadb.com/kb/en/create-user/), [ALTER USER](https://mariadb.com/kb/en/alter-user/), or [GRANT](https://mariadb.com/kb/en/grant/) statements. The following options are available:

| Option                      | Description                                                                                                                                                                                                                                                                                                 |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `REQUIRE NONE`              | TLS is not required for this account, but can still be used.                                                                                                                                                                                                                                                |
| `REQUIRE SSL`               | The account must use TLS, but no valid X509 certificate is required. This option cannot be combined with other TLS options.                                                                                                                                                                                 |
| `REQUIRE X509`              | The account must use TLS and must have a valid X509 certificate. This option implies `REQUIRE SSL`. This option cannot be combined with other TLS options.                                                                                                                                                  |
| `REQUIRE ISSUER 'issuer'`   | The account must use TLS and must have a valid X509 certificate. Also, the Certificate Authority must be the one specified via the string `issuer`. This option implies `REQUIRE X509`. This option can be combined with the `SUBJECT`, and `CIPHER` options in any order.                                  |
| `REQUIRE SUBJECT 'subject'` | The account must use TLS and must have a valid X509 certificate. Also, the certificate's Subject must be the one specified via the string `subject`. This option implies `REQUIRE X509`. This option can be combined with the `ISSUER`, and `CIPHER` options in any order.                                  |
| `REQUIRE CIPHER 'cipher'`   | The account must use TLS, but no valid X509 certificate is required. Also, the encryption used for the connection must use a specific cipher method specified in the string `cipher`. This option implies `REQUIRE SSL`. This option can be combined with the `ISSUER`, and `SUBJECT` options in any order. |

The `REQUIRE` keyword must be used only once for all specified options, and the `AND` keyword can be used to separate individual options, but it is not required.

For example, you can create a user account that requires these TLS options with the following:

```
CREATE USER 'alice'@'%'
 REQUIRE SUBJECT '/CN=alice/O=My Dom, Inc./C=US/ST=Oregon/L=Portland'
 AND ISSUER '/C=FI/ST=Somewhere/L=City/ O=Some Company/CN=Peter Parker/emailAddress=p.parker@marvel.com'
 AND CIPHER 'SHA-DES-CBC3-EDH-RSA';
```

If any of these options are set for a specific user account, then any client who tries to connect with that user account will have to be configured to connect with TLS.

See [Securing Connections for Client and Server](https://mariadb.com/kb/en/securing-connections-for-client-and-server/) for information on how to enable TLS on the client and server.

### Resource Limit Options <a href="#resource-limit-options" id="resource-limit-options"></a>

It is possible to set per-account limits for certain server resources. The following table shows the values that can be set per account:

| Limit Type                 | Decription                                                                                                                                                                                                                   |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `MAX_QUERIES_PER_HOUR`     | Number of statements that the account can issue per hour (including updates)                                                                                                                                                 |
| `MAX_UPDATES_PER_HOUR`     | Number of updates (not queries) that the account can issue per hour                                                                                                                                                          |
| `MAX_CONNECTIONS_PER_HOUR` | Number of connections that the account can start per hour                                                                                                                                                                    |
| `MAX_USER_CONNECTIONS`     | Number of simultaneous connections that can be accepted from the same account; if it is 0, `max_connections` will be used instead; if `max_connections` is 0, there is no limit for this account's simultaneous connections. |
| `MAX_STATEMENT_TIME`       | Timeout, in seconds, for statements executed by the user. See also [Aborting Statements that Exceed a Certain Time to Execute](https://mariadb.com/kb/en/aborting-statements/).                                              |

If any of these limits are set to `0`, then there is no limit for that resource for that user.

Here is an example showing how to create a user with resource limits:

```
CREATE USER 'someone'@'localhost' WITH
    MAX_USER_CONNECTIONS 10
    MAX_QUERIES_PER_HOUR 200;
```

The resources are tracked per account, which means `'user'@'server'`; not per user name or per connection.

The count can be reset for all users using [FLUSH USER\_RESOURCES](https://mariadb.com/kb/en/flush/), [FLUSH PRIVILEGES](https://mariadb.com/kb/en/flush/) or [mariadb-admin reload](https://mariadb.com/kb/en/mariadb-admin/).

Per account resource limits are stored in the [user](https://mariadb.com/kb/en/mysqluser-table/) table, in the [mysql](https://mariadb.com/kb/en/the-mysql-database-tables/) database. Columns used for resources limits are named `max_questions`, `max_updates`, `max_connections` (for `MAX_CONNECTIONS_PER_HOUR`), and `max_user_connections` (for `MAX_USER_CONNECTIONS`).

### Account Names <a href="#account-names" id="account-names"></a>

Account names have both a user name component and a host name component, and are specified as `'user_name'@'host_name'`.

The user name and host name may be unquoted, quoted as strings using double quotes (`"`) or single quotes (`'`), or quoted as identifiers using backticks (`` ` ``). You must use quotes when using special characters (such as a hyphen) or wildcard characters. If you quote, you must quote the user name and host name separately (for example `'user_name'@'host_name'`).

#### Host Name Component <a href="#host-name-component" id="host-name-component"></a>

If the host name is not provided, it is assumed to be `'%'`.

Host names may contain the wildcard characters `%` and `_`. They are matched as if by the [LIKE](https://mariadb.com/kb/en/like/) clause. If you need to use a wildcard character literally (for example, to match a domain name with an underscore), prefix the character with a backslash. See `LIKE` for more information on escaping wildcard characters.

Host name matches are case-insensitive. Host names can match either domain names or IP addresses. Use `'localhost'` as the host name to allow only local client connections. On Linux, the loopback interface (127.0.0.1) will not match 'localhost' as it is not considered a local connection: this means that only connections via UNIX-domain sockets will match 'localhost'.

You can use a netmask to match a range of IP addresses using `'base_ip/netmask'` as the host name. A user with an IP address _ip\_addr_ will be allowed to connect if the following condition is true:

```
ip_addr & netmask = base_ip
```

For example, given a user:

```
CREATE USER 'maria'@'247.150.130.0/255.255.255.0';
```

the IP addresses satisfying this condition range from 247.150.130.0 to 247.150.130.255.

Using `255.255.255.255` is equivalent to not using a netmask at all. Netmasks cannot be used for IPv6 addresses.

Note that the credentials added when creating a user with the `'%'` wildcard host will not grant access in all cases. For example, some systems come with an anonymous localhost user, and when connecting from localhost this will take precedence.

Before [MariaDB 10.6](https://mariadb.com/kb/en/what-is-mariadb-106/), the host name component could be up to 60 characters in length. Starting from [MariaDB 10.6](https://mariadb.com/kb/en/what-is-mariadb-106/), it can be up to 255 characters.

#### User Name Component <a href="#user-name-component" id="user-name-component"></a>

User names must match exactly, including case. A user name that is empty is known as an anonymous account and is allowed to match a login attempt with any user name component. These are described more in the next section.

For valid identifiers to use as user names, see [Identifier Names](https://mariadb.com/kb/en/identifier-names/).

It is possible for more than one account to match when a user connects. MariaDB selects the first matching account after sorting according to the following criteria:

* Accounts with an exact host name are sorted before accounts using a wildcard in the host name. Host names using a netmask are considered to be exact for sorting.
* Accounts with a wildcard in the host name are sorted according to the position of the first wildcard character. Those with a wildcard character later in the host name sort before those with a wildcard character earlier in the host name.
* Accounts with a non-empty user name sort before accounts with an empty user name.
* Accounts with an empty user name are sorted last. As mentioned previously, these are known as anonymous accounts. These are described more in the next section.

The following table shows a list of example account as sorted by these criteria:

```
+---------+-------------+
| User    | Host        |
+---------+-------------+
| joffrey | 192.168.0.3 |
|         | 192.168.0.% |
| joffrey | 192.168.%   |
|         | 192.168.%   |
+---------+-------------+
```

Once connected, you only have the privileges granted to the account that matched, not all accounts that could have matched. For example, consider the following commands:

```
CREATE USER 'joffrey'@'192.168.0.3';
CREATE USER 'joffrey'@'%';
GRANT SELECT ON test.t1 to 'joffrey'@'192.168.0.3';
GRANT SELECT ON test.t2 to 'joffrey'@'%';
```

If you connect as joffrey from `192.168.0.3`, you will have the `SELECT` privilege on the table `test.t1`, but not on the table `test.t2`. If you connect as joffrey from any other IP address, you will have the `SELECT` privilege on the table `test.t2`, but not on the table `test.t1`.

Usernames can be up to 80 characters long before 10.6 and starting from 10.6 it can be 128 characters long.

#### Anonymous Accounts <a href="#anonymous-accounts" id="anonymous-accounts"></a>

Anonymous accounts are accounts where the user name portion of the account name is empty. These accounts act as special catch-all accounts. If a user attempts to log into the system from a host, and an anonymous account exists with a host name portion that matches the user's host, then the user will log in as the anonymous account if there is no more specific account match for the user name that the user entered.

For example, here are some anonymous accounts:

```
CREATE USER ''@'localhost';
CREATE USER ''@'192.168.0.3';
```

**Fixing a Legacy Default Anonymous Account**

On some systems, the [mysql.db](https://mariadb.com/kb/en/mysqldb-table/) table has some entries for the `''@'%'` anonymous account by default. Unfortunately, there is no matching entry in the [mysql.user](https://mariadb.com/kb/en/mysqluser-table/)/[mysql.global\_priv\_table](https://mariadb.com/kb/en/mysqlglobal_priv-table/) table, which means that this anonymous account doesn't exactly exist, but it does have privileges--usually on the default `test` database created by [mariadb-install-db](https://mariadb.com/kb/en/mariadb-install-db/). These account-less privileges are a legacy that is leftover from a time when MySQL's privilege system was less advanced.

This situation means that you will run into errors if you try to create a `''@'%'` account. For example:

```
CREATE USER ''@'%';
ERROR 1396 (HY000): Operation CREATE USER failed for ''@'%'
```

The fix is to [DELETE](https://mariadb.com/kb/en/delete/) the row in the [mysql.db](https://mariadb.com/kb/en/mysqldb-table/) table and then execute [FLUSH PRIVILEGES](https://mariadb.com/kb/en/flush/):

```
DELETE FROM mysql.db WHERE User='' AND Host='%';
FLUSH PRIVILEGES;
```

Note that `FLUSH PRIVILEGES` is only needed if one modifies the `mysql` tables directly. It is not needed when using `CREATE USER`, `DROP USER`, `GRANT` etc.

And then the account can be created:

```
CREATE USER ''@'%';
Query OK, 0 rows affected (0.01 sec)
```

See [MDEV-13486](https://jira.mariadb.org/browse/MDEV-13486) for more information.

### Password Expiry <a href="#password-expiry" id="password-expiry"></a>

Besides automatic password expiry, as determined by [default\_password\_lifetime](https://mariadb.com/kb/en/server-system-variables/#default_password_lifetime), password expiry times can be set on an individual user basis, overriding the global setting, for example:

```
CREATE USER 'monty'@'localhost' PASSWORD EXPIRE INTERVAL 120 DAY;
```

See [User Password Expiry](https://mariadb.com/kb/en/user-password-expiry/) for more details.

### Account Locking <a href="#account-locking" id="account-locking"></a>

Account locking permits privileged administrators to lock/unlock user accounts. No new client connections will be permitted if an account is locked (existing connections are not affected). For example: `<<sql>>` CREATE USER 'marijn'@'localhost' ACCOUNT LOCK;

See [Account Locking](https://mariadb.com/kb/en/account-locking/) for more details. <\</product>>

From [MariaDB 10.4.7](https://mariadb.com/kb/en/mariadb-1047-release-notes/) and [MariaDB 10.5.8](https://mariadb.com/kb/en/mariadb-1058-release-notes/), the _lock\_option_ and _password\_option_ clauses can occur in either order.

### See Also <a href="#see-also" id="see-also"></a>

* [GRANT](https://mariadb.com/kb/en/grant/)
* [ALTER USER](https://mariadb.com/kb/en/alter-user/)
* [RENAME USER](https://mariadb.com/kb/en/rename-user/)
* [DROP USER](https://mariadb.com/kb/en/drop-user/)
* [CREATE ROLE](https://mariadb.com/kb/en/create-role/)
* [SET PASSWORD](https://mariadb.com/kb/en/set-password/)
* [SHOW CREATE USER](https://mariadb.com/kb/en/show-create-user/)
* [Troubleshooting Connection Issues](https://mariadb.com/kb/en/troubleshooting-connection-issues/)
* [Authentication from MariaDB 10.4](https://mariadb.com/kb/en/authentication-from-mariadb-104/)
* [Identifier Names](https://mariadb.com/kb/en/identifier-names/)
* [mysql.user table](https://mariadb.com/kb/en/mysqluser-table/)
* [mysql.global\_priv\_table](https://mariadb.com/kb/en/mysqlglobal_priv-table/)
* [Password Validation Plugins](https://mariadb.com/kb/en/password-validation-plugins/) - permits the setting of basic criteria for passwords
* [Authentication Plugins](https://mariadb.com/kb/en/authentication-plugins/) - allow various authentication methods to be used, and new ones to be developed.
