# MYSQL\_JSON

**MariaDB starting with** [**10.5.7**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-5-series/mariadb-1057-release-notes)

The `TYPE_MYSQL_JSON` plugin was first released in [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-5-series/mariadb-1057-release-notes).

The JSON type in MySQL stores the JSON object in its own native form, while in MariaDB the [JSON type](../../data-types/string-data-types/json.md) is a [LONGTEXT](../../data-types/string-data-types/longtext.md). Opening a table with a JSON type created in MySQL would result in an error:

```
select * from mysql_json_table;
ERROR 4161 (HY000): Unknown data type: 'MYSQL_JSON'
```

The mysql\_json plugin is used to make it easier to upgrade to MariaDB.

## Installing

Installing can be done in a [number of ways](../plugin-overview.md#installing-a-plugin), for example:

```
install soname 'type_mysql_json';
```

See [Making MariaDB understand MySQL JSON](https://mariadb.org/making-mariadb-understand-mysql-json/) for a full description.

CC BY-SA / Gnu FDL
