# MariaDB Connector/C 2.3.4 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-c/2.3.4)[Release Notes](mariadb-connector-c-234-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-23-changelogs/mariadb-connector-c-234-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 4 Dec 2017

This is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of the MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Notable Bug Fixes

* [CONC-282](https://jira.mariadb.org/browse/CONC-282): Connector/C now provides additional information on the package version: `mariadb_config --cc_version` lists the package version. Besides `MARIADB_PACKAGE_VERSION`, the numeric representation `MARIADB_PACKAGE_VERSION_ID` can now be used within preprocessor directives.
* [CONC-281](https://jira.mariadb.org/browse/CONC-281): `mysql_stmt_fetch_column` doesn't work with prior call to `mysql_stmt_store_result`
* OpenSSL fixes:
  * When negotiating TLS protocol during handshake, use server preferences instead of client preferences. This will allow using TLSv12 (OpenSSL server) and/or TLSv1.1 (Yassl server).
  * Don't check server ca unless verification flag was set. This will allow Connector/C to establish a tls/ssl connection without certificates.

For a list of changes made in this release, with links to detailed\
information on each push, see the[changelog](../changelogs/mariadb-connector-c-23-changelogs/mariadb-connector-c-234-changelog.md).

{% include "https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/~/reusable/vX1KAy0t1XuYJaGsK28T/" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
