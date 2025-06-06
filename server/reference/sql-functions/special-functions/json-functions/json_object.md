# JSON\_OBJECT

## Syntax

```
JSON_OBJECT([key, value[, key, value] ...])
```

## Description

Returns a JSON object containing the given key/value pairs. The key/value list can be empty.

An error will occur if there are an odd number of arguments, or any key name is NULL.

## Example

```
SELECT JSON_OBJECT("id", 1, "name", "Monty");
+---------------------------------------+
| JSON_OBJECT("id", 1, "name", "Monty") |
+---------------------------------------+
| {"id": 1, "name": "Monty"}            |
+---------------------------------------+
```

## See also

* [JSON\_MAKE\_OBJECT](../../../storage-engines/connect/connect-table-types/connect-json-table-type.md#json_make_object), the CONNECT storage engine function

CC BY-SA / Gnu FDL
