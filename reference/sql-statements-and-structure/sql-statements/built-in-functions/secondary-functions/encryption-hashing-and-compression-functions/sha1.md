# SHA1

#

# Syntax

```
SHA1(str), SHA(str)
```

#

# Description

Calculates an SHA-1 160-bit checksum for the string *`str`*, as described in
RFC 3174 (Secure Hash Algorithm).

The value is returned as a string of 40 hex digits, or NULL if the argument was NULL. As of [MariaDB 5.5](/en/what-is-mariadb-55/), the return value is a nonbinary string in the connection [character set and collation](/en/data-types-character-sets-and-collations/), determined by the values of the [character_set_connection](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_connection) and [collation_connection](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) system variables. Before 5.5, the return value was a binary string.

#

# Examples

```
SELECT SHA1('some boring text');
+------------------------------------------+
| SHA1('some boring text') |
+------------------------------------------+
| af969fc2085b1bb6d31e517d5c456def5cdd7093 |
+------------------------------------------+
```