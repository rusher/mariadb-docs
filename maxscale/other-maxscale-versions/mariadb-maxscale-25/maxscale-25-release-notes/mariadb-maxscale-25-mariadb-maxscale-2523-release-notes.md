
# MariaDB MaxScale 2.5.23 Release Notes

# MariaDB MaxScale 2.5.23 Release Notes -- 2023-11-28


Release 2.5.23 is a GA release.


This document describes the changes in release 2.5.23, when compared to the
previous release in the same series.


If you are upgrading from an older major version of MaxScale, please read the
[upgrading document](../maxscale-25-upgrading/mariadb-maxscale-25-upgrading-mariadb-maxscale-from-24-to-25.md) for
this MaxScale version.


For any problems you encounter, please consider submitting a bug
report on [our Jira](https://jira.mariadb.org/projects/MXS).


## Bug fixes


* [MXS-4348](https://jira.mariadb.org/browse/MXS-4348) Full SASL support is not enabled for kafka modules
* [MXS-4317](https://jira.mariadb.org/browse/MXS-4317) Smartrouter interrupts the wrong query


## Known Issues and Limitations


There are some limitations and known issues within this version of MaxScale.
For more information, please refer to the [Limitations](../about-maxscale-25/mariadb-maxscale-25-limitations-and-known-issues-within-mariadb-maxscale.md) document.


## Packaging


RPM and Debian packages are provided for supported the Linux distributions.


Packages can be downloaded [here](https://mariadb.com/downloads/#mariadb_platform-mariadb_maxscale).


## Source Code


The source code of MaxScale is tagged at GitHub with a tag, which is identical
with the version of MaxScale. For instance, the tag of version X.Y.Z of MaxScale
is `maxscale-X.Y.Z`. Further, the default branch is always the latest GA version
of MaxScale.


The source code is available [here](https://github.com/mariadb-corporation/MaxScale).


CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
