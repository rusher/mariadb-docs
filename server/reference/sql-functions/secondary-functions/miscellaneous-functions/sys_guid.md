# SYS\_GUID

**MariaDB starting with** [**10.6.1**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1061-release-notes)

The SYS\_GUID function was introduced in [MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1061-release-notes) to enhance Oracle compatibility. Similar functionality can be achieved with the [UUID](uuid.md) function.

## Syntax

```
SYS_GUID()
```

## Description

Returns a 16-byte globally unique identifier (GUID), similar to the [UUID](uuid.md) function, but without the `-` character.

## Example

```
SELECT SYS_GUID();
+----------------------------------+
| SYS_GUID()                       |
+----------------------------------+
| 2C574E45BA2811EBB265F859713E4BE4 |
+----------------------------------+
```

## See Also

* [UUID](uuid.md)
* [UUID\_SHORT](uuid_short.md)
* [UUID data type](../../../data-types/string-data-types/uuid-data-type.md)

CC BY-SA / Gnu FDL
