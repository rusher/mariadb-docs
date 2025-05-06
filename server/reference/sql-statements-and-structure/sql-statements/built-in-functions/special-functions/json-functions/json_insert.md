
# JSON_INSERT

## Syntax


```
JSON_INSERT(json_doc, path, val[, path, val] ...)
```


## Description


Inserts data into a JSON document, returning the resulting document or NULL if either of the *json_doc* or *path* arguments are null.


An error will occur if the JSON document is invalid, or if any of the paths are invalid or contain a `*` or `**` wildcard.


JSON_INSERT can only insert data while [JSON_REPLACE](json_replace.md) can only update. [JSON_SET](json_set.md) can update or insert data.


## Examples


```
SET @json = '{ "A": 0, "B": [1, 2]}';

SELECT JSON_INSERT(@json, '$.C', '[3, 4]');
+--------------------------------------+
| JSON_INSERT(@json, '$.C', '[3, 4]')  |
+--------------------------------------+
| { "A": 0, "B": [1, 2], "C":"[3, 4]"} |
+--------------------------------------+
```

## See Also


* [JSON video tutorial](https://www.youtube.com/watch?v=sLE7jPETp8g) covering JSON_INSERT.


CC BY-SA / Gnu FDL

