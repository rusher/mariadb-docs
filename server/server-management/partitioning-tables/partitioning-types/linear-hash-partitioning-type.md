
# LINEAR HASH Partitioning Type

## Syntax


```
PARTITION BY LINEAR HASH (partitioning_expression)
[PARTITIONS(number_of_partitions)]
```

## Description


LINEAR HASH partitioning is a form of [partitioning](../README.md), similar to [HASH partitioning](hash-partitioning-type.md), in which the server takes care of the partition in which to place the data, ensuring a relatively even distribution among the partitions.


LINEAR HASH partitioning makes use of a powers-of-two algorithm, while HASH partitioning uses the modulus of the hashing function's value. Adding, dropping, merging and splitting partitions is much faster than with the [HASH partitioning type](hash-partitioning-type.md), however, data is less likely to be evenly distributed over the partitions.


## Example


```
CREATE OR REPLACE TABLE t1 (c1 INT, c2 DATETIME) 
  PARTITION BY LINEAR HASH(TO_DAYS(c2)) 
  PARTITIONS 5;
```
