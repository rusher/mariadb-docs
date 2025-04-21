
# RELEASE_LOCK

## Syntax


```
RELEASE_LOCK(str)
```


## Description


Releases the lock named by the string `str` that was obtained with [GET_LOCK()](get_lock.md). Returns 1 if the lock was released, 0 if the lock was not established by this thread (in which case the lock is not
released), and `NULL` if the named lock did not exist. The lock does not exist if it was never obtained by a call to `GET_LOCK()` or if it has previously been released.


`str` is case insensitive. If `str` is an empty string or `NULL`, `RELEASE_LOCK()` returns `NULL` and does nothing.


Statements using the `RELEASE_LOCK` function are not [safe for statement-based replication](../../../../../../server-usage/replication-cluster-multi-master/standard-replication/unsafe-statements-for-statement-based-replication.md).


The [DO statement](../../../stored-routine-statements/do.md) is convenient to use with `RELEASE_LOCK()`.


## Examples


Connection1:


```
SELECT GET_LOCK('lock1',10);
+----------------------+
| GET_LOCK('lock1',10) |
+----------------------+
|                    1 |
+----------------------+
```

Connection 2:


```
SELECT GET_LOCK('lock2',10);
+----------------------+
| GET_LOCK('lock2',10) |
+----------------------+
|                    1 |
+----------------------+
```

Connection 1:


```
SELECT RELEASE_LOCK('lock1'), RELEASE_LOCK('lock2'), RELEASE_LOCK('lock3');
+-----------------------+-----------------------+-----------------------+
| RELEASE_LOCK('lock1') | RELEASE_LOCK('lock2') | RELEASE_LOCK('lock3') |
+-----------------------+-----------------------+-----------------------+
|                     1 |                     0 |                  NULL |
+-----------------------+-----------------------+-----------------------+
```

It is possible to hold the same lock recursively. This example is viewed using the [metadata_lock_info](../../../../../plugins/other-plugins/metadata-lock-info-plugin.md) plugin:


```
SELECT GET_LOCK('lock3',10);
+----------------------+
| GET_LOCK('lock3',10) |
+----------------------+
|                    1 |
+----------------------+

SELECT GET_LOCK('lock3',10);
+----------------------+
| GET_LOCK('lock3',10) |
+----------------------+
|                    1 |
+----------------------+

SELECT * FROM INFORMATION_SCHEMA.METADATA_LOCK_INFO;
+-----------+---------------------+---------------+-----------+--------------+------------+
| THREAD_ID | LOCK_MODE           | LOCK_DURATION | LOCK_TYPE | TABLE_SCHEMA | TABLE_NAME |
+-----------+---------------------+---------------+-----------+--------------+------------+
|        46 | MDL_SHARED_NO_WRITE | NULL          | User lock | lock3        |            |
+-----------+---------------------+---------------+-----------+--------------+------------+

SELECT RELEASE_LOCK('lock3');
+-----------------------+
| RELEASE_LOCK('lock3') |
+-----------------------+
|                     1 |
+-----------------------+

SELECT * FROM INFORMATION_SCHEMA.METADATA_LOCK_INFO;
+-----------+---------------------+---------------+-----------+--------------+------------+
| THREAD_ID | LOCK_MODE           | LOCK_DURATION | LOCK_TYPE | TABLE_SCHEMA | TABLE_NAME |
+-----------+---------------------+---------------+-----------+--------------+------------+
|        46 | MDL_SHARED_NO_WRITE | NULL          | User lock | lock3        |            |
+-----------+---------------------+---------------+-----------+--------------+------------+

SELECT RELEASE_LOCK('lock3');
+-----------------------+
| RELEASE_LOCK('lock3') |
+-----------------------+
|                     1 |
+-----------------------+

SELECT * FROM INFORMATION_SCHEMA.METADATA_LOCK_INFO;
Empty set (0.000 sec)
```

## See Also


* [GET_LOCK](get_lock.md)
* [IS_FREE_LOCK](is_free_lock.md)
* [IS_USED_LOCK](is_used_lock.md)
* [RELEASE_ALL_LOCKS](release_all_locks.md)

