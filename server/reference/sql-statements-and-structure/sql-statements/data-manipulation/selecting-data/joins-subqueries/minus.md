
# MINUS


##### MariaDB starting with [10.6.1](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md)
`MINUS` was introduced as a synonym for [EXCEPT](except.md) from [MariaDB 10.6.1](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1061-release-notes.md) when [SQL_MODE=ORACLE](../../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md) is set.


```
CREATE TABLE seqs (i INT);
INSERT INTO seqs VALUES (1),(2),(2),(3),(3),(4),(5),(6);

SET SQL_MODE='ORACLE';

SELECT i FROM seqs WHERE i <= 3 MINUS SELECT i FROM seqs WHERE i>=3;
+------+
| i    |
+------+
|    1 |
|    2 |
+------+
```
