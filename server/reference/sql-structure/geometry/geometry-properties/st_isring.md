
# ST_IsRing

## Syntax


```
ST_IsRing(g)
IsRing(g)
```

## Description


Returns true if a given [LINESTRING](../geometry-constructors/linestring.md) is a ring, that is, both [ST_IsClosed](st_isclosed.md) and [ST_IsSimple](st_issimple.md). A simple curve does not pass through the same point more than once. However, see [MDEV-7510](https://jira.mariadb.org/browse/MDEV-7510).


`St_IsRing()` and `IsRing()` are synonyms.


CC BY-SA / Gnu FDL

