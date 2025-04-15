
# MaxScale 24.02 Upgrading MariaDB MaxScale from 22.08 to 23.02

# Upgrading MariaDB MaxScale from 22.08 to 23.02


This document describes possible issues when upgrading MariaDB MaxScale from
version 22.08 to 23.02.


For more information about MaxScale 23.02, refer to the
[ChangeLog](../mariadb-maxscale-2402-maxscale-2402-changelog.md).


Before starting the upgrade, any existing configuration files should be backed
up.


# Removed Features


* The `<code>csmon</code>` and `<code>auroramon</code>` monitors have been removed.
* The obsolete `<code>maxctrl drain</code>` command has been removed.
* The `<code>maxctrl cluster</code>` commands have been removed.
