
# Information Schema ENABLED_ROLES Table

The [Information Schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>ENABLED_ROLES</code>` table shows the enabled [roles](../../../../../../../security/user-account-management/roles/roles_overview.md) for the current session.


It contains the following column:



| Column | Description |
| --- | --- |
| Column | Description |
| ROLE_NAME | The enabled role name, or NULL. |



This table lists all roles that are currently enabled, one role per row — the current role, roles granted to the current role, roles granted to these roles and so on. If no role is set, the row contains a `<code>NULL</code>` value.


The roles that the current user can enable are listed in the [APPLICABLE_ROLES](information-schema-applicable_roles-table.md) Information Schema table.


See also [CURRENT_ROLE()](../../../../built-in-functions/secondary-functions/information-functions/current_role.md).


## Examples


```
SELECT * FROM information_schema.ENABLED_ROLES;
+-----------+
| ROLE_NAME |
+-----------+
| NULL      |
+-----------+

SET ROLE staff;

SELECT * FROM information_schema.ENABLED_ROLES;
+-----------+
| ROLE_NAME |
+-----------+
| staff     |
+-----------+
```
