# MyISAM

MyISAM was the default [storage engine](../) from MySQL 3.23 until it was replaced by [InnoDB](../innodb/) in MariaDB and MySQL 5.5. It's a light, non-transactional engine with great performance, is easy to copy between systems and has a small data footprint.

You're encouraged to rather use the [Aria](../aria/) storage engine for new applications, which has even better performance and the goal of being crash-safe.

Until [MariaDB 10.4](broken-reference), [system tables](../../sql-statements/administrative-sql-statements/system-tables/) used the MyISAM storage engine.
