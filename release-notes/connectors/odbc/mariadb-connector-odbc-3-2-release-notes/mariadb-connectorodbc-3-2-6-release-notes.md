# MariaDB Connector/ODBC 3.2.6 Release Notes

<a href="https://mariadb.com/downloads/connectors/connectors-data-access/odbc-connector" class="button primary">Download</a>   <a href="mariadb-connectorodbc-3-2-6-release-notes.md" class="button secondary">Release Notes</a>   <a href="../changelogs/mariadb-connector-odbc-3-2-changelogs/mariadb-connector-odbc-3.2.6-changelog.md" class="button secondary">Changelog</a>   <a href="https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc" class="button secondary">About MariaDB Connector/ODBC</a>

**Release date:**

This is a [Stable (GA)](../../../mariadb-release-criteria.md) release of MariaDB Connector/ODBC 3.2.

MariaDB Connector/ODBC 3.2.6 is built on top of[MariaDB Connector/C v.3.4.5](../../c/mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md).

## Bug Fixes

* [ODBC-460](https://jira.mariadb.org/browse/ODBC-460) - Crash in SQLExecDirect on UPDATE statement with array of parameters
* [ODBC-461](https://jira.mariadb.org/browse/ODBC-461) - The destructor releasing server side prepared statement could throw and this exception would not be caught
* [ODBC-458](https://jira.mariadb.org/browse/ODBC-458) - MS Access won't work with the linked table if best row id is BIGINT
* [ODBC-459](https://jira.mariadb.org/browse/ODBC-459) - MS Access shows record with AUTO\_INCREMENT primary key as #Deleted after insert that does not specify that field value
* [ODBC-462](https://jira.mariadb.org/browse/ODBC-462) - SQLExecDirect on array of parameters could issue multistatement query even if multistatement option had not been selected for the connection.
* [ODBC-464](https://jira.mariadb.org/browse/ODBC-464) - Multiple issues with current implementation of SQLCancel
* [ODBC-466](https://jira.mariadb.org/browse/ODBC-466) - SQLCancel could run on already dropped statement due to race condition
* [ODBC-467](https://jira.mariadb.org/browse/ODBC-467) - Possible crash in SQLCancelHandle

## New Feature

* [ODBC-457](https://jira.mariadb.org/browse/ODBC-457) - Introduced option TRUNCDT to skip time truncation error. Setting it to non-zero value makes connector not to return error on date/time type parameter value truncation. These are when value for SQL\_TIME contains fractional part, or for SQL\_DATE contains non-zero time. In particular, that permits to insert value with fractional part into TIME field which in MariaDB can have fractional part as ODBC SQL\_TIME type.

## Changelog

For a complete list of every change made in this release, with links to detailed information on each push, see the [changelog](../changelogs/mariadb-connector-odbc-3-2-changelogs/mariadb-connector-odbc-3.2.6-changelog.md).

{% include "../../../../.gitbook/includes/announce.md" %}
