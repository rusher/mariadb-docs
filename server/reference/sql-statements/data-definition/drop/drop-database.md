# DROP DATABASE

## Syntax

```
DROP {DATABASE | SCHEMA} [IF EXISTS] db_name
```

## Description

`DROP DATABASE` drops all tables in the database and deletes the database. Be very careful with this statement! To use DROP DATABASE,\
you need the [DROP privilege](../../account-management-sql-statements/grant.md#table-privileges) on the database. `DROP SCHEMA` is a synonym for `DROP DATABASE`.

**Important:** When a database is dropped, user privileges on the database are not automatically dropped. See [GRANT](../../account-management-sql-statements/grant.md).

#### IF EXISTS

Use `IF EXISTS` to prevent an error from occurring for databases that do not exist. A `NOTE` is generated for each non-existent database when using `IF EXISTS`. See [SHOW WARNINGS](../../administrative-sql-statements/show/show-warnings.md).

### Atomic DDL

**MariaDB starting with** [**10.6.1**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1061-release-notes)

[MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1061-release-notes) supports [Atomic DDL](../atomic-ddl.md).`DROP DATABASE` is implemented as

```
loop over all tables
  DROP TABLE table
```

Each individual [DROP TABLE](drop-table.md) is atomic while `DROP DATABASE` as a whole is crash-safe.

## Examples

```
DROP DATABASE bufg;
Query OK, 0 rows affected (0.39 sec)

DROP DATABASE bufg;
ERROR 1008 (HY000): Can't drop database 'bufg'; database doesn't exist

 \W
Show warnings enabled.

DROP DATABASE IF EXISTS bufg;
Query OK, 0 rows affected, 1 warning (0.00 sec)
Note (Code 1008): Can't drop database 'bufg'; database doesn't exist
```

## See Also

* [CREATE DATABASE](../create/create-database.md)
* [ALTER DATABASE](../alter/alter-database.md)
* [SHOW DATABASES](../../administrative-sql-statements/show/show-databases.md)
* [Information Schema SCHEMATA Table](../../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-schemata-table.md)
* [SHOW CREATE DATABASE](../../administrative-sql-statements/show/show-create-database.md)

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
