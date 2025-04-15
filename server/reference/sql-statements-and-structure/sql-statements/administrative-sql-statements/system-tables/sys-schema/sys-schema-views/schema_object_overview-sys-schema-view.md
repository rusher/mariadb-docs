# schema_object_overview Sys Schema View

#

#### MariaDB starting with [10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-106)

The [Sys Schema](../sys-schema-sys_config-table.md) was introduced in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-106)

#

# Description

A count of the number of objects within each schema, sorted by schema and object.

Contains the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| db | Schema name |
| object_type | Object name |
| count | Count of the number of objects |

#

# Example

```
SELECT * FROM sys.schema_object_overview;
+--------------------+---------------+-------+
| db | object_type | count |
+--------------------+---------------+-------+
| information_schema | SYSTEM VIEW | 79 |
| mysql | BASE TABLE | 30 |
| mysql | INDEX (BTREE) | 76 |
| mysql | PROCEDURE | 2 |
| mysql | VIEW | 1 |
| performance_schema | BASE TABLE | 81 |
| sys | BASE TABLE | 1 |
| sys | FUNCTION | 22 |
| sys | INDEX (BTREE) | 1 |
| sys | PROCEDURE | 26 |
| sys | VIEW | 100 |
+--------------------+---------------+-------+
```