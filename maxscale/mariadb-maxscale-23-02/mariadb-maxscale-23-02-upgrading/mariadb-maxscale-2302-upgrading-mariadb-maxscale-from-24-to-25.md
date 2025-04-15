
# Upgrading MariaDB MaxScale from 2.4 to 2.5

# Upgrading MariaDB MaxScale from 2.4 to 2.5


This document describes possible issues when upgrading MariaDB
MaxScale from version 2.4 to 2.5.


For more information about MaxScale 2.5, refer to the
[ChangeLog](../mariadb-maxscale-2302-changelog.md).


Before starting the upgrade, any existing configuration files should be
backed up.


## MaxAdmin


The deprecated MaxAdmin interface has been removed in 2.5.0 in favor of the REST
API and the MaxCtrl command line client. The `<code>cli</code>` and `<code>maxscaled</code>` modules can
no longer be used.


## Authentication


The credentials used by services now require additional grants. For a full list
of required grants, refer to the
[protocol documentation](../mariadb-maxscale-23-02-authenticators/mariadb-maxscale-2302-authentication-modules.md).


## MariaDB-Monitor


The settings `<code>detect_stale_master</code>`, `<code>detect_standalone_master</code>` and
`<code>detect_stale_slave</code>` are replaced by `<code>master_conditions</code>` and
`<code>slave_conditions</code>`. The old settings may still be used, but will be removed in
a later version.


### Password encryption


The encrypted passwords feature has been updated to be more secure. Users are
recommended to generate a new encryption key and and re-encrypt their passwords
using the `<code>maxkeys</code>` and `<code>maxpasswd</code>` utilities. Old passwords still work.


## Default Server State


The default state of servers in 2.4 was `<code>Running</code>` and in 2.5 it is now
`<code>Down</code>`. This was done to prevent newly added servers from being accidentally
used before they were monitored.


## Columnstore Monitor


It is now mandatory to specify in the configuration what version the
monitored Columnstore cluster is.



```
[CSMonitor]
type=monitor
module=csmon
version=1.5
...
```



Please see the [documentation](https://mariadb.com/kb/Monitors/ColumnStore-Monitor#master-selection)
for details.


## New binlog router


The binlog router delivered with MaxScale 2.5 is completely new and
not 100% backward compatible with the binlog router delivered with
earlier MaxScale versions. If you use the binlog router, carefully
assess whether the functionality provided by the new one fulfills
your requirements, before upgrading MaxScale.


## Tee Filter


The tee filter parameter `<code>service</code>` has been deprecated in favor of the `<code>target</code>`
parameter. All usages of `<code>service</code>` can be replaced with `<code>target</code>`.
