# MariaDB 10.9.0 Release Notes

The most recent release of [MariaDB 10.9](what-is-mariadb-109.md) is:[**MariaDB 10.9.8**](mariadb-10-9-8-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.9.8/)

[Download 10.9.0](https://downloads.mariadb.org/mariadb/10.9.0)[Release Notes](mariadb-1090-release-notes.md)[Changelog](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-1080-changelog/README.md)[Overview of 10.9](what-is-mariadb-109.md)

**Release date:** 23 March 2022

**Do not use&#x20;**_**alpha**_**&#x20;releases in production!**

[MariaDB 10.9](what-is-mariadb-109.md) is a current development series of MariaDB. It is an evolution\
of [MariaDB 10.8](../release-notes-mariadb-10-8-series/what-is-mariadb-108.md) with several entirely new features.

[MariaDB 10.9.0](mariadb-1090-release-notes.md) is not a single release, but is instead a number of preview releases based on feature branches. Each should be considered [_**Alpha**_](../../../mariadb-release-criteria.md).\
Read more about feature preview releases [here](https://mariadb.org/preview-releases/).

Thanks, and enjoy MariaDB!

Remember, these features are in separate _preview packages_. The subsection header text corresponds to the preview package name.

### JSON

* [JSON\_OVERLAPS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_overlaps) function ([MDEV-27677](https://jira.mariadb.org/browse/MDEV-27677))
* Implement range notation for [JSONPath](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/JSONPath_Expressions/README.md) ([MDEV-27911](https://jira.mariadb.org/browse/MDEV-27911))
* Support [JSONPath](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/JSONPath_Expressions/README.md) negative index ([MDEV-22224](https://jira.mariadb.org/browse/MDEV-22224))

### SHOW ANALYZE FORMAT=JSON

* Extend [SHOW EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-explain) to support \[SHOW ANALYZE [FORMAT=JSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-analyze)] ([MDEV-27021](https://jira.mariadb.org/browse/MDEV-27021))
* Add EXPLAIN FOR CONNECTION syntax support to [SHOW EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-explain) ([MDEV-10000](https://jira.mariadb.org/browse/MDEV-10000))

### Async redo log write

* Asynchronous [redo log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-redo-log) write ([MDEV-26603](https://jira.mariadb.org/browse/MDEV-26603)) (not included in [MariaDB 10.9.1](mariadb-1091-release-notes.md))

### Miscellaneous

* Implement the --do-domain-ids, --ignore-domain-ids, and --ignore-server-ids options for [mariadb-binlog/mysqlbinlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) ([MDEV-20119](https://jira.mariadb.org/browse/MDEV-20119))
* [information\_schema.tables.table\_type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-tables-table) now shows TEMPORARY for local temporary tables ([MDEV-12459](https://jira.mariadb.org/browse/MDEV-12459)) (not included in [MariaDB 10.9.1](mariadb-1091-release-notes.md))
* Merge [old](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#old) to [old\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#old_mode) sql variable ([MDEV-24920](https://jira.mariadb.org/browse/MDEV-24920))
* [Hashicorp Key Management Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin) for implementing [encryption](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption) using keys stored in the Hashicorp Vault KMS ([MDEV-19281](https://jira.mariadb.org/browse/MDEV-19281))
* JSON file interface to wsrep node state / SST progress logging ([MDEV-26971](https://jira.mariadb.org/browse/MDEV-26971))
* Allow [innodb\_log\_file\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_file_size) to change without server restart ([MDEV-27812](https://jira.mariadb.org/browse/MDEV-27812))

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
