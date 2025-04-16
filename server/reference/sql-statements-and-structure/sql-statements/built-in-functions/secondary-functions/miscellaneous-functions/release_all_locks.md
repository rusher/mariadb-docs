
# RELEASE_ALL_LOCKS


##### MariaDB until [10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)
RELEASE_ALL_LOCKS was added in [MariaDB 10.5.2](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md).


## Syntax


```
RELEASE_ALL_LOCKS()
```


## Description


Releases all named locks held by the current session. Returns the number of locks released, or `0` if none were held.


Statements using the `RELEASE_ALL_LOCKS` function are [not safe for statement-based replication](../../../../../../server-usage/replication-cluster-multi-master/standard-replication/unsafe-statements-for-statement-based-replication.md).


## Examples


```
SELECT RELEASE_ALL_LOCKS();
+---------------------+
| RELEASE_ALL_LOCKS() | 
+---------------------+
|                   0 |
+---------------------+

SELECT GET_LOCK('lock1',10);
+----------------------+
| GET_LOCK('lock1',10) |
+----------------------+
|                    1 |
+----------------------+

SELECT RELEASE_ALL_LOCKS();
+---------------------+
| RELEASE_ALL_LOCKS() | 
+---------------------+
|                   1 |
+---------------------+
```

## See Also


* [GET_LOCK](get_lock.md)
* [IS_FREE_LOCK](is_free_lock.md)
* [IS_USED_LOCK](is_used_lock.md)
* [RELEASE_LOCK](release_lock.md)

