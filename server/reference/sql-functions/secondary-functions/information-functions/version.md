# VERSION

## Syntax

```
VERSION()
```

## Description

Returns a string that indicates the MariaDB server version. The string\
uses the utf8 [character set](../../../data-types/string-data-types/character-sets/).

## Examples

```
SELECT VERSION();
+----------------+
| VERSION()      |
+----------------+
| 10.4.7-MariaDB |
+----------------+
```

The `VERSION()` string may have one or more of the following suffixes:

| Suffix    | Description                                                               |
| --------- | ------------------------------------------------------------------------- |
| Suffix    | Description                                                               |
| -embedded | The server is an embedded server (libmariadbd).                           |
| -log      | General logging, slow logging or binary (replication) logging is enabled. |
| -debug    | The server is compiled for debugging.                                     |
| -valgrind | The server is compiled to be instrumented with valgrind.                  |

## Changing the Version String

Some old legacy code may break because they are parsing the`VERSION` string and expecting a MySQL string or a simple version\
string like Joomla til API17, see [MDEV-7780](https://jira.mariadb.org/browse/MDEV-7780).

One can fool these applications by setting the version string from the command line or the my.cnf files with [--version=...](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#version).

GPLv2 fill\_help\_tables.sql
