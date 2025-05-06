
# User Password Expiry


Password expiry permits administrators to expire user passwords, either manually or automatically.


## System Variables


There are two system variables which affect password expiry: [default_password_lifetime](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#default_password_lifetime), which determines the amount of time between requiring the user to change their password. `0`, the default, means automatic password expiry is not active.


The second variable, [disconnect_on_expired_password](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#disconnect_on_expired_password) determines whether a client is permitted to connect if their password has expired, or whether they are permitted to connect in sandbox mode, able to perform a limited subset of queries related to resetting the password, in particular [SET PASSWORD](../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/set-password.md) and [SET](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set.md).


## Setting a Password Expiry Limit for a User


Besides automatic password expiry, as determined by [default_password_lifetime](../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#default_password_lifetime), password expiry times can be set on an individual user basis, overriding the global using the [CREATE USER](../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user.md) or [ALTER USER](../../reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/alter-user.md) statements, for example:


```
CREATE USER 'monty'@'localhost' PASSWORD EXPIRE INTERVAL 120 DAY;
```

```
ALTER USER 'monty'@'localhost' PASSWORD EXPIRE INTERVAL 120 DAY;
```

Limits can be disabled by use of the `NEVER` keyword, for example:


```
CREATE USER 'monty'@'localhost' PASSWORD EXPIRE NEVER;
```

```
ALTER USER 'monty'@'localhost' PASSWORD EXPIRE NEVER;
```

A manually set limit can be restored the system default by use of `DEFAULT`, for example:


```
CREATE USER 'monty'@'localhost' PASSWORD EXPIRE DEFAULT;
```

```
ALTER USER 'monty'@'localhost' PASSWORD EXPIRE DEFAULT;
```

Note that the limit is defined as the number of days since the last password change. And the last password change is the value of `CURRENT_TIMESTAMP` when the password was changed last. If the `@@secure_timestamp` variable is set to NO (which is its default value) any user can modify the session timestamp arbitrarily, in particular, they can pretend that the password was changed at some point in time far in the future, effectively disabling any password expiration limit.
To prevent it you need to make sure the `@@secure_timestamp` is set or to audit password expiration limits regularly.


## SHOW CREATE USER


The [SHOW CREATE USER](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-create-user.md) statement will display information about the password expiry status of the user. Unlike MySQL, it will not display if the user is unlocked, or if the password expiry is set to default.


```
CREATE USER 'monty'@'localhost' PASSWORD EXPIRE INTERVAL 120 DAY;
CREATE USER 'konstantin'@'localhost' PASSWORD EXPIRE NEVER;
CREATE USER 'amse'@'localhost' PASSWORD EXPIRE DEFAULT;

SHOW CREATE USER 'monty'@'localhost';
+------------------------------------------------------------------+
| CREATE USER for monty@localhost                                  |
+------------------------------------------------------------------+
| CREATE USER 'monty'@'localhost' PASSWORD EXPIRE INTERVAL 120 DAY |
+------------------------------------------------------------------+

SHOW CREATE USER 'konstantin'@'localhost';
+------------------------------------------------------------+
| CREATE USER for konstantin@localhost                       |
+------------------------------------------------------------+
| CREATE USER 'konstantin'@'localhost' PASSWORD EXPIRE NEVER |
+------------------------------------------------------------+

SHOW CREATE USER 'amse'@'localhost';
+--------------------------------+
| CREATE USER for amse@localhost |
+--------------------------------+
| CREATE USER 'amse'@'localhost' |
+--------------------------------+
```

## Checking When Passwords Expire



##### MariaDB starting with [11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115)
From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115), the [Information Schema USERS table](../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-users-table.md) stores password expiry and password error information. An unprivileged user can access their own user data from the table.


The following query can also be used to check when the current passwords expire for all users:


```
WITH password_expiration_info AS (
  SELECT User, Host,
  IF(
   IFNULL(JSON_EXTRACT(Priv, '$.password_lifetime'), -1) = -1,
   @@global.default_password_lifetime,
   JSON_EXTRACT(Priv, '$.password_lifetime')
  ) AS password_lifetime,
  JSON_EXTRACT(Priv, '$.password_last_changed') AS password_last_changed
  FROM mysql.global_priv
)
SELECT pei.User, pei.Host,
  pei.password_lifetime,
  FROM_UNIXTIME(pei.password_last_changed) AS password_last_changed_datetime,
  FROM_UNIXTIME(
   pei.password_last_changed +
   (pei.password_lifetime * 60 * 60 * 24)
  ) AS password_expiration_datetime
  FROM password_expiration_info pei
  WHERE pei.password_lifetime != 0
   AND pei.password_last_changed IS NOT NULL
UNION
SELECT pei.User, pei.Host,
  pei.password_lifetime,
  FROM_UNIXTIME(pei.password_last_changed) AS password_last_changed_datetime,
  0 AS password_expiration_datetime
  FROM password_expiration_info pei
  WHERE pei.password_lifetime = 0
   OR pei.password_last_changed IS NULL;
```

## --connect-expired-password Client Option


The [mariadb client](../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) `--connect-expired-password` option notifies the server that the client is prepared to handle expired password sandbox mode (even if the `--batch` option was specified).


## See Also


* [Account Locking and Password Expiry](https://www.youtube.com/watch?v=AWM_fWZ3XIw) video tutorial


CC BY-SA / Gnu FDL

