# TINYINT

#

# Syntax

```
TINYINT[(M)] [SIGNED | UNSIGNED | ZEROFILL]
```

#

# Description

A very small [integer](/kb/en/sql_language-data_types-int/). The signed range is -128 to 127. The unsigned range is 0 to 255. For details on the attributes, see [Numeric Data Type Overview](numeric-data-type-overview.md).

[INT1](int1.md) is a synonym for `TINYINT`. [BOOL and BOOLEAN](boolean.md) are synonyms for `TINYINT(1)`.

#

# Examples

```
CREATE TABLE tinyints (a TINYINT,b TINYINT UNSIGNED,c TINYINT ZEROFILL);
```

With [strict_mode](../../../server-management/variables-and-modes/sql-mode.md#strict-mode) set, the default from [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-102-series/mariadb-1024-release-notes):

```
INSERT INTO tinyints VALUES (-10,-10,-10);
ERROR 1264 (22003): Out of range value for column 'b' at row 1

INSERT INTO tinyints VALUES (-10,10,-10);
ERROR 1264 (22003): Out of range value for column 'c' at row 1

INSERT INTO tinyints VALUES (-10,10,10);

SELECT * FROM tinyints;
+------+------+------+
| a | b | c |
+------+------+------+
| -10 | 10 | 010 |
+------+------+------+

INSERT INTO tinyints VALUES (128,128,128);
ERROR 1264 (22003): Out of range value for column 'a' at row 1

INSERT INTO tinyints VALUES (127,128,128);

SELECT * FROM tinyints;
+------+------+------+
| a | b | c |
+------+------+------+
| -10 | 10 | 010 |
| 127 | 128 | 128 |
+------+------+------+
```

With [strict_mode](../../../server-management/variables-and-modes/sql-mode.md#strict-mode) unset, the default until [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-102-series/mariadb-1023-release-notes):

```
INSERT INTO tinyints VALUES (-10,-10,-10);
Query OK, 1 row affected, 2 warnings (0.08 sec)
Warning (Code 1264): Out of range value for column 'b' at row 1
Warning (Code 1264): Out of range value for column 'c' at row 1

INSERT INTO tinyints VALUES (-10,10,-10);
Query OK, 1 row affected, 1 warning (0.11 sec)
Warning (Code 1264): Out of range value for column 'c' at row 1

INSERT INTO tinyints VALUES (-10,10,10);

SELECT * FROM tinyints;
+------+------+------+
| a | b | c |
+------+------+------+
| -10 | 0 | 000 |
| -10 | 10 | 000 |
| -10 | 10 | 010 |
+------+------+------+

INSERT INTO tinyints VALUES (128,128,128);
Query OK, 1 row affected, 1 warning (0.19 sec)
Warning (Code 1264): Out of range value for column 'a' at row 1

INSERT INTO tinyints VALUES (127,128,128);

SELECT * FROM tinyints;
+------+------+------+
| a | b | c |
+------+------+------+
| -10 | 0 | 000 |
| -10 | 10 | 000 |
| -10 | 10 | 010 |
| 127 | 128 | 128 |
| 127 | 128 | 128 |
+------+------+------+
```

#

# See Also

* [Numeric Data Type Overview](numeric-data-type-overview.md)
* [SMALLINT](smallint.md)
* [MEDIUMINT](mediumint.md)
* [INTEGER](../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/intvar_event.md)
* [BIGINT](bigint.md)
* [BOOLEAN](boolean.md)