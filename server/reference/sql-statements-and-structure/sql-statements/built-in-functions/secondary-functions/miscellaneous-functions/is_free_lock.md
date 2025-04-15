
# IS_FREE_LOCK

## Syntax


```
IS_FREE_LOCK(str)
```


## Description


Checks whether the lock named `<code>str</code>` is free to use (that is, not locked).
Returns `<code class="highlight fixed" style="white-space:pre-wrap">1</code>` if the lock is free (no one is using the lock),
 `<code class="highlight fixed" style="white-space:pre-wrap">0</code>` if the lock is in use, and `<code class="highlight fixed" style="white-space:pre-wrap">NULL</code>` if an
error occurs (such as an incorrect argument, like an empty string or `<code class="highlight fixed" style="white-space:pre-wrap">NULL</code>`). `<code class="highlight fixed" style="white-space:pre-wrap">str</code>` is case insensitive.


If the [metadata_lock_info](../../../../../plugins/other-plugins/metadata-lock-info-plugin.md) plugin is installed, the [Information Schema](../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) [metadata_lock_info](../../../administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-metadata_lock_info-table.md) table contains information about locks of this kind (as well as [metadata locks](../../../transactions/metadata-locking.md)).


Statements using the `<code>IS_FREE_LOCK</code>` function are [not safe for statement-based replication](../../../../../../server-usage/replication-cluster-multi-master/standard-replication/unsafe-statements-for-statement-based-replication.md).


## See Also


* [GET_LOCK](get_lock.md)
* [RELEASE_LOCK](release_lock.md)
* [IS_USED_LOCK](is_used_lock.md)
* [RELEASE_ALL_LOCKS](release_all_locks.md)

