
# Upgrading MariaDB MaxScale from 2.5 to 6

# Upgrading MariaDB MaxScale from 2.5 to 6


This document describes possible issues when upgrading MariaDB MaxScale from
version 2.5 to 6.


Note that the versioning scheme has changed and that version 6 immediately
follows version 2.5. Effectively, the non-changing `<code>2.</code>`-prefix has been dropped
and henceforth at a major release, the *major*, instead of the *minor* version
number, will be bumped. This change also affects how maintenance releases are
versioned. For instance, 2.5.1, the first GA version of MaxScale 2.5, was
followed by the maintenace release 2.5.2. 6.1, the first GA version of MaxScale
6, will be followed by the maintenance release 6.2.


For more information about MaxScale 6, refer to the
[ChangeLog](../mariadb-maxscale-2302-changelog.md).


Before starting the upgrade, any existing configuration files should be backed
up.


## Duration Type Parameters


Using duration type parameters without an explicit suffix has been deprecated in
MaxScale 2.4. In MaxScale 6 they are no longer allowed when used with the REST
API or MaxCtrl. This means that any `<code>create</code>` or `<code>alter</code>` commands in MaxCtrl that
use a duration type parameter must explicitly specify the suffix of the unit.


For example, the following command:



```
maxctrl alter service My-Service connection_keepalive 30000
```



should be replaced with:



```
maxctrl alter service My-Service connection_keepalive 30000ms
```



Duration type parameters can still be defined in the configuration file without
an explicit suffix but this behavior is deprecated. The recommended approach is
to add explicit suffixes to all duration type parameters when upgrading to
MaxScale 6.


## Changed Parameters


### `<code>threads</code>`


The default value of `<code>threads</code>` was changed to `<code>auto</code>`.


## Removed Parameters


### Core Parameters


The following deprecated core parameters have been removed:


* `<code>thread_stack_size</code>`


### Schemarouter


The deprecated aliases for the schemarouter parameters `<code>ignore_databases</code>` and
`<code>ignore_databases_regex</code>` have been removed. They can be replaced with
`<code>ignore_tables</code>` and `<code>ignore_tables_regex</code>`.


In addition, the `<code>preferred_server</code>` parameter that was deprecated in 2.5 has
also been removed.


## Session Command History


The `<code>prune_sescmd_history</code>`, `<code>max_sescmd_history</code>` and `<code>disable_sescmd_history</code>`
have been made into generic service parameters that are shared between all
routers that support it.


The default value of `<code>prune_sescmd_history</code>` was changed from `<code>false</code>` to
`<code>true</code>`. This was done as most MaxScale installations either benefit from it
being enabled or are not affected by it.
