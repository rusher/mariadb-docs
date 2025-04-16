
# Storage Engine Index Types

This refers to the index_type definition when creating an index, i.e. BTREE, HASH or RTREE.


For more information on general types of indexes, such as primary keys, unique indexes etc, go to [Getting Started with Indexes](getting-started-with-indexes.md).



| Storage Engine | Permitted Indexes |
| --- | --- |
| Storage Engine | Permitted Indexes |
| [Aria](../../../../ref/storage-engines/s3-storage-engine/aria_s3_copy.md) | BTREE, RTREE |
| [MyISAM](../../../../ref/storage-engines/myisam-storage-engine/myisam-system-variables.md) | BTREE, RTREE |
| [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) | BTREE |
| [MEMORY/HEAP](../../../../ref/storage-engines/memory-storage-engine.md) | HASH, BTREE |



BTREE is generally the default index type. For [MEMORY](../../../../ref/storage-engines/memory-storage-engine.md) tables, HASH is the default. [TokuDB](../../../../ref/storage-engines/tokudb/tokudb-resources.md) uses a particular data structure called *fractal trees*, which is optimized for data that do not entirely fit memory.


Understanding the B-tree and hash data structures can help predict how different queries perform on different storage engines that use these data structures in their indexes, particularly for the MEMORY storage engine that lets you choose B-tree or hash indexes.
B-Tree Index Characteristics


## B-tree Indexes


B-tree indexes are used for column comparisons using the >, >=, =, >=, < or BETWEEN operators, as well as for LIKE comparisons that begin with a constant.


For example, the query `SELECT * FROM Employees WHERE First_Name LIKE 'Maria%';` can make use of a B-tree index, while `SELECT * FROM Employees WHERE First_Name LIKE '%aria';` cannot.


B-tree indexes also permit leftmost prefixing for searching of rows.


If the number or rows doesn't change, hash indexes occupy a fixed amount of memory, which is lower than the memory occupied by BTREE indexes.


## Hash Indexes


Hash indexes, in contrast, can only be used for equality comparisons, so those using the = or <=> operators. They cannot be used for ordering, and provide no information to the optimizer on how many rows exist between two values.


Hash indexes do not permit leftmost prefixing - only the whole index can be used.


## R-tree Indexes


See [SPATIAL](../../../../ref/sql-statements-and-structure/geographic-geometric-features/spatial-index.md) for more information.

