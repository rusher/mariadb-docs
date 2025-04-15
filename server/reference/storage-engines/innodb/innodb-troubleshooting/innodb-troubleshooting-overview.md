# InnoDB Troubleshooting Overview

As with most errors, first take a look at the contents of the [MariaDB error log](../../../../server-management/server-monitoring-logs/error-log.md). If dealing with a deadlock, setting the [innodb_print_all_deadlocks](/en/xtradbinnodb-server-system-variables/#innodb_print_all_deadlocks) option (off by default) will output details of all deadlocks to the error log.

It can also help to enable the various [InnoDB Monitors](/en/xtradb-innodb-monitors/) relating to the problem you are experiencing. There are four types: the standard InnoDB monitor, the InnoDB Lock Monitor, InnoDB Tablespace Monitor and the InnoDB Table Monitor.

Running [CHECK TABLE](../../../sql-statements-and-structure/sql-statements/table-statements/check-table.md) will help determine whether there are errors in the table.

For problems with the InnoDB Data Dictionary, see [InnoDB Data Dictionary Troubleshooting](innodb-data-dictionary-troubleshooting.md).

#

# See Also

* [InnoDB Data Dictionary Troubleshooting](innodb-data-dictionary-troubleshooting.md)
* [InnoDB Recovery Modes](/en/xtradbinnodb-recovery-modes/)
* [Error Codes](/en/error-codes/)