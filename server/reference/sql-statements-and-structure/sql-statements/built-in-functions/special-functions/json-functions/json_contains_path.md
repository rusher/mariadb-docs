
# JSON_CONTAINS_PATH

## Syntax


```
JSON_CONTAINS_PATH(json_doc, return_arg, path[, path] ...)
```

## Description


Indicates whether the given JSON document contains data at the specified path or paths. Returns `<code>1</code>` if it does, `<code>0</code>` if not and NULL if any of the arguments are null.


The *return_arg* can be `<code>one</code>` or `<code>all</code>`:


* `<code>one</code>` - Returns `<code>1</code>` if at least one path exists within the JSON document.
* `<code>all</code>` - Returns `<code>1</code>` only if all paths exist within the JSON document.


## Examples


```
SET @json = '{"A": 1, "B": [2], "C": [3, 4]}';

SELECT JSON_CONTAINS_PATH(@json, 'one', '$.A', '$.D');
+------------------------------------------------+
| JSON_CONTAINS_PATH(@json, 'one', '$.A', '$.D') |
+------------------------------------------------+
|                                              1 |
+------------------------------------------------+
1 row in set (0.00 sec)

SELECT JSON_CONTAINS_PATH(@json, 'all', '$.A', '$.D');
+------------------------------------------------+
| JSON_CONTAINS_PATH(@json, 'all', '$.A', '$.D') |
+------------------------------------------------+
|                                              0 |
+------------------------------------------------+
```
