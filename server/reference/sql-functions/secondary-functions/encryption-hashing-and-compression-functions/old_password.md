# OLD\_PASSWORD

## Syntax

```
OLD_PASSWORD(str)
```

## Description

`OLD_PASSWORD()` was added to MySQL when the implementation of[PASSWORD()](password.md) was changed to improve security. `OLD_PASSWORD()` returns the\
value of the old (pre-MySQL 4.1) implementation of PASSWORD() as a\
string, and is intended to permit you to reset passwords for any\
pre-4.1 clients that need to connect to a more recent MySQL server version, or any version of MariaDB,\
without locking them out.

As of [MariaDB 5.5](broken-reference), the return value is a nonbinary string in the connection [character set and collation](../../../data-types/string-data-types/character-sets/), determined by the values of the [character\_set\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_connection) and [collation\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) system variables. Before 5.5, the return value was a binary string.

The return value is 16 bytes in length, or NULL if the argument was NULL.

## See Also

* [PASSWORD()](password.md)
* [MySQL manual on password hashing](https://dev.mysql.com/doc/refman/5.1/en/password-hashing.html)

GPLv2 fill\_help\_tables.sql
