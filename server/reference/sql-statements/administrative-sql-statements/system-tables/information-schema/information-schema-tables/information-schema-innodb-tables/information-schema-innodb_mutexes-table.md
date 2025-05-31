# Information Schema INNODB\_MUTEXES Table

The `INNODB_MUTEXES` table monitors mutex and rw locks waits. It has the following columns:

| Column       | Description                                         |
| ------------ | --------------------------------------------------- |
| Column       | Description                                         |
| NAME         | Name of the lock, as it appears in the source code. |
| CREATE\_FILE | File name of the mutex implementation.              |
| CREATE\_LINE | Line number of the mutex implementation.            |
| OS\_WAITS    | How many times the mutex occurred.                  |

The `CREATE_FILE` and `CREATE_LINE` columns depend on the InnoDB/XtraDB version.

Note that since [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes), the table has only been providing information about\
rw\_lock\_t, not any mutexes. From [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes) until [MariaDB 10.2.32](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10232-release-notes), [MariaDB 10.3.23](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10323-release-notes), [MariaDB 10.4.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10413-release-notes) and [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-5-series/mariadb-1051-release-notes), the `NAME` column was not populated ([MDEV-21636](https://jira.mariadb.org/browse/MDEV-21636)).

The [SHOW ENGINE INNODB STATUS](../../../../show/show-engine.md#show-engine-innodb-mutex) statement provides similar information.

## Examples

```
SELECT * FROM INNODB_MUTEXES;
+------------------------------+---------------------+-------------+----------+
| NAME                         | CREATE_FILE         | CREATE_LINE | OS_WAITS |
+------------------------------+---------------------+-------------+----------+
| &dict_sys->mutex             | dict0dict.cc        |         989 |        2 |
| &buf_pool->flush_state_mutex | buf0buf.cc          |        1388 |        1 |
| &log_sys->checkpoint_lock    | log0log.cc          |        1014 |        2 |
| &block->lock                 | combined buf0buf.cc |        1120 |        1 |
+------------------------------+---------------------+-------------+----------+
```

CC BY-SA / Gnu FDL
