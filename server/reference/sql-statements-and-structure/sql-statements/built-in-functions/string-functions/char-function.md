# CHAR Function

#

# Syntax

```
CHAR(N,... [USING charset_name])
```

#

# Description

`CHAR()` interprets each argument as an `[INT](../../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/intvar_event.md)` and returns a string consisting of the characters given by the code values of those integers. `NULL` values are skipped. By default, `CHAR()` returns a binary string. To produce a string in a given [character set](/en/data-types-character-sets-and-collations/), use the optional `USING` clause:

```
SELECT CHARSET(CHAR(0x65)), CHARSET(CHAR(0x65 USING utf8));
+---------------------+--------------------------------+
| CHARSET(CHAR(0x65)) | CHARSET(CHAR(0x65 USING utf8)) |
+---------------------+--------------------------------+
| binary | utf8 |
+---------------------+--------------------------------+
```

If `USING` is given and the result string is illegal for the given character set, a warning is issued. Also, if strict [SQL mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/sql_modemssql) is enabled, the result from `CHAR()` becomes `NULL`.

#

# Examples

```
SELECT CHAR(77,97,114,'105',97,'68',66);
+----------------------------------+
| CHAR(77,97,114,'105',97,'68',66) |
+----------------------------------+
| MariaDB |
+----------------------------------+

SELECT CHAR(77,77.3,'77.3');
+----------------------+
| CHAR(77,77.3,'77.3') |
+----------------------+
| MMM |
+----------------------+
1 row in set, 1 warning (0.00 sec)

Warning (Code 1292): Truncated incorrect INTEGER value: '77.3'
```

#

# See Also

* [Character Sets and Collations](/en/data-types-character-sets-and-collations/)
* [ASCII()](ascii.md) - Return ASCII value of first character
* [ORD()](../../data-manipulation/selecting-data/order-by.md) - Return value for character in single or multi-byte character sets
* [CHR](chr.md) - Similar, Oracle-compatible, function