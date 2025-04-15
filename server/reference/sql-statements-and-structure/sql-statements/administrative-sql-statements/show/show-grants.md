
# SHOW GRANTS


## Syntax


```
SHOW GRANTS [FOR user|role]
```

## Description


The `<code>SHOW GRANTS</code>` statement lists privileges granted to a particular user or role.


### Users


The statement lists the [GRANT](../../account-management-sql-commands/grant.md) statement or
statements that must be issued to duplicate the privileges that are granted to
a MariaDB user account. The account is named using the same format as for the
`<code class="fixed" style="white-space:pre-wrap">GRANT</code>` statement; for example,
'`<code class="fixed" style="white-space:pre-wrap">jeffrey'@'localhost</code>`'. If you specify only the user name part
of the account name, a host name part of '`<code class="fixed" style="white-space:pre-wrap">%</code>`' is used. For
additional information about specifying account names, see
[GRANT](../../account-management-sql-commands/grant.md).


```
SHOW GRANTS FOR 'root'@'localhost';
+---------------------------------------------------------------------+
| Grants for root@localhost                                           |
+---------------------------------------------------------------------+
| GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION |
+---------------------------------------------------------------------+
```

To list the privileges granted to the account that you are using to
connect to the server, you can use any of the following statements:


```
SHOW GRANTS;
SHOW GRANTS FOR CURRENT_USER;
SHOW GRANTS FOR CURRENT_USER();
```

If `<code class="highlight fixed" style="white-space:pre-wrap">SHOW GRANTS FOR CURRENT_USER</code>` (or any
of the equivalent syntaxes) is used in `<code class="highlight fixed" style="white-space:pre-wrap">DEFINER</code>` context (such
as within a stored procedure that is defined with 
 `<code class="highlight fixed" style="white-space:pre-wrap">SQL SECURITY DEFINER</code>`), the grants displayed are those of the
definer and not the invoker.


### Roles


`<code>SHOW GRANTS</code>` can also be used to view the privileges granted to a [role](../../../../../security/user-account-management/roles/roles_overview.md).


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



##### MariaDB starting with [10.11](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md)
[GRANT ... TO PUBLIC](../../account-management-sql-commands/grant.md#to-public) was introduced in [MariaDB 10.11](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md) to grant privileges to all users. `<code>SHOW GRANTS FOR PUBLIC</code>` shows all these grants.

```
SHOW GRANTS FOR public;
+------------------------------------------------+
| Grants for PUBLIC                              |
+------------------------------------------------+
| GRANT ALL PRIVILEGES ON `dev_db`.* TO `PUBLIC` |
+------------------------------------------------+
```


## See Also


* [Authentication from MariaDB 10.4](../../../../../security/user-account-management/authentication-from-mariadb-10-4.md)
* [SHOW CREATE USER](show-create-user.md) shows how the user was created.
* [SHOW PRIVILEGES](show-privileges.md) shows the privileges supported by MariaDB.
* [Roles](../../../../../security/user-account-management/roles/roles_overview.md)

