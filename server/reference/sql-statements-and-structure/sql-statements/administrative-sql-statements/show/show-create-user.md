
# SHOW CREATE USER

## Syntax


```
SHOW CREATE USER [user]
```

## Description


Shows the [CREATE USER](../../account-management-sql-commands/create-user.md) statement that creates the given user. The statement requires the [SELECT](../../account-management-sql-commands/grant.md#table-privileges) privilege for the [mysql](../system-tables/the-mysql-database-tables/README.md) database, except for the current user. The [CREATE USER](../../account-management-sql-commands/create-user.md) statement for the current user is shown where no user is specified.


`<code>SHOW CREATE USER</code>` quotes identifiers according to the value of the [sql_quote_show_create](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) system variable.


## Examples


```
CREATE USER foo4@test require cipher 'text' 
  issuer 'foo_issuer' subject 'foo_subject';

SHOW CREATE USER foo4@test\G
*************************** 1. row ***************************
CREATE USER 'foo4'@'test' 
  REQUIRE ISSUER 'foo_issuer' 
  SUBJECT 'foo_subject' 
  CIPHER 'text'
```

[User Password Expiry](../../../../../security/user-account-management/user-password-expiry.md):


```
CREATE USER 'monty'@'localhost' PASSWORD EXPIRE INTERVAL 120 DAY;

SHOW CREATE USER 'monty'@'localhost';
+------------------------------------------------------------------+
| CREATE USER for monty@localhost                                  |
+------------------------------------------------------------------+
| CREATE USER 'monty'@'localhost' PASSWORD EXPIRE INTERVAL 120 DAY |
+------------------------------------------------------------------+
```

## See Also


* [CREATE USER](../../account-management-sql-commands/create-user.md)
* [ALTER USER](../../account-management-sql-commands/alter-user.md)
* [SHOW GRANTS](show-grants.md) shows the `<code>GRANTS/PRIVILEGES</code>` for a user.
* [SHOW PRIVILEGES](show-privileges.md) shows the privileges supported by MariaDB.

