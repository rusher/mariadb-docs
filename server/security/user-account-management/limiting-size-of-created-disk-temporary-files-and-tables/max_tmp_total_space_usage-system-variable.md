
# max_tmp_total_space_usage System Variable

#### `<code>max_tmp_total_space_usage</code>`


* Description: The maximum total size in bytes of all temporary file and temporary table usage over all connections. A value of 0 disables this feature. Set in blocks of 65536, rounded down if not a multiple of 65536. See [Limiting Size of Created Disk Temporary Files and Tables Overview](limiting-size-of-created-disk-temporary-files-and-tables-overview.md) for details. Called max_total_tmp_space_usage in [MariaDB 11.5.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-0-release-notes.md) only.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--max-tmp-total-space-usage=num</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>` (bigint unsigned)
* Default Value: `<code>1099511627776</code>`
* Range: `<code>0</code>` to `<code>18446744073709551615</code>` (blocks of `<code>65536</code>`)
* Introduced: [MariaDB 11.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-115.md)


