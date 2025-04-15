
# IS

## Syntax


```
IS boolean_value
```

## Description


Tests a value against a boolean value, where `<code>boolean_value</code>` can be
TRUE, FALSE, or UNKNOWN.


There is an important difference between using IS TRUE or comparing a value with TRUE using `<code>=</code>`. When using `<code>=</code>`, only `<code>1</code>` equals to TRUE. But when using IS TRUE, all values which are logically true (like a number > 1) return TRUE.


## Examples


```
SELECT 1 IS TRUE, 0 IS FALSE, NULL IS UNKNOWN;
+-----------+------------+-----------------+
| 1 IS TRUE | 0 IS FALSE | NULL IS UNKNOWN |
+-----------+------------+-----------------+
|         1 |          1 |               1 |
+-----------+------------+-----------------+
```

Difference between `<code>=</code>` and `<code>IS TRUE</code>`:


```
SELECT 2 = TRUE, 2 IS TRUE;
+----------+-----------+
| 2 = TRUE | 2 IS TRUE |
+----------+-----------+
|        0 |         1 |
+----------+-----------+
```

## See Also


* [Boolean Literals](../../sql-language-structure/sql-language-structure-boolean-literals.md)
* [BOOLEAN Data Type](../../../data-types/data-types-numeric-data-types/boolean.md)
* [Operator Precedence](../operator-precedence.md)

