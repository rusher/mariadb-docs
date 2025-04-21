
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


Note that, if the `PIPES_AS_CONCAT` [SQL_MODE](../../../../server-management/variables-and-modes/sql-mode.md) is set, `||` is used as a string concatenation operator. This means that `a || b` is the same as `CONCAT(a,b)`. See `[CONCAT()](../../sql-statements/built-in-functions/string-functions/concat.md)` for details.


### Oracle Mode


In [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/sql_modeoracle#null-handling), `||` ignores [null](null).


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

In [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/sql_modeoracle#null-handling):


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
* [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/sql_modeoracle#null-handling)

