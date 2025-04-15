
# IS NOT NULL

## Syntax


```
IS NOT NULL
```

## Description


Tests whether a value is not NULL. See also [NULL Values in MariaDB](../../../data-types/null-values.md).


## Examples


```
SELECT 1 IS NOT NULL, 0 IS NOT NULL, NULL IS NOT NULL;
+---------------+---------------+------------------+
| 1 IS NOT NULL | 0 IS NOT NULL | NULL IS NOT NULL |
+---------------+---------------+------------------+
|             1 |             1 |                0 |
+---------------+---------------+------------------+
```

## See also


* [NULL values](../../../data-types/null-values.md)
* [IS NULL operator](is-null.md)
* [COALESCE function](coalesce.md)
* [IFNULL function](../../sql-statements/built-in-functions/control-flow-functions/ifnull.md)
* [NULLIF function](../../sql-statements/built-in-functions/control-flow-functions/nullif.md)
* [CONNECT data types](../../../storage-engines/connect/connect-data-types.md#null-handling)

