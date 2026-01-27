# wsrep\_sst\_mariabackup

#### `wsrep_sst_mariabackup` Variables

The `wsrep_sst_mariabackup` script handles the actual data transfer and processing during an SST. The variables it reads from the `[sst]` group control aspects of the backup format, compression, transfer mechanism, and logging.

The `wsrep_sst_mariadbbackup` script parses the following options:

* `sfmt` (streamfmt)
  * Default: `mbstream`
  * Description: Defines the streaming format used by `mariabackup` for the SST. `mbstream` indicates that `mariabackup` will output a continuous stream of data. Other potential values (though not explicitly shown as defaults) might be related to different backup methods or tools.

***

* `tfmt` (transferfmt)
  * Default: `socat`
  * Description: Specifies the transfer format or utility used to move the data stream from the donor to the joiner node. `socat` is a common command-line tool for data transfer, often used for setting up various network connections.

***

* `sockopt` (socket options)
  * Description: Allows additional socket options to be passed to the underlying network communication. This includes settings for TCP buffers, keep-alives, or other network-related tunables to optimize transfer performance.

***

* `progress`
  * Description: Controls whether progress information about the SST is displayed or logged. Enabling this option provides visual indicators or detailed log entries about the transfer's advancement.

***

* `ttime` (time)
  * Default: `0`
  * Description: A timeout value in seconds for certain operations during the SST, or a flag related to timing the transfer. A value of `0` indicates no timeout or that timing is handled elsewhere.

***

* `cpat`
  * Description: Related to a "copy pattern" or specific path handling during the SST. Its function depends on how the `wsrep_sst_mariabackup` script uses this pattern for file or directory management.

***

* `scomp` (compressor)
  * Description: Specifies the compression utility to be used on the data stream before transfer. Common values include `gzip`, `pigz`, `lz4`, or `qpress`, which reduce the data size for faster transmission over the network.

***

* `sdecomp` (decompressor)
  * Description: Specifies the decompression utility to be used on the receiving end (joiner node) to decompress the data stream that was compressed by `scomp`. It should correspond to the `scomp` setting.

***

* `rlimit` (resource limit)
  * Description: Sets a maximum data transfer rate for State Snapshot Transfers (SST) in which the node serves as a donor. The `rlimit` parameter accepts any value supported by the `pv` utility’s `--rate-limit` option. Note that using this option requires `progress` to be specified and the `pv` utility to be installed on the system.

***

* `uextra` (use-extra)
  * Default: `0`
  * Description: Controls the SST connection method that `mariabackup` uses to connect to the local MariaDB server.  By default _(_`uextra=0`_),_ mariabackup connects through the standard database por&#x74;_._ When `uextra=1` is enabled, the connection attempts to use either:
    * The unix socket (if available), or&#x20;
    * The extra\_port (if specified in MariaDB server settings).

***

* `speciald` (sst-special-dirs)
  * Default: `1`
  * Description: A boolean flag that controls whether `mariabackup` handles  special directories (e.g., `innodb_log_group_home_dir`, `datadir`) in a specific way during the SST, rather than just copying them as regular files. This is important for maintaining data consistency.

***

* `stimeout` (sst-initial-timeout)
  * Default: `300`
  * Description: Sets an initial timeout in seconds for the SST process. If the SST doesn't make progress or complete within this initial period, it might be aborted.

***

* `ssyslog` (sst-syslog)
  * Default: `0`
  * Description: A boolean flag (0 or 1) that controls whether SST-related messages should be logged to syslog. This can be useful for centralized logging and monitoring of Galera cluster events.

***

* `sstlogarchive` (sst-log-archive)
  * Default: `1`
  * Description: A boolean flag (0 or 1) that determines whether SST logs should be archived. Archiving logs helps in post-mortem analysis and troubleshooting of SST failures.

***

* `sstlogarchivedir` (sst-log-archive-dir)
  * Description: Specifies the directory where SST logs should be archived if `sstlogarchive` is enabled.

