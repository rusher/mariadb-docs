
# Transaction Timeouts

MariaDB has always had the [wait_timeout](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#wait_timeout) and [interactive_timeout](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#interactive_timeout) settings, which close connections after a certain period of inactivity.


However, these are by default set to a long wait period. In situations where transactions may be started, but not committed or rolled back, more granular control and a shorter timeout may be desirable so as to avoid locks being held for too long.


[MariaDB 10.3](../../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md) introduced three new variables to handle this situation.


* [idle_transaction_timeout](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#idle_transaction_timeout) (all transactions)
* [idle_write_transaction_timeout](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#idle_write_transaction_timeout) (write transactions - called `idle_readwrite_transaction_timeout` until [MariaDB 10.3.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1032-release-notes.md))
* [idle_readonly_transaction_timeout](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#idle_readonly_transaction_timeout) (read transactions)


These accept a time in seconds to time out, by closing the connection, transactions that are idle for longer than this period. By default all are set to zero, or no timeout.


[idle_transaction_timeout](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#idle_transaction_timeout) affects all transactions, [idle_write_transaction_timeout](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#idle_write_transaction_timeout) affects write transactions only and [idle_readonly_transaction_timeout](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#idle_readonly_transaction_timeout) affects read transactions only. The latter two variables work independently. However, if either is set along with [idle_transaction_timeout](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#idle_transaction_timeout), the settings for [idle_write_transaction_timeout](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#idle_write_transaction_timeout) or [idle_readonly_transaction_timeout](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#idle_readonly_transaction_timeout) will take precedence.


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
