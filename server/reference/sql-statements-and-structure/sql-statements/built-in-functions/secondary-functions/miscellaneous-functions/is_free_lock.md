# IS_FREE_LOCK

#

# Syntax

```
IS_FREE_LOCK(str)
```

#

# Description

Checks whether the lock named `str` is free to use (that is, not locked).
Returns `1` if the lock is free (no one is using the lock),
 `0` if the lock is in use, and `NULL` if an
error occurs (such as an incorrect argument, like an empty string or `NULL`). `str` is case insensitive.

If the [metadata_lock_info](/en/metadata_lock_info/) plugin is installed, the [Information Schema](/en/information_schema/) [metadata_lock_info](../../../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-metadata_lock_info-table.md) table contains information about locks of this kind (as well as [metadata locks](../../../transactions/metadata-locking.md)).

Statements using the `IS_FREE_LOCK` function are [not safe for statement-based replication](../../../../../../server-usage/replication-cluster-multi-master/standard-replication/unsafe-statements-for-statement-based-replication.md).

#

# See Also

* [GET_LOCK](get_lock.md)
* [RELEASE_LOCK](release_lock.md)
* [IS_USED_LOCK](is_used_lock.md)
* [RELEASE_ALL_LOCKS](release_all_locks.md)