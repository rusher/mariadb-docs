# HASH Partitioning Type

## Syntax

```sql
PARTITION BY HASH (partitioning_expression)
[PARTITIONS(number_of_partitions)]
```

## Description

HASH partitioning is a form of [partitioning](../) in which the server takes care of the partition in which to place the data, ensuring an even distribution among the partitions.

It requires a column value, or an expression based on a column value, which is hashed, as well as the number of partitions into which to divide the table.

_partitioning\_expression_ needs to return a non-constant, deterministic integer. It is evaluated for each insert and update, so overly complex expressions can lead to performance issues. A hashing function operating on a single column, and where the value changes consistently with the column value, allows for easy pruning on ranges of partitions, and is usually a better choice. For this reason, using multiple columns in a hashing expression is not usually recommended.

_number\_of\_partitions_ is a positive integer specifying the number of partitions into which to divide the table. If the `PARTITIONS` clause is omitted, the default number of partitions is one.

### Determining the Partition

To determine which partition to use, the following calculation is performed:\
MOD(partitioning\_expression, number\_of\_partitions)

For example, if the expression is TO\_DAYS(datetime\_column) and the number of partitions is 5, inserting a datetime value of '2023-11-15' would determine the partition as follows:

* TO\_DAYS('2023-11-15') gives a value of 739204
* MOD(739204,5) returns 4\
  so the 4th partition is used.

HASH partitioning making use of the modulus of the hashing function's value. The [LINEAR HASH partitioning type](linear-hash-partitioning-type.md) is similar, using a powers-of-two algorithm. Data is more likely to be evenly distributed over the partitions than with the LINEAR HASH partitioning type, however, adding, dropping, merging and splitting partitions is much slower.

## Examples

```sql
CREATE OR REPLACE TABLE t1 (c1 INT, c2 DATETIME) 
  PARTITION BY HASH(TO_DAYS(c2)) 
  PARTITIONS 5;
```

Using the [Information Schema PARTITIONS Table](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-partitions-table.md) for more information:

```sql
INSERT INTO t1 VALUES (1,'2023-11-15');

SELECT PARTITION_NAME,TABLE_ROWS FROM INFORMATION_SCHEMA.PARTITIONS 
  WHERE TABLE_SCHEMA='test' AND TABLE_NAME='t1';
+----------------+------------+
| PARTITION_NAME | TABLE_ROWS |
+----------------+------------+
| p0             |          0 |
| p1             |          0 |
| p2             |          0 |
| p3             |          0 |
| p4             |          1 |
+----------------+------------+
```

## See Also

* [Partition Maintenance](../partition-maintenance.md) for suggestions on using partitions

CC BY-SA / Gnu FDL
