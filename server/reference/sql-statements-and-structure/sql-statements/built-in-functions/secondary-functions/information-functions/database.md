
# DATABASE

## Syntax


```
DATABASE()
SCHEMA()
```

## Description


Returns the default (current) database name as a string in the utf8 [character set](../../../../../data-types/string-data-types/character-sets/README.md). If there is no default database, DATABASE() returns NULL. Within a [stored routine](../../../../../../server-usage/programming-customizing-mariadb/stored-routines/README.md), the default database is the database that the routine is associated with, which is not necessarily the same as the database that is the default in the calling context.


SCHEMA() is a synonym for DATABASE().


To select a default database, the [USE](../../../../../../../general-resources/learning-and-training/training-and-tutorials/beginner-mariadb-articles/useful-mariadb-queries.md) statement can be run. Another way to set the default database is specifying its name at [mariadb](../../../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) command line client startup.


## Examples


```
SELECT DATABASE();
+------------+
| DATABASE() |
+------------+
| NULL       |
+------------+

USE test;
Database changed

SELECT DATABASE();
+------------+
| DATABASE() |
+------------+
| test       |
+------------+
```
