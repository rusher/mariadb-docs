
# IS_USED_LOCK

## Syntax


```
IS_USED_LOCK(str)
```


## Description


Checks whether the lock named `str` is in use (that is, locked). If so,
it returns the connection identifier of the client that holds the
lock. Otherwise, it returns `NULL`. `str` is case insensitive.


If the [metadata_lock_info](../../../../../plugins/other-plugins/metadata-lock-info-plugin.md) plugin is installed, the [Information Schema](../../../administrative-sql-statements/system-tables/information-schema/README.md) [metadata_lock_info](../../../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-metadata_lock_info-table.md) table contains information about locks of this kind (as well as [metadata locks](../../../transactions/metadata-locking.md)).


Statements using the `IS_USED_LOCK` function are [not safe for statement-based replication](../../../../../../server-usage/replication-cluster-multi-master/standard-replication/unsafe-statements-for-statement-based-replication.md).


## See Also


* [GET_LOCK](get_lock.md)
* [RELEASE_LOCK](release_lock.md)
* [IS_FREE_LOCK](is_free_lock.md)
* [RELEASE_ALL_LOCKS](release_all_locks.md)


GPLv2 fill_help_tables.sql

