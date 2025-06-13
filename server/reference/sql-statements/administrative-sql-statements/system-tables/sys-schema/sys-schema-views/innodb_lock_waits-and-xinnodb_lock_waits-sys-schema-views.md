# innodb\_lock\_waits and x$innodb\_lock\_waits Sys Schema Views

**MariaDB starting with** [**10.6**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106)

These [Sys Schema](../) views were introduced in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106).

## Description

The `innodb_lock_waits` and `x$innodb_lock_waits` views summarize InnoDB locks that transactions are waiting upon, by default sorted in descending buffer size.

The `innodb_lock_waits` view is intended to be easier for human reading, while the `x$innodb_lock_waits` view provides the data in raw form, intended for tools that process the data.

They contain the following columns:

| Column                          | Description                                                                                                             |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Column                          | Description                                                                                                             |
| wait\_started                   | Time that lock wait began.                                                                                              |
| wait\_age                       | TIME value for the length of the lock wait.                                                                             |
| wait\_age\_secs                 | Seconds value for the length of the lock wait.                                                                          |
| locked\_table\_schema           | Schema containing the locked table.                                                                                     |
| locked\_table\_name             | Name of the locked table.                                                                                               |
| locked\_table\_partition        | Name of the locked partition, or NULL if none.                                                                          |
| locked\_table\_subpartition     | Name of the locked subpartition, or NULL if none.                                                                       |
| locked\_index                   | Name of the locked index.                                                                                               |
| locked\_type                    | Type of the waiting lock.                                                                                               |
| waiting\_trx\_id                | ID of the waiting transaction.                                                                                          |
| waiting\_trx\_started           | Time that the waiting transaction started.                                                                              |
| waiting\_trx\_age               | TIME value for the length of time that the transaction has been waiting.                                                |
| waiting\_trx\_rows\_locked      | Number of rows locked by the waiting transaction.                                                                       |
| waiting\_trx\_rows\_modified    | Number of rows modified by the waiting transaction.                                                                     |
| waiting\_pid                    | Processlist ID of the waiting transaction.                                                                              |
| waiting\_query                  | Statement waiting for the lock.                                                                                         |
| waiting\_lock\_id               | ID of the waiting lock.                                                                                                 |
| waiting\_lock\_mode             | Mode of the waiting lock.                                                                                               |
| blocking\_trx\_id               | ID of the transaction blocking the waiting lock.                                                                        |
| blocking\_pid                   | Processlist ID of the blocking transaction.                                                                             |
| blocking\_query                 | Statement the blocking transaction is executing, or NULL if the session that issued the blocking query has become idle. |
| blocking\_lock\_id              | ID of the lock blocking the waiting lock.                                                                               |
| blocking\_lock\_mode            | Mode of the lock blocking the waiting lock.                                                                             |
| blocking\_trx\_started          | Time the blocking transaction started.                                                                                  |
| blocking\_trx\_age              | TIME value for how long the blocking transaction has been executing.                                                    |
| blocking\_trx\_rows\_locked     | Number of rows locked by the blocking transaction.                                                                      |
| blocking\_trx\_rows\_modified   | Number of rows modified by the blocking transaction.                                                                    |
| sql\_kill\_blocking\_query      | KILL statement that could be used to kill the blocking statement.                                                       |
| sql\_kill\_blocking\_connection | KILL statement that could be used to kill the blocking statement session.                                               |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
