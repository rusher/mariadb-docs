# Identifier Case-sensitivity

Whether objects are case-sensitive or not is partly determined by the underlying operating system. Unix-based systems are case-sensitive, Windows is not, while Mac OS X is usually case-insensitive by default, but devices can be configured as case-sensitive using Disk Utility.

Database, table, table aliases and [trigger](../../../server-usage/triggers-events/triggers/) names are affected by the systems case-sensitivity, while index, column, column aliases, [stored routine](../../../server-usage/stored-routines/) and [event](../../../server-usage/triggers-events/event-scheduler/events.md) names are never case sensitive.

Log file group name are case sensitive.

The [lower\_case\_table\_names](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lower_case_table_names) server system variable plays a key role. It determines whether table names, aliases and database names are compared in a case-sensitive manner. If set to 0 (the default on Unix-based systems), table names and aliases and database names are compared in a case-sensitive manner. If set to 1 (the default on Windows), names are stored in lowercase and not compared in a case-sensitive manner. If set to 2 (the default on Mac OS X), names are stored as declared, but compared in lowercase.

It is thus possible to make Unix-based systems behave like Windows and ignore case-sensitivity. The reverse is not true prior to Windows 10, as the underlying Windows filesystem could not support this. It is possible since Windows 10, although case-insensitivity is still the default operating system setting.

Even on case-insensitive systems, you are required to use the same case consistently within the same statement. The following statement fails, as it refers to the table name in a different case.

```
SELECT * FROM a_table WHERE A_table.id>10;
```

For a full list of identifier naming rules, see [Identifier Names](identifier-names.md).

Please note that [lower\_case\_table\_names](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lower_case_table_names) is a database initialization parameter. This means that, along with [innodb\_page\_size](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#innodb_page_size), this variable must be set before running [mariadb-install-db](../../../clients-and-utilities/mariadb-install-db.md), and will not change the behavior of servers unless applied before the creation of core system databases.

CC BY-SA / Gnu FDL
