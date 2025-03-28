# CURRENT_USER

#

# Syntax

```
CURRENT_USER, CURRENT_USER()
```

#

# Description

Returns the user name and host name combination for the MariaDB account
that the server used to authenticate the current client. This account
determines your access privileges. The return value is a string in the
utf8 [character set](/kb/en/data-types-character-sets-and-collations/).

The value of `CURRENT_USER()` can differ from the value of [USER()](../../../../../../security/user-account-management/user-password-expiry.md). [CURRENT_ROLE()](current_role.md) returns the current active role.

Statements using the `CURRENT_USER` function are not [safe for statement-based replication](/kb/en/unsafe-statements-for-replication/).

#

# Examples

```
shell> mysql --user="anonymous"

select user(),current_user();
+---------------------+----------------+
| user() | current_user() |
+---------------------+----------------+
| anonymous@localhost | @localhost |
+---------------------+----------------+
```

When calling `CURRENT_USER()` in a stored procedure, it returns the owner of the stored procedure, as defined with `DEFINER`.

#

# See Also

* [USER()](../../../../../../security/user-account-management/user-password-expiry.md)
* [SESSION_USER()](session_user.md)
* [CREATE PROCEDURE](../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/create-procedure.md)