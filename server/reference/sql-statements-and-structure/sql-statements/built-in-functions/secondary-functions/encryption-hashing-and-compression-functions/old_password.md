
# OLD_PASSWORD

## Syntax


```
OLD_PASSWORD(str)
```


## Description


`OLD_PASSWORD()` was added to MySQL when the implementation of 
[PASSWORD()](../../../../../plugins/password-validation-plugins/password-reuse-check-plugin.md) was changed to improve security. `OLD_PASSWORD()` returns the
value of the old (pre-MySQL 4.1) implementation of PASSWORD() as a
string, and is intended to permit you to reset passwords for any
pre-4.1 clients that need to connect to a more recent MySQL server version, or any version of MariaDB,
without locking them out.


As of [MariaDB 5.5](../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md), the return value is a nonbinary string in the connection [character set and collation](../../../../../data-types/string-data-types/character-sets/README.md), determined by the values of the [character_set_connection](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_connection) and [collation_connection](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) system variables. Before 5.5, the return value was a binary string.


The return value is 16 bytes in length, or NULL if the argument was NULL.


## See Also


* [PASSWORD()](../../../../../plugins/password-validation-plugins/password-reuse-check-plugin.md)
* [MySQL manual on password hashing](https://dev.mysql.com/doc/refman/5.1/en/password-hashing.html)

