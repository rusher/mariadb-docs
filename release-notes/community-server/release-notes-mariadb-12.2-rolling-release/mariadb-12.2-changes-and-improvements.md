# MariaDB 12.2 Changes & Improvements

{% include "../../.gitbook/includes/latest-12-2.md" %}

MariaDB 12.2 is a [rolling release](../about/release-model.md). It is an evolution of [MariaDB 12.1](../release-notes-mariadb-12.1-rolling-releases/changes-and-improvements-in-mariadb-12.1.md) with several entirely new features.

## New Features

### Compatibility features <a href="#compatibility-features" id="compatibility-features"></a>

* [Optimizer hint](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/optimizer-hints): \[NO\_]ROWID\_FILTER ([MDEV-36089](https://jira.mariadb.org/browse/MDEV-36089)),&#x20;
* [Optimizer hint](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/optimizer-hints): \[NO\_]INDEX\_MERGE ([MDEV-36125](https://jira.mariadb.org/browse/MDEV-36125))
* [Optimizer hints](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/optimizer-hints): Implicit query block names ([MDEV-37511](https://jira.mariadb.org/browse/MDEV-37511))
* Implement Oracle [TO\_NUMBER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/to_number) function ([MDEV-20022](https://jira.mariadb.org/browse/MDEV-20022))
* Implement Oracle [TRUNC](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/trunc) function ([MDEV-20023](https://jira.mariadb.org/browse/MDEV-20023))

### Miscellaneous <a href="#miscellaneous" id="miscellaneous"></a>

* Remove depth limit of 32 from JSON functions ([MDEV-32854](https://jira.mariadb.org/browse/MDEV-32854))
* Implement Global temporary tables ([MDEV-35915](https://jira.mariadb.org/browse/MDEV-35915) I)
* improved support of replication between tables of different structure ([MDEV-36290](https://jira.mariadb.org/browse/MDEV-36290))
* Indexes on derived tables with GROUP BY produce wrong out\_rows estimates ([MDEV-36321](https://jira.mariadb.org/browse/MDEV-36321))
* Add [INFORMATION\_SCHEMA.TRIGGERED\_UPDATE\_COLUMNS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-triggered_update_columns) ([MDEV-36996](https://jira.mariadb.org/browse/MDEV-36996))
* Implement [INFORMATION\_SCHEMA.PARAMETERS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-parameters-table).PARAMETER\_DEFAULT column ([MDEV-37054](https://jira.mariadb.org/browse/MDEV-37054))

## List of All MariaDB 12.2 Releases

| Date        | Release              | Status  | Release Notes | Changelog |
| ----------- | -------------------- | ------- | ------------- | --------- |
| 23 Sep 2025 | MariaDB 12.2 Preview | Preview |               |           |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
