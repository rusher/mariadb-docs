# JSON\_VALID

## Syntax

```
JSON_VALID(value)
```

## Description

Indicates whether the given value is a valid JSON document or not. Returns `1` if valid, `0` if not, and NULL if the argument is NULL.

From [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes), the JSON\_VALID function is automatically used as a [CHECK constraint](../../../sql-statements/data-definition/constraint.md#check-constraints) for the [JSON data type alias](../../../data-types/string-data-types/json.md) in order to ensure that a valid json document is inserted.

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

* [JSON video tutorial](https://www.youtube.com/watch?v=sLE7jPETp8g) covering JSON\_VALID.

CC BY-SA / Gnu FDL
