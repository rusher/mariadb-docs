# VARCHAR

#

# Syntax

```
[NATIONAL] VARCHAR(M) [CHARACTER SET charset_name] [COLLATE collation_name]
```

#

# Description

A variable-length string. M represents the maximum column length in
characters. The range of M is 0 to 65,532. The effective maximum
length of a VARCHAR is subject to the maximum row size and the character set used. For
example, utf8 characters can require up to three bytes per character,
so a VARCHAR column that uses the utf8 character set can be declared
to be a maximum of 21,844 characters.

**Note:** For the [ColumnStore](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/columnstore-system-variables) engine, M represents the maximum column length in
bytes.

MariaDB stores VARCHAR values as a one-byte or two-byte length prefix
plus data. The length prefix indicates the number of bytes in the
value. A VARCHAR column uses one length byte if values require no more
than 255 bytes, two length bytes if values may require more than 255
bytes.

MariaDB follows the standard SQL specification, and does not remove trailing spaces from VARCHAR values.

VARCHAR(0) columns can contain 2 values: an empty string or NULL. Such columns cannot be part of an index. The [CONNECT](../../../security/user-account-management/catalogs/connecting-to-a-server-configured-for-catalogs.md) storage engine does not support VARCHAR(0).

VARCHAR is shorthand for CHARACTER VARYING. NATIONAL VARCHAR is the
standard SQL way to define that a VARCHAR column should use some
predefined character set. MariaDB uses utf8 as this
predefined character set, as does MySQL 4.1 and up.
NVARCHAR is shorthand for NATIONAL VARCHAR.

Before [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-102), all MariaDB [collations](/kb/en/character-sets/) were of type `PADSPACE`, meaning that VARCHAR (as well as [CHAR](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/charset-narrowing-optimization.md) and [TEXT](text.md) values) are compared without regard for trailing spaces. This does not apply to the [LIKE](../../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/like.md) pattern-matching operator, which takes into account trailing spaces. From [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-102), a number of [NO PAD collations](character-sets/supported-character-sets-and-collations.md#no-pad-collations) are available.

If a unique index consists of a column where trailing pad characters are stripped or ignored, inserts into that column where values differ only by the number of trailing pad characters will result in a duplicate-key error.

#

# Examples

The following are equivalent:

```
VARCHAR(30) CHARACTER SET utf8
NATIONAL VARCHAR(30)
NVARCHAR(30)
NCHAR VARCHAR(30)
NATIONAL CHARACTER VARYING(30)
NATIONAL CHAR VARYING(30)
```

Trailing spaces:

```
CREATE TABLE strtest (v VARCHAR(10));
INSERT INTO strtest VALUES('Maria ');

SELECT v='Maria',v='Maria ' FROM strtest;
+-----------+--------------+
| v='Maria' | v='Maria ' |
+-----------+--------------+
| 1 | 1 |
+-----------+--------------+

SELECT v LIKE 'Maria',v LIKE 'Maria ' FROM strtest;
+----------------+-------------------+
| v LIKE 'Maria' | v LIKE 'Maria ' |
+----------------+-------------------+
| 0 | 1 |
+----------------+-------------------+
```

#

# Truncation

* Depending on whether or not [strict sql mode](../../../server-management/variables-and-modes/sql-mode.md#strict-mode) is set, you will either get a warning or an error if you try to insert a string that is too long into a VARCHAR column. If the extra characters are spaces, the spaces that can't fit will be removed and you will always get a warning, regardless of the [sql mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/sql_modemssql) setting.

#

# Difference Between VARCHAR and [TEXT](text.md)

* VARCHAR columns can be fully indexed. [TEXT](text.md) columns can only be indexed over a specified length.
* Using [TEXT](text.md) or [BLOB](blob.md) in a [SELECT](../../../server-usage/replication-cluster-multi-master/standard-replication/selectively-skipping-replication-of-binlog-events.md) query that uses temporary tables for storing intermediate results will force the temporary table to be disk based (using the [Aria storage engine](../../storage-engines/aria/aria-storage-engine.md) instead of the [memory storage engine](../../storage-engines/memory-storage-engine.md), which is a bit slower. This is not that bad as the [Aria storage engine](../../storage-engines/aria/aria-storage-engine.md) caches the rows in memory. To get the benefit of this, one should ensure that the [aria_pagecache_buffer_size](../../storage-engines/aria/aria-system-variables.md#aria_pagecache_buffer_size) variable is big enough to hold most of the row and index data for temporary tables.

#

# Oracle Mode

In [Oracle mode from MariaDB 10.3](/kb/en/sql_modeoracle-from-mariadb-103/#synonyms-for-basic-sql-types), `VARCHAR2` is a synonym.

#

## For Storage Engine Developers

* Internally the full length of the VARCHAR column is allocated inside each TABLE objects record[] structure. As there are three such buffers, each open table will allocate 3 times max-length-to-store-varchar bytes of memory.
* [TEXT](text.md) and [BLOB](blob.md) columns are stored with a pointer (4 or 8 bytes) + a 1-4 bytes length. The [TEXT](text.md) data is only stored once. This means that internally `TEXT` uses less memory for each open table but instead has the additional overhead that each `TEXT` object needs to be allocated and freed for each row access (with some caching in between).

#

# See Also

* [VARBINARY](varbinary.md)
* [TEXT](text.md)
* [CHAR](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/charset-narrowing-optimization.md)
* [Character Sets and Collations](/kb/en/data-types-character-sets-and-collations/)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)
* [Oracle mode from MariaDB 10.3](/kb/en/sql_modeoracle-from-mariadb-103/#synonyms-for-basic-sql-types)