# Connector/C 2.0.0 Release Notes

The most recent [_**Stable**_](../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-c/2.0.0)[Release Notes](mariadb-client-library-for-c-200-release-notes.md)[Changelog](changelogs/mariadb-client-library-for-c-200-changelog.md)[About MariaDB Connector/C](broken-reference)

**Release date:** 3 Apr 2014

This is a [_**Stable**_](../../mariadb-release-criteria.md) _**(GA)**_ release of the MariaDB\
Client Library for C. In general, marking this release as _stable_ means that\
there are no known serious bugs, except for those marked as feature requests,\
that no bugs were fixed since last release that caused a notable code changes,\
and that we believe the code is ready for general usage (based on bug inflow).

**For a description of this library see the**[**MariaDB Client Library for C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## New features:

* Support of SSL client/server connection: Compared to the MariaDB GPL client library this implementation uses a global (per library instance) SSL context which needs less memory and results in better performance.
* Read-a-head cache to reduce the system load and time.
* Added an additional experimental layer to communicate with other databases via plugins, e.g. Sqllite. This feature is disabled by default and not recommended for production use.
* Dynamic columns support via dynamic column API
* Support for utf16 character set
* Documentation, currently available in html format only
* Graphical installation wizard for Windows platforms (msi installer)
* compressed protocol support for large packets
* support for quoted values in configuration files
* character set auto detection
* Compiler support. MariaDB client library for C 2.0.0 will compile now also under mingw and Objective/C
* Performance schema support for connection attributes
* Added microseconds support for prepared statements:\
  datetime, timestamp and time to string conversion now return microsenconds
* Graphical installation wizard for Windows platforms (msi installer)
* IPV6 support
* allow old password authentication (pre 4.1 passwords)
* Support for connection timeout parameter on windows platforms
* New API functions:
  * mysql\_options\_v (for option calls which require multiple parameters). For compatibility to libmysql the function mysql\_options4 is defined as a macro.
  * mysql\_get\_parameters
  * mysql\_read\_query\_result
  * mysql\_stmt\_more\_results
  * mysql\_stmt\_next\_result
  * mysql\_ps\_fetch\_functions (was internal before,now it can be used by client applications e.g. ODBC to convert between different types)

## Bug fixes

MariaDB client library for C 2.0.0 contains about 80 bug fixes. For a complete\
list and description please check the[Jira bug system](https://jira.mariadb.org/browse/CONC-83?jql=project%20%3D%20CONC)

## Changelog

For a list of changes made in this release, with links to detailed\
information on each push, see the[changelog](changelogs/mariadb-client-library-for-c-200-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
