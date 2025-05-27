# SET PASSWORD

## Syntax

```
SET PASSWORD [FOR user] =
    {
        PASSWORD('some password')
      | OLD_PASSWORD('some password')
      | 'encrypted password'
    }
```

## Description

The `SET PASSWORD` statement assigns a password to an existing MariaDB user\
account.

If the password is specified using the `[PASSWORD()](../built-in-functions/secondary-functions/encryption-hashing-and-compression-functions/password.md)` or `[OLD_PASSWORD()](../built-in-functions/secondary-functions/encryption-hashing-and-compression-functions/old_password.md)`\
function, the literal text of the password should be given. If the\
password is specified without using either function, the password\
should be the already-encrypted password value as returned by`[PASSWORD()](../built-in-functions/secondary-functions/encryption-hashing-and-compression-functions/password.md)`.

`[OLD_PASSWORD()](../built-in-functions/secondary-functions/encryption-hashing-and-compression-functions/old_password.md)` should only be used if your MariaDB/MySQL clients are very old (< 4.0.0).

With no `FOR` clause, this statement sets the password for the current\
user. Any client that has connected to the server using a non-anonymous\
account can change the password for that account.

With a `FOR` clause, this statement sets the password for a specific\
account on the current server host. Only clients that have the `UPDATE`\
privilege for the `mysql` database can do this. The user value should be\
given in `user_name@host_name` format, where `user_name` and `host_name` are\
exactly as they are listed in the User and Host columns of the`[mysql.user](../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-user-table.md)` table (or view in current versions) entry.

The argument to `[PASSWORD()](../built-in-functions/secondary-functions/encryption-hashing-and-compression-functions/password.md)` and the password given to MariaDB clients can be of arbitrary length.

## Authentication Plugin Support

`SET PASSWORD` (with or without `PASSWORD()`) works for accounts authenticated via any [authentication plugin](../../plugins/authentication-plugins/) that supports passwords stored in the `[mysql.global_priv](../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-global_priv-table.md)` table.

The `[ed25519](../../../plugins/authentication-plugins/authentication-plugin-ed25519.md)`, `[mysql_native_password](../../../plugins/authentication-plugins/authentication-plugin-mysql_native_password.md)`, and `[mysql_old_password](../../../plugins/authentication-plugins/authentication-plugin-mysql_old_password.md)` authentication plugins store passwords in the `[mysql.global_priv](../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-global_priv-table.md)` table.

If you run `SET PASSWORD` on an account that authenticates with one of these authentication plugins that stores passwords in the `[mysql.global_priv](../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-global_priv-table.md)` table, then the `PASSWORD()` function is evaluated by the specific authentication plugin used by the account. The authentication plugin hashes the password with a method that is compatible with that specific authentication plugin.

The `[unix_socket](../../../plugins/authentication-plugins/authentication-plugin-unix-socket.md)`, `[named_pipe](../../../plugins/authentication-plugins/authentication-plugin-named-pipe.md)`, `[gssapi](../../../plugins/authentication-plugins/authentication-plugin-gssapi.md)`, and `[pam](../../../plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md)` authentication plugins do **not** store passwords in the `[mysql.global_priv](../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-global_priv-table.md)` table. These authentication plugins rely on other methods to authenticate the user.

If you attempt to run `SET PASSWORD` on an account that authenticates with one of these authentication plugins that doesn't store a password in the `[mysql.global_priv](../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-global_priv-table.md)` table, then MariaDB Server will issue an error like the following:

```
SET PASSWORD is ignored for users authenticating via unix_socket plugin
```

See [Authentication from MariaDB 10.4](../../../security/user-account-management/authentication-from-mariadb-10-4.md) for an overview of authentication changes in MariaDB.

## Passwordless User Accounts

User accounts do not always require passwords to login.

The `[unix_socket](../../../plugins/authentication-plugins/authentication-plugin-unix-socket.md)` , `[named_pipe](../../../plugins/authentication-plugins/authentication-plugin-named-pipe.md)` and `[gssapi](../../../plugins/authentication-plugins/authentication-plugin-gssapi.md)` authentication plugins do not require a password to authenticate the user.

The `[pam](../../../plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md)` authentication plugin may or may not require a password to authenticate the user, depending on the specific configuration.

The `[mysql_native_password](../../../plugins/authentication-plugins/authentication-plugin-mysql_native_password.md)` and `[mysql_old_password](../../../plugins/authentication-plugins/authentication-plugin-mysql_old_password.md)` authentication plugins require passwords for authentication, but the password can be blank. In that case, no password is required.

If you provide a password while attempting to log into the server as an account that doesn't require a password, then MariaDB server will simply ignore the password.

A user account can be defined to use multiple authentication plugins in a specific order of preference. This specific scenario may be more noticeable in these versions, since an account could be associated with some authentication plugins that require a password, and some that do not.

## Example

For example, if you had an entry with User and\
Host column values of '`bob`' and\
'`%.loc.gov`', you would write the\
statement like this:

```
SET PASSWORD FOR 'bob'@'%.loc.gov' = PASSWORD('newpass');
```

If you want to delete a password for a user, you would do:

```
SET PASSWORD FOR 'bob'@localhost = PASSWORD("");
```

## See Also

* [Password Validation Plugins](../../plugins/password-validation-plugins/) - permits the setting of basic criteria for passwords
* [ALTER USER](alter-user.md)

GPLv2 fill\_help\_tables.sql
