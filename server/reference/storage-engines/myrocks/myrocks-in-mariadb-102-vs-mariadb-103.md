# MyRocks in MariaDB 10.2 vs MariaDB 10.3

MyRocks storage engine itself is identical in [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) and [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103).

[MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103) has a feature that should be interesting for MyRocks users. It is the [gtid\_pos\_auto\_engines](../../../ha-and-performance/standard-replication/gtid.md#gtid_pos_auto_engines) option ([MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179)). This is a performance feature for replication slaves that use multiple transactional storage engines.

For further information, see [mysql.gtid\_slave\_pos table](../../sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md).

CC BY-SA / Gnu FDL
