
# MariaDB MaxScale 2.0.4 Release Notes -- 2017-02-01

# MariaDB MaxScale 2.0.4 Release Notes -- 2017-02-01


Release 2.0.4 is a GA release.


This document describes the changes in release 2.0.4, when compared to
release [2.0.3](../../mariadb-maxscale-21-06/README.md).


If you are upgrading from release 1.4, please also read the release
notes of release [2.0.3](https://mariadb.com/kb/en/node:mariadb-maxscale-203-release-notes),
release [2.0.2](../../mariadb-maxscale-21-06/README.md),
release [2.0.1](../../mariadb-maxscale-21-06/README.md) and
[2.0.0](../../mariadb-maxscale-21-06/README.md).


For any problems you encounter, please submit a bug report at
[Jira](https://jira.mariadb.org).


## Changed Features


* The dbfwfilter now rejects all prepared statements instead of ignoring
 them. This affects wildcard, columns, on_queries and no_where_clause
 type rules which previously ignored prepared statements.
* The dbfwfilter now allows COM_PING and other commands though when
 `action=allow`. See [../Filters/Database-Firewall-Filter.md](https://mariadb.com/kb/en/documentation)
 for more details.
* The MariaDB Connector-C was upgraded to a preliminary release of version 2.3.3 (fixes MXS-951).


## Bug fixes


[Here](https://jira.mariadb.org/issues/?jql=project%20%3D%20MXS%20AND%20issuetype%20%3D%20Bug%20AND%20status%20%3D%20Closed%20AND%20fixVersion%20%3D%202.0.4)
is a list of bugs fixed since the release of MaxScale 2.0.3.


* [MXS-1111](https://jira.mariadb.org/browse/MXS-1111): Request Ping not allowed
* [MXS-1082](https://jira.mariadb.org/browse/MXS-1082): Block prepared statements
* [MXS-1080](https://jira.mariadb.org/browse/MXS-1080): Readwritesplit (documentation of max_slave_replication_lag)
* [MXS-951](https://jira.mariadb.org/browse/MXS-951): Using utf8mb4 on galera hosts stops maxscale connections


## Known Issues and Limitations


There are some limitations and known issues within this version of MaxScale.
For more information, please refer to the [Limitations](../about-maxscale-20/mariadb-maxscale-20-limitations-and-known-issues-within-mariadb-maxscale.md) document.


## Packaging


RPM and Debian packages are provided for the Linux distributions supported
by MariaDB Enterprise.


Packages can be downloaded [here](https://mariadb.com/resources/downloads).


## Source Code


The source code of MaxScale is tagged at GitHub with a tag, which is derived
from the version of MaxScale. For instance, the tag of version `X.Y.Z` of MaxScale
is `maxscale-X.Y.Z`.


The source code is available [here](https://github.com/mariadb-corporation/MaxScale).
