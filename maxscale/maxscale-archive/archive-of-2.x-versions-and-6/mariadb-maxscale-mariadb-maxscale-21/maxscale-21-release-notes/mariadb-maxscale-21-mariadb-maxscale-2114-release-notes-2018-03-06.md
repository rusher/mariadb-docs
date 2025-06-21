# MariaDB MaxScale 2.1.14 Release Notes -- 2018-03-06

Release 2.1.14 is a GA release.

This document describes the changes in release 2.1.14, when compared\
to release [2.1.13](../../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/).

If you are upgrading from release 2.0, please also read the following\
release notes:

* [2.1.13](https://mariadb.com/kb/en/node:mariadb-maxscale-21-mariadb-maxscale-2113-release-notes-2018-01-05)
* [2.1.12](../../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [2.1.11](../../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [2.1.10](../../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [2.1.9](../../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [2.1.8](../../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [2.1.7](../../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [2.1.6](../../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [2.1.5](../../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [2.1.4](mariadb-maxscale-21-mariadb-maxscale-214-release-notes-2017-07-03.md)
* [2.1.3](../../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)
* [2.1.2](mariadb-maxscale-21-mariadb-maxscale-212-release-notes-2017-04-03.md)
* [2.1.1](mariadb-maxscale-21-mariadb-maxscale-211-release-notes-2017-03-14.md)
* [2.1.0](mariadb-maxscale-21-mariadb-maxscale-210-release-notes-2017-02-16.md)

For any problems you encounter, please consider submitting a bug report at[Jira](https://jira.mariadb.org).

### New Features

#### Users Refresh Time

It is now possible to adjust how frequently MaxScale may refresh\
the users of service. Please refer to the documentation for[details](../maxscale-21-getting-started/mariadb-maxscale-21-mariadb-maxscale-configuration-usage-scenarios.md#users_refresh_time).

#### Local Address

It is now possible to specify what local address MaxScale should\
use when connecting to servers. Please refer to the documentation\
for [details](../maxscale-21-getting-started/mariadb-maxscale-21-mariadb-maxscale-configuration-usage-scenarios.md#local_address).

### Bug fixes

[Here is a list of bugs fixed in MaxScale 2.1.14.](https://jira.mariadb.org/issues/?jql=project%20%3D%20MXS%20AND%20issuetype%20%3D%20Bug%20AND%20status%20%3D%20Closed%20AND%20fixVersion%20%3D%202.1.14)

* [MXS-1688](https://jira.mariadb.org/browse/MXS-1688) Some date functions are not parsed properly with schemarouter
* [MXS-1684](https://jira.mariadb.org/browse/MXS-1684) Empty space on a line in rule file confuses dbfwfilter which refuses to start
* [MXS-1678](https://jira.mariadb.org/browse/MXS-1678) Stopping IO thread on relay master causes it to be promoted as master
* [MXS-1669](https://jira.mariadb.org/browse/MXS-1669) maxadmin show threads counters are probably incorrect
* [MXS-1661](https://jira.mariadb.org/browse/MXS-1661) Excessive logging by MySQLAuth at authentication error (was: MySQLAuth SQLite database can be permanently locked)
* [MXS-1660](https://jira.mariadb.org/browse/MXS-1660) Failure to resolve hostname is considered an error
* [MXS-1627](https://jira.mariadb.org/browse/MXS-1627) MySQLAuth loads users that use authentication plugins
* [MXS-1621](https://jira.mariadb.org/browse/MXS-1621) ALTER TABLE with AFTER keyword doesn't work
* [MXS-1620](https://jira.mariadb.org/browse/MXS-1620) CentOS package symbols are stripped
* [MXS-1602](https://jira.mariadb.org/browse/MXS-1602) cannot connect to maxinfo with python client
* [MXS-1601](https://jira.mariadb.org/browse/MXS-1601) maxinfo crash at execute query 'flush;'
* [MXS-1600](https://jira.mariadb.org/browse/MXS-1600) maxscale it seen to not coop well with lower-case-table-names=1 on cnf
* [MXS-1576](https://jira.mariadb.org/browse/MXS-1576) Maxscale crashes when starting if .avro and .avsc files are present
* [MXS-1575](https://jira.mariadb.org/browse/MXS-1575) maxscale crashed with Avro conversion service
* [MXS-1543](https://jira.mariadb.org/browse/MXS-1543) Avrorouter doesn't detect MIXED or STATEMENT format replication
* [MXS-1534](https://jira.mariadb.org/browse/MXS-1534) Avrorouter not functioning
* [MXS-1416](https://jira.mariadb.org/browse/MXS-1416) maxscale should not try to do anything when started with --config-check

### Packaging

RPM and Debian packages are provided for the Linux distributions supported by\
MariaDB Enterprise.

Packages can be downloaded [here](https://mariadb.com/resources/downloads).

### Source Code

The source code of MaxScale is tagged at GitHub with a tag, which is identical\
with the version of MaxScale. For instance, the tag of version X.Y.Z of MaxScale\
is maxscale-X.Y.Z.

The source code is available [here](https://github.com/mariadb-corporation/MaxScale).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
