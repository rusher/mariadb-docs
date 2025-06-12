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
    visible: true
---

# ColumnStore Partition Management

1. [Introduction "Introduction"](columnstore-partition-management.md#introduction)
2. [Managing partitions by partition number "Managing partitions by partition number"](columnstore-partition-management.md#managing-partitions-by-partition-number)
3. [Displaying partition information "Displaying partition information"](columnstore-partition-management.md#displaying-partition-information)
4. [Disabling partitions "Disabling partitions"](columnstore-partition-management.md#disabling-partitions)
5. [Enabling partitions "Enabling partitions"](columnstore-partition-management.md#enabling-partitions)
6. [Dropping partitions "Dropping partitions"](columnstore-partition-management.md#dropping-partitions)
7. [Managing partitions by column value "Managing partitions by column value"](columnstore-partition-management.md#managing-partitions-by-column-value)
8. [Displaying partition information "Displaying partition information"](columnstore-partition-management.md#displaying-partition-information)
9. [Disabling partitions "Disabling partitions"](columnstore-partition-management.md#disabling-partitions)
10. [Enabling partitions "Enabling partitions"](columnstore-partition-management.md#enabling-partitions)
11. [Dropping partitions "Dropping partitions"](columnstore-partition-management.md#dropping-partitions)
12. [Dropping data not wholly within one partition "Dropping data not wholly within one partition"](columnstore-partition-management.md#dropping-data-not-wholly-within-one-partition)

## Introduction

MariaDB ColumnStore automatically creates logical horizontal partitions across every column. For ordered or semi-ordered data fields such as an order date this will result in a highly effective partitioning scheme based on that column. This allows for increased performance of queries filtering on that column since partition elimination can be performed. It also allows for data lifecycle management as data can be disabled or dropped by partition cheaply. Caution should be used when disabling or dropping partitions as these commands are destructive.

It is important to understand that a Partition in ColumnStore terms is actually 2 extents (16 million rows) and that extents & partitions are created according to the following algorithm in 1.0.x:

1. Create 4 extents in 4 files
2. When these are filled up (after 32M rows), create 4 more extents in the 4 files created in step 1.
3. When these are filled up (after 64M rows), create a new partition.

## Managing partitions by partition number

### Displaying partition information

Information about all partitions for a given column can be retrieved using the _calShowPartitions_ stored procedure which takes either two or three mandatory parameters: \[_database\_name_], _table\_name_, and _column\_name_. If two parameters are provided the current database is assumed. For example:

```
select calShowPartitions('orders','orderdate');
+-----------------------------------------+
| calShowPartitions('orders','orderdate') |
+-----------------------------------------+
| Part# Min        Max        Status
  0.0.1 1992-01-01 1998-08-02 Enabled
  0.1.2 1998-08-03 2004-05-15 Enabled
  0.2.3 2004-05-16 2010-07-24 Enabled |
+-----------------------------------------+

1 row in set (0.05 sec)
```

### Disabling partitions

The _calDisablePartitions_ stored procedure allows for disabling of one or more partitions. A disabled partition still exists on the file system (and can be enabled again at a later time) but will not participate in any query, DML or import activity. The procedure takes either two or three mandatory parameters: \[_database\_name_], _table\_name_, and _partition\_numbers_ separated by commas. If two parameters are provided the current database is assumed. For example:

```
select calDisablePartitions('orders','0.0.1');
+----------------------------------------+
| calDisablePartitions('orders','0.0.1') |
+----------------------------------------+
| Partitions are disabled successfully.  |
+----------------------------------------+
1 row in set (0.28 sec)
```

The result showing the first partition has been disabled:

```
select calShowPartitions('orders','orderdate');
+-----------------------------------------+
| calShowPartitions('orders','orderdate') |
+-----------------------------------------+
| Part# Min        Max        Status
  0.0.1 1992-01-01 1998-08-02 Disabled
  0.1.2 1998-08-03 2004-05-15 Enabled
  0.2.3 2004-05-16 2010-07-24 Enabled |
+-----------------------------------------+
1 row in set (0.05 sec)
```

### Enabling partitions

The _calEnablePartitions_ stored procedure allows for enabling of one or more partitions. The procedure takes the same set of parameters as _calDisablePartitions_. For example:

```
select calEnablePartitions('orders', '0.0.1');
+----------------------------------------+
| calEnablePartitions('orders', '0.0.1') |
+----------------------------------------+
| Partitions are enabled successfully.   |
+----------------------------------------+
1 row in set (0.28 sec)
```

The result showing the first partition has been enabled:

```
select calShowPartitions('orders','orderdate');
+-----------------------------------------+
| calShowPartitions('orders','orderdate') |
+-----------------------------------------+
| Part# Min        Max        Status
  0.0.1 1992-01-01 1998-08-02 Enabled
  0.1.2 1998-08-03 2004-05-15 Enabled
  0.2.3 2004-05-16 2010-07-24 Enabled |
+-----------------------------------------+
1 rows in set (0.05 sec)
```

### Dropping partitions

The _calDropPartitions_ stored procedure allows for dropping of one or more partitions. Dropping means that the underlying storage is deleted and the partition is completely removed. A partition can be dropped from either enabled or disabled state. The procedure takes the same set of parameters as _calDisablePartitions_. Extra caution should be used with this procedure since it is destructive and cannot be reversed. For example:

```
select calDropPartitions('orders', '0.0.1');
+--------------------------------------+
| calDropPartitions('orders', '0.0.1') |
+--------------------------------------+
| Partitions are enabled successfully  |
+--------------------------------------+
1 row in set (0.28 sec)
```

The result showing the first partition has been dropped:

```
select calShowPartitions('orders','orderdate');
+-----------------------------------------+
| calShowPartitions('orders','orderdate') |
+-----------------------------------------+
| Part# Min        Max        Status
  0.1.2 1998-08-03 2004-05-15 Enabled
  0.2.3 2004-05-16 2010-07-24 Enabled |
+-----------------------------------------+
1 row in set (0.05 sec)
```

## Managing partitions by column value

### Displaying partition information

Information about a range of parititions for a given column can be retrieved using the _calShowPartitionsByValue_ stored procedure. This procedure takes either four or five mandatory parameters: \[_database\_name_], _table\_name_, _column\_name_, _start\_value_, and _end\_value_. If four parameters are provided the current database is assumed. Only casual partition column types ([INTEGER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/int), [DECIMAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/decimal), [DATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/date), [DATETIME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/datetime), [CHAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/char) up to 8 bytes and[VARCHAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/varchar) up to 7 bytes) are supported for this function.

The function returns a list of partitions whose minimum and maximum values for the column 'col\_name' fall completely within the range of 'start\_value' and 'end\_value'. For example:

```
select calShowPartitionsByValue('orders','orderdate', '1992-01-01', '2010-07-24');
+----------------------------------------------------------------------------+
| calShowPartitionsbyvalue('orders','orderdate', '1992-01-02', '2010-07-24') |
+----------------------------------------------------------------------------+
| Part# Min        Max        Status
  0.0.1 1992-01-01 1998-08-02 Enabled
  0.1.2 1998-08-03 2004-05-15 Enabled
  0.2.3 2004-05-16 2010-07-24 Enabled |
+----------------------------------------------------------------------------+
1 row in set (0.05 sec)
```

### Disabling partitions

The _calDisablePartitionsByValue_ stored procedure allows for disabling of one or more partitions by value. A disabled partition still exists on the file system (and can be enabled again at a later time) but will not participate in any query, DML or import activity. The procedure takes the same set of arguments as _calShowPartitionsByValue_. A good practice is to use _calShowPartitionsByValue_ to identify the partitions to be disabled and then the same argument values used to construct the _calDisablePartitionsByValue_ call. For example:

```
select calDisablePartitionsByValue('orders','orderdate', '1992-01-01', '1998-08-02');
+---------------------------------------------------------------------------------+
| caldisablepartitionsbyvalue ('orders', 'o_orderdate','1992-01-01','1998-08-02') |
+---------------------------------------------------------------------------------+
| Partitions are disabled successfully                                            |
+---------------------------------------------------------------------------------+
1 row in set (0.28 sec)
```

The result showing the first partition has been disabled:

```
select calShowPartitionsByValue('orders','orderdate', '1992-01-01', '2010-07-24');
+----------------------------------------------------------------------------+
| calShowPartitionsbyvalue('orders','orderdate', '1992-01-02','2010-07-24’ ) |
+----------------------------------------------------------------------------+
| Part# Min        Max        Status
  0.0.1 1992-01-01 1998-08-02 Disabled
  0.1.2 1998-08-03 2004-05-15 Enabled
  0.2.3 2004-05-16 2010-07-24 Enabled |
+----------------------------------------------------------------------------+
1 row in set (0.05 sec)
```

### Enabling partitions

The _calEnablePartitionsbyValue_ stored procedure allows for enabling of one or more partitions by value. The procedure takes the same set of arguments as _calShowPartitionsByValue_. A good practice is to use _calShowPartitionsByValue_ to identify the partitions to be enabled and then the same argument values used to construct the _calEnablePartitionsbyValue_ call. For example:

```
select calEnablePartitionsByValue('orders','orderdate', '1992-01-01', '1998-08-02');
+--------------------------------------------------------------------------------+
| calenablepartitionsbyvalue ('orders', 'o_orderdate','1992-01-01','1998-08-02') |
+--------------------------------------------------------------------------------+
| Partitions are enabled successfully                                            |
+--------------------------------------------------------------------------------+
1 row in set (0.28 sec)
```

The result showing the first partition has been enabled:

```
select calShowPartitionsByValue('orders','orderdate', '1992-01-01', '2010-07-24');
+----------------------------------------------------------------------------+
| calShowPartitionsbyvalue('orders','orderdate', '1992-01-02','2010-07-24' ) |
+----------------------------------------------------------------------------+
| Part# Min        Max        Status
  0.0.1 1992-01-01 1998-08-02 Enabled
  0.1.2 1998-08-03 2004-05-15 Enabled
  0.2.3 2004-05-16 2010-07-24 Enabled |
+----------------------------------------------------------------------------+
1 rows in set (0.05 sec)
```

### Dropping partitions

The _calDropPartitionsByValue_ stored procedure allows for dropping of one or more partitions by value. Dropping means that the underlying storage is deleted and the partition is completely removed. A partition can be dropped from either enabled or disabled state. The procedure takes the same set of arguments as _calShowPartitionsByValue_. A good practice is to use _calShowPartitionsByValue_ to identify the partitions to be enabled and then the same argument values used to construct the _calDropPartitionsByValue_ call. Extra caution should be used with this procedure since it is destructive and cannot be reversed. For example:

```
select calDropPartitionsByValue('orders','orderdate', '1992-01-01', '1998-08-02');
+------------------------------------------------------------------------------+
| caldroppartitionsbyvalue ('orders', 'o_orderdate','1992-01-01','1998-08-02') |
+------------------------------------------------------------------------------+
| Partitions are enabled successfully.                                         |
+------------------------------------------------------------------------------+
1 row in set (0.28 sec)
```

The result showing the first partition has been dropped:

```
select calShowPartitionsByValue('orders','orderdate', '1992-01-01', '2010-07-24');
+----------------------------------------------------------------------------+
| calShowPartitionsbyvalue('orders','orderdate', '1992-01-02','2010-07-24' ) |
+----------------------------------------------------------------------------+
| Part# Min        Max        Status
  0.1.2 1998-08-03 2004-05-15 Enabled
  0.2.3 2004-05-16 2010-07-24 Enabled |
+----------------------------------------------------------------------------+
1 row in set (0.05 sec)
```

## Dropping data not wholly within one partition

Since the partitioning scheme is system maintained the min and max values are not directly specified but influenced by the order of data loading. If the goal is to drop a specific date range then additional deletes are required to achieve this. The following cases may occur:

* For semi-ordered data, there may be overlap between min and max values between partitions.
* As in the example above, the partition ranged from 1992-01-01 to 1998-08-02. Potentially it may be desirable to drop the remaining 1998 rows.

A bulk delete statement can be used to delete the remaining rows that do not fall exactly within partition ranges. The partition drops will be fastest, however the system optimizes bulk delete statements to delete by block internally so are still relatively fast.

```
delete from orders where orderdate <= '1998-12-31';
```

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
