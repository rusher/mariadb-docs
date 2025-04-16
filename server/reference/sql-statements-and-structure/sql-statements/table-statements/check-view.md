
# CHECK VIEW

## Syntax


```
CHECK VIEW view_name
```

## Description


The `CHECK VIEW` statement was introduced in [MariaDB 10.0.18](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10018-release-notes.md) to assist with fixing [MDEV-6916](https://jira.mariadb.org/browse/MDEV-6916), an issue introduced in [MariaDB 5.2](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md) where the view algorithms were swapped. It checks whether the view algorithm is correct. It is run as part of [mariadb-upgrade](../../../../clients-and-utilities/mariadb-upgrade.md), and should not normally be required in regular use.


## See Also


* [REPAIR VIEW](repair-view.md)

