# MariaDB MaxScale 2.2.5 Release Notes -- 2018-04-25

Release 2.2.5 is a GA release.

This document describes the changes in release 2.2.5, when compared to\
release 2.2.4.

For any problems you encounter, please consider submitting a bug\
report at [Jira](https://jira.mariadb.org).

### Changed Features

* Info level messages will now also be logged to syslog, if logging to\
  syslog is enabled.

### Dropped Features

### New Features

* The user can define custom SQL queries which are executed during switchover,\
  failover and rejoin. See [MariaDB Monitor documentation](../../mariadb-maxscale-21-06/)\
  for more information.

#### MaxCtrl: Raw REST API Calls

MaxCtrl is now able to perform raw HTTP GET calls that return the JSON\
data from the REST API. It also supports value extraction with JavaScript\
style syntax.

For example, extracting just the state of all servers as a JSON array can be\
done with the following command:

```
[markusjm@localhost ~]$ maxctrl api get servers data[].attributes.state
["Master, Running","Slave, Running","Slave, Running","Slave, Running"]
```

### Bug fixes

* [MXS-1819](https://jira.mariadb.org/browse/MXS-1819) log\_info does not log to syslog
* [MXS-1815](https://jira.mariadb.org/browse/MXS-1815) threads=auto doesn't work as documented
* [MXS-1814](https://jira.mariadb.org/browse/MXS-1814) Log warning when log\_debug is used with release packages
* [MXS-1808](https://jira.mariadb.org/browse/MXS-1808) COM\_STMT\_SEND\_LONG\_DATA lead to crash
* [MXS-1807](https://jira.mariadb.org/browse/MXS-1807) Module command domains are case sensitive
* [MXS-1805](https://jira.mariadb.org/browse/MXS-1805) MaxScale may hang with multiple concurrent maxadmin calls.
* [MXS-1803](https://jira.mariadb.org/browse/MXS-1803) MaxScale docker image does not work
* [MXS-1787](https://jira.mariadb.org/browse/MXS-1787) Crash with mysql client test `test_bug49972`
* [MXS-1786](https://jira.mariadb.org/browse/MXS-1786) Hang with COM\_STATISTICS
* [MXS-1785](https://jira.mariadb.org/browse/MXS-1785) request 16M-1 normal sql + 'select 1' core dump with debug mode
* [MXS-1776](https://jira.mariadb.org/browse/MXS-1776) Hang with mysql test case `test_basic_cursors`
* [MXS-1773](https://jira.mariadb.org/browse/MXS-1773) LOAD DATA LOCAL INFILE confuses readwritesplit
* [MXS-1765](https://jira.mariadb.org/browse/MXS-1765) Internal client connections write data in wrong order
* [MXS-1757](https://jira.mariadb.org/browse/MXS-1757) Problem while linking libavrorouter.so on Ubuntu 14.04
* [MXS-1751](https://jira.mariadb.org/browse/MXS-1751) Maxscale crashes when certain config is in play (with nodes down)
* [MXS-1747](https://jira.mariadb.org/browse/MXS-1747) Rejoin functions should print better errors
* [MXS-1746](https://jira.mariadb.org/browse/MXS-1746) The session-specific gtid\_domain\_id is queried instead of the global one
* [MXS-1743](https://jira.mariadb.org/browse/MXS-1743) Maxscale unable to enforce round-robin between read service for Slave
* [MXS-1618](https://jira.mariadb.org/browse/MXS-1618) Maxadmin Binary Hangs on a Big endian Platform

### Known Issues and Limitations

There are some limitations and known issues within this version of MaxScale.\
For more information, please refer to the [Limitations](../about-maxscale-22/mariadb-maxscale-22-limitations-and-known-issues-within-mariadb-maxscale.md) document.

### Packaging

RPM and Debian packages are provided for the Linux distributions supported\
by MariaDB Enterprise.

Packages can be downloaded [here](https://mariadb.com/downloads/mariadb-tx/maxscale).

### Source Code

The source code of MaxScale is tagged at GitHub with a tag, which is identical\
with the version of MaxScale. For instance, the tag of version X.Y.Z of MaxScale\
is X.Y.Z. Further, _master_ always refers to the latest released non-beta version.

The source code is available [here](https://github.com/mariadb-corporation/MaxScale).

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
