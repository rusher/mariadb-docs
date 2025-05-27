# CHR

## Syntax

```
CHR(N)
```

## Description

`CHR()` interprets each argument N as an integer and returns a `[VARCHAR(1)](../../../../data-types/string-data-types/varchar.md)` string consisting of the character given by the code values of the integer. The character set and collation of the string are set according to the values of the `[character_set_database](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_database)` and `[collation_database](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#collation_database)` system variables.

`CHR()` is similar to the `[CHAR()](char-function.md)` function, but only accepts a single argument.

`CHR()` is available in all [sql\_modes](../../../../server-management/variables-and-modes/sql-mode.md).

## Examples

```
SELECT CHR(67);
+---------+
| CHR(67) |
+---------+
| C       |
+---------+

SELECT CHR('67');
+-----------+
| CHR('67') |
+-----------+
| C         |
+-----------+

SELECT CHR('C');
+----------+
| CHR('C') |
+----------+
|          |
+----------+
1 row in set, 1 warning (0.000 sec)

SHOW WARNINGS;
+---------+------+----------------------------------------+
| Level   | Code | Message                                |
+---------+------+----------------------------------------+
| Warning | 1292 | Truncated incorrect INTEGER value: 'C' |
+---------+------+----------------------------------------+
```

## See Also

* [Character Sets and Collations](../../../data-types/string-data-types/character-sets/)
* [ASCII()](ascii.md) - Return ASCII value of first character
* [ORD()](ord.md) - Return value for character in single or multi-byte character sets
* [CHAR()](char-function.md) - Similar function which accepts multiple integers

CC BY-SA / Gnu FDL
