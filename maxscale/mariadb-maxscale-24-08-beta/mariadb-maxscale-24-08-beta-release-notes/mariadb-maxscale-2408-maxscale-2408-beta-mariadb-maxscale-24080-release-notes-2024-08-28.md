
# MaxScale 24.08 Beta MariaDB MaxScale 24.08.0 Release Notes -- 2024-08-28

# MariaDB MaxScale 24.08.0 Release Notes -- 2024-08-28


Release 24.08.0 is a Beta release.


This document describes the changes in release 24.08, when compared to
release 24.02.


For any problems you encounter, please consider submitting a bug
report on [our Jira](https://jira.mariadb.org/projects/MXS).


## Changed Features


### [MXS-5122](https://jira.mariadb.org/browse/MXS-5122) Scale everything according to the amount of available container resources


If MaxScale is running in a container, it will adapt to amount of resources (CPUs and
memory) available in the container. See [threads](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
and [query_classifier_cache_size](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
for more information.


## Dropped Features


## Deprecated Features


## New Features


### [MXS-3628](https://jira.mariadb.org/browse/MXS-3628) Fully support inclusion and exclusion in projection document of find


[NoSQL](../mariadb-maxscale-24-08-beta-protocols/mariadb-maxscale-2408-maxscale-2408-beta-nosql-protocol-module.md) now supports the exclusion
of any field and not only `<code>_id</code>`. Further, fields can also be added
and the value of an existing field reset using expressions.


### [MXS-4842](https://jira.mariadb.org/browse/MXS-4842) Safe failover and safe auto_failover


Added a *safe*-option to MariaDB Monitor *auto-failover*. *safe* does not
perform failover if data loss is certain. Equivalent manual command added.
See [monitor documentation](../mariadb-maxscale-2408-beta-maxscale-24-08-beta-monitors/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-monitor.md)
for more information.


### [MXS-4897](https://jira.mariadb.org/browse/MXS-4897) Add admin_ssl_cipher setting


Enabled REST-API TLS ciphers can be tuned with the global setting
[admin_ssl_cipher](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md).


### [MXS-4986](https://jira.mariadb.org/browse/MXS-4986) Add low overhead trace logging


The new
[trace_file_dir](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md) and
[trace_file_size](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
parameters can be used to enable a trace log that writes messages from all log
levels to a set of rotating log files.


This feature is an alternative to enabling
[log_info](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md) which is is not
always feasible in a production system due to the high volume of log data that
it creates. This overhead of writing large amounts of trace logging data could
be mitigated by placing the log directory on a volatile in-memory filesystem but
this risks losing important warning and error messages if the system were to be
restarted.


The new trace logging mechanism combines the best of both worlds by writing the
normal log messages to the MaxScale log while also writing the info level log
messages into a separate set of rotating log files. This way, the important
messages are kept even if the system is restarted while still allowing the
low-level trace logging to be used to analyze the root causes of client
application problems.


### [MXS-5016](https://jira.mariadb.org/browse/MXS-5016) Add support for MongoDB Compass


[NoSQL](../mariadb-maxscale-24-08-beta-protocols/mariadb-maxscale-2408-maxscale-2408-beta-nosql-protocol-module.md) now implements the commands needed by
[MongoDB Compass](https://www.mongodb.com/products/tools/compass), which
now can be used for browsing NoSQL collections.


### [MXS-5037](https://jira.mariadb.org/browse/MXS-5037) Track reads and writes at the server level


In addition to the existing `<code>routed_packets</code>` counter in the service and server
statistics, the number of reads and writes is also tracked with the new
`<code>routed_writes</code>` and `<code>routed_reads</code>` counters.


### [MXS-5041](https://jira.mariadb.org/browse/MXS-5041) Don't replay autocommit statements with transaction_replay


With `<code>transaction_replay_safe_commit=true</code>` (the default), readwritesplit will no
longer replay statements that were executed with `<code>autocommit=1</code>`. This means that
a statement like `<code>INSERT INTO software(name) VALUES ('MariaDB')</code>` will not be
replayed if it's done outside of a transaction and its execution was
interrupted. This feature makes `<code>transaction_replay</code>` safer by default and avoids
duplicate execution of statements that may commit a transaction.


### [MXS-5047](https://jira.mariadb.org/browse/MXS-5047) Test primary server writability in MariaDB Monitor


MariaDB Monitor can perform a write test on the primary server. Monitor can
be configured to perform a failover if the write test fails. This may help
deal with storage engine or disk hangups.
See [monitor documentation](../mariadb-maxscale-2408-beta-maxscale-24-08-beta-monitors/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-monitor.md)
for more information.


### [MXS-5049](https://jira.mariadb.org/browse/MXS-5049) Implement host_cache_size in MaxScale


Similar to MariaDB, MaxScale now stores the last 128 hostnames returned by
reverse name lookups. This improves the performance of clusters where clients
are authenticated based on a hostname instead of a plain IP address. The new
[host_cache_size](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
parameter can be used to control the size of the cache and the cache can be
disabled with `<code>host_cache_size=0</code>`.


### [MXS-5069](https://jira.mariadb.org/browse/MXS-5069) support bulk returning all individual results


MaxScale now supports the protocol extensions added in MariaDB 11.5.1 where the
bulk execution of statements returns multiple results.


### [MXS-5075](https://jira.mariadb.org/browse/MXS-5075) Add switchover option which leaves old primary server to maintenance mode


MariaDB Monitor module command *switchover* can now be called with key-value
arguments. This form also supports leaving the old primary in maintenance mode
instead of redirecting it. See
[monitor documentation](../mariadb-maxscale-2408-beta-maxscale-24-08-beta-monitors/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-monitor.md)
for more information.


### [MXS-5136](https://jira.mariadb.org/browse/MXS-5136) Extend the number of supported aggregation stages and operations.


[NoSQL](../mariadb-maxscale-24-08-beta-protocols/mariadb-maxscale-2408-maxscale-2408-beta-nosql-protocol-module.md) now implements the command
[aggregate](../mariadb-maxscale-24-08-beta-protocols/mariadb-maxscale-2408-maxscale-2408-beta-nosql-protocol-module.md)
and provides a number of aggregation pipe line
[stages](../mariadb-maxscale-24-08-beta-protocols/mariadb-maxscale-2408-maxscale-2408-beta-nosql-protocol-module.md) and
[operators](../mariadb-maxscale-24-08-beta-protocols/mariadb-maxscale-2408-maxscale-2408-beta-nosql-protocol-module.md).


### MaxGUI


Numerous additions have been added and improvements made to MaxGUI.
The most notable ones are listed here:


* [MXS-3852](https://jira.mariadb.org/browse/MXS-3852) Show Only SQL editor Sessions/Connections Status Separately On Maxscale GUI
* [MXS-3952](https://jira.mariadb.org/browse/MXS-3952) Auto-inject `<code>LIMIT</code>` and `<code>OFFSET</code>`, and allow no limit
* [MXS-4370](https://jira.mariadb.org/browse/MXS-4370) Auto expand active schema node
* [MXS-4849](https://jira.mariadb.org/browse/MXS-4849) Export the visualized configuration graph
* [MXS-4886](https://jira.mariadb.org/browse/MXS-4886) Query Editor: Add UI for creating and altering object


## Bug fixes


## Known Issues and Limitations


There are some limitations and known issues within this version of MaxScale.
For more information, please refer to the [Limitations](../mariadb-maxscale-24-08-beta-about/mariadb-maxscale-2408-maxscale-2408-beta-limitations-and-known-issues-within-mariadb-maxscale.md) document.


## Packaging


RPM and Debian packages are provided for the supported Linux distributions.


Packages can be downloaded [here](https://mariadb.com/downloads/#mariadb_platform-mariadb_maxscale).


## Source Code


The source code of MaxScale is tagged at GitHub with a tag, which is identical
with the version of MaxScale. For instance, the tag of version X.Y.Z of MaxScale
is `<code>maxscale-X.Y.Z</code>`. Further, the default branch is always the latest GA version
of MaxScale.


The source code is available [here](https://github.com/mariadb-corporation/MaxScale).
