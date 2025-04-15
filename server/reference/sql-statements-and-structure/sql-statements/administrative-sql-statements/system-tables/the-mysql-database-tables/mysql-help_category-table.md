# mysql.help_category Table

`mysql.help_category` is one of the four tables used by the [HELP command](../../help-command.md). It is populated when the server is installed by the `fill_help_tables.sql` script. The other help tables are [help_relation](/en/mysqlhelp_relation-table/), [help_topic](/en/mysqlhelp_topic-table/) and [help_keyword](/en/mysqlhelp_keyword-table/).

This table uses the [Aria](../../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/aria-encryption/aria-enabling-encryption.md) storage engine. Prior to [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-104) it used the [MyISAM](../../../../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk-table-information.md) engine.

The `mysql.help_category` table contains the following fields:

| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| help_category_id | smallint(5) unsigned | NO | PRI | NULL | |
| name | char(64) | NO | UNI | NULL | |
| parent_category_id | smallint(5) unsigned | YES | | NULL | |
| url | char(128) | NO | | NULL | |

#

# Example

```
SELECT * FROM help_category;
+------------------+-----------------------------------------------+--------------------+-----+
| help_category_id | name | parent_category_id | url |
+------------------+-----------------------------------------------+--------------------+-----+
| 1 | Geographic | 0 | |
| 2 | Polygon properties | 34 | |
| 3 | WKT | 34 | |
| 4 | Numeric Functions | 38 | |
| 5 | Plugins | 35 | |
| 6 | MBR | 34 | |
| 7 | Control flow functions | 38 | |
| 8 | Transactions | 35 | |
| 9 | Help Metadata | 35 | |
| 10 | Account Management | 35 | |
| 11 | Point properties | 34 | |
| 12 | Encryption Functions | 38 | |
| 13 | LineString properties | 34 | |
| 14 | Miscellaneous Functions | 38 | |
| 15 | Logical operators | 38 | |
| 16 | Functions and Modifiers for Use with GROUP BY | 35 | |
| 17 | Information Functions | 38 | |
| 18 | Comparison operators | 38 | |
| 19 | Bit Functions | 38 | |
| 20 | Table Maintenance | 35 | |
| 21 | User-Defined Functions | 35 | |
| 22 | Data Types | 35 | |
| 23 | Compound Statements | 35 | |
| 24 | Geometry constructors | 34 | |
| 25 | GeometryCollection properties | 1 | |
| 26 | Administration | 35 | |
| 27 | Data Manipulation | 35 | |
| 28 | Utility | 35 | |
| 29 | Language Structure | 35 | |
| 30 | Geometry relations | 34 | |
| 31 | Date and Time Functions | 38 | |
| 32 | WKB | 34 | |
| 33 | Procedures | 35 | |
| 34 | Geographic Features | 35 | |
| 35 | Contents | 0 | |
| 36 | Geometry properties | 34 | |
| 37 | String Functions | 38 | |
| 38 | Functions | 35 | |
| 39 | Data Definition | 35 | |
+------------------+-----------------------------------------------+--------------------+-----+
```