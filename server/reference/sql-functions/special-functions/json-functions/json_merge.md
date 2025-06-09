# JSON\_MERGE

## Syntax

```
JSON_MERGE(json_doc, json_doc[, json_doc] ...)
```

## Description

Merges the given JSON documents.

Returns the merged result,or NULL if any argument is NULL.

An error occurs if any of the arguments are not valid JSON documents.

`JSON_MERGE` has been deprecated since [MariaDB 10.2.25](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10225-release-notes), [MariaDB 10.3.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10316-release-notes) and [MariaDB 10.4.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1045-release-notes). [JSON\_MERGE\_PATCH](json_merge_patch.md) is an RFC 7396-compliant replacement, and [JSON\_MERGE\_PRESERVE](json_merge_preserve.md) is a synonym.

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

* [JSON\_MERGE\_PATCH](json_merge_patch.md)
* [JSON\_MERGE\_PRESERVE](json_merge_preserve.md)

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
