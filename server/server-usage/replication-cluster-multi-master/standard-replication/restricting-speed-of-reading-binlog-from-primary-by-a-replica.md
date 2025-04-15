
# Restricting Speed of Reading Binlog from Primary by a Replica

When a replica starts after being stopped for some time, or a new replica starts
that was created from a backup from some time back, a lot of old binlog events
may need to be downloaded from the primary. If this happens from many replicas
simultaneously, it can put a lot of load on the primary.


The **read_binlog_speed_limit** option can be used to reduce such load, by
limiting the speed at which events are downloaded. The limit is given as
maximum kilobytes per second to download on one replica connection.


With this option set, the replication I/O thread will limit the rate of
download. Since the I/O thread is often much faster to download events than
the SQL thread is at applying them, an appropriate value for
**read_binlog_speed_limit** may reduce load spikes on the primary without
much limit in the speed of the replica.


The option **read_binlog_speed_limit** is available starting from [MariaDB 10.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md).


#### `<code>read_binlog_speed_limit</code>`


* Description: Maximum speed(KB/s) to read binlog from primary.
* Commandline: `<code class="fixed" style="white-space:pre-wrap">--read-binlog-speed-limit[=#]</code>`
* Scope: Global
* Dynamic: Yes
* Data Type: `<code>numeric</code>`
* Default Value: `<code>0</code>`
* Range: `<code>0</code>` to `<code>4294967295</code>`
* Introduced: [MariaDB 10.2.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1023-release-notes.md)


