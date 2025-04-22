
# MyISAM

MyISAM was the default [storage engine](../README.md) from MySQL 3.23 until it was replaced by [InnoDB](../innodb/README.md) in MariaDB and MySQL 5.5. It's a light, non-transactional engine with great performance, is easy to copy between systems and has a small data footprint.


You're encouraged to rather use the [Aria](../aria/README.md) storage engine for new applications, which has even better performance and the goal of being crash-safe.


Until [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104), [system tables](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/README.md) used the MyISAM storage engine.

