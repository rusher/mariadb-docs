# JSON\_ARRAY\_INTERSECT

**MariaDB starting with** [**11.2.0**](../../../../../kb/en/mariadb-1120-release-notes/)

JSON\_ARRAY\_INTERSECT was added in [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes).

## Syntax

```
JSON_ARRAY_INTERSECT(arr1, arr2)
```

## Description

Finds intersection between two json arrays and returns an array of items found in both array.

## Examples

```
SET @json1= '[1,2,3]';
SET @json2= '[1,2,4]';

SELECT json_array_intersect(@json1, @json2); 
+--------------------------------------+
| json_array_intersect(@json1, @json2) |
+--------------------------------------+
| [1, 2]                               |
+--------------------------------------+
```

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
