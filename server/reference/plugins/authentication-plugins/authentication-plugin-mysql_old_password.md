
# Authentication Plugin - mysql_old_password

The `<code>mysql_old_password</code>` authentication plugin is the default authentication plugin that will be used for an account created when no authentication plugin is explicitly mentioned and `<code>[old_passwords=1](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old_passwords)</code>` is set. It uses the pre-MySQL 4.1 password hashing algorithm, which is also used by the `<code>[OLD_PASSWORD()](../../sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/encryption-hashing-and-compression-functions/old_password.md)</code>` function and by the `<code>[PASSWORD()](../password-validation-plugins/password-reuse-check-plugin.md)</code>` function when `<code>[old_passwords=1](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old_passwords)</code>` is set.


It is not recommended to use the `<code>mysql_old_password</code>` authentication plugin for new installations. The password hashing algorithm is no longer as secure as it used to be, and the plugin is primarily provided for backward-compatibility. The `<code>[ed25519](authentication-plugin-ed25519.md)</code>` authentication plugin is a more modern authentication plugin that provides simple password authentication.



## Installing the Plugin


The `<code>mysql_old_password</code>` authentication plugin is statically linked into the server, so no installation is necessary.


## Creating Users


The easiest way to create a user account with the `<code>mysql_old_password</code>` authentication plugin is to make sure that `<code>[old_passwords=1](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old_passwords)</code>` is set, and then create a user account via `<code>[CREATE USER](../../sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user.md)</code>` that does not specify an authentication plugin, but does specify a password via the `<code>[IDENTIFIED BY](../../sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user.md#identified-by-password)</code>` clause. For example:


```
SET old_passwords=1;
CREATE USER username@hostname IDENTIFIED BY 'mariadb';
```

If `<code>[SQL_MODE](../../../server-management/variables-and-modes/sql-mode.md)</code>` does not have `<code>NO_AUTO_CREATE_USER</code>` set, then you can also create the user via `<code>[GRANT](../../sql-statements-and-structure/sql-statements/account-management-sql-commands/grant.md)</code>`. For example:


```
SET old_passwords=1;
GRANT SELECT ON db.* TO username@hostname IDENTIFIED BY 'mariadb';
```

You can also create the user account by providing a password hash via the `<code>[IDENTIFIED BY PASSWORD](../../sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user.md#identified-by-password-password_hash)</code>` clause, and MariaDB will validate whether the password hash is one that is compatible with `<code>mysql_old_password</code>`. For example:


```
SET old_passwords=1;
Query OK, 0 rows affected (0.000 sec)

SELECT PASSWORD('mariadb');
+---------------------+
| PASSWORD('mariadb') |
+---------------------+
| 021bec665bf663f1    |
+---------------------+
1 row in set (0.000 sec)

CREATE USER username@hostname IDENTIFIED BY PASSWORD '021bec665bf663f1';
Query OK, 0 rows affected (0.000 sec)
```

Similar to all other [authentication plugins](README.md), you could also specify the name of the plugin in the `<code>[IDENTIFIED VIA](../../sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user.md#identified-viawith-authentication_plugin)</code>` clause while providing the password hash as the `<code>USING</code>` clause. For example:


```
CREATE USER username@hostname IDENTIFIED VIA mysql_old_password USING '021bec665bf663f1';
Query OK, 0 rows affected (0.000 sec)
```

## Changing User Passwords


You can change a user account's password with the `<code>[SET PASSWORD](../../sql-statements-and-structure/sql-statements/account-management-sql-commands/set-password.md)</code>` statement while providing the plain-text password as an argument to the `<code>[PASSWORD()](../password-validation-plugins/password-reuse-check-plugin.md)</code>` function. For example:


```
SET PASSWORD =  PASSWORD('new_secret')
```

You can also change the user account's password with the `<code>[ALTER USER](../../sql-statements-and-structure/sql-statements/account-management-sql-commands/alter-user.md)</code>` statement. You would have to make sure that `<code>[old_passwords=1](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old_passwords)</code>` is set, and then you would have to specify a password via the `<code>[IDENTIFIED BY](../../sql-statements-and-structure/sql-statements/account-management-sql-commands/alter-user.md#identified-by-password)</code>` clause. For example:


```
SET old_passwords=1;
ALTER USER username@hostname IDENTIFIED BY 'new_secret';
```

## Client Authentication Plugins


For clients that use the `<code>libmysqlclient</code>` or [MariaDB Connector/C](../../../../connectors/mariadb-connector-cpp/mariadb-connector-cpp-sample-application.md) libraries, MariaDB provides one client authentication plugin that is compatible with the `<code>mysql_old_password</code>` authentication plugin:


* `<code>mysql_old_password</code>`


When connecting with a [client or utility](/kb/en/clients-utilities/) to a server as a user account that authenticates with the `<code>mysql_old_password</code>` authentication plugin, you may need to tell the client where to find the relevant client authentication plugin by specifying the `<code>--plugin-dir</code>` option. For example:


```
mysql --plugin-dir=/usr/local/mysql/lib64/mysql/plugin --user=alice
```

However, the `<code>mysql_old_password</code>` client authentication plugin is generally statically linked into client libraries like `<code>libmysqlclient</code>` or [MariaDB Connector/C](../../../../connectors/mariadb-connector-cpp/mariadb-connector-cpp-sample-application.md), so this is not usually necessary.


### `<code>mysql_old_password</code>`


The `<code>mysql_old_password</code>` client authentication plugin hashes the password before sending it to the server.


## Support in Client Libraries


The `<code>mysql_old_password</code>` authentication plugin is one of the conventional authentication plugins, so all client libraries should support it.

