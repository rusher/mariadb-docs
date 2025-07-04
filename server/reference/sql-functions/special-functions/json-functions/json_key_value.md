# JSON\_KEY\_VALUE

**MariaDB starting with** [**11.2**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112)

JSON\_KEY\_VALUE was added in [MariaDB 11.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112).

## Syntax

```
JSON_KEY_VALUE(obj, json_path)
```

## Description

`JSON_KEY_VALUE` extracts key/value pairs from a JSON object. The JSON path parameter is used to only return key/value pairs for matching JSON objects.

## Example

```
SELECT JSON_KEY_VALUE('[[1, {"key1":"val1", "key2":"val2"}, 3], 2, 3]', '$[0][1]');
+-----------------------------------------------------------------------------+
| JSON_KEY_VALUE('[[1, {"key1":"val1", "key2":"val2"}, 3], 2, 3]', '$[0][1]') |
+-----------------------------------------------------------------------------+
| [{"key": "key1", "value": "val1"}, {"key": "key2", "value": "val2"}]        |
+-----------------------------------------------------------------------------+
```

JSON\_KEY\_VALUE() can be used as an argument to JSON\_TABLE(), which allows adding the key to a result set.

```
SELECT jt.* FROM JSON_TABLE(
JSON_KEY_VALUE('[[1, {"key1":"val1", "key2":"val2"}, 3], 2, 3]', '$[0][1]'),'$[*]'
COLUMNS (
k VARCHAR(20) PATH '$.key',
v VARCHAR(20) PATH '$.value',
id FOR ORDINALITY )) AS jt;
+------+------+------+
| k    | v    | id   |
+------+------+------+
| key1 | val1 |    1 |
| key2 | val2 |    2 |
+------+------+------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
