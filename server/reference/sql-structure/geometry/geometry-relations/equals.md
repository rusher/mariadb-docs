
# EQUALS

## Syntax


```
Equals(g1,g2)
```

From [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes):


```
MBREQUALS(g1,g2)
```

## Description


Returns `1` or `0` to indicate whether *`g1`* is spatially equal to *`g2`*.


EQUALS() is based on the original MySQL implementation and uses object bounding rectangles, while [ST_EQUALS()](equals.md) uses object shapes.


From [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes), `MBREQUALS` is a synonym for `Equals`.


GPLv2 fill_help_tables.sql

