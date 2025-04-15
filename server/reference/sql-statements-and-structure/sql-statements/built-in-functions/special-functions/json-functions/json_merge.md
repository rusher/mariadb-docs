
# JSON_MERGE

## Syntax


```
JSON_MERGE(json_doc, json_doc[, json_doc] ...)
```

## Description


Merges the given JSON documents.


Returns the merged result,or NULL if any argument is NULL.


An error occurs if any of the arguments are not valid JSON documents.


`<code>JSON_MERGE</code>` has been deprecated since [MariaDB 10.2.25](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10225-release-notes.md), [MariaDB 10.3.16](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10316-release-notes.md) and [MariaDB 10.4.5](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1045-release-notes.md). [JSON_MERGE_PATCH](json_merge_patch.md) is an RFC 7396-compliant replacement, and [JSON_MERGE_PRESERVE](json_merge_preserve.md) is a synonym.


## Example


```
SET @json1 = '[1, 2]';
SET @json2 = '[3, 4]';

SELECT JSON_MERGE(@json1,@json2);
+---------------------------+
| JSON_MERGE(@json1,@json2) |
+---------------------------+
| [1, 2, 3, 4]              |
+---------------------------+
```

## See Also


* [JSON_MERGE_PATCH](json_merge_patch.md)
* [JSON_MERGE_PRESERVE](json_merge_preserve.md)

