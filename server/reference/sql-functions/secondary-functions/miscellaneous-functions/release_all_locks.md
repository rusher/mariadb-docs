# RELEASE\_ALL\_LOCKS

**MariaDB until** [**10.5.2**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes)

RELEASE\_ALL\_LOCKS was added in [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes).

## Syntax

```
RELEASE_ALL_LOCKS()
```

## Description

Releases all named locks held by the current session. Returns the number of locks released, or `0` if none were held.

Statements using the `RELEASE_ALL_LOCKS` function are [not safe for statement-based replication](../../../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).

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

* [GET\_LOCK](get_lock.md)
* [IS\_FREE\_LOCK](is_free_lock.md)
* [IS\_USED\_LOCK](is_used_lock.md)
* [RELEASE\_LOCK](release_lock.md)

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
