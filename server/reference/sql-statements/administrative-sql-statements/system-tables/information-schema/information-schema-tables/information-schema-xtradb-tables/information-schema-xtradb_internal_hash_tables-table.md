# Information Schema XTRADB\_INTERNAL\_HASH\_TABLES Table

**MariaDB starting with** [**10.0.9**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1009-release-notes)

The `XTRADB_INTERNAL_HASH_TABLES` table was added in [MariaDB 10.0.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1009-release-notes).

The [Information Schema](../../) `XTRADB_INTERNAL_HASH_TABLES` table contains InnoDB/XtraDB hash table memory usage information.

The `PROCESS` [privilege](../../../../../account-management-sql-statements/grant.md) is required to view the table.

It has the following columns:

| Column                      | Description     |
| --------------------------- | --------------- |
| Column                      | Description     |
| INTERNAL\_HASH\_TABLE\_NAME | Hash table name |
| TOTAL\_MEMORY               | Total memory    |
| CONSTANT\_MEMORY            | Constant memory |
| VARIABLE\_MEMORY            | Variable memory |

## Example

```
SELECT * FROM information_schema.XTRADB_INTERNAL_HASH_TABLES;
+--------------------------------+--------------+-----------------+-----------------+
| INTERNAL_HASH_TABLE_NAME       | TOTAL_MEMORY | CONSTANT_MEMORY | VARIABLE_MEMORY |
+--------------------------------+--------------+-----------------+-----------------+
| Adaptive hash index            |      2217568 |         2213368 |            4200 |
| Page hash (buffer pool 0 only) |       139112 |          139112 |               0 |
| Dictionary Cache               |       613423 |          554768 |           58655 |
| File system                    |       816368 |          812272 |            4096 |
| Lock System                    |       332872 |          332872 |               0 |
| Recovery System                |            0 |               0 |               0 |
+--------------------------------+--------------+-----------------+-----------------+
```

CC BY-SA / Gnu FDL
