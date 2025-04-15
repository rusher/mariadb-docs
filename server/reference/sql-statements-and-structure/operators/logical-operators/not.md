
# !

## Syntax


```
NOT, !
```


## Description


Logical NOT. Evaluates to 1 if the operand is 0, to 0 if the operand
is non-zero, and NOT NULL returns NULL.


By default, the `<code>!</code>` operator has a [higher precedence](../operator-precedence.md). If the `<code>HIGH_NOT_PRECEDENCE</code>` [SQL_MODE](../../../../server-management/variables-and-modes/sql-mode.md) flag is set, `<code>NOT</code>` and `<code>!</code>` have the same precedence.


## Examples


```
SELECT NOT 10;
+--------+
| NOT 10 |
+--------+
|      0 |
+--------+

SELECT NOT 0;
+-------+
| NOT 0 |
+-------+
|     1 |
+-------+

SELECT NOT NULL;
+----------+
| NOT NULL |
+----------+
|     NULL |
+----------+

SELECT ! (1+1);
+---------+
| ! (1+1) |
+---------+
|       0 |
+---------+

SELECT ! 1+1;
+-------+
| ! 1+1 |
+-------+
|     1 |
+-------+
```

## See Also


* [Operator Precedence](../operator-precedence.md)

