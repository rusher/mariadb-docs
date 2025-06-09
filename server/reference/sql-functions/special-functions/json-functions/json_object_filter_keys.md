# JSON\_OBJECT\_FILTER\_KEYS

**MariaDB starting with** [**11.2.0**](https://mariadb.com/kb/en/mariadb-1120-release-notes/)

JSON\_OBJECT\_FILTER\_KEYS was added in [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes).

## Syntax

```
JSON_OBJECT_FILTER_KEYS(obj, array_keys)
```

## Description

`JSON_OBJECT_FILTER_KEYS` returns a JSON object with keys from the object that are also present in the array as string. It is used when one wants to get key-value pair such that the keys are common but the values may not be common.

## Example

```
SET @obj1= '{ "a": 1, "b": 2, "c": 3}';
SET @obj2= '{"b" : 10, "c": 20, "d": 30}';
SELECT JSON_OBJECT_FILTER_KEYS (@obj1, JSON_ARRAY_INTERSECT(JSON_KEYS(@obj1), JSON_KEYS(@obj2)));
+-------------------------------------------------------------------------------------------+
| JSON_OBJECT_FILTER_KEYS (@obj1, JSON_ARRAY_INTERSECT(JSON_KEYS(@obj1), JSON_KEYS(@obj2))) |
+-------------------------------------------------------------------------------------------+
| {"b": 2, "c": 3}                                                                          |
+-------------------------------------------------------------------------------------------+
```

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
