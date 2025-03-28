# INT

#

# Syntax

```
INT[(M)] [SIGNED | UNSIGNED | ZEROFILL]
INTEGER[(M)] [SIGNED | UNSIGNED | ZEROFILL]
```

#

# Description

A normal-size integer. When marked UNSIGNED, it ranges from 0 to 4294967295, otherwise its range is -2147483648 to 2147483647 (SIGNED is the default). If a column has been set to ZEROFILL, all values will be prepended by zeros so that the INT value contains a number of M digits. INTEGER is a synonym for INT.

**Note:** If the ZEROFILL attribute has been specified, the column will automatically become UNSIGNED.

`INT4` is a synonym for `INT`.

For details on the attributes, see [Numeric Data Type Overview](numeric-data-type-overview.md).

#

# Examples

```
CREATE TABLE ints (a INT,b INT UNSIGNED,c INT ZEROFILL);
```

With [strict_mode](../../../server-management/variables-and-modes/sql-mode.md#strict-mode) set, the default from [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-102-series/mariadb-1024-release-notes):

```
INSERT INTO ints VALUES (-10,-10,-10);
ERROR 1264 (22003): Out of range value for column 'b' at row 1

INSERT INTO ints VALUES (-10,10,-10);
ERROR 1264 (22003): Out of range value for column 'c' at row 1

INSERT INTO ints VALUES (-10,10,10);

INSERT INTO ints VALUES (2147483648,2147483648,2147483648);
ERROR 1264 (22003): Out of range value for column 'a' at row 1

INSERT INTO ints VALUES (2147483647,2147483648,2147483648);

SELECT * FROM ints;
+------------+------------+------------+
| a | b | c |
+------------+------------+------------+
| -10 | 10 | 0000000010 |
| 2147483647 | 2147483648 | 2147483648 |
+------------+------------+------------+
```

With [strict_mode](../../../server-management/variables-and-modes/sql-mode.md#strict-mode) unset, the default until [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-102-series/mariadb-1023-release-notes):

```
INSERT INTO ints VALUES (-10,-10,-10);
Query OK, 1 row affected, 2 warnings (0.10 sec)
Warning (Code 1264): Out of range value for column 'b' at row 1
Warning (Code 1264): Out of range value for column 'c' at row 1

INSERT INTO ints VALUES (-10,10,-10);
Query OK, 1 row affected, 1 warning (0.08 sec)
Warning (Code 1264): Out of range value for column 'c' at row 1

INSERT INTO ints VALUES (-10,10,10);

INSERT INTO ints VALUES (2147483648,2147483648,2147483648);
Query OK, 1 row affected, 1 warning (0.07 sec)
Warning (Code 1264): Out of range value for column 'a' at row 1

INSERT INTO ints VALUES (2147483647,2147483648,2147483648);

SELECT * FROM ints;
+------------+------------+------------+
| a | b | c |
+------------+------------+------------+
| -10 | 0 | 0000000000 |
| -10 | 10 | 0000000000 |
| -10 | 10 | 0000000010 |
| 2147483647 | 2147483648 | 2147483648 |
| 2147483647 | 2147483648 | 2147483648 |
+------------+------------+------------+
```

#

# See Also

* [Numeric Data Type Overview](numeric-data-type-overview.md)
* [TINYINT](tinyint.md)
* [SMALLINT](smallint.md)
* [MEDIUMINT](mediumint.md)
* [BIGINT](bigint.md)