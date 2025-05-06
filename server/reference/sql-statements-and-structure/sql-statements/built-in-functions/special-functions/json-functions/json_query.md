
# JSON_QUERY

## Syntax


```
JSON_QUERY(json_doc, path)
```

## Description


Given a JSON document, returns an object or array specified by the path. Returns NULL if not given a valid JSON document, or if there is no match.


## Examples


```
select json_query('{"key1":{"a":1, "b":[1,2]}}', '$.key1');
+-----------------------------------------------------+
| json_query('{"key1":{"a":1, "b":[1,2]}}', '$.key1') |
+-----------------------------------------------------+
| {"a":1, "b":[1,2]}                                  |
+-----------------------------------------------------+

select json_query('{"key1":123, "key1": [1,2,3]}', '$.key1');
+-------------------------------------------------------+
| json_query('{"key1":123, "key1": [1,2,3]}', '$.key1') |
+-------------------------------------------------------+
| [1,2,3]                                               |
+-------------------------------------------------------+
```


CC BY-SA / Gnu FDL

