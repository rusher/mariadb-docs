# wsrep\_sst\_mariabackup

#### `wsrep_sst_mariabackup` Variables

The `wsrep_sst_mariabackup` script handles the actual data transfer and processing during an SST. The variables it reads from the `[sst]` group control aspects of the backup format, compression, transfer mechanism, and logging.

The `wsrep_sst_mariadbbackup` script parses the following options:

```bash
~/myh/instances/10622$ cat bin/wsrep_sst_mariabackup | grep "parse_cnf sst"
    sfmt=$(parse_cnf sst streamfmt 'mbstream')
    tfmt=$(parse_cnf sst transferfmt 'socat')
    sockopt=$(parse_cnf sst sockopt)
    progress=$(parse_cnf sst progress)
    ttime=$(parse_cnf sst time 0)
    cpat=$(parse_cnf sst cpat "$cpat")
    scomp=$(parse_cnf sst compressor)
    sdecomp=$(parse_cnf sst decompressor)
    rlimit=$(parse_cnf sst rlimit)
    uextra=$(parse_cnf sst use-extra 0)
    speciald=$(parse_cnf sst 'sst-special-dirs' 1)
    stimeout=$(parse_cnf sst 'sst-initial-timeout' 300)
    ssyslog=$(parse_cnf sst 'sst-syslog' 0)
    sstlogarchive=$(parse_cnf sst 'sst-log-archive' 1)
    sstlogarchivedir=$(parse_cnf sst sst-log-archive-dir \
```

* `sfmt` (streamfmt)
  * Default: `mbstream`
  * Description: Defines the streaming format used by `mariabackup` for the SST. `mbstream` indicates that `mariabackup` will output a continuous stream of data. Other potential values (though not explicitly shown as defaults) might be related to different backup methods or tools.

***

* `tfmt` (transferfmt)
  * Default: `socat`
  * Description: Specifies the transfer format or utility used to move the data stream from the donor to the joiner node. `socat` is a common command-line tool for data transfer, often used for setting up various network connections.

***

* `sockopt` (socket options)
  * Description: Allows additional socket options to be passed to the underlying network communication. This could include settings for TCP buffers, keep-alives, or other network-related tunables to optimize the transfer performance.

***

* `progress`
  * Description: Likely controls whether progress information about the SST is displayed or logged. Setting this could enable visual indicators or detailed log entries about the transfer's advancement.

***

* `ttime` (time)
  * Default: `0`
  * Description: Possibly a timeout value in seconds for certain operations during the SST, or a flag related to timing the transfer. A value of `0` might indicate no timeout or that timing is handled elsewhere.

***

* `cpat`
  * Description: Appears to be related to a "copy pattern" or specific path handling during the SST. Its exact function would depend on how the `wsrep_sst_mariabackup` script uses this pattern for file or directory management.

***

* `scomp` (compressor)
  * Description: Specifies the compression utility to be used on the data stream before transfer. Common values could include `gzip`, `pigz`, `lz4`, or `qpress`, which reduce the data size for faster transmission over the network.

***

* `sdecomp` (decompressor)
  * Description: Specifies the decompression utility to be used on the receiving end (joiner node) to decompress the data stream that was compressed by `scomp`. It should correspond to the `scomp` setting.

***

* `rlimit` (resource limit)
  * Description: Potentially sets resource limits for the `mariabackup` process during the SST. This could include limits on CPU usage, memory, or file descriptors, preventing the SST from consuming excessive resources and impacting the server's performance.

***

* `uextra` (use-extra)
  * Default: `0`
  * Description: A boolean flag (0 or 1) that likely indicates whether to use extra or advanced features/parameters during the SST. The specific "extra" features would be determined by the `mariabackup` implementation.

***

* `speciald` (sst-special-dirs)
  * Default: `1`
  * Description: A boolean flag (0 or 1) that likely controls whether `mariabackup` should handle special directories (e.g., `innodb_log_group_home_dir`, `datadir`) in a specific way during the SST, rather than just copying them as regular files. This is important for maintaining data consistency.

***

* `stimeout` (sst-initial-timeout)
  * Default: `300`
  * Description: Sets an initial timeout in seconds for the SST process. If the SST doesn't make progress or complete within this initial period, it might be aborted.

***

* `ssyslog` (sst-syslog)
  * Default: `0`
  * Description: A boolean flag (0 or 1) that likely controls whether SST-related messages should be logged to syslog. This can be useful for centralized logging and monitoring of Galera cluster events.

***

* `sstlogarchive` (sst-log-archive)
  * Default: `1`
  * Description: A boolean flag (0 or 1) that likely determines whether SST logs should be archived. Archiving logs helps in post-mortem analysis and troubleshooting of SST failures.

***

* `sstlogarchivedir` (sst-log-archive-dir)
  * Description: Specifies the directory where SST logs should be archived if `sstlogarchive` is enabled.

