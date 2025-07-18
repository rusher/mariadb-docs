# CURRENT\_ROLE

## Syntax

```sql
CURRENT_ROLE, CURRENT_ROLE()
```

## Description

Returns the current [role](../../../../security/user-account-management/roles/) name. This determines your access privileges. The return value is a string in the\
utf8 [character set](../../../data-types/string-data-types/character-sets/).

If there is no current role, `NULL` is returned.

The output of `SELECT CURRENT_ROLE` is equivalent to the contents of the [ENABLED\_ROLES](../../../system-tables/information-schema/information-schema-tables/information-schema-enabled_roles-table.md) Information Schema table.

[USER()](user.md) returns the combination of user and host used to login. [CURRENT\_USER()](current_user.md) returns the account used to determine current connection's privileges.

Statements using the `CURRENT_ROLE` function are not [safe for statement-based replication](../../../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).

## Examples

```sql
SELECT CURRENT_ROLE;
+--------------+
| CURRENT_ROLE |
+--------------+
| NULL         |
+--------------+

SET ROLE staff;

SELECT CURRENT_ROLE;
+--------------+
| CURRENT_ROLE |
+--------------+
| staff        |
+--------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
