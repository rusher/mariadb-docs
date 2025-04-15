# SET DEFAULT ROLE

#

# Syntax

```
SET DEFAULT ROLE { role | NONE } [ FOR user@host ]
```

#

# Description

The `SET DEFAULT ROLE` statement sets a **default [role](../../../../security/user-account-management/roles/roles_overview.md)** for a specified (or current) user. A default role is automatically enabled when a user connects (an implicit [SET ROLE](set-role.md) statement is executed immediately after a connection is established).

To be able to set a role as a default, the role must already have been granted to that user, and one needs the privileges to enable this role (if you cannot do `SET ROLE X`, you won't be able to do `SET DEFAULT ROLE X`). To set a default role for another user one needs to have write access to the `mysql` database.

To remove a user's default role, use `SET DEFAULT ROLE NONE [ FOR user@host ]`. The record of the default role is not removed if the role is [dropped](drop-role.md) or [revoked](revoke.md#roles), so if the role is subsequently re-created or granted, it will again be the user's default role.

The default role is stored in the `default_role` column in the [mysql.user](/kb/en/mysqluser-table/) table/view, as well as in the [Information Schema APPLICABLE_ROLES table](../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-applicable_roles-table.md), so these can be viewed to see which role has been assigned to a user as the default.

#

# Examples

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