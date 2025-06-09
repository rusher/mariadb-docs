# EQUALS

## Syntax

```sql
Equals(g1,g2)
```

From [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes):

```sql
MBREQUALS(g1,g2)
```

## Description

Returns `1` or `0` to indicate whether _`g1`_ is spatially equal to _`g2`_.

EQUALS() is based on the original MySQL implementation and uses object bounding rectangles, while [ST\_EQUALS()](equals.md) uses object shapes.

From [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes), `MBREQUALS` is a synonym for `Equals`.

GPLv2 fill\_help\_tables.sql

{% @marketo/form formId="4316" %}
