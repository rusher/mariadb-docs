# MINUS

{% hint style="info" %}
`MINUS` is available starting from [**10.6.1**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1061-release-notes)**.**
{% endhint %}

`MINUS` is a synonym for [EXCEPT](except.md) when [SQL\_MODE=ORACLE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/sql_modeoracle) is set.

```sql
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

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
