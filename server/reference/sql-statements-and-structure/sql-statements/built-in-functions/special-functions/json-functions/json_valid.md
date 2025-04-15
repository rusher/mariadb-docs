
# JSON_VALID

## Syntax


```
JSON_VALID(value)
```


## Description


Indicates whether the given value is a valid JSON document or not. Returns `<code>1</code>` if valid, `<code>0</code>` if not, and NULL if the argument is NULL.


From [MariaDB 10.4.3](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1043-release-notes.md), the JSON_VALID function is automatically used as a [CHECK constraint](../../../data-definition/constraint.md#check-constraints) for the [JSON data type alias](../../../../../storage-engines/connect/json-sample-files.md) in order to ensure that a valid json document is inserted.


## Examples


```
SELECT JSON_VALID('{"id": 1, "name": "Monty"}');
+------------------------------------------+
| JSON_VALID('{"id": 1, "name": "Monty"}') |
+------------------------------------------+
|                                        1 |
+------------------------------------------+

SELECT JSON_VALID('{"id": 1, "name": "Monty", "oddfield"}');
+------------------------------------------------------+
| JSON_VALID('{"id": 1, "name": "Monty", "oddfield"}') |
+------------------------------------------------------+
|                                                    0 |
+------------------------------------------------------+
```

## See Also


* [JSON video tutorial](https://www.youtube.com/watch?v=sLE7jPETp8g) covering JSON_VALID.

