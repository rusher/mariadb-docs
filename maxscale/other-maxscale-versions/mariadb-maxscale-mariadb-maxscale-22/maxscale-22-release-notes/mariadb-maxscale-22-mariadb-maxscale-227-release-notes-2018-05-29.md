# mariadb-maxscale-22-mariadb-maxscale-227-release-notes-2018-05-29

Release 2.2.7 is a GA release.

This document describes the changes in release 2.2.7, when compared to\
release 2.2.6.

For any problems you encounter, please consider submitting a bug\
report at [Jira](https://jira.mariadb.org).

### Bug fixes

* [MXS-1882](https://jira.mariadb.org/browse/MXS-1882) Maxscale don't recognize logdir= in /etc/maxscale.cnf.d/maxscale.cnf
* [MXS-1879](https://jira.mariadb.org/browse/MXS-1879) use\_priorities is missed out of show monitor command
* [MXS-1878](https://jira.mariadb.org/browse/MXS-1878) Worker post fails due to: Resource temporarily unavailable
* [MXS-1875](https://jira.mariadb.org/browse/MXS-1875) MaxScale crashes 5 minutes after OS startup

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
