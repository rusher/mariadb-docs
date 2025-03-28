# LONGBLOB

#

# Syntax

```
LONGBLOB
```

#

# Description

A [BLOB](blob.md) column with a 
maximum length of 4,294,967,295 bytes or 4GB (232 - 1). The effective maximum length of LONGBLOB columns depends on the
configured maximum packet size in the client/server protocol and
available memory. Each LONGBLOB value is stored using a four-byte
length prefix that indicates the number of bytes in the value.

#

## Oracle Mode

In [Oracle mode from MariaDB 10.3](/kb/en/sql_modeoracle-from-mariadb-103/#synonyms-for-basic-sql-types), `BLOB` is a synonym for `LONGBLOB`.

#

# See Also

* [BLOB](blob.md)
* [BLOB and TEXT Data Types](blob-and-text-data-types.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)
* [Oracle mode from MariaDB 10.3](/kb/en/sql_modeoracle-from-mariadb-103/#synonyms-for-basic-sql-types)