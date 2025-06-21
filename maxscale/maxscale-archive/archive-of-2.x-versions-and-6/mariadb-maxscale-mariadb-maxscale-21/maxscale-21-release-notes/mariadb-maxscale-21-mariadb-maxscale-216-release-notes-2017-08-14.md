# MariaDB MaxScale 2.1.6 Release Notes -- 2017-08-14

Release 2.1.6 is a GA release.

This document describes the changes in release 2.1.6, when compared to\
release [2.1.5](../../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/).

If you are upgrading from release 2.0, please also read the following\
release notes:[2.1.5](https://mariadb.com/kb/en/node:mariadb-maxscale-215-release-notes-2017-07-31)[2.1.4](mariadb-maxscale-21-mariadb-maxscale-214-release-notes-2017-07-03.md)[2.1.3](../../../archive-of-2x.xx-versions/mariadb-maxscale-21-06/)[2.1.2](mariadb-maxscale-21-mariadb-maxscale-212-release-notes-2017-04-03.md)[2.1.1](mariadb-maxscale-21-mariadb-maxscale-211-release-notes-2017-03-14.md)[2.1.0](mariadb-maxscale-21-mariadb-maxscale-210-release-notes-2017-02-16.md)

For any problems you encounter, please consider submitting a bug\
report at [Jira](https://jira.mariadb.org).

### Bug fixes

[Here is a list of bugs fixed in MaxScale 2.1.6.](https://jira.mariadb.org/issues/?jql=project%20%3D%20MXS%20AND%20issuetype%20%3D%20Bug%20AND%20status%20%3D%20Closed%20AND%20fixVersion%20%3D%202.1.6)

* [MXS-1352](https://jira.mariadb.org/browse/MXS-1352) Not all query failures in monitors are reported
* [MXS-1351](https://jira.mariadb.org/browse/MXS-1351) Partially authenticated connections are put into the connection pool
* (MXS-1343)\[[MXS-1343](https://jira.mariadb.org/browse/MXS-1343)] MaxScale's binlogrouter does not send hostname to its master
* [MXS-1338](https://jira.mariadb.org/browse/MXS-1338) Buffer objects are bound to indiviudual buffers

### New Features

* It is now possible to configure the binlog router to identify itself\
  to the master using a custom hostname: [MXS-1343](https://jira.mariadb.org/browse/MXS-1343)

### Known Issues and Limitations

There are some limitations and known issues within this version of MaxScale.\
For more information, please refer to the [Limitations](../about-maxscale-21/mariadb-maxscale-21-limitations-and-known-issues-within-mariadb-maxscale.md) document.

### Packaging

RPM and Debian packages are provided for the Linux distributions supported\
by MariaDB Enterprise.

Packages can be downloaded [here](https://mariadb.com/resources/downloads).

### Source Code

The source code of MaxScale is tagged at GitHub with a tag, which is identical\
with the version of MaxScale. For instance, the tag of version X.Y.Z of MaxScale\
is maxscale-X.Y.Z.

The source code is available [here](https://github.com/mariadb-corporation/MaxScale).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
