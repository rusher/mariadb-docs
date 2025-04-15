
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


The `<code>SET PASSWORD</code>` statement assigns a password to an existing MariaDB user
account.


If the password is specified using the `<code>[PASSWORD()](../../../plugins/password-validation-plugins/password-reuse-check-plugin.md)</code>` or `<code>[OLD_PASSWORD()](../built-in-functions/secondary-functions/encryption-hashing-and-compression-functions/old_password.md)</code>`
function, the literal text of the password should be given. If the
password is specified without using either function, the password
should be the already-encrypted password value as returned by
`<code>[PASSWORD()](../../../plugins/password-validation-plugins/password-reuse-check-plugin.md)</code>`.


`<code>[OLD_PASSWORD()](../built-in-functions/secondary-functions/encryption-hashing-and-compression-functions/old_password.md)</code>` should only be used if your MariaDB/MySQL clients are very old (< 4.0.0).


With no `<code>FOR</code>` clause, this statement sets the password for the current
user. Any client that has connected to the server using a non-anonymous
account can change the password for that account.


With a `<code>FOR</code>` clause, this statement sets the password for a specific
account on the current server host. Only clients that have the `<code>UPDATE</code>`
privilege for the `<code>mysql</code>` database can do this. The user value should be
given in `<code class="fixed" style="white-space:pre-wrap">user_name@host_name</code>` format, where `<code>user_name</code>` and `<code>host_name</code>` are
exactly as they are listed in the User and Host columns of the
`<code>[mysql.user](../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-user-table.md)</code>` table (or view in current versions) entry.


The argument to `<code>[PASSWORD()](../../../plugins/password-validation-plugins/password-reuse-check-plugin.md)</code>` and the password given to MariaDB clients can be of arbitrary length.


## Authentication Plugin Support


`<code>SET PASSWORD</code>` (with or without `<code>PASSWORD()</code>`) works for accounts authenticated via any [authentication plugin](../../../plugins/authentication-plugins/README.md) that supports passwords stored in the `<code>[mysql.global_priv](../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-global_priv-table.md)</code>` table.


The `<code>[ed25519](../../../plugins/authentication-plugins/authentication-plugin-ed25519.md)</code>`, `<code>[mysql_native_password](../../../plugins/authentication-plugins/authentication-plugin-mysql_native_password.md)</code>`, and `<code>[mysql_old_password](../../../plugins/authentication-plugins/authentication-plugin-mysql_old_password.md)</code>` authentication plugins store passwords in the `<code>[mysql.global_priv](../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-global_priv-table.md)</code>` table.


If you run `<code>SET PASSWORD</code>` on an account that authenticates with one of these authentication plugins that stores passwords in the `<code>[mysql.global_priv](../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-global_priv-table.md)</code>` table, then the `<code>PASSWORD()</code>` function is evaluated by the specific authentication plugin used by the account. The authentication plugin hashes the password with a method that is compatible with that specific authentication plugin.


The `<code>[unix_socket](../../../plugins/authentication-plugins/authentication-plugin-unix-socket.md)</code>`, `<code>[named_pipe](../../../plugins/authentication-plugins/authentication-plugin-named-pipe.md)</code>`, `<code>[gssapi](../../../plugins/authentication-plugins/authentication-plugin-gssapi.md)</code>`, and `<code>[pam](../../../plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md)</code>` authentication plugins do **not** store passwords in the `<code>[mysql.global_priv](../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-global_priv-table.md)</code>` table. These authentication plugins rely on other methods to authenticate the user.


If you attempt to run `<code>SET PASSWORD</code>` on an account that authenticates with one of these authentication plugins that doesn't store a password in the `<code>[mysql.global_priv](../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-global_priv-table.md)</code>` table, then MariaDB Server will issue an error like the following:


```
SET PASSWORD is ignored for users authenticating via unix_socket plugin
```

See [Authentication from MariaDB 10.4](../../../../security/user-account-management/authentication-from-mariadb-10-4.md) for an overview of authentication changes in MariaDB.


## Passwordless User Accounts


User accounts do not always require passwords to login.


The `<code>[unix_socket](../../../plugins/authentication-plugins/authentication-plugin-unix-socket.md)</code>` , `<code>[named_pipe](../../../plugins/authentication-plugins/authentication-plugin-named-pipe.md)</code>` and `<code>[gssapi](../../../plugins/authentication-plugins/authentication-plugin-gssapi.md)</code>` authentication plugins do not require a password to authenticate the user.


The `<code>[pam](../../../plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md)</code>` authentication plugin may or may not require a password to authenticate the user, depending on the specific configuration.


The `<code>[mysql_native_password](../../../plugins/authentication-plugins/authentication-plugin-mysql_native_password.md)</code>` and `<code>[mysql_old_password](../../../plugins/authentication-plugins/authentication-plugin-mysql_old_password.md)</code>` authentication plugins require passwords for authentication, but the password can be blank. In that case, no password is required.


If you provide a password while attempting to log into the server as an account that doesn't require a password, then MariaDB server will simply ignore the password.


A user account can be defined to use multiple authentication plugins in a specific order of preference. This specific scenario may be more noticeable in these versions, since an account could be associated with some authentication plugins that require a password, and some that do not.


## Example


For example, if you had an entry with User and
Host column values of '`<code class="fixed" style="white-space:pre-wrap">bob</code>`' and 
'`<code class="fixed" style="white-space:pre-wrap">%.loc.gov</code>`', you would write the
statement like this:


```
SET PASSWORD FOR 'bob'@'%.loc.gov' = PASSWORD('newpass');
```

If you want to delete a password for a user, you would do:


```
SET PASSWORD FOR 'bob'@localhost = PASSWORD("");
```

## See Also


* [Password Validation Plugins](../../../plugins/password-validation-plugins/README.md) - permits the setting of basic criteria for passwords
* [ALTER USER](alter-user.md)

