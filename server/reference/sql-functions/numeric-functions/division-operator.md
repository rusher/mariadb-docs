# Division Operator (/)

## Syntax

```
/
```

## Description

Division operator. Dividing by zero will return NULL. By default, returns four digits after the decimal. This is determined by the server system variable [div\_precision\_increment](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#div_precision_increment) which by default is four. It can be set from 0 to 30.

Dividing by zero returns `NULL`. If the `ERROR_ON_DIVISION_BY_ZERO` [SQL\_MODE](../../../server-management/variables-and-modes/sql-mode.md) is used (the default since [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes)), a division by zero also produces a warning.

## Examples

```
SELECT 4/5;
+--------+
| 4/5    |
+--------+
| 0.8000 |
+--------+

SELECT 300/(2-2);
+-----------+
| 300/(2-2) |
+-----------+
|      NULL |
+-----------+

SELECT 300/7;
+---------+
| 300/7   |
+---------+
| 42.8571 |
+---------+
```

Changing [div\_precision\_increment](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#div_precision_increment) for the session from the default of four to six:

```
SET div_precision_increment = 6;

SELECT 300/7;
+-----------+
| 300/7     |
+-----------+
| 42.857143 |
+-----------+

SELECT 300/7;
+-----------+
| 300/7     |
+-----------+
| 42.857143 |
+-----------+
```

## See Also

* [Type Conversion](../string-functions/type-conversion.md)
* [Module operator (%)](../../sql-structure/operators/arithmetic-operators/modulo-operator.md)
* [Addition Operator (+)](addition-operator.md)
* [Subtraction Operator (-)](../../sql-structure/operators/arithmetic-operators/subtraction-operator.md)
* [Multiplication Operator (\*)](multiplication-operator.md)
* [truncate()](truncate.md)
* [Operator Precedence](../../sql-structure/operators/operator-precedence.md)
* [DIV function](div.md)

GPLv2 fill\_help\_tables.sql

{% @marketo/form formId="4316" %}
