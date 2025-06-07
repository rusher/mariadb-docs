# Transaction Timeouts

MariaDB has always had the [wait\_timeout](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#wait_timeout) and [interactive\_timeout](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#interactive_timeout) settings, which close connections after a certain period of inactivity.

However, these are by default set to a long wait period. In situations where transactions may be started, but not committed or rolled back, more granular control and a shorter timeout may be desirable so as to avoid locks being held for too long.

[MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103) introduced three new variables to handle this situation.

* [idle\_transaction\_timeout](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#idle_transaction_timeout) (all transactions)
* [idle\_write\_transaction\_timeout](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#idle_write_transaction_timeout) (write transactions - called `idle_readwrite_transaction_timeout` until [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1032-release-notes))
* [idle\_readonly\_transaction\_timeout](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#idle_readonly_transaction_timeout) (read transactions)

These accept a time in seconds to time out, by closing the connection, transactions that are idle for longer than this period. By default all are set to zero, or no timeout.

[idle\_transaction\_timeout](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#idle_transaction_timeout) affects all transactions, [idle\_write\_transaction\_timeout](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#idle_write_transaction_timeout) affects write transactions only and [idle\_readonly\_transaction\_timeout](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#idle_readonly_transaction_timeout) affects read transactions only. The latter two variables work independently. However, if either is set along with [idle\_transaction\_timeout](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#idle_transaction_timeout), the settings for [idle\_write\_transaction\_timeout](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#idle_write_transaction_timeout) or [idle\_readonly\_transaction\_timeout](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#idle_readonly_transaction_timeout) will take precedence.

## Examples

```
SET SESSION idle_transaction_timeout=2;
BEGIN;
SELECT * FROM t;
Empty set (0.000 sec)
## wait 3 seconds
SELECT * FROM t;
ERROR 2006 (HY000): MySQL server has gone away
```

```
SET SESSION idle_write_transaction_timeout=2;
BEGIN;
SELECT * FROM t;
Empty set (0.000 sec)
## wait 3 seconds
SELECT * FROM t;
Empty set (0.000 sec)
INSERT INTO t VALUES(1);
## wait 3 seconds
SELECT * FROM t;
ERROR 2006 (HY000): MySQL server has gone away
```

```
SET SESSION idle_transaction_timeout=2, SESSION idle_readonly_transaction_timeout=10;
BEGIN;
SELECT * FROM t;
Empty set (0.000 sec)
 ## wait 3 seconds
SELECT * FROM t;
Empty set (0.000 sec)
## wait 11 seconds
SELECT * FROM t;
ERROR 2006 (HY000): MySQL server has gone away
```

CC BY-SA / Gnu FDL
