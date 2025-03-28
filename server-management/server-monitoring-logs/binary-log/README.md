# Binary Log

The binary log contains a record of all changes to the databases, both data and structure. It consists of a set of binary log files and an index.

It is necessary for [replication](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql), and can also be used to restore data after a backup.