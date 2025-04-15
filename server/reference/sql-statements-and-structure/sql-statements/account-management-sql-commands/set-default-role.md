
# SET DEFAULT ROLE


## Syntax


```
SET DEFAULT ROLE { role | NONE } [ FOR user@host ]
```

## Description


The `<code>SET DEFAULT ROLE</code>` statement sets a **default [role](../../../../security/user-account-management/roles/roles_overview.md)** for a specified (or current) user. A default role is automatically enabled when a user connects (an implicit [SET ROLE](set-role.md) statement is executed immediately after a connection is established).


To be able to set a role as a default, the role must already have been granted to that user, and one needs the privileges to enable this role (if you cannot do `<code>SET ROLE X</code>`, you won't be able to do `<code>SET DEFAULT ROLE X</code>`). To set a default role for another user one needs to have write access to the `<code>mysql</code>` database.


To remove a user's default role, use `<code>SET DEFAULT ROLE NONE [ FOR user@host ]</code>`. The record of the default role is not removed if the role is [dropped](drop-role.md) or [revoked](revoke.md#roles), so if the role is subsequently re-created or granted, it will again be the user's default role.


The default role is stored in the `<code>default_role</code>` column in the [mysql.user](../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-user-table.md) table/view, as well as in the [Information Schema APPLICABLE_ROLES table](../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-applicable_roles-table.md), so these can be viewed to see which role has been assigned to a user as the default.


## Examples


Setting a default role for the current user:


```
SET DEFAULT ROLE journalist;
```

Removing a default role from the current user:


```
SET DEFAULT ROLE NONE;
```

Setting a default role for another user. The role has to have been granted to the user before it can be set as default:


```
CREATE ROLE journalist;
CREATE USER taniel;

SET DEFAULT ROLE journalist FOR taniel;
ERROR 1959 (OP000): Invalid role specification `journalist`

GRANT journalist TO taniel;
SET DEFAULT ROLE journalist FOR taniel;
```

Viewing mysql.user:


```
select * from mysql.user where user='taniel'\G
*************************** 1. row ***************************
                  Host: %
                  User: taniel
...
               is_role: N
          default_role: journalist
...
```

Removing a default role for another user


```
SET DEFAULT ROLE NONE FOR taniel;
```
