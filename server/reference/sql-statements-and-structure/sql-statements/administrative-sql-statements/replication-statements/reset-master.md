
# RESET MASTER

```
RESET MASTER [TO #]
```

Deletes all [binary log](../../../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) files listed in the index file, resets the
binary log index file to be empty, and creates a new binary log file with a suffix of .000001.


If `<code class="fixed" style="white-space:pre-wrap">TO #</code>` is given, then the first new binary log file will start from number #.


This statement is for use only when the master is started for the first time, and should never be used if any slaves are actively [replicating](README.md) from the binary log.


## See Also


* The [PURGE BINARY LOGS](../purge-binary-logs.md) statement is intended for use in active replication.

