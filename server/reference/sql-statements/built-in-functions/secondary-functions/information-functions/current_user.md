# CURRENT\_USER

## Syntax

```
CURRENT_USER, CURRENT_USER()
```

## Description

Returns the user name and host name combination for the MariaDB account\
that the server used to authenticate the current client. This account\
determines your access privileges. The return value is a string in the\
utf8 [character set](../../../../data-types/string-data-types/character-sets/).

The value of `CURRENT_USER()` can differ from the value of [USER()](user.md). [CURRENT\_ROLE()](current_role.md) returns the current active role.

Statements using the `CURRENT_USER` function are not [safe for statement-based replication](../../../../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).

## Examples

```
shell> mysql --user="anonymous"

select user(),current_user();
+---------------------+----------------+
| user()              | current_user() |
+---------------------+----------------+
| anonymous@localhost | @localhost     |
+---------------------+----------------+
```

When calling `CURRENT_USER()` in a stored procedure, it returns the owner of the stored procedure, as defined with `DEFINER`.

## See Also

* [USER()](user.md)
* [SESSION\_USER()](session_user.md)
* [CREATE PROCEDURE](../../../../../server-usage/stored-routines/stored-procedures/create-procedure.md)

GPLv2 fill\_help\_tables.sql
