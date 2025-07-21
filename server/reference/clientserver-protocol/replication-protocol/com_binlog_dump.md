# COM\_BINLOG\_DUMP

This is a command the slave sends to the master after [COM\_REGISTER\_SLAVE](com_register_slave.md).

The master server sends the [binlog events](1-binlog-events.md) from the requested file and position, or if GTID registration is in use, from the GTID value set in the earlier registration phase.

The payload is:

* [uint<1>](../protocol-data-types.md#fixed-length-bytes) command (COM\_BINLOG\_DUMP = 0x12)
* [uint<4>](../protocol-data-types.md#fixed-length-bytes) The requested binlog position
* [uint<2>](../protocol-data-types.md#fixed-length-bytes) Flags
* [uint<4>](../protocol-data-types.md#fixed-length-bytes) Slave server\_id
* [string](../protocol-data-types.md#fixed-length-bytes) The requested binlog file name

**Note**

* Flags, usually set to 0.\
  It can be set to BINLOG\_SEND\_ANNOTATE\_ROWS\_EVENT (0x02)\
  if the slave server wants to receive the MariaDB 10 [ANNOTATE\_ROWS](annotate_rows_event.md) events.\
  It can also be set to BINLOG\_DUMP\_NON\_BLOCK (1):\
  in the case the slave is receiving an EOF packet after last event sent by the master.
* Requested binlog position can be 4 when registering to master server for the very first time\
  or when requesting events from a particular binlog file from the beginning of it.
* The requested binlog file can empty when registering for the very first time if master log file is unknown\
  or with GTID registration (not required).
* After sending events to the replica the server kills connection.

When replication resumes or it is restarted (STOP SLAVE; START SLAVE) the slave server always\
sends the latest binlog file name and position even if GTID registration is in place.

#### Example of COM\_BINLOG\_DUMP

```
1b 00 00 00 12 34 06 00    00 02 00 75 27 00 00 6d    .....4.....u'..m
  79 73 71 6c 2d 62 69 6e    2e 30 30 30 30 33 34       ysql-bin.000034
```

After 4 bytes network protocol header we can see:

* command \[1] = 12
* requested binlog position \[4] = 34 06 00 00 => 00 00 06 34 = 1588
* flags \[2] = 02 00 => 2 = BINLOG\_SEND\_ANNOTATE\_ROWS\_EVENT
* binlog file\[n] = mysql-bin.000034

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
