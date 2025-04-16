
# REVOKE


## Privileges


### Syntax


```
REVOKE 
    priv_type [(column_list)]
      [, priv_type [(column_list)]] ...
    ON [object_type] priv_level
    FROM user [, user] ...

REVOKE ALL PRIVILEGES, GRANT OPTION
    FROM user [, user] ...
```

### Description


The `REVOKE` statement enables system administrators to revoke
privileges (or roles - see [section below](#roles)) from MariaDB accounts. Each account is named using the same format
as for the `GRANT` statement; for example,
'`jeffrey'@'localhost`'. If you specify only the user name part
of the account name, a host name part of '`<code>%</code>`' is used. For
details on the levels at which privileges exist, the allowable
`priv_type` and `priv_level` values, and the
syntax for specifying users and passwords, see [GRANT](grant.md).


To use the first `REVOKE` syntax, you must have the
`GRANT OPTION` privilege, and you must have the privileges that
you are revoking.


To revoke all privileges, use the second syntax, which drops all
global, database, table, column, and routine privileges for the named
user or users:


```
REVOKE ALL PRIVILEGES, GRANT OPTION FROM user [, user] ...
```

To use this `REVOKE` syntax, you must have the global
[CREATE USER](create-user.md) privilege or the
[UPDATE](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md) privilege for the mysql database. See
[GRANT](grant.md).


### Examples


```
REVOKE SUPER ON *.* FROM 'alexander'@'localhost';
```

## Roles


### Syntax


```
REVOKE role  [, role ...]
    FROM grantee [, grantee2 ... ]

REVOKE ADMIN OPTION FOR role FROM grantee [, grantee2]
```

### Description


`REVOKE` is also used to remove a [role](../../../../security/user-account-management/roles/roles_overview.md) from a user or another role that it's previously been assigned to. If a role has previously been set as a [default role](set-default-role.md), `REVOKE` does not remove the record of the default role from the [mysql.user](../administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-user-table.md) table. If the role is subsequently granted again, it will again be the user's default. Use [SET DEFAULT ROLE NONE](set-default-role.md) to explicitly remove this.


Before [MariaDB 10.1.13](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10113-release-notes.md), the `REVOKE role` statement was not permitted in [prepared statements](../prepared-statements/README.md).


### Example


```
REVOKE journalist FROM hulda
```
