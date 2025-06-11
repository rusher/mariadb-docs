---
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
---

# ColumnStore System Databases

When using ColumnStore, MariaDB Server creates a series of system databases used for operational purposes.

| Database             | Description                                                                                                                                                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Database             | Description                                                                                                                                                                                                                  |
| calpontsys           | Database maintains table metadata about ColumnStore tables.                                                                                                                                                                  |
| infinidb\_querystats | Database maintains information about query performance. For more information, see [Query Analysis](../high-availability/analyzing-queries-in-columnstore.md).                                                                |
| columnstore\_info    | The database for stored procedures is used to retrieve information about ColumnStore usage. For more information, see the [ColumnStore Information Schema](../sql-commands/columnstore-information-schema-tables.md) tables. |

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
