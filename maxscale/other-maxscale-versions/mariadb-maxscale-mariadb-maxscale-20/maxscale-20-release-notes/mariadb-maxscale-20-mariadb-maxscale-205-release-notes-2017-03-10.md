# MariaDB MaxScale 2.0.5 Release Notes -- 2017-03-10

Release 2.0.5 is a GA release.

This document describes the changes in release 2.0.5, when compared to\
release [2.0.4](../../mariadb-maxscale-21-06/).

If you are upgrading from release 1.4, please also read the following\
release notes:[2.0.4](https://mariadb.com/kb/en/node:mariadb-maxscale-204-release-notes-2017-02-01),[2.0.3](../../mariadb-maxscale-21-06/),[2.0.2](../../mariadb-maxscale-21-06/),[2.0.1](../../mariadb-maxscale-21-06/) and[2.0.0](../../mariadb-maxscale-21-06/).

For any problems you encounter, please submit a bug report at[Jira](https://jira.mariadb.org).

### Bug fixes

[Here](https://jira.mariadb.org/issues/?jql=project%20%3D%20MXS%20AND%20issuetype%20%3D%20Bug%20AND%20status%20%3D%20Closed%20AND%20fixVersion%20%3D%202.0.5)\
is a list of bugs fixed since the release of MaxScale 2.0.4.

* [MXS-1130](https://jira.mariadb.org/browse/MXS-1130): Unexpected length encoding 'ff' encountered
* [MXS-1123](https://jira.mariadb.org/browse/MXS-1123): connect\_timeout setting causes frequent disconnects
* [MXS-1081](https://jira.mariadb.org/browse/MXS-1081): Avro data file corruption
* [MXS-1025](https://jira.mariadb.org/browse/MXS-1025): qc\_sqlite always reports " Statement was parsed, but not classified"

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
