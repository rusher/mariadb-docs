
# JSON_CONTAINS

## Syntax


```
JSON_CONTAINS(json_doc, val[, path])
```

## Description


Returns whether or not the specified value is found in the given JSON document or, optionally, at the specified path within the document. Returns `<code>1</code>` if it does, `<code>0</code>` if not and NULL if any of the arguments are null. An error occurs if the document or path is not valid, or contains the `<code>*</code>` or `<code>**</code>` wildcards.


## Examples


```
SET @json = '{"A": 0, "B": {"C": 1}, "D": 2}';

SELECT JSON_CONTAINS(@json, '2', '$.A');
+----------------------------------+
| JSON_CONTAINS(@json, '2', '$.A') |
+----------------------------------+
|                                0 |
+----------------------------------+

SELECT JSON_CONTAINS(@json, '2', '$.D');
+----------------------------------+
| JSON_CONTAINS(@json, '2', '$.D') |
+----------------------------------+
|                                1 |
+----------------------------------+

SELECT JSON_CONTAINS(@json, '{"C": 1}', '$.A');
+-----------------------------------------+
| JSON_CONTAINS(@json, '{"C": 1}', '$.A') |
+-----------------------------------------+
|                                       0 |
+-----------------------------------------+

SELECT JSON_CONTAINS(@json, '{"C": 1}', '$.B');
+-----------------------------------------+
| JSON_CONTAINS(@json, '{"C": 1}', '$.B') |
+-----------------------------------------+
|                                       1 |
+-----------------------------------------+
```
