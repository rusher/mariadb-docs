# LONGTEXT

#

# Syntax

```
LONGTEXT [CHARACTER SET charset_name] [COLLATE collation_name]
```

#

# Description

A [TEXT](text.md) column with a maximum length of 4,294,967,295 or 4GB (`232 - 1`) characters. The effective maximum length is less if the value contains multi-byte characters. The effective maximum length of LONGTEXT columns also depends on the configured maximum packet size in the client/server protocol and available memory. Each LONGTEXT value is stored using a four-byte length prefix that indicates the number of bytes in the value.

From [MariaDB 10.2.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-102-series/mariadb-1027-release-notes), JSON is an alias for LONGTEXT. See [JSON Data Type](json-data-type.md) for details.

#

# Oracle Mode

In [Oracle mode from MariaDB 10.3](/kb/en/sql_modeoracle-from-mariadb-103/#synonyms-for-basic-sql-types), `CLOB` is a synonym for `LONGTEXT`.

#

# See Also

* [TEXT](text.md)
* [BLOB and TEXT Data Types](blob-and-text-data-types.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)
* [JSON Data Type](json-data-type.md)
* [Oracle mode from MariaDB 10.3](/kb/en/sql_modeoracle-from-mariadb-103/#synonyms-for-basic-sql-types)