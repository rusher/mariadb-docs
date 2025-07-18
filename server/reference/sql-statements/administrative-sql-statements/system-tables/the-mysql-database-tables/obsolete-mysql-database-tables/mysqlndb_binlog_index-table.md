# mysql.ndb\_binlog\_index Table

The `mysql.ndb_binlog_index` table is not used by MariaDB. It was kept for MySQL compatibility reasons, and is used there for MySQL Cluster.

For MariaDB clustering, see [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/).

The table contains the following fields:

| Field     | Type                | Null | Key | Default |
| --------- | ------------------- | ---- | --- | ------- |
| Position  | bigint(20) unsigned | NO   |     | NULL    |
| File      | varchar(255)        | NO   |     | NULL    |
| epoch     | bigint(20) unsigned | NO   | PRI | NULL    |
| inserts   | bigint(20) unsigned | NO   |     | NULL    |
| updates   | bigint(20) unsigned | NO   |     | NULL    |
| deletes   | bigint(20) unsigned | NO   |     | NULL    |
| schemaops | bigint(20) unsigned | NO   |     | NULL    |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
