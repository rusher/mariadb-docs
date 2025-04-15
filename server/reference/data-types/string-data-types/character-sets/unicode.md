
# Unicode

Unicode is a standard for encoding text across multiple writing systems. MariaDB supports a number of [character sets](README.md) for storing Unicode data:



| Character Set | Description |
| --- | --- |
| Character Set | Description |
| ucs2 | UCS-2, each character is represented by a 2-byte code with the most significant byte first. Fixed-length 16-bit encoding. |
| utf8 | Until [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), this was a UTF-8 encoding using one to three bytes per character. Basic Latin letters, numbers and punctuation use one byte. European and Middle East letters mostly fit into 2 bytes. Korean, Chinese, and Japanese ideographs use 3-bytes. No supplementary characters are stored. From [MariaDB 10.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md), utf8 is an alias for utf8mb3, but this can changed to ut8mb4 by changing the default value of the [old_mode](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old_mode) system variable. From [MariaDB 11.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md), utf8 is an alias for utf8mb4. |
| utf8mb3 | UTF-8 encoding using one to three bytes per character. Basic Latin letters, numbers and punctuation use one byte. European and Middle East letters mostly fit into 2 bytes. Korean, Chinese, and Japanese ideographs use 3-bytes. No supplementary characters are stored. Until [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), this was an alias for utf8. From [MariaDB 10.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md), utf8 is by default an alias for utf8mb3, but this can changed to ut8mb4 by changing the default value of the [old_mode](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old_mode) system variable. |
| utf8mb4 | UTF-8 encoding the same as utf8mb3 but which stores supplementary characters in four bytes. |
| utf16 | UTF-16, same as ucs2, but stores supplementary characters in 32 bits. 16 or 32-bits. |
| utf32 | UTF-32, fixed-length 32-bit encoding. |



Support for the UCA-14.0.0 collations was added in [MariaDB 10.10](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md) ([MDEV-27009](https://jira.mariadb.org/browse/MDEV-27009)) .


Support for the MySQL 8.0 UCA-9-0-0 (utf8mb4_0900_...) collations will be added to [MariaDB 11.4.5](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-4-series/mariadb-11-4-5-release-notes.md)

