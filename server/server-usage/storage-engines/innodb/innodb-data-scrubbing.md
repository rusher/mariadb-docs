# InnoDB Data Scrubbing

Note that most of the background and redo log scrubbing code has been removed in [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes). See [MDEV-15528](https://jira.mariadb.org/browse/MDEV-15528) and [MDEV-21870](https://jira.mariadb.org/browse/MDEV-21870).

Sometimes there is a requirement that when some data is deleted, it is really gone. This might be the case when one stores user's personal information or some other sensitive data. Normally though, when a row is deleted, the space is only marked as free on the page. It may eventually be overwritten, but there is no guarantee when that will happen. A copy of the deleted rows may also be present in the log files.

[MariaDB 10.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-3-release-notes) introduced support for [InnoDB](./) data scrubbing. Background threads periodically scan tablespaces and logs and remove all data that should be deleted. The number of background threads for tablespace scans is set by [innodb-encryption-threads](innodb-system-variables.md). Log scrubbing happens in a separate thread.

To configure scrubbing one can use the following variables:

|                                                                                                                       |           |                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [innodb-background-scrub-data-check-interval](innodb-system-variables.md#innodb_background_scrub_data_check_interval) | Seconds   | Check at this intervall if tablespaces needs scrubbing. Deprecated and ignored from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes).                 |
| [innodb-background-scrub-data-compressed](innodb-system-variables.md#innodb_background_scrub_data_compressed)         | Boolean   | Enable scrubbing of compressed data by background threads. Deprecated and ignored from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes).              |
| [innodb-background-scrub-data-interval](innodb-system-variables.md#innodb_background_scrub_data_interval)             | Seconds   | Scrub spaces that were last scrubbed longer than this many seconds ago. Deprecated and ignored from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes). |
| [innodb-background-scrub-data-uncompressed](innodb-system-variables.md#innodb_background_scrub_data_uncompressed)     | Boolean   | Enable scrubbing of uncompressed data by background threads. Deprecated and ignored from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes).            |
| [innodb-immediate-scrub-data-uncompressed](innodb-system-variables.md#innodb_immediate_scrub_data_uncompressed)       | Boolean   | Enable scrubbing of uncompressed data                                                                                                                                                                                                                       |
| [innodb-scrub-log](innodb-system-variables.md#innodb_scrub_log)                                                       | Boolean   | Enable redo log scrubbing. Deprecated and ignored from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes).                                              |
| [innodb-scrub-log-speed](innodb-system-variables.md#innodb_scrub_log_speed)                                           | Bytes/sec | Redo log scrubbing speed in bytes/sec. Deprecated and ignored from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes).                                  |

Redo log scrubbing did not fully work as intended, and was deprecated and ignored in [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes) ([MDEV-21870](https://jira.mariadb.org/browse/MDEV-21870)). If old log contents should be kept secret, then enabling [innodb\_encrypt\_log](innodb-system-variables.md#innodb_encrypt_log) or setting a smaller [innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size) could help.

The [Information Schema INNODB\_TABLESPACES\_SCRUBBING table](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_tablespaces_scrubbing-table.md) contains scrubbing information.

## Thanks

* Scrubbing was donated to the MariaDB project by Google.

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
