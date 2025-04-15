
# MyRocks in MariaDB 10.2 vs MariaDB 10.3

MyRocks storage engine itself is identical in [MariaDB 10.2](../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md) and [MariaDB 10.3](../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md).


[MariaDB 10.3](../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md) has a feature that should be interesting for MyRocks users. It is the [gtid_pos_auto_engines](../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md#gtid_pos_auto_engines) option ([MDEV-12179](https://jira.mariadb.org/browse/MDEV-12179)). This is a performance feature for replication slaves that use multiple transactional storage engines.


For further information, see [mysql.gtid_slave_pos table](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md).

