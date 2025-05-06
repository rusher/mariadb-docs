
# LINEAR KEY Partitioning Type

### Syntax


```
LINEAR PARTITION BY KEY ([column_names])
[PARTITIONS (number_of_partitions)]
```

## Description


LINEAR KEY partitioning is a form of [partitioning](../README.md), similar to [KEY partitioning](key-partitioning-type.md).


LINEAR KEY partitioning makes use of a powers-of-two algorithm, while KEY partitioning 
uses modulo arithmetic, to determine the partition number.


Adding, dropping, merging and splitting partitions is much faster than with the [KEY partitioning type](key-partitioning-type.md), however, data is less likely to be evenly distributed over the partitions.


## Example


```
CREATE OR REPLACE TABLE t1 (v1 INT)
  PARTITION BY LINEAR KEY (v1)
  PARTITIONS 2;
```


CC BY-SA / Gnu FDL

