# SHOW GRANTS

## Syntax

```
SHOW GRANTS [FOR user|role]
```

## Description

The `SHOW GRANTS` statement lists privileges granted to a particular user or role.

### Users

The statement lists the [GRANT](../../account-management-sql-commands/grant.md) statement or\
statements that must be issued to duplicate the privileges that are granted to\
a MariaDB user account. The account is named using the same format as for the`GRANT` statement; for example,\
'`jeffrey'@'localhost`'. If you specify only the user name part\
of the account name, a host name part of '`%`' is used. For\
additional information about specifying account names, see[GRANT](../../account-management-sql-commands/grant.md).

```
SHOW GRANTS FOR 'root'@'localhost';
+---------------------------------------------------------------------+
| Grants for root@localhost                                           |
+---------------------------------------------------------------------+
| GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION |
+---------------------------------------------------------------------+
```

To list the privileges granted to the account that you are using to\
connect to the server, you can use any of the following statements:

```
SHOW GRANTS;
SHOW GRANTS FOR CURRENT_USER;
SHOW GRANTS FOR CURRENT_USER();
```

If `SHOW GRANTS FOR CURRENT_USER` (or any\
of the equivalent syntaxes) is used in `DEFINER` context (such\
as within a stored procedure that is defined with`SQL SECURITY DEFINER`), the grants displayed are those of the\
definer and not the invoker.

### Roles

`SHOW GRANTS` can also be used to view the privileges granted to a [role](../../../../security/user-account-management/roles/).

#### Example

```
SHOW GRANTS FOR journalist;
+------------------------------------------+
| Grants for journalist                    |
+------------------------------------------+
| GRANT USAGE ON *.* TO 'journalist'       |
| GRANT DELETE ON `test`.* TO 'journalist' |
+------------------------------------------+
```

### FOR PUBLIC

**MariaDB starting with** [**10.11**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-11-series/what-is-mariadb-1011)

[GRANT ... TO PUBLIC](../../account-management-sql-commands/grant.md#to-public) was introduced in [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-11-series/what-is-mariadb-1011) to grant privileges to all users. `SHOW GRANTS FOR PUBLIC` shows all these grants.

```
SHOW GRANTS FOR public;
+------------------------------------------------+
| Grants for PUBLIC                              |
+------------------------------------------------+
| GRANT ALL PRIVILEGES ON `dev_db`.* TO `PUBLIC` |
+------------------------------------------------+
```

## See Also

* [Authentication from MariaDB 10.4](../../../../security/user-account-management/authentication-from-mariadb-10-4.md)
* [SHOW CREATE USER](show-create-user.md) shows how the user was created.
* [SHOW PRIVILEGES](show-privileges.md) shows the privileges supported by MariaDB.
* [Roles](../../../../security/user-account-management/roles/)

GPLv2 fill\_help\_tables.sql
