
# |

## Syntax


```
|
```

## Description


Bitwise OR. Converts the values to binary and compares bits. If either of the corresponding bits has a value of 1, the resulting bit is also 1.


See also [bitwise AND](bitwise_and.md).


## Examples


```
SELECT 2|1;
+-----+
| 2|1 |
+-----+
|   3 |
+-----+

SELECT 29 | 15;
+---------+
| 29 | 15 |
+---------+
|      31 |
+---------+
```

## See Also


* [Operator Precedence](../../../../operators/operator-precedence.md)

