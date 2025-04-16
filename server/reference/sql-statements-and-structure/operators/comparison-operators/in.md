
# IN

## Syntax


```
expr IN (value,...)
```

## Description


Returns 1 if *`expr`* is equal to any of the values in the IN list, else
returns 0. If all values are constants, they are evaluated according
to the type of *`expr`* and sorted. The search for the item then is done
using a binary search. This means IN is very quick if the IN value
list consists entirely of constants. Otherwise, type conversion takes
place according to the rules described at [Type Conversion](../../sql-statements/built-in-functions/string-functions/type-conversion.md), but
applied to all the arguments.


If *`expr`* is NULL, IN always returns NULL. If at least one of the values in the list is NULL, and one of the comparisons is true, the result is 1. If at least one of the values in the list is NULL and none of the comparisons is true, the result is NULL.


## Examples


```
SELECT 2 IN (0,3,5,7);
+----------------+
| 2 IN (0,3,5,7) |
+----------------+
|              0 |
+----------------+
```

```
SELECT 'wefwf' IN ('wee','wefwf','weg');
+----------------------------------+
| 'wefwf' IN ('wee','wefwf','weg') |
+----------------------------------+
|                                1 |
+----------------------------------+
```

Type conversion:


```
SELECT 1 IN ('1', '2', '3');
+----------------------+
| 1 IN ('1', '2', '3') |
+----------------------+
|                    1 |
+----------------------+
```

```
SELECT NULL IN (1, 2, 3);
+-------------------+
| NULL IN (1, 2, 3) |
+-------------------+
|              NULL |
+-------------------+

SELECT 1 IN (1, 2, NULL);
+-------------------+
| 1 IN (1, 2, NULL) |
+-------------------+
|                 1 |
+-------------------+

SELECT 5 IN (1, 2, NULL);
+-------------------+
| 5 IN (1, 2, NULL) |
+-------------------+
|              NULL |
+-------------------+
```

## See Also


* [Conversion of Big IN Predicates Into Subqueries](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/subquery-optimizations/conversion-of-big-in-predicates-into-subqueries.md)
* [Operator Precedence](../operator-precedence.md)

