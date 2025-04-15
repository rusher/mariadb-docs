
# ROUND

## Syntax


```
ROUND(X), ROUND(X,D)
```

## Description


Rounds the argument `<code>X</code>` to `<code>D</code>` decimal places. `<code>D</code>` defaults to `<code>0</code>` if not specified.
`<code>D</code>` can be negative to cause `<code>D</code>` digits left of the decimal point of the
value `<code>X</code>` to become zero.


The rounding algorithm depends on the data type of `<code>X</code>`:


* for floating point types ([FLOAT](../../../../data-types/data-types-numeric-data-types/float.md), [DOUBLE](../../../../data-types/data-types-numeric-data-types/double.md)) the C libraries rounding function is used, so the behavior *may* differ between operating systems
* for fixed point types ([DECIMAL](../../../../data-types/data-types-numeric-data-types/decimal.md), [DEC/NUMBER/FIXED](../../../../data-types/data-types-numeric-data-types/dec-numeric-fixed.md)) the "round half up" rule is used, meaning that e.g. a value ending in exactly .5 is always rounded up.


## Examples


```
SELECT ROUND(-1.23);
+--------------+
| ROUND(-1.23) |
+--------------+
|           -1 |
+--------------+

SELECT ROUND(-1.58);
+--------------+
| ROUND(-1.58) |
+--------------+
|           -2 |
+--------------+

SELECT ROUND(1.58); 
+-------------+
| ROUND(1.58) |
+-------------+
|           2 |
+-------------+

SELECT ROUND(1.298, 1);
+-----------------+
| ROUND(1.298, 1) |
+-----------------+
|             1.3 |
+-----------------+

SELECT ROUND(1.298, 0);
+-----------------+
| ROUND(1.298, 0) |
+-----------------+
|               1 |
+-----------------+

SELECT ROUND(23.298, -1);
+-------------------+
| ROUND(23.298, -1) |
+-------------------+
|                20 |
+-------------------+
```
