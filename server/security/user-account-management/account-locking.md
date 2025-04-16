
# Account Locking


## Description


Account locking is available for all current versions of MariaDB. Account locking permits privileged administrators to lock/unlock user accounts. No new client connections will be permitted if an account is locked (existing connections are not affected).


User accounts can be locked at creation, with the [CREATE USER](../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user.md) statement, or modified after creation with the [ALTER USER](../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/alter-user.md) statement. For example:


```
CREATE USER 'lorin'@'localhost' ACCOUNT LOCK;
```

or


```
ALTER USER 'marijn'@'localhost' ACCOUNT LOCK;
```

The server will return an `ER_ACCOUNT_HAS_BEEN_LOCKED` error when locked users attempt to connect:


```
mariadb -ulorin
  ERROR 4151 (HY000): Access denied, this account is locked
```

The [ALTER USER](../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/alter-user.md) statement is also used to unlock a user:


```
ALTER USER 'lorin'@'localhost' ACCOUNT UNLOCK;
```

The [SHOW CREATE USER](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-user.md) statement will show whether the account is locked:


```
SHOW CREATE USER 'marijn'@'localhost';
+-----------------------------------------------+
| CREATE USER for marijn@localhost              |
+-----------------------------------------------+
| CREATE USER 'marijn'@'localhost' ACCOUNT LOCK |
+-----------------------------------------------+
```

as well as querying the [mysql.global_priv table](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-global_priv-table.md):


```
SELECT CONCAT(user, '@', host, ' => ', JSON_DETAILED(priv)) FROM mysql.global_priv 
  WHERE user='marijn';
+--------------------------------------------------------------------------------------+
| CONCAT(user, '@', host, ' => ', JSON_DETAILED(priv))                                 |
+--------------------------------------------------------------------------------------+
| marijn@localhost => {
    "access": 0,
    "plugin": "mysql_native_password",
    "authentication_string": "",
    "account_locked": true,
    "password_last_changed": 1558017158
} |
+--------------------------------------------------------------------------------------+
```

## See Also


* [Account Locking and Password Expiry](https://www.youtube.com/watch?v=AWM_fWZ3XIw) video tutorial

<span></span>
