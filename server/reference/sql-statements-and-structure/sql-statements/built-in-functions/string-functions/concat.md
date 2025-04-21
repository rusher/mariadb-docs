
# CONCAT

## Syntax


```
CONCAT(str1,str2,...)
```


## Description


Returns the string that results from concatenating the arguments. May have one or more arguments. If all arguments are non-binary strings, the result is a non-binary string. If the arguments include any binary strings, the result is a binary string. A numeric argument is converted to its equivalent binary string form; if you want to avoid that, you can use an explicit type cast, as in this example:


```
SELECT CONCAT(CAST(int_col AS CHAR), char_col);
```

`CONCAT()` returns `NULL` if any argument is `NULL`.


A `NULL` parameter hides all information contained in other parameters from the result. Sometimes this is not desirable; to avoid this, you can:


* Use the `[CONCAT_WS()](concat_ws.md)` function with an empty separator, because that function is `NULL`-safe.
* Use `[IFNULL()](../control-flow-functions/ifnull.md)` to turn NULLs into empty strings.


### Oracle Mode


In [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/sql_modeoracle), `CONCAT` ignores [null](null).


## Examples


```
SELECT CONCAT('Ma', 'ria', 'DB');
+---------------------------+
| CONCAT('Ma', 'ria', 'DB') |
+---------------------------+
| MariaDB                   |
+---------------------------+

SELECT CONCAT('Ma', 'ria', NULL, 'DB');
+---------------------------------+
| CONCAT('Ma', 'ria', NULL, 'DB') |
+---------------------------------+
| NULL                            |
+---------------------------------+

SELECT CONCAT(42.0);
+--------------+
| CONCAT(42.0) |
+--------------+
| 42.0         |
+--------------+
```

Using `IFNULL()` to handle NULLs:


```
SELECT CONCAT('The value of @v is: ', IFNULL(@v, ''));
+------------------------------------------------+
| CONCAT('The value of @v is: ', IFNULL(@v, '')) |
+------------------------------------------------+
| The value of @v is:                            |
+------------------------------------------------+
```

In [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/sql_modeoracle), from [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103):


```
SELECT CONCAT('Ma', 'ria', NULL, 'DB');
+---------------------------------+
| CONCAT('Ma', 'ria', NULL, 'DB') |
+---------------------------------+
| MariaDB                         |
+---------------------------------+
```

## See Also


* [GROUP_CONCAT()](../aggregate-functions/group_concat.md)
* [Oracle mode from MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/sql_modeoracle)

