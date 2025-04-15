# RESET MASTER

```
RESET MASTER [TO #]
```

Deletes all [binary log](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) files listed in the index file, resets the
binary log index file to be empty, and creates a new binary log file with a suffix of .000001.

If `TO #` is given, then the first new binary log file will start from number #.

This statement is for use only when the master is started for the first time, and should never be used if any slaves are actively [replicating](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/replication-compatibility-between-mariadb-and-mysql) from the binary log.

#

# See Also

* The [PURGE BINARY LOGS](/kb/en/sql-commands-purge-logs/) statement is intended for use in active replication.