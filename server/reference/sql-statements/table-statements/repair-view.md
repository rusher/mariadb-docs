# REPAIR VIEW

## Syntax

```
REPAIR [NO_WRITE_TO_BINLOG | LOCAL] VIEW  view_name[, view_name] ... [FROM MYSQL]
```

## Description

The `REPAIR VIEW` statement was introduced to assist with fixing [MDEV-6916](https://jira.mariadb.org/browse/MDEV-6916), an issue introduced in [MariaDB 5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2) where the view algorithms were swapped compared to their MySQL on disk representation. It checks whether the view algorithm is correct. It is run as part of [mariadb-upgrade](../../../clients-and-utilities/mariadb-upgrade.md), and should not normally be required in regular use.

By default it corrects the checksum and if necessary adds the mariadb-version field. If the optional `FROM MYSQL` clause is used, and no mariadb-version field is present, the MERGE and TEMPTABLE algorithms are toggled.

By default, `REPAIR VIEW` statements are written to the [binary log](../../../server-management/server-monitoring-logs/binary-log/) and will be [replicated](broken-reference). The `NO_WRITE_TO_BINLOG` keyword (`LOCAL` is an alias) will ensure the statement is not written to the binary log.

## See Also

* [CHECK VIEW](check-view.md)

CC BY-SA / Gnu FDL
