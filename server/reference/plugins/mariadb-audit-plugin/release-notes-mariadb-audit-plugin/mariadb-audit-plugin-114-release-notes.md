# MariaDB Audit Plugin 1.1.4 Release Notes

**Release date:** 21 Feb 2014

This is a [_**Stable**_](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-release-criteria) _**(GA)**_ release. In general this means that there are no known serious bugs, except for those marked as feature requests, that no bugs were fixed since last release that caused a notable code changes, and that we believe the code is ready for general usage (based on bug inflow).

## Important Notices

* MariaDB will include the [Audit Plugin](../) by default from versions 5.5.37 and 10.0.10. At the time of writing these versions haven't yet been released.
* The MariaDB Audit Plugin works for MariaDB, MySQL and Percona Server.

## Download

If you want to download the MariaDB Audit Plugin separately from the MariaDB server, it happens on [SkySQL's site](https://www.skysql.com/downloads/mariadb-audit-plugin).

## Main Improvements

* When a MariaDB Audit Plugin variable (e.g. server\_audit\_file\_path) is changed the last query ("SET ..") will be added to the log before the new settings apply. With this, switching off auditing will also be audited.
* Warnings about missing table events when query cache is disabled has been added.
* Handling of server\_audit\_excl\_users and incl\_users. Users cannot be added to both lists. If a user is added to a excl list and already is in the incl list, the user is not included to the excl list and an error is given. If a user is added to the incl list, that already is in the excl list, the user is removed from the excl list and added to incl and a warning is given.

## Added platform and database server support

* The Audit Plugin is now supported in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0) and as said above it will be included by default into [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0), starting from version 10.0.9
* Previous versions of the Audit Plugin couldn't be used with Percona Server, but now support for that has been added.

## Bug Fixes

* [MDEV-4472](https://jira.mariadb.org/browse/MDEV-4472) Fix for threadpool notifications of thread connects/disconnects
* [MDEV-5693](https://jira.mariadb.org/browse/MDEV-5693) ps-protocol mode caused a Audit Plugin test case failure
* [MDEV-4472](https://jira.mariadb.org/browse/MDEV-4472) Fix for Percona Server
* [MDEV-4472](https://jira.mariadb.org/browse/MDEV-4472) Fixes to usage of exc-users and incl-users
* [MDEV-5365](https://jira.mariadb.org/browse/MDEV-5365) Fixed issue with server\_audit\_excl\_users and server\_audit\_incl\_users in SHOW VARIABLES
* [MDEV-4472](https://jira.mariadb.org/browse/MDEV-4472) \_my\_hash\_init in 10.0 fix.

## MariaDB Audit Plugin 1.1.4 Changelog

The issue number links will take you to the corresponding issue in MariaDB project tracking.

* Revision 3912, 2014-02-17
  * [MDEV-4472](https://jira.mariadb.org/browse/MDEV-4472) server\_audit.opt added. A temporary solution for Threadpool. Currently it doesn't notify plugins properly about thread connects/disconnects.
* Revision 3911, 2014-02-17
  * [MDEV-5693](https://jira.mariadb.org/browse/MDEV-5693) server\_audit.test fails in --ps-protocol mode. Notifying from the mysqld\_stmt\_prepare/mysqld\_stmt\_execute has it's specifics. The command in this case is 'Prepare' and 'Execute' (not just 'Query'). When error is notified from the mysqld\_stmt\_prepare, the query string is empty. Fixed by tacking it all into account.
* Revision: 3910, 2014-02-14
  * [MDEV-4472](https://jira.mariadb.org/browse/MDEV-4472) Fix for Percona Server.
* Revision: 3909, 2014-01-30
  * [MDEV-4472](https://jira.mariadb.org/browse/MDEV-4472) Fixes to make the exc-users and incl-users work more smoothly.
* Revision: 3908, 2013-11-30
  * [MDEV-5365](https://jira.mariadb.org/browse/MDEV-5365) server\_audit\_excl\_users and server\_audit\_incl\_users behave weird when assigned. As these variables used same temporary buffer, the same content was shown to SHOW VARIABLES. Fixed by using separate buffers. Also warning added when the QUERY CACHE is active that TABLE events can be hidden by it.
* Revision: 3907, 2013-11-15
  * [MDEV-4472](https://jira.mariadb.org/browse/MDEV-4472) Version number set to 1.1.4. Additions 17.
* Revision: 3906, 2013-11-14
  * [MDEV-4472](https://jira.mariadb.org/browse/MDEV-4472) \_my\_hash\_init in 10.0 fix.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
