
# max_tmp_session_space_usage System Variable

#### `max_tmp_session_space_usage`


* Description: The maximum total size of temporary file and temporary table usage. A value of 0 disables this feature. Set in blocks of 65536, rounded down if not a multiple of 65536. See [Limiting Size of Created Disk Temporary Files and Tables Overview](limiting-size-of-created-disk-temporary-files-and-tables-overview.md) for details. Named max_tmp_space_usage in [MariaDB 11.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-0-release-notes) only.
* Commandline: `--max-tmp-session-space-usage=num`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric` (bigint unsigned)
* Default Value: `1099511627776`
* Range: `0` to `18446744073709551615` (blocks of `65536`)
* Introduced: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115)


