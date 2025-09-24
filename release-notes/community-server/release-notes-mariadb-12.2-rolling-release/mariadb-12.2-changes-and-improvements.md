# MariaDB 12.2 Changes & Improvements

{% hint style="info" %}
<p align="center">The most recent release of MariaDB 12.2 is:</p>

<h4 align="center"><strong>MariaDB 12.2.0</strong> Preview <a href="https://downloads.mariadb.org/mariadb/12.2.0/" class="button primary">Download Now</a></h4>

<p align="center"><a href="https://downloads.mariadb.org/mariadb/12.2.0/"><sub><em>Alternate download from mariadb.org</em></sub></a></p>
{% endhint %}

MariaDB 12.2 is a [rolling release](../about/release-model.md). It is an evolution of [MariaDB 12.1](../release-notes-mariadb-12.1-rolling-releases/changes-and-improvements-in-mariadb-12.1.md) with several entirely new features.

## New Features

### Compatibility features <a href="#compatibility-features" id="compatibility-features"></a>

* [Optimizer hint](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/optimizer-hints): \[NO\_]ROWID\_FILTER ([MDEV-36089](https://jira.mariadb.org/browse/MDEV-36089)),&#x20;
* [Optimizer hint](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/optimizer-hints): \[NO\_]INDEX\_MERGE ([MDEV-36125](https://jira.mariadb.org/browse/MDEV-36125))
* [Optimizer hints](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/optimizer-hints): Implicit query block names ([MDEV-37511](https://jira.mariadb.org/browse/MDEV-37511))
* sql\_mode="oracle" does not support TO\_NUMBER() function ([MDEV-20022](https://jira.mariadb.org/browse/MDEV-20022))
* Implement Oracle TRUNC() function ([MDEV-20023](https://jira.mariadb.org/browse/MDEV-20023))

### Miscellaneous <a href="#miscellaneous" id="miscellaneous"></a>

* Make JSON DEPTH unlimited ([MDEV-32854](https://jira.mariadb.org/browse/MDEV-32854))
* Implement Global temporary tables ([MDEV-35915](https://jira.mariadb.org/browse/MDEV-35915) I)
* improved support of replication between tables of different structure ([MDEV-36290](https://jira.mariadb.org/browse/MDEV-36290))
* Indexes on derived tables with GROUP BY produce wrong out\_rows estimates ([MDEV-36321](https://jira.mariadb.org/browse/MDEV-36321))
* INFORMATION\_SCHEMA.TRIGGERED\_UPDATE\_COLUMNS ([MDEV-36996](https://jira.mariadb.org/browse/MDEV-36996))
* Implement INFORMATION\_SCHEMA.PARAMETERS.PARAMETER\_DEFAULT column ([MDEV-37054](https://jira.mariadb.org/browse/MDEV-37054))

## List of All MariaDB 12.2 Releases

| Date        | Release        | Status  | Release Notes | Changelog |
| ----------- | -------------- | ------- | ------------- | --------- |
| 23 Sep 2025 | MariaDB 12.2.0 | Preview |               |           |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
