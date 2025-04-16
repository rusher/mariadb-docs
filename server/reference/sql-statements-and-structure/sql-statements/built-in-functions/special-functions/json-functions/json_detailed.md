
# JSON_DETAILED

## Syntax


```
JSON_DETAILED(json_doc[, tab_size])
JSON_PRETTY(json_doc[, tab_size])
```


## Description


Represents JSON in the most understandable way emphasizing nested structures.


`JSON_PRETTY` was added as an alias for `JSON_DETAILED` in [MariaDB 10.10.3](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-10-series/mariadb-10-10-3-release-notes.md), [MariaDB 10.9.5](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-9-series/mariadb-10-9-5-release-notes.md), [MariaDB 10.8.7](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-10-8-7-release-notes.md), [MariaDB 10.7.8](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-7-series/mariadb-10-7-8-release-notes.md), [MariaDB 10.6.12](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-12-release-notes.md), [MariaDB 10.5.19](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10-5-19-release-notes.md) and [MariaDB 10.4.28](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10-4-28-release-notes.md).


## Example


```
SET @j = '{ "A":1,"B":[2,3]}';

SELECT @j;
+--------------------+
| @j                 |
+--------------------+
| { "A":1,"B":[2,3]} |
+--------------------+

SELECT JSON_DETAILED(@j);
+------------------------------------------------------------+
| JSON_DETAILED(@j)                                          |
+------------------------------------------------------------+
| {
    "A": 1,
    "B": 
    [
        2,
        3
    ]
} |
+------------------------------------------------------------+
```

## See Also


* [JSON video tutorial](https://www.youtube.com/watch?v=sLE7jPETp8g) covering JSON_DETAILED.

