# RESET MASTER

```
RESET MASTER [TO #]
```

Deletes all [binary log](../../../server-management/server-monitoring-logs/binary-log/) files listed in the index file, resets the\
binary log index file to be empty, and creates a new binary log file with a suffix of .000001.

If `TO #` is given, then the first new binary log file will start from number #.

This statement is for use only when the master is started for the first time, and should never be used if any slaves are actively [replicating](broken-reference) from the binary log.

## See Also

* The [PURGE BINARY LOGS](../../../reference/sql-statements/administrative-sql-statements/purge-binary-logs.md) statement is intended for use in active replication.

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
