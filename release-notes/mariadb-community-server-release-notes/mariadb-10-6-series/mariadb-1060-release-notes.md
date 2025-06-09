# MariaDB 10.6.0 Release Notes

The most recent release of [MariaDB 10.6](what-is-mariadb-106.md) is:[**MariaDB 10.6.21**](mariadb-10-6-21-release-notes.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.6.21/)

[Download 10.6.0](https://downloads.mariadb.org/mariadb/10.6.0/)[Release Notes](mariadb-1060-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-106-series/mariadb-1060-changelog.md)[Overview of 10.6](what-is-mariadb-106.md)

**Release date:** 26 Apr 2021

[MariaDB 10.6](what-is-mariadb-106.md) is the current development series of MariaDB. It is an evolution\
of [MariaDB 10.5](../mariadb-10-5-series/what-is-mariadb-105.md) with several entirely new features.

[MariaDB 10.6.0](mariadb-1060-release-notes.md) is an [_**Alpha**_](../../mariadb-release-criteria.md) release.

**Do not use&#x20;**_**alpha**_**&#x20;releases in production!**

**For an overview of** [**MariaDB 10.6**](what-is-mariadb-106.md) **see the**[**What is MariaDB 10.6?**](what-is-mariadb-106.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

This is the first alpha release in the [MariaDB 10.6](what-is-mariadb-106.md) series.

Notable changes of this release include:

### SQL Syntax

* [Indexes can be ignored](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-indexes/ignored-indexes) ([MDEV-7317](https://jira.mariadb.org/browse/MDEV-7317))
* Implement SQL-standard [SELECT ... OFFSET ... FETCH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select-offset-fetch) ([MDEV-23908](https://jira.mariadb.org/browse/MDEV-23908))
* Add [SELECT ... SKIP LOCKED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select#skip-locked) syntax (InnoDB only) ([MDEV-13115](https://jira.mariadb.org/browse/MDEV-13115))
* [JSON\_TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_table), used to extract JSON data based on a JSON path expression and to return it as a relational table ([MDEV-17399](https://jira.mariadb.org/browse/MDEV-17399))

#### Oracle Compatibility

* Anonymous [subqueries in a FROM clause](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/subqueries/subqueries-in-a-from-clause-derived-tables) (no AS clause) are permitted in [ORACLE mode](broken-reference)

### Storage Engines

* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/tokudb) has been removed ([MDEV-19780](https://jira.mariadb.org/browse/MDEV-19780))
* [CassandraSE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/cassandra) has been removed ([MDEV-23024](https://jira.mariadb.org/browse/MDEV-23024))

### InnoDB

* Optimization to speed up inserts into an empty table ([MDEV-515](https://jira.mariadb.org/browse/MDEV-515))
* Make [InnoDB's COMPRESSED row format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-row-formats/innodb-compressed-row-format) [read-only by default](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-row-formats/innodb-compressed-row-format#read-only) ([MDEV-23497](https://jira.mariadb.org/browse/MDEV-23497))
* [Information Schema SYS\_TABLESPACES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tablespaces-table) now directly reflects the filesystem, and [SYS\_DATAFILES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_datafiles-table) has been removed ([MDEV-22343](https://jira.mariadb.org/browse/MDEV-22343))
* `innodb_flush_method=O_DIRECT` is enabled by default ([MDEV-24854](https://jira.mariadb.org/browse/MDEV-24854)), and `liburing` replaces `libaio` on recent Linux kernels ([MDEV-24883](https://jira.mariadb.org/browse/MDEV-24883)).
* The InnoDB transaction deadlock reporter was improved ([MDEV-24738](https://jira.mariadb.org/browse/MDEV-24738)).
* The old [MariaDB 5.5](broken-reference)-compatible `innodb` checksum is no longer supported, only `crc32` and `full_crc32`. Removed the `*innodb` and `*none` options from [innodb\_checksum\_algorithm](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_checksum_algorithm), and the `--strict-check`/`-C` and `--write`/`-w` options from [innochecksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/innochecksum) ([MDEV-25105](https://jira.mariadb.org/browse/MDEV-25105))

### Replication, Galera and Binlog

* Increase [master\_host](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to#master_host) limit to 255, user to 128 ([MDEV-24312](https://jira.mariadb.org/browse/MDEV-24312))
* The [wsrep\_mode](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_mode) system variable, for turning on WSREP features which are not part of default behavior (including the experimental Aria replication) ([MDEV-20008](https://jira.mariadb.org/browse/MDEV-20008), [MDEV-20715](https://jira.mariadb.org/browse/MDEV-20715), [MDEV-24946](https://jira.mariadb.org/browse/MDEV-24946))

### Sys Schema

* Bundle [sys-schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/sys-schema), a collection of views, functions and procedures to help administrators get insight into database usage. ([MDEV-9077](https://jira.mariadb.org/browse/MDEV-9077))

### Performance Schema

* Merged replication instrumentation and tables ([MDEV-16437](https://jira.mariadb.org/browse/MDEV-16437), [MDEV-20220](https://jira.mariadb.org/browse/MDEV-20220))

### General

* Do not resend unchanged resultset metadata for prepared statements ([MDEV-19237](https://jira.mariadb.org/browse/MDEV-19237))
* [--bind-address=hostname](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#bind_address) now listens on both IPv6 and IPv4 addresses ([MDEV-6536](https://jira.mariadb.org/browse/MDEV-6536))
* Support systemd socket activation ([MDEV-5536](https://jira.mariadb.org/browse/MDEV-5536))
* For the [GSSAPI plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi), support AD or local group name, and SIDs on Windows ([MDEV-23959](https://jira.mariadb.org/browse/MDEV-23959))
* Check for $MARIADB\_HOME/my.cnf ([MDEV-21365](https://jira.mariadb.org/browse/MDEV-21365))
* [max\_recursive\_iterations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#max_recursive_iterations) has been reduced to 1000 ([MDEV-17239](https://jira.mariadb.org/browse/MDEV-17239))
* Setting system variables to negative values will no longer set them to the maximum value ([MDEV-22219](https://jira.mariadb.org/browse/MDEV-22219))

### Galera

* [wsrep\_mode](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_mode) variable for turning on WSREP features which are not part of default behavior.
* [wsrep\_strict\_ddl](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_strict_ddl) has been deprecated. Use [wsrep\_mode=STRICT\_REPLICATION](mariadb-1060-release-notes.md#wsrep_mode) instead.

### InnoDB Variables

The following deprecated variables have been removed ([MDEV-23397](https://jira.mariadb.org/browse/MDEV-23397)):

* [innodb\_adaptive\_max\_sleep\_delay](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_adaptive_max_sleep_delay)
* [innodb\_background\_scrub\_data\_check\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_background_scrub_data_check_interval)
* [innodb\_background\_scrub\_data\_compressed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_background_scrub_data_compressed)
* [innodb\_background\_scrub\_data\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_background_scrub_data_interval)
* [innodb\_background\_scrub\_data\_uncompressed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_background_scrub_data_uncompressed)
* [innodb\_buffer\_pool\_instances](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_instances)
* [innodb\_commit\_concurrency](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_commit_concurrency)
* [innodb\_concurrency\_tickets](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_concurrency_tickets)
* [innodb\_file\_format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_file_format)
* [innodb\_large\_prefix](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_large_prefix)
* [innodb\_log\_checksums](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_checksums)
* [innodb\_log\_compressed\_pages](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_compressed_pages)
* [innodb\_log\_files\_in\_group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_files_in_group)
* [innodb\_log\_optimize\_ddl](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_optimize_ddl)
* [innodb\_page\_cleaners](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_page_cleaners)
* [innodb\_replication\_delay](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_replication_delay)
* [innodb\_scrub\_log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_scrub_log)
* [innodb\_scrub\_log\_speed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_scrub_log_speed)
* [innodb\_thread\_concurrency](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_thread_concurrency)
* [innodb\_thread\_sleep\_delay](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_thread_sleep_delay)
* [innodb\_undo\_logs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_undo_logs)

## Changelog

For a complete list of changes made in [MariaDB 10.6.0](mariadb-1060-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-106-series/mariadb-1060-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.6.0](mariadb-1060-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-6-0-now-available/).

**Do not use&#x20;**_**alpha**_**&#x20;releases in production!**

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
