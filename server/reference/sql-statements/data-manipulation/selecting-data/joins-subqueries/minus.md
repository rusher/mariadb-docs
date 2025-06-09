# MINUS

**MariaDB starting with** [**10.6.1**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1061-release-notes)

`MINUS` was introduced as a synonym for [EXCEPT](except.md) from [MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1061-release-notes) when [SQL\_MODE=ORACLE](broken-reference) is set.

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

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
