
# mysql.global_priv Table

The `mysql.global_priv` table contains information about users that have permission to access the MariaDB server, and their global privileges. It was introduced in [MariaDB 10.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1041-release-notes) to replace the [mysql.user](mysql-user-table.md) table in earlier versions.


Note that the MariaDB privileges occur at many levels. A user may not be granted `create` privilege at the user level, but may still have `create` permission on certain tables or databases, for example. See [privileges](../../../account-management-sql-commands/grant.md) for a more complete view of the MariaDB privilege system.


The `mysql.global_priv` table contains the following fields:



| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| Host | char(60) | NO | PRI |  | Host (together with User makes up the unique identifier for this account). |
| User | char(80) | NO | PRI |  | User (together with Host makes up the unique identifier for this account). |
| Priv | longtext | NO |  |  | Global privileges, granted to the account and other account properties |



From [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes), in order to help the server understand which version a privilege record was written by, the `priv` field contains a new JSON field, `version_id` ([MDEV-21704](https://jira.mariadb.org/browse/MDEV-21704)).


## Examples



```
select * from mysql.global_priv;
+-----------+-------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Host      | User        | Priv                                                                                                                                  |
+-----------+-------------+---------------------------------------------------------------------------------------------------------------------------------------+
| localhost | root        | {"access": 18446744073709551615,"plugin":"mysql_native_password","authentication_string":"*6C387FC3893DBA1E3BA155E74754DA6682D04747"} |
| 127.%     | msandbox    | {"access":1073740799,"plugin":"mysql_native_password","authentication_string":"*6C387FC3893DBA1E3BA155E74754DA6682D04747"}            |
| localhost | msandbox    | {"access":1073740799,"plugin":"mysql_native_password","authentication_string":"*6C387FC3893DBA1E3BA155E74754DA6682D04747"}            |
| localhost | msandbox_rw | {"access":487487,"plugin":"mysql_native_password","authentication_string":"*6C387FC3893DBA1E3BA155E74754DA6682D04747"}                |
| 127.%     | msandbox_rw | {"access":487487,"plugin":"mysql_native_password","authentication_string":"*6C387FC3893DBA1E3BA155E74754DA6682D04747"}                |
| 127.%     | msandbox_ro | {"access":262145,"plugin":"mysql_native_password","authentication_string":"*6C387FC3893DBA1E3BA155E74754DA6682D04747"}                |
| localhost | msandbox_ro | {"access":262145,"plugin":"mysql_native_password","authentication_string":"*6C387FC3893DBA1E3BA155E74754DA6682D04747"}                |
| 127.%     | rsandbox    | {"access":524288,"plugin":"mysql_native_password","authentication_string":"*B07EB15A2E7BD9620DAE47B194D5B9DBA14377AD"}                |
+-----------+-------------+---------------------------------------------------------------------------------------------------------------------------------------+
```


Readable format:


```
SELECT CONCAT(user, '@', host, ' => ', JSON_DETAILED(priv)) FROM mysql.global_priv;

+--------------------------------------------------------------------------------------+
| CONCAT(user, '@', host, ' => ', JSON_DETAILED(priv))                                 |
+--------------------------------------------------------------------------------------+
| root@localhost => {
    "access": 18446744073709551615,
    "plugin": "mysql_native_password",
    "authentication_string": "*6C387FC3893DBA1E3BA155E74754DA6682D04747"
} |
| msandbox@127.% => {
    "access": 1073740799,
    "plugin": "mysql_native_password",
    "authentication_string": "*6C387FC3893DBA1E3BA155E74754DA6682D04747"
}           |
+--------------------------------------------------------------------------------------+
```

A particular user:


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

From [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes):


```
GRANT FILE ON *.* TO user1@localhost;
SELECT Host, User, JSON_DETAILED(Priv) FROM mysql.global_priv WHERE user='user1'\G

*************************** 1. row ***************************
               Host: localhost
               User: user1
JSON_DETAILED(Priv): {
    "access": 512,
    "plugin": "mysql_native_password",
    "authentication_string": "",
    "password_last_changed": 1581070979,
    "version_id": 100502
}
```

## Mapping the `access` Field Values to Grants


The `access` field contains the grants of the user which can be mapped to individual grants with the following table. The most up-to-date information can be found in the `sql/privilege.h` file in the source code.



| Grant | Bit |
| --- | --- |
| Grant | Bit |
| SELECT | (1UL << 0) |
| INSERT | (1UL << 1) |
| UPDATE | (1UL << 2) |
| DELETE | (1UL << 3) |
| CREATE | (1UL << 4) |
| DROP | (1UL << 5) |
| RELOAD | (1UL << 6) |
| SHUTDOWN | (1UL << 7) |
| PROCESS | (1UL << 8) |
| FILE | (1UL << 9) |
| GRANT | (1UL << 10) |
| REFERENCES | (1UL << 11) |
| INDEX | (1UL << 12) |
| ALTER | (1UL << 13) |
| SHOW_DB | (1UL << 14) |
| SUPER | (1UL << 15) |
| CREATE_TMP | (1UL << 16) |
| LOCK_TABLES | (1UL << 17) |
| EXECUTE | (1UL << 18) |
| REPL_SLAVE | (1UL << 19) |
| BINLOG_MONITOR | (1UL << 20) |
| CREATE_VIEW | (1UL << 21) |
| SHOW_VIEW | (1UL << 22) |
| CREATE_PROC | (1UL << 23) |
| ALTER_PROC | (1UL << 24) |
| CREATE_USER | (1UL << 25) |
| EVENT | (1UL << 26) |
| TRIGGER | (1UL << 27) |
| CREATE_TABLESPACE | (1UL << 28) |
| DELETE_HISTORY | (1UL << 29) |
| SET_USER | (1UL << 30) |
| FEDERATED_ADMIN | (1UL << 31) |
| CONNECTION_ADMIN | (1ULL << 32) |
| READ_ONLY_ADMIN | (1ULL << 33) |
| REPL_SLAVE_ADMIN | (1ULL << 34) |
| REPL_MASTER_ADMIN | (1ULL << 35) |
| BINLOG_ADMIN | (1ULL << 36) |
| BINLOG_REPLAY | (1ULL << 37) |
| SLAVE_MONITOR | (1ULL << 38) |
| SHOW_CREATE_ROUTINE | (1ULL << 39) |


