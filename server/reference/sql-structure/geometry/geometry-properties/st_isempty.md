# ST\_ISEMPTY

## Syntax

```sql
ST_IsEmpty(g)
IsEmpty(g)
```

## Description

IsEmpty is a function defined by the OpenGIS specification, but is not fully implemented by MariaDB or MySQL.

Since MariaDB and MySQL do not support GIS EMPTY values such as POINT EMPTY, as implemented it simply returns `1` if the geometry value _`g`_ is invalid, `0` if it is valid, and `NULL` if the argument is `NULL`.

`ST_IsEmpty()` and `IsEmpty()` are synonyms.

GPLv2 fill\_help\_tables.sql
