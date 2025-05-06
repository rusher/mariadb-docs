
# JSON_MERGE_PATCH

## Syntax


```
JSON_MERGE_PATCH(json_doc, json_doc[, json_doc] ...)
```

## Description


Merges the given JSON documents, returning the merged result, or NULL if any argument is NULL.


`JSON_MERGE_PATCH` is an RFC 7396-compliant replacement for [JSON_MERGE](json_merge.md), which has been deprecated.


Unlike [JSON_MERGE_PRESERVE](json_merge_preserve.md), members with duplicate keys are not preserved.


## Example


```
SET @json1 = '[1, 2]';
SET @json2 = '[2, 3]';
SELECT JSON_MERGE_PATCH(@json1,@json2),JSON_MERGE_PRESERVE(@json1,@json2);
+---------------------------------+------------------------------------+
| JSON_MERGE_PATCH(@json1,@json2) | JSON_MERGE_PRESERVE(@json1,@json2) |
+---------------------------------+------------------------------------+
| [2, 3]                          | [1, 2, 2, 3]                       |
+---------------------------------+------------------------------------+
```


CC BY-SA / Gnu FDL

