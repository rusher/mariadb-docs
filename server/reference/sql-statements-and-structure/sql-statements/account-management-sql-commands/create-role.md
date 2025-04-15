
# CREATE ROLE

## Syntax


```
CREATE [OR REPLACE] ROLE [IF NOT EXISTS] role 
  [WITH ADMIN 
    {CURRENT_USER | CURRENT_ROLE | user | role}]
```


## Description


The `<code>CREATE ROLE</code>` statement creates one or more MariaDB [roles](../../../../security/user-account-management/roles/roles_overview.md). To
use it, you must have the global [CREATE USER](grant.md#create-user)
privilege or the [INSERT](grant.md#table-privileges) privilege for the mysql
database. For each account, `<code>CREATE ROLE</code>` creates a new row in the
[mysql.user](../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-user-table.md) table that has no privileges, and with the
corresponding `<code>is_role</code>` field set to `<code>Y</code>`. It also creates a record in the
[mysql.roles_mapping](../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-roles_mapping-table.md) table.


If any of the specified roles already exist, `<code>ERROR 1396 (HY000)</code>` results. If
an error occurs, `<code>CREATE ROLE</code>` will still create the roles that do not result
in an error. The maximum length for a role is 128 characters. Role names can be
quoted, as explained in the [Identifier names](../../sql-language-structure/identifier-names.md) page. Only
one error is produced for all roles which have not been created:


```
ERROR 1396 (HY000): Operation CREATE ROLE failed for 'a','b','c'
```

Failed `<code>CREATE</code>` or `<code>DROP</code>` operations, for both users and roles, produce the
same error code.


`<code>PUBLIC</code>` and `<code>NONE</code>` are reserved, and cannot be used as role names. `<code>NONE</code>` is used to [unset a role](set-role.md) and `<code>PUBLIC</code>` has a special use in other systems, such as Oracle, so is reserved for compatibility purposes.


For valid identifiers to use as role names, see [Identifier Names](../../sql-language-structure/identifier-names.md).


#### WITH ADMIN


The optional `<code>WITH ADMIN</code>` clause determines whether the current user, the
current role or another user or role has use of the newly created role. If the
clause is omitted, `<code>WITH ADMIN CURRENT_USER</code>` is treated as the default, which
means that the current user will be able to [GRANT](grant.md#roles) this role to
users.


#### OR REPLACE


If the optional `<code>OR REPLACE</code>` clause is used, it acts as a shortcut for:


```
DROP ROLE IF EXISTS name;
CREATE ROLE name ...;
```

#### IF NOT EXISTS


When the `<code>IF NOT EXISTS</code>` clause is used, MariaDB will return a warning instead of an error if the specified role already exists. Cannot be used together with the `<code>OR REPLACE</code>` clause.


## Examples


```
CREATE ROLE journalist;

CREATE ROLE developer WITH ADMIN lorinda@localhost;
```

Granting the role to another user. Only user `<code>lorinda@localhost</code>` has permission to grant the `<code>developer</code>` role:


```
SELECT USER();
+-------------------+
| USER()            |
+-------------------+
| henning@localhost |
+-------------------+
...
GRANT developer TO ian@localhost;
Access denied for user 'henning'@'localhost'

 SELECT USER();
+-------------------+
| USER()            |
+-------------------+
| lorinda@localhost |
+-------------------+

GRANT m_role TO ian@localhost;
```

The `<code>OR REPLACE</code>` and `<code>IF NOT EXISTS</code>` clauses. The `<code>journalist</code>` role already exists:


```
CREATE ROLE journalist;
ERROR 1396 (HY000): Operation CREATE ROLE failed for 'journalist'

CREATE OR REPLACE ROLE journalist;
Query OK, 0 rows affected (0.00 sec)

CREATE ROLE IF NOT EXISTS journalist;
Query OK, 0 rows affected, 1 warning (0.00 sec)
```

```
SHOW WARNINGS;
+-------+------+---------------------------------------------------+
| Level | Code | Message                                           |
+-------+------+---------------------------------------------------+
| Note  | 1975 | Can't create role 'journalist'; it already exists |
+-------+------+---------------------------------------------------+
```

## See Also


* [Identifier Names](../../sql-language-structure/identifier-names.md)
* [Roles Overview](../../../../security/user-account-management/roles/roles_overview.md)
* [DROP ROLE](drop-role.md)

