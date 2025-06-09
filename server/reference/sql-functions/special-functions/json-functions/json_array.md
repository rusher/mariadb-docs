# JSON\_ARRAY

## Syntax

```
JSON_ARRAY([value[, value2] ...])
```

## Description

Returns a JSON array containing the listed values. The list can be empty.

## Example

```
SELECT Json_Array(56, 3.1416, 'My name is "Foo"', NULL);
+--------------------------------------------------+
| Json_Array(56, 3.1416, 'My name is "Foo"', NULL) |
+--------------------------------------------------+
| [56, 3.1416, "My name is \"Foo\"", null]         |
+--------------------------------------------------+
```

## See also

* [JSON\_MAKE\_ARRAY](../../../storage-engines/connect/connect-table-types/connect-json-table-type.md#json_make_array), the CONNECT storage engine function

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
