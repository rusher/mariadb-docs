# BINLOG_GTID_POS

#

# Syntax

```
BINLOG_GTID_POS(binlog_filename,binlog_offset)
```

#

# Description

The BINLOG_GTID_POS() function takes as input an old-style [binary log](../../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) position in the form of a file name and a file offset. It looks up the position in the current binlog, and returns a string representation of the corresponding [GTID](/kb/en/global-transaction-id/) position. If the position is not found in the current binlog, NULL is returned.

#

# Examples

```
SELECT BINLOG_GTID_POS("master-bin.000001", 600);
```

#

# See Also

* [SHOW BINLOG EVENTS](../../../administrative-sql-statements/show/show-binlog-events.md) - Show events and their positions in the binary log