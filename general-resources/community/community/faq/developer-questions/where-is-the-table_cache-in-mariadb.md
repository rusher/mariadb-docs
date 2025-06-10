# Where is the table\_cache in MariaDB?

All versions of MariaDB are based on MySQL 5.1 and greater, thus the `table_cache` option is deprecated in favor of `table_open_cache`. This is also documented at: [mariadbd Options](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options).

For further reading, please refer to the MySQL manual: [How MySQL Opens and Closes Tables](https://dev.mysql.com/doc/refman/5.1/en/table-cache.html).

Examples of use cases:

```sql
MariaDB [(none)]> SHOW GLOBAL STATUS LIKE 'opened_tables';
+---------------+--------+
| Variable_name | Value  |
+---------------+--------+
| Opened_tables | 354858 |
+---------------+--------+
1 row in set (0.00 sec)

MariaDB [(none)]> SELECT @@table_open_cache;
+--------------------+
| @@table_open_cache |
+--------------------+
|                400 |
+--------------------+
1 row in set (0.00 sec)
```

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
