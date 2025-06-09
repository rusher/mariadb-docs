
# MariaDB MaxScale 2.1.4 Release Notes -- 2017-07-03

# MariaDB MaxScale 2.1.4 Release Notes -- 2017-07-03


Release 2.1.4 is a GA release.


This document describes the changes in release 2.1.4, when compared to
release [2.1.3](mariadb-maxscale-22-mariadb-maxscale-213-release-notes-2017-05-23.md).


If you are upgrading from release 2.0, please also read the following
release notes:
[2.1.3](https://mariadb.com/kb/en/node:mariadb-maxscale-22-mariadb-maxscale-213-release-notes-2017-05-23)
[2.1.2](mariadb-maxscale-22-mariadb-maxscale-212-release-notes-2017-04-03.md)
[2.1.1](mariadb-maxscale-22-mariadb-maxscale-211-release-notes-2017-03-14.md)
[2.1.0](mariadb-maxscale-22-mariadb-maxscale-210-release-notes-2017-02-16.md)


For any problems you encounter, please consider submitting a bug
report at [Jira](https://jira.mariadb.org).


## Changed Features


### Masking


* The masking filter now has a default fill character `X`, which
 is used if only a value has been specified and the length of
 the value does not match the length of the value received from
 the server.


Please refer to the
 [masking documentation](../maxscale-22-filters/mariadb-maxscale-22-masking.md)
 for details.


### maxadmin


* Error message for failed login attempt has been improved.


## Bug fixes


[Here is a list of bugs fixed since the release of MaxScale 2.1.3.](https://jira.mariadb.org/issues/?jql=project%20%3D%20MXS%20AND%20issuetype%20%3D%20Bug%20AND%20status%20%3D%20Closed%20AND%20fixVersion%20%3D%202.1.4)


* [MXS-1308](https://jira.mariadb.org/browse/MXS-1308) Crash with multimaster=true in mysqlmon
* [MXS-1304](https://jira.mariadb.org/browse/MXS-1304) Invalid write in gw_str_xor
* [MXS-1299](https://jira.mariadb.org/browse/MXS-1299) CREATE TABLE LIKE fails with avrorouter
* [MXS-1296](https://jira.mariadb.org/browse/MXS-1296) Lowercase start transaction is not detected
* [MXS-1294](https://jira.mariadb.org/browse/MXS-1294) cdc_schema.py uses Python 3
* [MXS-1287](https://jira.mariadb.org/browse/MXS-1287) Slaves of external servers can't be used as slaves
* [MXS-1279](https://jira.mariadb.org/browse/MXS-1279) Runtime changes to monitor credentials expect wrong parameter names
* [MXS-1271](https://jira.mariadb.org/browse/MXS-1271) cdc.py consuming 100% of CPU and never sending to kafka


## Known Issues and Limitations


There are some limitations and known issues within this version of MaxScale.
For more information, please refer to the [Limitations](../about-maxscale-22/mariadb-maxscale-22-limitations-and-known-issues-within-mariadb-maxscale.md) document.


## Packaging


RPM and Debian packages are provided for the Linux distributions supported
by MariaDB Enterprise.


Packages can be downloaded [here](https://mariadb.com/resources/downloads).


## Source Code


The source code of MaxScale is tagged at GitHub with a tag, which is identical
with the version of MaxScale. For instance, the tag of version X.Y.Z of MaxScale
is X.Y.Z.


The source code is available [here](https://github.com/mariadb-corporation/MaxScale).


CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
