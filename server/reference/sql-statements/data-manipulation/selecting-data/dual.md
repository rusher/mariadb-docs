
# DUAL

## Description


You are allowed to specify `DUAL` as a dummy table name in
situations where no tables are referenced, such as the following [SELECT](select.md) statement:


```
SELECT 1 + 1 FROM DUAL;
+-------+
| 1 + 1 |
+-------+
|     2 |
+-------+
```

`DUAL` is purely for the convenience of people who require
 that all `SELECT` statements should have
 `FROM` and possibly other clauses. MariaDB ignores the
 clauses. MariaDB does not require `FROM DUAL` if no tables
 are referenced.


FROM DUAL could be used when you only SELECT computed values, but require a WHERE clause, perhaps to test that a script correctly handles empty resultsets:


```
SELECT 1 FROM DUAL WHERE FALSE;
Empty set (0.00 sec)
```

## See Also


* [SELECT](select.md)


<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>


{% @marketo/form formId="4316" %}
