# TEXT

#

# Syntax

```
TEXT[(M)] [CHARACTER SET charset_name] [COLLATE collation_name]
```

#

# Description

A `TEXT` column with a maximum length of `65,535` (`216 - 1`)
characters. The effective maximum length is less if the value contains
multi-byte characters. Each `TEXT` value is stored using a two-byte length
prefix that indicates the number of bytes in the value. If you need a bigger storage, consider using [MEDIUMTEXT](mediumtext.md) instead.

An optional length `M` can be given for this type. If this is done, MariaDB
creates the column as the smallest `TEXT` type large enough to hold values
`M` characters long.

Before [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-102), all MariaDB [collations](/kb/en/character-sets/) were of type PADSPACE, meaning that TEXT (as well as [VARCHAR](varchar.md) and [CHAR](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/charset-narrowing-optimization.md) values) are compared without regard for trailing spaces. This does not apply to the [LIKE](../../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/like.md) pattern-matching operator, which takes into account trailing spaces.

`BLOB` and `TEXT` columns can be assigned a [DEFAULT](../../sql-statements-and-structure/sql-statements/data-definition/create/create-tablespace.md#default) value. This was not possible prior to [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-102).

#

# Examples

Trailing spaces:

```
CREATE TABLE strtest (d TEXT(10));
INSERT INTO strtest VALUES('Maria ');

SELECT d='Maria',d='Maria ' FROM strtest;
+-----------+--------------+
| d='Maria' | d='Maria ' |
+-----------+--------------+
| 1 | 1 |
+-----------+--------------+

SELECT d LIKE 'Maria',d LIKE 'Maria ' FROM strtest;
+----------------+-------------------+
| d LIKE 'Maria' | d LIKE 'Maria ' |
+----------------+-------------------+
| 0 | 1 |
+----------------+-------------------+
```

#

# Indexing

A [unique index](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/getting-started-with-indexes.md#unique-index) can be created on a `TEXT` column. This was not possible prior to [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-104)

Internally, this uses hash indexing to quickly check the values and if a hash collision is found, the actual stored values are compared in order to retain the uniqueness.

#

# Difference between [VARCHAR](varchar.md) and TEXT

* [VARCHAR](varchar.md) columns can be fully indexed. `TEXT` columns can only be indexed over a specified length.
* Using TEXT or [BLOB](blob.md) in a [SELECT](../../../server-usage/replication-cluster-multi-master/standard-replication/selectively-skipping-replication-of-binlog-events.md) query that uses temporary tables for storing intermediate results will force the temporary table to be disk based (using the [Aria storage engine](../../storage-engines/aria/aria-storage-engine.md) instead of the [memory storage engine](../../storage-engines/memory-storage-engine.md), which is a bit slower. This is not that bad as the [Aria storage engine](../../storage-engines/aria/aria-storage-engine.md) caches the rows in memory. To get the benefit of this, one should ensure that the [aria_pagecache_buffer_size](../../storage-engines/aria/aria-system-variables.md#aria_pagecache_buffer_size) variable is big enough to hold most of the row and index data for temporary tables.

#

## For Storage Engine Developers

* Internally the full length of the [VARCHAR](varchar.md) column is allocated inside each TABLE objects record[] structure. As there are three such buffers, each open table will allocate 3 times max-length-to-store-varchar bytes of memory.
* `TEXT` and `BLOB` columns are stored with a pointer (4 or 8 bytes) + a 1-4 bytes length. The `TEXT` data is only stored once. This means that internally `TEXT` uses less memory for each open table but instead has the additional overhead that each `TEXT` object needs to be allocated and freed for each row access (with some caching in between).

#

# See Also

* [BLOB and TEXT Data Types](blob-and-text-data-types.md)
* [MEDIUMTEXT](mediumtext.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)