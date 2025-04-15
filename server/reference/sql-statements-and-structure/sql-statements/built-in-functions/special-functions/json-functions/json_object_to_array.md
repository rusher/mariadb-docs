
# JSON_OBJECT_TO_ARRAY


##### MariaDB starting with [11.2.0](/kb/en/mariadb-1120-release-notes/)
JSON_OBJECT_TO_ARRAY was added in [MariaDB 11.2.0](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes.md).


## Syntax


```
JSON_OBJECT_TO_ARRAY(Obj)
```

## Description


It is used to convert all JSON objects found in a JSON document to JSON arrays where each item in the outer array represents a single key-value pair from the object. It is used when we want not just common keys, but also common values. It can be used in conjunction with JSON_ARRAY_INTERSECT().


## Examples


```
SET @obj1= '{ "a": [1, 2, 3], "b": { "key1":"val1", "key2": {"key3":"val3"} }}';

SELECT JSON_OBJECT_TO_ARRAY(@obj1);
+-----------------------------------------------------------------------+
| JSON_OBJECT_TO_ARRAY(@obj1)                                           |
+-----------------------------------------------------------------------+
| [["a", [1, 2, 3]], ["b", {"key1": "val1", "key2": {"key3": "val3"}}]] |
+-----------------------------------------------------------------------+
```
