# How do I downgrade from MySQL 5.5 to MariaDB 5.3/5.2/5.1?

This question is outdated. [MariaDB 5.5](/en/what-is-mariadb-55/) is out now, so when moving from MySQL 5.5 you should go directly to [MariaDB 5.5](/en/what-is-mariadb-55/) and not to any earlier version of MariaDB.

As of the current writing, [MariaDB 5.5](/en/what-is-mariadb-55/) based on MySQL 5.5 is not released yet. You may have an environment where you have upgraded to MySQL 5.5 or are currently using MySQL 5.5 but you want to now run [MariaDB 5.3](/en/what-is-mariadb-53/). For this to work, you need to downgrade your installation as [MariaDB 5.3](/en/what-is-mariadb-53/)/5.2/5.1 is based on MySQL 5.1.

The MySQL Reference Manual talks about [downgrading MySQL](http://dev.mysql.com/doc/refman/5.5/en/downgrading.html). Note the change in `mysql.proc.comment`. The table is seen to be corrupt and in need of repair. You might want to run `[mysql_upgrade](../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade.md)` in MariaDB or a user left a comment to perform:

```
ALTER TABLE `mysql`.`proc` MODIFY COLUMN `comment` CHAR(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '';
```