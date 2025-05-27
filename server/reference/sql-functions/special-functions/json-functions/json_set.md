
# JSON_SET

## Syntax


```
JSON_SET(json_doc, path, val[, path, val] ...)
```

## Description


Updates or inserts data into a JSON document, returning the result, or NULL if any of the arguments are NULL or the optional path fails to find an object.


An error will occur if the JSON document is invalid, the path is invalid or if the path contains a * or **wildcard.**


JSON_SET can update or insert data, while [JSON_REPLACE](json_replace.md) can only update, and [JSON_INSERT](json_insert.md) only insert.


## Examples


```
SELECT JSON_SET(Priv, '$.locked', 'true') FROM mysql.global_priv
```


CC BY-SA / Gnu FDL

