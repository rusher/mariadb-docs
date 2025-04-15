
# MaxScale 21.06 MariaDB MaxScale 6.1.0 Release Notes -- 2021-07-15

# MariaDB MaxScale 6.1.0 Release Notes -- 2021-07-15


Release 6.1.0 is a GA release.


This document describes the changes in release 6.1.0, when compared to the
previous release in the same series.


If you are upgrading from an older major version of MaxScale, please read the
[upgrading document](https://mariadb.com/kb/Upgrading/Upgrading-To-MaxScale-6) for
this MaxScale version.


For any problems you encounter, please consider submitting a bug
report on [our Jira](https://jira.mariadb.org/projects/MXS).


## Bug fixes


* [MXS-3661](https://jira.mariadb.org/browse/MXS-3661) The list of servers might get duplicated for routers using mariadbmon
* [MXS-3660](https://jira.mariadb.org/browse/MXS-3660) MaxScale crashes if backend connection creation fails on a system error
* [MXS-3658](https://jira.mariadb.org/browse/MXS-3658) If the monitor is dynamic, both static and volatile servers will be used.


## Known Issues and Limitations


There are some limitations and known issues within this version of MaxScale.
For more information, please refer to the [Limitations](../mariadb-maxscale-21-06-about/mariadb-maxscale-2106-maxscale-2106-limitations-and-known-issues-within-mariadb-maxscale.md) document.


## Packaging


RPM and Debian packages are provided for the supported Linux distributions.


Packages can be downloaded [here](https://mariadb.com/downloads/#mariadb_platform-mariadb_maxscale).


## Source Code


The source code of MaxScale is tagged at GitHub with a tag, which is identical
with the version of MaxScale. For instance, the tag of version X.Y.Z of MaxScale
is `<code>maxscale-X.Y.Z</code>`. Further, the default branch is always the latest GA version
of MaxScale.


The source code is available [here](https://github.com/mariadb-corporation/MaxScale).
