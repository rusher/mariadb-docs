
# Replication as a Backup Solution

[Replication](../../server-usage/replication-cluster-multi-master/README.md) can be used to support the [backup](README.md) strategy.


Replication alone is *not* sufficient for backup. It assists in protecting against hardware failure on the primary server, but does not protect against data loss. An accidental or malicious `DROP DATABASE` or `TRUNCATE TABLE` statement will be replicated onto the replica as well. Care needs to be taken to prevent data getting out of sync between the primary and the replica.


The terms *master* and *slave* have historically been used in replication, and MariaDB has begun the process of adding *primary* and *replica* synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.



Replication is most commonly used to support backups as follows:


* A primary server replicates to a replica
* Backups are then run off the replica without any impact on the primary.


Backups can have a significant effect on a server, and a high-availability primary may not be able to be stopped, locked or simply handle the extra load of a backup. Running the backup from a replica has the advantage of being able to shutdown or lock the replica and perform a backup without any impact on the primary server.


Note that when backing up off a replica server, it is important to ensure that the servers keep the data in sync. See for example [Replication and Foreign Keys](../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-foreign-keys.md) for a situation when identical statements can result in different data on a replica and a primary.


## See Also


* [Replication](../../server-usage/replication-cluster-multi-master/README.md)
* [Replication Compatibility](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/mariadb-vs-mysql-compatibility#replication-compatibility)
* [Backing Up and Restoring](README.md)

