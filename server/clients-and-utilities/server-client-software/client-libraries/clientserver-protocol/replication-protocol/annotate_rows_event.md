
# ANNOTATE_ROWS_EVENT

ANNOTATE_ROWS_EVENT events accompany row events and describe the query which caused the row event.


You can enable this with [--binlog-annotate-row-events](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) (default on from [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes)).


In the binary log, each Annotate_rows event precedes the corresponding Table map event.


For additional information refer to the [annotate_rows_log_event](../../../../mariadb-binlog/annotate_rows_log_event.md) documentation.


**Note**: the master server sends ANNOTATE_ROWS_EVENT events only
if the Slave server connects with the BINLOG_SEND_ANNOTATE_ROWS_EVENT flag (value is 2)
in the COM_BINLOG_DUMP Slave Registration phase.


#### Header


* Event Type is 160 (0xa0)


#### Fields



* [string<EOF>](../protocol-data-types.md#fixed-length-bytes) The SQL statement (not null-terminated)



### Complete Example with CRC32


```
ee b7 15 5a a0 01 00 00  00 36 00 00 00 80 0b 00  ...Z.....6......
00 00 00 69 6e 73 65 72  74 20 69 6e 74 6f 20 74  ...insert into t
65 73 74 2e 74 34 20 76  61 6c 75 65 73 28 31 30  est.t4 values(10
30 29 6d 4c 42 33                                 0)mLB3
```

