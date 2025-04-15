
# CHR

## Syntax


```
CHR(N)
```

## Description


`<code>CHR()</code>` interprets each argument N as an integer and returns a `<code>[VARCHAR(1)](../../../../data-types/string-data-types/varchar.md)</code>` string consisting of the character given by the code values of the integer. The character set and collation of the string are set according to the values of the `<code>[character_set_database](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_database)</code>` and `<code>[collation_database](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#collation_database)</code>` system variables.


`<code>CHR()</code>` is similar to the `<code>[CHAR()](char-function.md)</code>` function, but only accepts a single argument.


`<code>CHR()</code>` is available in all [sql_modes](../../../../../server-management/variables-and-modes/sql-mode.md).


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


* [Character Sets and Collations](../../../../data-types/string-data-types/character-sets/README.md)
* [ASCII()](ascii.md) - Return ASCII value of first character
* [ORD()](ord.md) - Return value for character in single or multi-byte character sets
* [CHAR()](char-function.md) - Similar function which accepts multiple integers

