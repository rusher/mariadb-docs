
# privileges_by_table_by_level Sys Schema View


##### MariaDB starting with [11.4](../../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md)
This [Sys Schema](sys-schema-views-host_summary_by_statement_latency-and-xhost_summary_by_sta.md) view was introduced in [MariaDB 11.4.0](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-0-release-notes.md).


## Description


Shows granted privileges broken down by table on which they allow access and level on which they were granted.


For example, if a user `x` has `SELECT` privilege granted `ON db.*`, this view will list all tables in the `db` schema with the user `x` having `SELECT` privilege on them. This is different from [INFORMATION_SCHEMA.TABLE_PRIVILEGES](../../information-schema/information-schema-tables/information-schema-table_privileges-table.md), which only lists privileges granted on the table level.



| Column | Description |
| --- | --- |
| Column | Description |
| TABLE_SCHEMA | Database name. |
| TABLE_NAME | Table name. |
| GRANTEE | [Account name](../../../../account-management-sql-commands/create-user.md#account-names) that was [granted](../../../../account-management-sql-commands/grant.md) the privilege. |
| PRIVILEGE | [Privilege](../../../../account-management-sql-commands/grant.md), such as SELECT or DROP. |
| LEVEL | [Privilege level](../../../../account-management-sql-commands/grant.md), such as GLOBAL or SCHEMA. |



## Example


```
SELECT * FROM sys.privileges_by_table_by_level;
+--------------+------------+---------------------------+----------------+--------+
| TABLE_SCHEMA | TABLE_NAME | GRANTEE                   | PRIVILEGE      | LEVEL  |
+--------------+------------+---------------------------+----------------+--------+
...
| test         | t2         | 'root'@'localhost'        | SELECT         | GLOBAL |
| test         | t1         | 'root'@'localhost'        | SELECT         | GLOBAL |
| test         | t3         | 'root'@'localhost'        | SELECT         | GLOBAL |
| test         | t2         | 'root'@'localhost'        | INSERT         | GLOBAL |
| test         | t1         | 'root'@'localhost'        | INSERT         | GLOBAL |
| test         | t3         | 'root'@'localhost'        | INSERT         | GLOBAL |
| test         | t2         | 'root'@'localhost'        | UPDATE         | GLOBAL |
| test         | t1         | 'root'@'localhost'        | UPDATE         | GLOBAL |
| test         | t3         | 'root'@'localhost'        | UPDATE         | GLOBAL |
| test         | t2         | 'root'@'localhost'        | DELETE         | GLOBAL |
| test         | t1         | 'root'@'localhost'        | DELETE         | GLOBAL |
| test         | t3         | 'root'@'localhost'        | DELETE         | GLOBAL |
| test         | t2         | 'root'@'localhost'        | CREATE         | GLOBAL |
| test         | t1         | 'root'@'localhost'        | CREATE         | GLOBAL |
| test         | t3         | 'root'@'localhost'        | CREATE         | GLOBAL |
| test         | t2         | 'root'@'localhost'        | DROP           | GLOBAL |
| test         | t1         | 'root'@'localhost'        | DROP           | GLOBAL |
| test         | t3         | 'root'@'localhost'        | DROP           | GLOBAL |
| test         | t2         | 'root'@'localhost'        | REFERENCES     | GLOBAL |
| test         | t1         | 'root'@'localhost'        | REFERENCES     | GLOBAL |
| test         | t3         | 'root'@'localhost'        | REFERENCES     | GLOBAL |
| test         | t2         | 'root'@'localhost'        | INDEX          | GLOBAL |
| test         | t1         | 'root'@'localhost'        | INDEX          | GLOBAL |
| test         | t3         | 'root'@'localhost'        | INDEX          | GLOBAL |
| test         | t2         | 'root'@'localhost'        | ALTER          | GLOBAL |
| test         | t1         | 'root'@'localhost'        | ALTER          | GLOBAL |
| test         | t3         | 'root'@'localhost'        | ALTER          | GLOBAL |
| test         | t2         | 'root'@'localhost'        | SHOW VIEW      | GLOBAL |
| test         | t1         | 'root'@'localhost'        | SHOW VIEW      | GLOBAL |
| test         | t3         | 'root'@'localhost'        | SHOW VIEW      | GLOBAL |
| test         | t2         | 'root'@'localhost'        | TRIGGER        | GLOBAL |
| test         | t1         | 'root'@'localhost'        | TRIGGER        | GLOBAL |
| test         | t3         | 'root'@'localhost'        | TRIGGER        | GLOBAL |
| test         | t2         | 'root'@'localhost'        | DELETE HISTORY | GLOBAL |
| test         | t1         | 'root'@'localhost'        | DELETE HISTORY | GLOBAL |
| test         | t3         | 'root'@'localhost'        | DELETE HISTORY | GLOBAL |
| test         | t2         | 'PUBLIC'@''               | SELECT         | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | SELECT         | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | SELECT         | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | INSERT         | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | INSERT         | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | INSERT         | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | UPDATE         | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | UPDATE         | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | UPDATE         | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | DELETE         | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | DELETE         | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | DELETE         | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | CREATE         | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | CREATE         | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | CREATE         | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | DROP           | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | DROP           | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | DROP           | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | REFERENCES     | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | REFERENCES     | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | REFERENCES     | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | INDEX          | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | INDEX          | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | INDEX          | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | ALTER          | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | ALTER          | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | ALTER          | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | SHOW VIEW      | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | SHOW VIEW      | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | SHOW VIEW      | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | TRIGGER        | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | TRIGGER        | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | TRIGGER        | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | DELETE HISTORY | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | DELETE HISTORY | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | DELETE HISTORY | SCHEMA |
+--------------+------------+---------------------------+----------------+--------+
```

## See Also


* [GRANT](../../../../account-management-sql-commands/grant.md) (description of the privileges and how to grant them)
* [INFORMATION_SCHEMA.TABLE_PRIVILEGES](../../information-schema/information-schema-tables/information-schema-table_privileges-table.md)
* [MDEV-24486](https://jira.mariadb.org/browse/MDEV-24486)

