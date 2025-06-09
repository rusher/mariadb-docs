# MariaDB Connector/J 1.5.5 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/1.5.5/)[Release Notes](mariadb-connector-j-155-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-15-changelogs/mariadb-connector-j-155-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 9 Nov 2016

MariaDB Connector/J 1.5.5 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

## Notable Changes

This version is a bug-fix release.

* [CONJ-386](https://jira.mariadb.org/browse/CONJ-386) : Disabling useBatchMultiSend option for Aurora, since can hang connection.
* [CONJ-385](https://jira.mariadb.org/browse/CONJ-385) : Store procedure with resultSet get wrong getUpdateCount() value (0 in place of -1)
* [CONJ-383](https://jira.mariadb.org/browse/CONJ-383) : permit OldAuthSwitchRequest protocol (compatibility with 5.5 server using plugin)
* [CONJ-382](https://jira.mariadb.org/browse/CONJ-382) : Client sockets remain when server close socket on connection (when server maximum connections number has been reached)
* [CONJ-381](https://jira.mariadb.org/browse/CONJ-381) : Metadata getProcedureColumns precision's information corrected for date/timestamp/datetime
* [CONJ-379](https://jira.mariadb.org/browse/CONJ-379) : Metadata TINYTEXT type return Types.LONGVARCHAR instead of Types.VARCHAR
* [CONJ-376](https://jira.mariadb.org/browse/CONJ-376) : Maxscale compatibility : Permit protocol compression only if server permit it
* [CONJ-375](https://jira.mariadb.org/browse/CONJ-375) : Load data infile with large files fails with OutOfMemoryError correction
* [CONJ-370](https://jira.mariadb.org/browse/CONJ-370) : use KeyStore default property when not using keyStore option
* [CONJ-369](https://jira.mariadb.org/browse/CONJ-369) : Encoding on clob column when useServerPrepStmts=true correction
* [CONJ-362](https://jira.mariadb.org/browse/CONJ-362) : fix a possible race condition MariaDbPooledConnection

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
