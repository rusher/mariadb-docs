# MariaDB Connector/ODBC 3.1.17 Release Notes

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-odbc-3-1-17-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-3117-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 30 Aug 2022

This is a [Stable (GA)](../../../mariadb-release-criteria.md) release of MariaDB Connector/ODBC 3.1.

MariaDB Connector/ODBC 3.1.17 is built on top of[MariaDB Connector/C v.3.3.2](../../c/mariadb-connector-c-33-release-notes/mariadb-connector-c-332-release-notes.md).

## Notable Changes

* Result-set streaming feature has been added ([ODBC-369](https://jira.mariadb.org/browse/ODBC-369))
  * When using it, an application cannot cache the entire result-set on the client side, but will fetch it from the server row by row
  * The feature is enabled with the connection string option: `NO_CACHE` or `STREAMRS` is the alias, alternatively bit `1048576` in the `OPTION` can be used
  * The feature only comes into action with `SQL_CURSOR_FORWARD_ONLY` cursors. It will be always used if combined with the `FORWARDONLY` connection string option, or `OPTION`'s bit `2097152`.
  * Some features cannot work in combination with this feature, and the error HY000 with the message "The requested operation is blocked by another streaming operation" will be thrown by the connector in such case.
  * No new query can be executed before the application finishes fetching the streamed result-set. In particular, positioned operation on open cursor cannot be performed, if streaming is used for the cursor. Thus not all existing application may use this new feature.

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-3117-changelog.md).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
