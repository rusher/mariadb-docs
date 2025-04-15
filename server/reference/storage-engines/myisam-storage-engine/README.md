
# MyISAM

MyISAM was the default [storage engine](../../../../general-resources/learning-and-training/video-presentations-and-screencasts/storage-engines-and-plugins-videos.md) from MySQL 3.23 until it was replaced by [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) in MariaDB and MySQL 5.5. It's a light, non-transactional engine with great performance, is easy to copy between systems and has a small data footprint.


You're encouraged to rather use the [Aria](../s3-storage-engine/aria_s3_copy.md) storage engine for new applications, which has even better performance and the goal of being crash-safe.


Until [MariaDB 10.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md), [system tables](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/README.md) used the MyISAM storage engine.

