# MyISAM

MyISAM was the default [storage engine](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/storage-engine-index-types.md) from MySQL 3.23 until it was replaced by [InnoDB](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) in MariaDB and MySQL 5.5. It's a light, non-transactional engine with great performance, is easy to copy between systems and has a small data footprint.

You're encouraged to rather use the [Aria](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/aria-encryption/aria-enabling-encryption.md) storage engine for new applications, which has even better performance and the goal of being crash-safe.

Until [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-104), [system tables](/en/system-tables/) used the MyISAM storage engine.