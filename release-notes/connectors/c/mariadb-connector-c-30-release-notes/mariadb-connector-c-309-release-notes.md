# MariaDB Connector/C 3.0.9 Release Notes

[Download](https://mariadb.com/downloads/?showall=1\&tab=connectors)[Release Notes](mariadb-connector-c-309-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-30-changelogs/mariadb-connector-c-309-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 11 Feb 2019

This is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of the MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Notable Bug fixes

* [CONC-384](https://jira.mariadb.org/browse/CONC-384): Incorrect packet when a connection attribute name or value is equal to or greater than 251
* [CONC-388](https://jira.mariadb.org/browse/CONC-388): field->def\_length is always set to 0 (only used by deprecated function mysql\_list\_fields).
* Getter should get and the setter should set CLIENT\_CAN\_HANDLE\_EXPIRED\_PASSWORDS (Thanls to Robert Bindar)
* Build system
  * [CONC-385](https://jira.mariadb.org/browse/CONC-385): Removed some cmake system checks
  * [CONC-387](https://jira.mariadb.org/browse/CONC-387): Fix case sensitive include file names for cross compiling
  * Fixed cnake policy CMP007
  * Support static linking auth plugins (Thanks to Inada Naoki)
  * Remove pdb files from Windows Release build (Thanks to Inada Naoki)
  * Fix build with deprecated OpenSSL API: replaced ERR\_remove\_state by ERR\_remove\_thread\_state. (Thanks to Rosen Penev)

## New features

* Disable LOAD DATA LOCAL INFILE suport by default and auto-enable it for the duration of one query, if the query string starts with the word "load". In all other cases the application should enable LOAD DATA LOCAL INFILE support explicitly.
* Changed return code for mysql\_optionv/mysql\_get\_optionv to 1 (was -1) and added CR\_NOT\_IMPLEMENTED error message if a option is unknown or not supported. This will fix possible error when setting connection attribute failed. (Thanks to Coray Hickey for providing this patch).

## Changelog

For a list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-c-30-changelogs/mariadb-connector-c-309-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
