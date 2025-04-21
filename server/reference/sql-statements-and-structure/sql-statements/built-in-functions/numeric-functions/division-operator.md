
# Division Operator (/)

## Syntax


```
/
```


## Description


Division operator. Dividing by zero will return NULL. By default, returns four digits after the decimal. This is determined by the server system variable [div_precision_increment](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#div_precision_increment) which by default is four. It can be set from 0 to 30.


Dividing by zero returns `NULL`. If the `ERROR_ON_DIVISION_BY_ZERO` [SQL_MODE](../../../../../server-management/variables-and-modes/sql-mode.md) is used (the default since [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes)), a division by zero also produces a warning.


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

Changing [div_precision_increment](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#div_precision_increment) for the session from the default of four to six:


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
* [Module operator (%)](../../../operators/arithmetic-operators/modulo-operator.md)
* [Addition Operator (+)](addition-operator.md)
* [Subtraction Operator (-)](../../../operators/arithmetic-operators/subtraction-operator-.md)
* [Multiplication Operator (*)](multiplication-operator.md)
* [truncate()](truncate.md)
* [Operator Precedence](../../../operators/operator-precedence.md)
* [DIV function](div.md)

