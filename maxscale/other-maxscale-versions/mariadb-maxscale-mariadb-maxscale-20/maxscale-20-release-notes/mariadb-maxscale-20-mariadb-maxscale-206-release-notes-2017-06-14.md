# MariaDB MaxScale 2.0.6 Release Notes -- 2017-06-14

Release 2.0.6 is a GA release.

This document describes the changes in release 2.0.6, when compared to\
release [2.0.5](mariadb-maxscale-20-mariadb-maxscale-205-release-notes-2017-03-10.md).

If you are upgrading from release 1.4, please also read the following\
release notes:[2.0.5](https://mariadb.com/kb/en/node:mariadb-maxscale-20-mariadb-maxscale-205-release-notes-2017-03-10),[2.0.4](mariadb-maxscale-20-mariadb-maxscale-204-release-notes-2017-02-01.md),[2.0.3](mariadb-maxscale-20-mariadb-maxscale-203-release-notes.md),[2.0.2](mariadb-maxscale-20-mariadb-maxscale-202-release-notes.md),[2.0.1](mariadb-maxscale-20-mariadb-maxscale-201-release-notes.md) and[2.0.0](mariadb-maxscale-20-mariadb-maxscale-200-release-notes.md).

For any problems you encounter, please submit a bug report at[Jira](https://jira.mariadb.org).

### Bug fixes

[Here](https://jira.mariadb.org/issues/?jql=project%20%3D%20MXS%20AND%20issuetype%20%3D%20Bug%20AND%20status%20%3D%20Closed%20AND%20fixVersion%20%3D%202.0.6)\
is a list of bugs fixed since the release of MaxScale 2.0.5.

* [MXS-1244](https://jira.mariadb.org/browse/MXS-1244): MySQL monitor "detect\_replication\_lag=true" doesn't work with "mysql51\_replication=true"
* [MXS-1221](https://jira.mariadb.org/browse/MXS-1221): Nagios plugin scripts does not process -S option properly
* [MXS-1218](https://jira.mariadb.org/browse/MXS-1218): Use correct conversion specifier when printing 64-bit integers
* [MXS-1216](https://jira.mariadb.org/browse/MXS-1216): Fatal error while converting data
* [MXS-1191](https://jira.mariadb.org/browse/MXS-1191): Alter statement to a table with no create statement.
* [MXS-1180](https://jira.mariadb.org/browse/MXS-1180): cdc.py not producing anything with JSON format, but does with AVRO
* [MXS-1178](https://jira.mariadb.org/browse/MXS-1178): master\_accept\_reads doesn't work with detect\_replication\_lag

### Known Issues and Limitations

There are some limitations and known issues within this version of MaxScale.\
For more information, please refer to the [Limitations](../about-maxscale-20/mariadb-maxscale-20-limitations-and-known-issues-within-mariadb-maxscale.md) document.

### Packaging

RPM and Debian packages are provided for the Linux distributions supported\
by MariaDB Enterprise.

Packages can be downloaded [here](https://mariadb.com/resources/downloads).

### Source Code

The source code of MaxScale is tagged at GitHub with a tag, which is derived\
from the version of MaxScale. For instance, the tag of version `X.Y.Z` of MaxScale\
is `maxscale-X.Y.Z`.

The source code is available [here](https://github.com/mariadb-corporation/MaxScale).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
