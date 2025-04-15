
# Upgrading MariaDB MaxScale from 2.3 to 2.4

# Upgrading MariaDB MaxScale from 2.3 to 2.4


This document describes possible issues when upgrading MariaDB
MaxScale from version 2.3 to 2.4.


For more information about MariaDB MaxScale 2.4, please refer
to the [ChangeLog](../mariadb-maxscale-24-changelog.md).


Before starting the upgrade, we recommend you back up your current
configuration file.


## Section Names


### Reserved Names


Section and object names starting with `<code>@@</code>` are now reserved for
internal use by MaxScale.


In case such names have been used, they must manually be changed
in all configuration files of MaxScale, before MaxScale 2.4 is started.


Those files are:


* The main configuration file; typically `<code>/etc/maxscale.cnf</code>`.
* All nested configuration files; typically `<code>/etc/maxscale.cnf.d/*</code>`.
* All dynamic configuration files; typically `<code>/var/lib/maxscale/maxscale.cnd.d/*</code>`.


### Whitespace in Names


Whitespace in section names that was deprecated in MaxScale 2.2 will now be
rejected, which will cause the startup of MaxScale to fail.


To prevent that, section names like



```
[My Server]
...

[My Service]
...
servers=My Server
```



must be changed, for instance, to



```
[MyServer]
...

[MyService]
...
servers=MyServer
```



## Durations


Durations can now be specified using one of the suffixes `<code>h</code>`, `<code>m</code>`, `<code>s</code>`
and `<code>ms</code>` for specifying durations in hours, minutes, seconds and
milliseconds, respectively.


*Not* providing an explicit unit has been deprecated in MaxScale 2.4,
so it is adviseable to add suffixes to durations. For instance,



```
some_param=60s
some_param=60000ms
```



## Improved Admin User Encryption


MaxScale 2.4 will use a SHA2-512 hash for new admin user passwords. To upgrade a
user to use the better hashing algorithm, either recreate the user or use the
`<code>maxctrl alter user</code>` command.


## MariaDB-Monitor


The following settings have been removed and cause a startup error
if defined:


* `<code>mysql51_replication</code>`
* `<code>multimaster</code>`
* `<code>allow_cluster_recovery</code>`.


## ReadWriteSplit


* If multiple masters are available for a readwritesplit service, the one with
 the lowest connection count is selected.
* If a master server is placed into maintenance mode, all open transactions are
 allowed to gracefully finish before the session is closed. To forcefully close
 the connections, use the `<code>--force</code>` option for `<code>maxctrl set server</code>`.
* The `<code>lazy_connect</code>` feature can be used as a workaround to
 [MXS-619](https://jira.mariadb.org/browse/MXS-619). It also reduces the
 overall load on the system when connections are rapidly opened and closed.
* Transaction replays now have a limit on how many times a replay is
 attempted. The default values is five attempts and is controlled by the
 `<code>transaction_replay_attempts</code>` parameter.
* If transaction replay is enabled and a deadlock occurs (SQLSTATE 40XXX), the
 transaction is automatically retried.
