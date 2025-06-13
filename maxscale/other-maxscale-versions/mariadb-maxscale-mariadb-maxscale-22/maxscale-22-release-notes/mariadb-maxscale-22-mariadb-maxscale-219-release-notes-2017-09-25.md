# MariaDB MaxScale 2.1.9 Release Notes -- 2017-09-25

Release 2.1.9 is a GA release.

This document describes the changes in release 2.1.9, when compared to release[2.1.8](mariadb-maxscale-22-mariadb-maxscale-218-release-notes-2017-09-20.md).

If you are upgrading from release 2.0, please also read the following release\
notes:

* [2.1.8](https://mariadb.com/kb/en/node:mariadb-maxscale-22-mariadb-maxscale-218-release-notes-2017-09-20)
* [2.1.7](mariadb-maxscale-22-mariadb-maxscale-217-release-notes-2017-09-11.md)
* [2.1.6](mariadb-maxscale-22-mariadb-maxscale-216-release-notes-2017-08-14.md)
* [2.1.5](mariadb-maxscale-22-mariadb-maxscale-215-release-notes-2017-07-31.md)
* [2.1.4](mariadb-maxscale-22-mariadb-maxscale-214-release-notes-2017-07-03.md)
* [2.1.3](mariadb-maxscale-22-mariadb-maxscale-213-release-notes-2017-05-23.md)
* [2.1.2](mariadb-maxscale-22-mariadb-maxscale-212-release-notes-2017-04-03.md)
* [2.1.1](mariadb-maxscale-22-mariadb-maxscale-211-release-notes-2017-03-14.md)
* [2.1.0](mariadb-maxscale-22-mariadb-maxscale-210-release-notes-2017-02-16.md)

For any problems you encounter, please consider submitting a bug report at[Jira](https://jira.mariadb.org).

### Bug fixes

[Here is a list of bugs fixed in MaxScale 2.1.9.](https://jira.mariadb.org/issues/?jql=project%20%3D%20MXS%20AND%20issuetype%20%3D%20Bug%20AND%20status%20%3D%20Closed%20AND%20fixVersion%20%3D%202.1.9)

* [MXS-1435](https://jira.mariadb.org/browse/MXS-1435) Persistent connections can hang on COM\_QUIT
* [MXS-1377](https://jira.mariadb.org/browse/MXS-1377) maxscale doesn't cleanup pid file on startup error
* [MXS-1295](https://jira.mariadb.org/browse/MXS-1295) MaxScale's readwritesplit router does not take into account the fact that stored procedure call may change the value of a user variable

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
