# MD5

#

# Syntax

```
MD5(str)
```

#

# Description

Calculates an MD5 128-bit checksum for the string.

The return value is a 32-hex digit string, and as of [MariaDB 5.5](/en/what-is-mariadb-55/), is a nonbinary string in the connection [character set and collation](/en/data-types-character-sets-and-collations/), determined by the values of the [character_set_connection](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_connection) and [collation_connection](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) system variables. Before 5.5, the return value was a binary string.

NULL is returned if the argument was NULL.

#

# Examples

```
SELECT MD5('testing');
+----------------------------------+
| MD5('testing') |
+----------------------------------+
| ae2b1fca515949e5d54fb22b8ed95575 |
+----------------------------------+
```