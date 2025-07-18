# Error 1178: The storage engine for the table doesn't support

| Error Code | SQLSTATE | Error                       | Description                                         |
| ---------- | -------- | --------------------------- | --------------------------------------------------- |
| 1178       | 42000    | ER\_CHECK\_NOT\_IMPLEMENTED | The storage engine for the table doesn't support %s |

## Possible Causes and Solutions

MariaDB [storage engines](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/storage-engines/README.md) differ in many ways, and not all operations are supported by each engine. Perhaps you don't need the intended operation for the engine, or perhaps you need a different storage engine. For example, [sequences](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/sql-structure/sequences/README.md) don't support [analyze table](../../sql-statements/table-statements/analyze-table.md), as it's an unnecessary operation on a sequence table, which only contains one row.

```
CREATE SEQUENCE s START WITH 100 INCREMENT BY 10;

ANALYZE TABLE s;
+--------+---------+----------+----------------------------------------------------------+
| Table  | Op      | Msg_type | Msg_text                                                 |
+--------+---------+----------+----------------------------------------------------------+
| test.s | analyze | note     | The storage engine for the table doesn't support analyze |
+--------+---------+----------+----------------------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
