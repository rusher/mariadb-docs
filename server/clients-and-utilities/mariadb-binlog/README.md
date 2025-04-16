
# mariadb-binlog

`mariadb-binlog` is a utility included with MariaDB for processing [binary log](../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) and [relay log](../../server-management/server-monitoring-logs/binary-log/relay-log.md) files.


The MariaDB server's binary log is a set of files containing "events" which
represent modifications to the contents of a MariaDB database. These events are
written in a binary (i.e. non-human-readable) format. The mariadb-binlog utility
is used to view these events in plain text.


Prior to [MariaDB 10.5](../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), the client was called `mysqlbinlog`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.

<span></span>
