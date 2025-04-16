
# JSON_EQUALS


##### MariaDB starting with [10.7.0](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1070-release-notes.md)
JSON_EQUALS was added in [MariaDB 10.7.0](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-1070-release-notes.md)


## Syntax


```
JSON_EQUALS(json1, json2)
```

## Description


Checks if there is equality between two json objects. Returns `1` if it there is, `0` if not, or NULL if any of the arguments are null.


## Examples


```
SELECT JSON_EQUALS('{"a"   :[1, 2, 3],"b":[4]}', '{"b":[4],"a":[1, 2, 3.0]}');
+------------------------------------------------------------------------+
| JSON_EQUALS('{"a"   :[1, 2, 3],"b":[4]}', '{"b":[4],"a":[1, 2, 3.0]}') |
+------------------------------------------------------------------------+
|                                                                      1 |
+------------------------------------------------------------------------+

SELECT JSON_EQUALS('{"a":[1, 2, 3]}', '{"a":[1, 2, 3.01]}');
+------------------------------------------------------+
| JSON_EQUALS('{"a":[1, 2, 3]}', '{"a":[1, 2, 3.01]}') |
+------------------------------------------------------+
|                                                    0 |
+------------------------------------------------------+
```

## See Also


* [JSON_NORMALIZE](json_normalize.md)

