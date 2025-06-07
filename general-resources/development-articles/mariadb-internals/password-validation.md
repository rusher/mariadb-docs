# Password Validation Plugin API

“Password validation” means ensuring that user passwords meet certain minimal security requirements. A dedicated plugin API allows the creation of password validation plugins that will check user passwords as they are set (in [SET PASSWORD](../../community/sql-statements/account-management-sql-statements/set-password.md) and [GRANT](../../community/sql-statements/account-management-sql-statements/grant.md) statements) and either allow or reject them.

## SQL-Level Extensions

MariaDB comes with three password validation plugins — the [simple\_password\_check](../../community/plugins/password-validation-plugins/simple-password-check-plugin.md) plugin, the [cracklib\_password\_check](../../community/plugins/password-validation-plugins/cracklib-password-check-plugin.md) plugin and the [password\_reuse\_check](../../community/plugins/password-validation-plugins/password-reuse-check-plugin.md) plugin. They are not enabled by default; use [INSTALL SONAME](../../community/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) (or [INSTALL PLUGIN](../../community/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md)) statement to install them.

When at least one password plugin is loaded, all new passwords will be validated and password-changing statements will fail if the password will not pass validation checks. Several password validation plugin can be loaded at the same time — in this case a password must pass **all** validation checks by **all** plugins.

### Password-Changing Statements

One can use various SQL statements to change a user password:

#### With Plain Text Password

```
SET PASSWORD = PASSWORD('plain-text password');
SET PASSWORD FOR `user`@`host` = PASSWORD('plain-text password');
SET PASSWORD = OLD_PASSWORD('plain-text password');
SET PASSWORD FOR `user`@`host` = OLD_PASSWORD('plain-text password');
CREATE USER `user`@`host` IDENTIFIED BY 'plain-text password';
GRANT privileges TO `user`@`host` IDENTIFIED BY 'plain-text password';
```

These statements are subject to password validation. If at least one password validation plugin is loaded, plain-text passwords specified in these statements will be validated.

#### With Password Hash

```
SET PASSWORD = 'password hash';
SET PASSWORD FOR `user`@`host` = 'password hash';
CREATE USER `user`@`host` IDENTIFIED BY PASSWORD 'password hash';
CREATE USER `user`@`host` IDENTIFIED VIA mysql_native_password USING 'password hash';
CREATE USER `user`@`host` IDENTIFIED VIA mysql_old_password USING 'password hash';
GRANT privileges TO `user`@`host` IDENTIFIED BY PASSWORD 'password hash';
GRANT privileges TO `user`@`host` IDENTIFIED VIA mysql_native_password USING 'password hash';
GRANT privileges TO `user`@`host` IDENTIFIED VIA mysql_old_password USING 'password hash';
```

These statements can not possibly use password validation — there is nothing to validate, the original plain-text password is not available.\
MariaDB introduces a **strict password validation** mode — controlled by a [strict\_password\_validation](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#strict_password_validation) global server variable.\
If the strict password validation is enabled and at least one password validation plugin is loaded then these “unvalidatable” passwords will be rejected. Otherwise they will be accepted. By default a strict password validation is enabled (but note that it has no effect if no password validation plugin is loaded).

## Examples

Failed password validation:

```
GRANT SELECT ON *.* to foobar IDENTIFIED BY 'raboof';
ERROR HY000: Your password does not satisfy the current policy requirements

SHOW WARNINGS;
+---------+------+----------------------------------------------------------------+
| Level	  | Code | Message                                                        |
+---------+------+----------------------------------------------------------------+
| Warning | 1819 | cracklib: it is based on your username                         |
| Error	  | 1819 | Your password does not satisfy the current policy requirements |
+---------+------+----------------------------------------------------------------+
```

Strict password validation:

```
GRANT SELECT ON *.* TO foo IDENTIFIED BY PASSWORD '2222222222222222';
ERROR HY000: The MariaDB server is running with the --strict-password-validation option so it cannot execute this statement
```

## Plugin API

Password validation plugin API is very simple. A plugin must implement only one method — `validate_password()`. This method takes two arguments — user name and the plain-text password. And it returns 0 when the password has passed the validation and 1 otherwise,

See also `mysql/plugin_password_validation.h` and password validation plugins in `plugin/simple_password_check/` and `plugins/cracklib_password_check/`.

CC BY-SA / Gnu FDL
