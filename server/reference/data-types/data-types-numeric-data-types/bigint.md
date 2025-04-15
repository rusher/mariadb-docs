# BIGINT

#

# Syntax

```
BIGINT[(M)] [SIGNED | UNSIGNED | ZEROFILL]
```

#

# Description

A large integer. The signed range is `-9223372036854775808` to
`9223372036854775807`. The unsigned range is `0` to
`18446744073709551615`.

If a column has been set to ZEROFILL, all values will be prepended by zeros so that the BIGINT value contains a number of M digits.

**Note:** If the ZEROFILL attribute has been specified, the column will automatically become UNSIGNED.

For more details on the attributes, see [Numeric Data Type Overview](numeric-data-type-overview.md).

`SERIAL` is an alias for:

```
BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE
```

`INT8` is a synonym for `BIGINT`.

#

# Examples

```
CREATE TABLE bigints (a BIGINT,b BIGINT UNSIGNED,c BIGINT ZEROFILL);
```

With [strict_mode](../../../server-management/variables-and-modes/sql-mode.md#strict-mode) set, the default from [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-102-series/mariadb-1024-release-notes):

```
INSERT INTO bigints VALUES (-10,-10,-10);
ERROR 1264 (22003): Out of range value for column 'b' at row 1

INSERT INTO bigints VALUES (-10,10,-10);
ERROR 1264 (22003): Out of range value for column 'c' at row 1

INSERT INTO bigints VALUES (-10,10,10);

INSERT INTO bigints VALUES (9223372036854775808,9223372036854775808,9223372036854775808);
ERROR 1264 (22003): Out of range value for column 'a' at row 1

INSERT INTO bigints VALUES (9223372036854775807,9223372036854775808,9223372036854775808);

SELECT * FROM bigints;
+---------------------+---------------------+----------------------+
| a | b | c |
+---------------------+---------------------+----------------------+
| -10 | 10 | 00000000000000000010 |
| 9223372036854775807 | 9223372036854775808 | 09223372036854775808 |
+---------------------+---------------------+----------------------+
```

With [strict_mode](../../../server-management/variables-and-modes/sql-mode.md#strict-mode) unset, the default until [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-102-series/mariadb-1023-release-notes):

```
INSERT INTO bigints VALUES (-10,-10,-10);
Query OK, 1 row affected, 2 warnings (0.08 sec)
Warning (Code 1264): Out of range value for column 'b' at row 1
Warning (Code 1264): Out of range value for column 'c' at row 1

INSERT INTO bigints VALUES (-10,10,-10);
Query OK, 1 row affected, 1 warning (0.08 sec)
Warning (Code 1264): Out of range value for column 'c' at row 1

INSERT INTO bigints VALUES (-10,10,10);

INSERT INTO bigints VALUES (9223372036854775808,9223372036854775808,9223372036854775808);
Query OK, 1 row affected, 1 warning (0.07 sec)
Warning (Code 1264): Out of range value for column 'a' at row 1

INSERT INTO bigints VALUES (9223372036854775807,9223372036854775808,9223372036854775808);

SELECT * FROM bigints;
+---------------------+---------------------+----------------------+
| a | b | c |
+---------------------+---------------------+----------------------+
| -10 | 0 | 00000000000000000000 |
| -10 | 10 | 00000000000000000000 |
| -10 | 10 | 00000000000000000010 |
| 9223372036854775807 | 9223372036854775808 | 09223372036854775808 |
| 9223372036854775807 | 9223372036854775808 | 09223372036854775808 |
+---------------------+---------------------+----------------------+
```

#

# See Also

* [Numeric Data Type Overview](numeric-data-type-overview.md)
* [TINYINT](tinyint.md)
* [SMALLINT](smallint.md)
* [MEDIUMINT](mediumint.md)
* [INTEGER](../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/intvar_event.md)