# mariadb-binlog

`mariadb-binlog` is a utility included with MariaDB for processing [binary log](../../../server-management/server-monitoring-logs/binary-log/) and [relay log](../../../server-management/server-monitoring-logs/binary-log/relay-log.md) files.

The MariaDB server's binary log is a set of files containing "events" which\
represent modifications to the contents of a MariaDB database. These events are\
written in a binary (i.e. non-human-readable) format. The mariadb-binlog utility\
is used to view these events in plain text.

Prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/mariadb-10-5-series/what-is-mariadb-105), the client was called `mysqlbinlog`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.
