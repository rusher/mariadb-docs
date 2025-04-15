
# CRC32C


##### MariaDB starting with [10.8](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-108.md)
Introduced in [MariaDB 10.8.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes.md) to compute a cyclic redundancy check (CRC) value using the Castagnoli polynomial.


## Syntax


```
CRC32C([par,]expr)
```

## Description


MariaDB has always included a native unary function [CRC32()](crc32.md) that computes the CRC-32 of a string using the ISO 3309 polynomial that used by zlib and many others.


InnoDB and MyRocks use a different polynomial, which was implemented in SSE4.2 instructions that were introduced in the Intel Nehalem microarchitecture. This is commonly called CRC-32C (Castagnoli).


The CRC32C function uses the Castagnoli polynomial.


This allows `<code>SELECT…INTO DUMPFILE</code>` to be used for the creation of files with
valid checksums, such as a logically empty InnoDB redo log file
`<code>ib_logfile0</code>` corresponding to a particular log sequence number.


The optional parameter allows the checksum to be computed in pieces:
CRC32C('MariaDB')=CRC32C(CRC32C('Maria'),'DB').


## Examples


```
SELECT CRC32C('MariaDB');
+-------------------+
| CRC32C('MariaDB') |
+-------------------+
|         809606978 |
+-------------------+

SELECT CRC32C(CRC32C('Maria'),'DB');
+------------------------------+
| CRC32C(CRC32C('Maria'),'DB') |
+------------------------------+
|                    809606978 |
+------------------------------+
```
