
# SET ROLE

## Syntax


```
SET ROLE { role | NONE }
```


## Description


The `<code>SET ROLE</code>` statement enables a [role](../../../../security/user-account-management/roles/roles_overview.md), along with all of its associated permissions, for the current session. To unset a role, use `<code>NONE</code>` .


If a role that doesn't exist, or to which the user has not been assigned, is specified, an `<code>ERROR 1959 (OP000): Invalid role specification</code>` error occurs.


An automatic SET ROLE is implicitly performed when a user connects if that user has been assigned a default role. See [SET DEFAULT ROLE](set-default-role.md).


## Example


```
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

SET ROLE NONE;

SELECT CURRENT_ROLE();
+----------------+
| CURRENT_ROLE() |
+----------------+
| NULL           |
+----------------+
```
