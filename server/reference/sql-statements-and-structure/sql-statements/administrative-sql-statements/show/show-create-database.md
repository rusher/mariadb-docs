
# SHOW CREATE DATABASE

## Syntax


```
SHOW CREATE {DATABASE | SCHEMA} db_name
```


## Description


Shows the [CREATE DATABASE](../../data-definition/create/create-database.md) statement that
creates the given database. `<code>SHOW CREATE SCHEMA</code>` is a synonym
for `<code>SHOW CREATE DATABASE</code>`. `<code>SHOW CREATE DATABASE</code>` quotes database names according to the value of the [sql_quote_show_create](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) server system variable.


## Examples


```
SHOW CREATE DATABASE test;
+----------+-----------------------------------------------------------------+
| Database | Create Database                                                 |
+----------+-----------------------------------------------------------------+
| test     | CREATE DATABASE `test` /*!40100 DEFAULT CHARACTER SET latin1 */ |
+----------+-----------------------------------------------------------------+

SHOW CREATE SCHEMA test;
+----------+-----------------------------------------------------------------+
| Database | Create Database                                                 |
+----------+-----------------------------------------------------------------+
| test     | CREATE DATABASE `test` /*!40100 DEFAULT CHARACTER SET latin1 */ |
+----------+-----------------------------------------------------------------+
```

With [sql_quote_show_create](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) off:


```
SHOW CREATE DATABASE test;
+----------+---------------------------------------------------------------+
| Database | Create Database                                               |
+----------+---------------------------------------------------------------+
| test     | CREATE DATABASE test /*!40100 DEFAULT CHARACTER SET latin1 */ |
+----------+---------------------------------------------------------------+
```

With a comment, from [MariaDB 10.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md):


```
SHOW CREATE DATABASE p;
+----------+--------------------------------------------------------------------------------------+
| Database | Create Database                                                                      |
+----------+--------------------------------------------------------------------------------------+
| p        | CREATE DATABASE `p` /*!40100 DEFAULT CHARACTER SET latin1 */ COMMENT 'presentations' |
+----------+--------------------------------------------------------------------------------------+
```

## See Also


* [CREATE DATABASE](../../data-definition/create/create-database.md)
* [ALTER DATABASE](../../data-definition/alter/alter-database.md)
* [Character Sets and Collations](../../../../data-types/string-data-types/character-sets/supported-character-sets-and-collations.md)

