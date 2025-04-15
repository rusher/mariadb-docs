
# SYSDATE

## Syntax


```
SYSDATE([precision])
```


## Description


Returns the current date and time as a value in 'YYYY-MM-DD HH:MM:SS'
or YYYYMMDDHHMMSS.uuuuuu format, depending on whether the function is
used in a string or numeric context.


The optional *precision* determines the microsecond precision. See [Microseconds in MariaDB](microseconds-in-mariadb.md).


SYSDATE() returns the time at which it executes. This differs from the
behavior for [NOW()](now.md), which returns a constant time that indicates the
time at which the statement began to execute. (Within a stored routine
or trigger, NOW() returns the time at which the routine or triggering
statement began to execute.)


In addition, changing the [timestamp system variable](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#timestamp) with a [SET](../../../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md) `<code>timestamp</code>` statement affects the value returned by
NOW() but not by SYSDATE(). This means that timestamp settings in the
[binary log](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) have no effect on invocations of SYSDATE().


Because SYSDATE() can return different values even within the same statement, and is not affected by SET TIMESTAMP, it is non-deterministic and therefore unsafe for replication if statement-based binary logging is used. If that is a problem, you can use row-based logging, or start the server with the [--sysdate-is-now](../../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-sysdate-is-now) mariadbd option to cause SYSDATE() to be an alias for NOW(). The non-deterministic nature of SYSDATE() also means that indexes cannot be used for evaluating expressions that refer to it, and that statements using the SYSDATE() function are [unsafe for statement-based replication](../../../../../server-usage/replication-cluster-multi-master/standard-replication/unsafe-statements-for-statement-based-replication.md).


## Examples


Difference between NOW() and SYSDATE():


```
SELECT NOW(), SLEEP(2), NOW();
+---------------------+----------+---------------------+
| NOW()               | SLEEP(2) | NOW()               |
+---------------------+----------+---------------------+
| 2010-03-27 13:23:40 |        0 | 2010-03-27 13:23:40 |
+---------------------+----------+---------------------+

SELECT SYSDATE(), SLEEP(2), SYSDATE();
+---------------------+----------+---------------------+
| SYSDATE()           | SLEEP(2) | SYSDATE()           |
+---------------------+----------+---------------------+
| 2010-03-27 13:23:52 |        0 | 2010-03-27 13:23:54 |
+---------------------+----------+---------------------+
```

With precision:


```
SELECT SYSDATE(4);
+--------------------------+
| SYSDATE(4)               |
+--------------------------+
| 2018-07-10 10:17:13.1689 |
+--------------------------+
```

## See Also


* [Microseconds in MariaDB](microseconds-in-mariadb.md)
* [timestamp server system variable](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#timestamp)

