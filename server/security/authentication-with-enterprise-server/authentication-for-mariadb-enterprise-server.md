# Authentication for MariaDB Enterprise Server

## Overview

[MariaDB Enterprise Server](https://mariadb.com/kb/en/mariadb-enterprise-server/) authentication is performed by database user accounts. Database user accounts are specified by user name, the hostname from which the account is connecting, and the authentication plugins configured for the account, such as mysql\_native\_password, pam, or unix\_socket.

## Change Password

The password for a [database user account](https://mariadb.com/kb/en/database_user_account) can be changed using the [ALTER TABLE](../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md), [ALTER USER](../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/alter-user.md), and [SET PASSWORD](../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/set-password.md) statements.

```
With ALTER USER:

ALTER USER 'USER'@'192.0.2.%'
   IDENTIFIED BY 'PASSWD';
```

```
With SET PASSWORD:

SET PASSWORD FOR 'USER'@'192.0.2.%'
   = PASSWORD('PASSWD');
```

## Password Validation Plugins

If your MariaDB Enterprise Server node has a password validation plugin installed, then the password should also meet the configured requirements. When you try to set or change a user's password and the password validation plugin rejects the password, the following error message will be shown:

```
ERROR HY000: Your password does not satisfy the current policy requirements.
```

By default, the MariaDB Enterprise Server installs the [simple\_password\_check](../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md) plugin, but the [cracklib\_password\_check](../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md) plugin is also available.

For [simple\_password\_check](../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md), the password requirements are configured by several system variables:

* [simple\_password\_check\_digits](../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md#simple_password_check_digits)
* [imple\_password\_check\_letters\_same\_case](../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md#simple_password_check_letters_same_cases)
* [simple\_password\_check\_minimal\_length](../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md#simple_password_check_minimal_length)
* [simple\_password\_check\_other\_characters](../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md#simple_password_check_other_characters)

## Authentication Plugins

MariaDB Enterprise Server uses authentication plugins to support different authentication methods. The default authentication plugin is mysql\_native\_password.

* [Authentication with ed25519](https://mariadb.com/kb/en/authentication-with-ed25519)
* [Authentication with gssapi](authentication-with-gssapi.md)
* [Authentication with mysql\_native\_password](https://mariadb.com/kb/en/authentication-with-mysql_native_password)
* [Authentication with mysql\_old\_password](https://mariadb.com/kb/en/authentication-with-mysql_old_password)
* [Authentication with pam](https://mariadb.com/kb/en/authentication-with-pam)
* [Authentication with unix\_socket](https://mariadb.com/kb/en/authentication-with-unix_socket)
* [Authentication with PARSEC](../../reference/plugins/authentication-plugins/authentication-plugin-parsec.md)

Copyright © 2025 MariaDB
