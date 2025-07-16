# MariaDB 12.0 Changes & Improvements

MariaDB 12.0 is a [rolling release](../../mariadb-release-model.md). It is an evolution of [MariaDB 11.8](../mariadb-11-8-series/what-is-mariadb-118.md) with several entirely new features.

## New Features

### Security <a href="#security" id="security"></a>

* Support for passphrase protected keys ([MDEV-14091](https://jira.mariadb.org/browse/MDEV-14091))
* New statement [SET SESSION AUTHORIZATION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/set-session-authorization) for performing actions as another user ([MDEV-20299](https://jira.mariadb.org/browse/MDEV-20299))
* Implement SHA2 support for file\_key\_management.so plugin (TDE) ([MDEV-34712](https://jira.mariadb.org/browse/MDEV-34712))

### Data types <a href="#data-types" id="data-types"></a>

* Comparison [ROW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/row)(stored\_func(),1)=ROW(1,1) erroneously called stored\_func() twice per row. It led to a performance degradation, as well as to a double execution of the possible stored function side effects. ([MDEV-36322](https://jira.mariadb.org/browse/MDEV-36322))

### Stored Routines <a href="#stored-routines" id="stored-routines"></a>

* Add support for the pre-defined weak SYS\_REFCURSOR ([MDEV-20034](https://jira.mariadb.org/browse/MDEV-20034))

### Server <a href="#server" id="server"></a>

* Add the FM format to [TO\_CHAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/to_char), which suppresses following padding ([MDEV-36216](https://jira.mariadb.org/browse/MDEV-36216))
* [mariadb-check](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/table-tools/mariadb-check) and [CHECK TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/check-table) now support [SEQUENCE tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/sequence-storage-engine) ([MDEV-22491](https://jira.mariadb.org/browse/MDEV-22491))

### Optimizer <a href="#optimizer" id="optimizer"></a>

* find\_order\_in\_list mismatch when order item needs fixing() ([MDEV-36607](https://jira.mariadb.org/browse/MDEV-36607))
* If the join\_condition is specified via USING (column\_list), the query plan depends on the sequence of tables in the query ([MDEV-36592](https://jira.mariadb.org/browse/MDEV-36592))
* Add support for optimizer hints ([MDEV-35504](https://jira.mariadb.org/browse/MDEV-35504))
  * QB\_NAME()
  * NO\_RANGE\_OPTIMIZATION()
  * NO\_ICP()
  * MRR(), NO\_MRR()
  * BKA(), NO\_BKA()
  * BNL(), NO\_BNL()
* Add support for subquery optimizer hints ([MDEV-34888](https://jira.mariadb.org/browse/MDEV-34888))
  * SEMIJOIN()
  * SUBQUERY()
* Add support for join order hints ([MDEV-34870](https://jira.mariadb.org/browse/MDEV-34870))
  * JOIN\_FIXED\_ORDER similar to existing STRAIGHT\_JOIN hint
  * JOIN\_ORDER to apply the specified table order
  * JOIN\_PREFIX to hint what tables should be first in the join
  * JOIN\_SUFFIX to hint what tables should be last in the join
* Add support for the MAX\_EXECUTION\_TIME hint ([MDEV-34860](https://jira.mariadb.org/browse/MDEV-34860))

### GIS <a href="#gis" id="gis"></a>

New [GIS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/geometry/gis-features-in-533) functions. These functions improve compatibility with MySQL 8.

* [ST\_Validate](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_validate) ([MDEV-34137](https://jira.mariadb.org/browse/MDEV-34137))
* [MBRCoveredBy](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/mbr-minimum-bounding-rectangle/mbrcoveredby) ([MDEV-34138](https://jira.mariadb.org/browse/MDEV-34138))
* [ST\_Simplify](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_simplify) ([MDEV-34141](https://jira.mariadb.org/browse/MDEV-34141))
* [ST\_GeoHash](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_geohash) ([MDEV-34158](https://jira.mariadb.org/browse/MDEV-34158))
* [ST\_LatFromGeoHash](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_latfromgeohash) ([MDEV-34159](https://jira.mariadb.org/browse/MDEV-34159))
* [ST\_LongFromGeoHash](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_longfromgeohash) ([MDEV-34160](https://jira.mariadb.org/browse/MDEV-34160))
* [ST\_PointFromGeoHash](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_pointfromgeohash) ([MDEV-34277](https://jira.mariadb.org/browse/MDEV-34277))
* [ST\_IsValid](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_isvalid) ([MDEV-34276](https://jira.mariadb.org/browse/MDEV-34276))
* [ST\_Collect](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_collect) ([MDEV-34278](https://jira.mariadb.org/browse/MDEV-34278))

### Trigger <a href="#trigger" id="trigger"></a>

* Add support for TRIGGERS that fire on multiple events ([MDEV-10164](https://jira.mariadb.org/browse/MDEV-10164))

### Replication <a href="#replication" id="replication"></a>

* Server displays if it was started with the [skip-slave-start](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options#skip-slave-start) option ([MDEV-27669](https://jira.mariadb.org/browse/MDEV-27669))

### Galera <a href="#galera" id="galera"></a>

* Skip FK checks in Galera during applying in IST ([MDEV-34822](https://jira.mariadb.org/browse/MDEV-34822))

### Audit Plugin <a href="#audit-plugin" id="audit-plugin"></a>

* Log HOST:PORT of incoming connection instead of just the host ([MDEV-1282](https://jira.mariadb.org/browse/MDEV-1282))
* Add tls\_version field for connection audit plugins ([MDEV-33834](https://jira.mariadb.org/browse/MDEV-33834))

### Configuration <a href="#configuration" id="configuration"></a>

* Get option group suffix from $MARIADB\_GROUP\_SUFFIX in addition to $MYSQL\_GROUP\_SUFFIX ([MDEV-21375](https://jira.mariadb.org/browse/MDEV-21375))

### mariadb Client

* Can set an alternative directory path for searching scripts invoked via the source command, with the [--script-dir](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mariadb-command-line-client#-script-dir) mariadb client option ([MDEV-23818](https://jira.mariadb.org/browse/MDEV-23818))

## List of All MariaDB 12.0 Releases

| Date        | Release                                           | Status  | Release Notes                                    | Changelog                                                                             |
| ----------- | ------------------------------------------------- | ------- | ------------------------------------------------ | ------------------------------------------------------------------------------------- |
| 5 Jun 2025  | [MariaDB 12.0.1](mariadb-12.0.1-release-notes.md) | RC      | [Release Notes](mariadb-12.0.1-release-notes.md) | [Changelog](../changelogs/changelogs-mariadb-12.0-series/mariadb-12.0.1-changelog.md) |
| 26 May 2025 | MariaDB 12.0.0                                    | Preview |                                                  |                                                                                       |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
