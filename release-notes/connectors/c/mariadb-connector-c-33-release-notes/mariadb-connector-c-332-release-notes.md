# MariaDB Connector/C 3.3.2 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://mariadb.com/downloads/connectors)[Release Notes](mariadb-connector-c-332-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-33-changelogs/mariadb-connector-c-332-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 22 Aug 2022

This is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release of MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Notable changes

* [CONC-598](https://jira.mariadb.org/browse/CONC-598): Callback support for status and session\_tracking

## Bugs fixed

* [CONC-600](https://jira.mariadb.org/browse/CONC-600): Ignore unknown events in replication/binlog API
* [CONC-601](https://jira.mariadb.org/browse/CONC-601): Fixed build for MacOS when using bundled zlib library.
* [CONC-602](https://jira.mariadb.org/browse/CONC-602): Fixed memory leak in non-blocking API. Kudos to Hyung Hwan who found this issue and provided a fix.
* [CONC-603](https://jira.mariadb.org/browse/CONC-603): Fixed error handling in TLS read/write
* [CONC-604](https://jira.mariadb.org/browse/CONC-604): Fixed crash when reconnecting via TLS
* [CONC-605](https://jira.mariadb.org/browse/CONC-605): Disable sigpipe errors for GnuTLS
* [CONC-606](https://jira.mariadb.org/browse/CONC-606): Replaced server error code constants in communication (ma\_net)
* [CONC-607](https://jira.mariadb.org/browse/CONC-607): Infinite loop in pvio\_socket\_internal\_connect(). Kudos to Hugo Wen who found this issue and provided a fix.

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-c-33-changelogs/mariadb-connector-c-332-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
