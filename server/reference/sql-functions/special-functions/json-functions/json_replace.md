
# JSON_REPLACE

## Syntax


```
JSON_REPLACE(json_doc, path, val[, path, val] ...)
```


## Description


Replaces existing values in a JSON document, returning the result, or NULL if any of the arguments are NULL.


An error will occur if the JSON document is invalid, the path is invalid or if the path contains a `*` or `**` wildcard.


Paths and values are evaluated from left to right, with the result from the earlier evaluation being used as the value for the next.


JSON_REPLACE can only update data, while [JSON_INSERT](json_insert.md) can only insert. [JSON_SET](json_set.md) can update or insert data.


## Examples


```
SELECT JSON_REPLACE('{ "A": 1, "B": [2, 3]}', '$.B[1]', 4);
+-----------------------------------------------------+
| JSON_REPLACE('{ "A": 1, "B": [2, 3]}', '$.B[1]', 4) |
+-----------------------------------------------------+
| { "A": 1, "B": [2, 4]}                              |
+-----------------------------------------------------+
```

## See Also


* [JSON video tutorial](https://www.youtube.com/watch?v=sLE7jPETp8g) covering JSON_REPLACE.


CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
