# Connector/ODBC 3.2.0 Release Notes

{% include "../../../.gitbook/includes/latest-odbc.md" %}

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/odbc-connector/) | [Release Notes](mariadb-connector-odbc-3-2-0-release-notes.md) | [Changelog](../changelogs/mariadb-connector-odbc-3-2-changelogs/mariadb-connector-odbc-3-2-0-changelog.md) | [About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 21 Apr 2023

This is a [alpha](../../../community-server/about/release-criteria.md) release of MariaDB Connector/ODBC 3.2.

**Do not use&#x20;**_**alpha**_**&#x20;releases in production!**

MariaDB Connector/ODBC 3.2.0 is built on top of [MariaDB Connector/C v.3.3.2](../../c/3.3/3.3.2.md), and contains all fixes and changes from [MariaDB Connector/ODBC v.3.1.18](../mariadb-connector-odbc-3-1-release-notes/mariadb-connector-odbc-3-1-18-release-notes.md)

## Notable Changes

* [ODBC-222](https://jira.mariadb.org/browse/ODBC-222) - SQLExecDirect ODBC API function now uses text protocol and client side prepared statements(CSPS). That can be automatically switched to use of binary protocol and server side prepared statement(SSPS) if necessary(for example for CALL statement).\
  ODBC API function SQLPrepare uses by default SSPS, but it can switch to CSPS, for example in case of multistatement query.\
  The connection string option `PREPONCLIENT` to use CSPS by default also in SQLPrepare has been added. In some cases driver will still revert to use of SSPS even if this option is selected. One example of such case is a request of resultset metadata before SQLExecute API function call.
* [ODBC-86](https://jira.mariadb.org/browse/ODBC-86) - parameter array operations are now optimized also for the case of text protocol and CSPS use. i.e. driver can construct batch of queries based on values in parameter arrays for sending it via text protocol. Sending parameter arrays via binary protocol is supported already in 3.1 version and is preferable way for this operation.
* [ODBC-290](https://jira.mariadb.org/browse/ODBC-290) - Cursor type now defaults to SQL\_CURSOR\_FORWARD\_ONLY as it is required by specs. 3.1.x series has default cursor type SQL\_CURSOR\_STATIC
* [ODBC-298](https://jira.mariadb.org/browse/ODBC-298) - NULL value of catalog name parameter of SQLTables ODBC API function is now treated as "current schema" by default, and not as "any schema"
* [ODBC-388](https://jira.mariadb.org/browse/ODBC-388) - Support of connection attributes. For setting connection attributes the `ATTR` connection string option can be used in following format

```
ATTR={<attrname1>=<attrvalue1>[,<attrname2=attrvalue2,...]}
```

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the [changelog](../changelogs/mariadb-connector-odbc-3-2-changelogs/mariadb-connector-odbc-3-2-0-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
