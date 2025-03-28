# Information Schema DISKS Table

#

# Description

The `DISKS` table is created when the [DISKS](../../../../../../plugins/other-plugins/disks-plugin.md) plugin is enabled, and shows metadata about disks on the system.

Before [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-104-series/mariadb-1047-release-notes), [MariaDB 10.3.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10317-release-notes), [MariaDB 10.2.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-102-series/mariadb-10226-release-notes) and [MariaDB 10.1.41](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-101-series/mariadb-10141-release-notes), this plugin did **not** check [user privileges](../../../../account-management-sql-commands/grant.md). When it is enabled, **any** user can query the `INFORMATION_SCHEMA.DISKS` table and see all the information it provides.

Since [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-104-series/mariadb-1047-release-notes), [MariaDB 10.3.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10317-release-notes), [MariaDB 10.2.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-102-series/mariadb-10226-release-notes) and [MariaDB 10.1.41](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-101-series/mariadb-10141-release-notes), it requires the [FILE privilege](../../../../account-management-sql-commands/grant.md).

The plugin only works on Linux.

The table contains the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| DISK | Name of the disk itself. |
| PATH | Mount point of the disk. |
| TOTAL | Total space in KiB. |
| USED | Used amount of space in KiB. |
| AVAILABLE | Amount of space in KiB available to non-root users. |

Note that as the amount of space available to root (OS user) may be more that what is available to non-root users, 'available' + 'used' may be less than 'total'.

All paths to which a particular disk has been mounted are reported. The rationale is that someone might want to take different action e.g. depending on which disk is relevant for a particular path. This leads to the same disk being reported multiple times.

#

# Example

```
SELECT * FROM information_schema.DISKS;

+-----------+-------+----------+---------+-----------+
| Disk | Path | Total | Used | Available |
+-----------+-------+----------+---------+-----------+
| /dev/vda1 | / | 26203116 | 2178424 | 24024692 |
| /dev/vda1 | /boot | 26203116 | 2178424 | 24024692 |
| /dev/vda1 | /etc | 26203116 | 2178424 | 24024692 |
+-----------+-------+----------+---------+-----------+
```

#

# See Also

* [Disks Plugin](../../../../../../plugins/other-plugins/disks-plugin.md) for details on installing, options
* [Plugin Overview](../../../../../../plugins/plugin-overview.md) for details on managing plugins.