
# EQUALS

## Syntax


```
Equals(g1,g2)
```

From [MariaDB 10.2.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md):


```
MBREQUALS(g1,g2)
```

## Description


Returns `<code>1</code>` or `<code>0</code>` to indicate whether *`<code>g1</code>`* is spatially equal to *`<code>g2</code>`*.


EQUALS() is based on the original MySQL implementation and uses object bounding rectangles, while [ST_EQUALS()](equals.md) uses object shapes.


From [MariaDB 10.2.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md), `<code>MBREQUALS</code>` is a synonym for `<code>Equals</code>`.

