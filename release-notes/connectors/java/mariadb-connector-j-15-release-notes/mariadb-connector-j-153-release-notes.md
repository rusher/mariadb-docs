# MariaDB Connector/J 1.5.3 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/1.5.3/)[Release Notes](mariadb-connector-j-153-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-15-changelogs/mariadb-connector-j-153-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 4 Oct 2016

MariaDB Connector/J 1.5.3 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For a description of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

## Notable Changes

This version is a bug-fix release.

* [CONJ-358](https://jira.mariadb.org/browse/CONJ-358) : Permit using private key with password that differs from keyStore password
* [CONJ-356](https://jira.mariadb.org/browse/CONJ-356) : secure connection : use KeyStore private key and associate public keys certificates only
* [CONJ-342](https://jira.mariadb.org/browse/CONJ-342) : Empty clientCertificateKeyStoreUrl option correction
* [CONJ-353](https://jira.mariadb.org/browse/CONJ-353) : IBM jdk compatibility issue
* [CONJ-354](https://jira.mariadb.org/browse/CONJ-354) : Streaming issue when using procedures in PrepareStatement/Statement
* [CONJ-345](https://jira.mariadb.org/browse/CONJ-345) : Regression with using COLLATE keyword in PrepareStatement query
* [CONJ-352](https://jira.mariadb.org/browse/CONJ-352) : metadata correction on getPrecision() for numeric fields
* [CONJ-350](https://jira.mariadb.org/browse/CONJ-350) : make prepare fallback to client prepare if query cannot be prepare

New Option :

| keyPassword |
| ----------- |
| keyPassword |

Some options which names where confusing have been renamed (the old names still works):

| Old option name                   | new option name    | change                                                  |
| --------------------------------- | ------------------ | ------------------------------------------------------- |
| Old option name                   | new option name    | change                                                  |
| clientCertificateKeyStoreUrl      | keyStore           | like system property "javax.net.ssl.keyStore"           |
| clientCertificateKeyStorePassword | keyStorePassword   | like system property "javax.net.ssl.keyStorePassword"   |
| trustCertificateKeyStoreUrl       | trustStore         | like system property "javax.net.ssl.trustStore"         |
| trustCertificateKeyStorePassword  | trustStorePassword | like system property "javax.net.ssl.trustStorePassword" |

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
