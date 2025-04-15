
# MariaDB MaxScale 2.0.3 Release Notes

# MariaDB MaxScale 2.0.3 Release Notes


Release 2.0.3 is a GA release.


This document describes the changes in release 2.0.3, when compared to
release [2.0.2](../../mariadb-maxscale-21-06/README.md).


If you are upgrading from release 1.4.4, please also read the release
notes of release [2.0.0](../../mariadb-maxscale-21-06/README.md),
release [2.0.1](../../mariadb-maxscale-21-06/README.md) and
release [2.0.2](https://mariadb.com/kb/en/node:mariadb-maxscale-202-release-notes).


For any problems you encounter, please submit a bug report at
[Jira](https://jira.mariadb.org).


## Updated Features


### [MXS-1027](https://jira.mariadb.org/browse/MXS-1027) Add Upstart support (including respawn) for MaxScale


MaxScale now provides an Upstart configuration file for systems that do not
support systemd.


## Bug fixes


[Here](https://jira.mariadb.org/issues/?jql=project%20%3D%20MXS%20AND%20issuetype%20%3D%20Bug%20AND%20status%20%3D%20Closed%20AND%20fixVersion%20%3D%202.0.3)
is a list of bugs fixed since the release of MaxScale 2.0.2.


* [MXS-1048](https://jira.mariadb.org/browse/MXS-1048): ShemaRouter can't handle backquoted database names
* [MXS-1047](https://jira.mariadb.org/browse/MXS-1047): Batch inserts through Maxscale with C/J stall
* [MXS-1045](https://jira.mariadb.org/browse/MXS-1045): Defunct processes after maxscale have executed script during failover
* [MXS-1044](https://jira.mariadb.org/browse/MXS-1044): Init-Script for SLES 11 displays error messages when called
* [MXS-1043](https://jira.mariadb.org/browse/MXS-1043): Reading last insert id from @@identity variable does not work with maxscale
* [MXS-1033](https://jira.mariadb.org/browse/MXS-1033): maxscale crushes on maxadmin request
* [MXS-1026](https://jira.mariadb.org/browse/MXS-1026): Crash with NullAuth authenticator
* [MXS-1009](https://jira.mariadb.org/browse/MXS-1009): maxinfo sigsegv in spinlock_release
* [MXS-964](https://jira.mariadb.org/browse/MXS-964): Fatal: MaxScale 2.0.1 received fatal signal 6
* [MXS-956](https://jira.mariadb.org/browse/MXS-956): Maxscale crash: Removing DCB 0x7fbf94016760 but was in state DCB_STATE_DISCONNECTED which is not legal for a call to dcb_close


## Known Issues and Limitations


There are some limitations and known issues within this version of MaxScale.
For more information, please refer to the [Limitations](../about-maxscale-20/mariadb-maxscale-20-limitations-and-known-issues-within-mariadb-maxscale.md) document.


## Packaging


RPM and Debian packages are provided for the Linux distributions supported
by MariaDB Enterprise.


Packages can be downloaded [here](https://mariadb.com/resources/downloads).


## Source Code


The source code of MaxScale is tagged at GitHub with a tag, which is derived
from the version of MaxScale. For instance, the tag of version `<code>X.Y.Z</code>` of MaxScale
is `<code>maxscale-X.Y.Z</code>`.


The source code is available [here](https://github.com/mariadb-corporation/MaxScale).
