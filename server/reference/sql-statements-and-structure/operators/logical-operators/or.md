
# ||

## Syntax


```
OR, ||
```


## Description


Logical OR. When both operands are non-NULL, the result is 1 if any
operand is non-zero, and 0 otherwise. With a NULL operand, the result
is 1 if the other operand is non-zero, and NULL otherwise. If both
operands are NULL, the result is NULL.


For this operator, [short-circuit evaluation](../operator-precedence.md#short-circuit-evaluation) can be used.


Note that, if the `<code>PIPES_AS_CONCAT</code>` [SQL_MODE](../../../../server-management/variables-and-modes/sql-mode.md) is set, `<code>||</code>` is used as a string concatenation operator. This means that `<code>a || b</code>` is the same as `<code>CONCAT(a,b)</code>`. See `<code>[CONCAT()](../../sql-statements/built-in-functions/string-functions/concat_ws.md)</code>` for details.


### Oracle Mode


In [Oracle mode](../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md#null-handling), `<code>||</code>` ignores [nullif.md](../../sql-statements/built-in-functions/control-flow-functions/nullif.md).


## Examples


```
SELECT 1 || 1;
+--------+
| 1 || 1 |
+--------+
|      1 |
+--------+

SELECT 1 || 0;
+--------+
| 1 || 0 |
+--------+
|      1 |
+--------+

SELECT 0 || 0;
+--------+
| 0 || 0 |
+--------+
|      0 |
+--------+

SELECT 0 || NULL;
+-----------+
| 0 || NULL |
+-----------+
|      NULL |
+-----------+

SELECT 1 || NULL;
+-----------+
| 1 || NULL |
+-----------+
|         1 |
+-----------+
```

In [Oracle mode](../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md#null-handling):


```
SELECT 0 || NULL;
+-----------+
| 0 || NULL |
+-----------+
| 0         |
+-----------+
```

## See Also


## See Also


* [Operator Precedence](../operator-precedence.md)
* [Oracle mode](../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md#null-handling)

