# 2-Binlog Event Header

All the [binlog events](/en/binlog-events/) stored in a [binary log file](../../../../../server-usage/programming-customizing-mariadb/stored-routines/binary-logging-of-stored-routines.md) have a common structure:

* an event header
* event data

#

## Event Header Structure, 19 Bytes

* [uint<4>](../protocol-data-types.md#fixed-length-bytes) Timestamp (creation time)
* [uint<1>](../protocol-data-types.md#fixed-length-bytes) [Event Type](#event-type) (type_code)
* [uint<4>](../protocol-data-types.md#fixed-length-bytes) Server_id (server which created the event)
* [uint<4>](../protocol-data-types.md#fixed-length-bytes) Event Length (header + data)
* [uint<4>](../protocol-data-types.md#fixed-length-bytes) Next Event position
* [uint<2>](../protocol-data-types.md#fixed-length-bytes) [Event flags](#event-flag)

**Note**: if CRC32 is in use, the Event Length is 4 bytes bigger in size.
The 4 bytes CRC32 are written at the end of the event (just after the last 'data' byte).

#

### Encrypted Binlog Events

For encrypted binlog events, only the event length is in plaintext and everything else is encrypted.

To decrypt the binlog event:

* Store the event length in memory
* Move the timestamp into the event length position
* Decrypt the whole payload except the first four bytes
* Move the timestamp back to its original position
* Copy the original event length back to its position

Regardless of the cipher used to encrypt the binlogs, the encrypted data will be the same size as the original unencrypted event. For events that are encrypted in CBC mode and whose length is not a multiple of the cipher block size, the final partial block is encrypted using a form of [residual block termination](https://en.wikipedia.org/wiki/Residual_block_termination):

* Encrypt the current IV of the binlog file in ECB mode
* XOR the remaining bytes with the encrypted IV

#

## Event Type

| Hex | Event type description |
| --- | --- |
| Hex | Event type description |
| 0x02 | [QUERY_EVENT](query_event.md) |
| 0x03 | [STOP_EVENT](stop_event.md) |
| 0x04 | [ROTATE_EVENT](rotate_event.md) |
| 0x10 | [XID_EVENT](xid_event.md) |
| 0x0d | [RAND_EVENT](rand_event.md) |
| 0x0e | [USER_VAR_EVENT](user_var_event.md) |
| 0x0f | [FORMAT_DESCRIPTION_EVENT](format_description_event.md) |
| 0x13 | [TABLE_MAP_EVENT](table_map_event.md) |
| 0x1b | [HEARTBEAT_LOG_EVENT](heartbeat_log_event.md) |
| 0xa0 | [ANNOTATE_ROWS_EVENT](annotate_rows_event.md) |
| 0xa1 | [BINLOG_CHECKPOINT_EVENT](binlog_checkpoint_event.md) |
| 0xa2 | [GTID_EVENT](gtid_event.md) |
| 0xa3 | [GTID_LIST_EVENT](gtid_list_event.md) |
| 0xa4 | [START_ENCRYPTION_EVENT](start_encryption_event.md) |
| 0xa5 | [QUERY_COMPRESSED_EVENT](query_event.md) |
| 0xa6 | [WRITE_ROWS_COMPRESSED_V1](rows_event_v1v2-rows_compressed_event_v1.md) |
| 0xa7 | [UPDATE_ROWS_COMPRESSED_V1](rows_event_v1v2-rows_compressed_event_v1.md) |
| 0xa8 | [DELETE_ROWS_COMPRESSED_V1](rows_event_v1v2-rows_compressed_event_v1.md) |
| 0xa9 | [WRITE_ROWS_V1](rows_event_v1v2-rows_compressed_event_v1.md) |
| 0xaa | [UPDATE_ROWS_V1](rows_event_v1v2-rows_compressed_event_v1.md) |
| 0xab | [DELETE_ROWS_V1](rows_event_v1v2-rows_compressed_event_v1.md) |

#

## Fake Events

These are generated on the fly, never written.

| 0x04 | [FAKE_ROTATE_EVENT](fake-rotate_event.md) |
| 0xa3 | [FAKE_GTID_LIST_EVENT](fake-gtid_list-event.md) |

#

## Event Flag

| Hex | Event flag description |
| --- | --- |
| Hex | Event flag description |
| 0x0001 | LOG_EVENT_BINLOG_IN_USE_FThis flag only makes sense for Format_description_log_event. It is set when the event is written, and *reset* when a binlog file is closed (yes, it's the only case when MySQL modifies already written part of binlog). Thus it is a reliable indicator that binlog was closed correctly. |
| 0x0002 | LOG_EVENT_FORCED_ROTATE_F(unused) |
| 0x0004 | LOG_EVENT_THREAD_SPECIFIC_F If the query depends on the thread (for example: TEMPORARY TABLE) |
| 0x0008 | LOG_EVENT_SUPPRESS_USE_F Suppress the generation of 'USE' statements before the actual statement. This flag should be set for any events that does not need the current database set to function correctly. Most notable cases are 'CREATE DATABASE' and 'DROP DATABASE'. |
| 0x0010 | LOG_EVENT_UPDATE_TABLE_MAP_VERSION_F (unused) |
| 0x0020 | LOG_EVENT_ARTIFICIAL_F Artificial events are created arbitarily and not written to binary log.These events should not update the master log position when slave SQL thread executes them. |
| 0x0040 | LOG_EVENT_RELAY_LOG_F Events with this flag set are created by slave IO thread and written to relay log |
| 0x0080 | LOG_EVENT_IGNORABLE_F For an event, 'e', carrying a type code, that a slave,'s', does not recognize, 's' will check 'e' forLOG_EVENT_IGNORABLE_F, and if the flag is set, then 'e'is ignored. Otherwise, 's' acknowledges that it has found an unknown event in the relay log. |
| 0x0100 | LOG_EVENT_NO_FILTER_F (no description yet) |
| 0x0200 | LOG_EVENT_MTS_ISOLATE_F (no description yet) |
| 0x8000 | LOG_EVENT_SKIP_REPLICATION_F Flag set by application creating the event (with @@skip_replication);the slave will skip replication of such eventsif --replicate-events-marked-for-skip is not set to REPLICATE.This is a MariaDB flag; we allocate it from the end of the available values to reduce risk of conflict with new MySQL flags. |

#

### Event Header example of [FORMAT_DESCRIPTION_EVENT](format_description_event.md)

This is the first event in the binlog file at pos 4

```
a4 85 9e 59 0f 8c 27 00 00 f5 00 00 00 f9 00 00 ...Y..'.........
00 00 00 04 00 31 30 2e 31 2e 32 34 2d 4d 61 72 .....10.1.24-Mar
69 61 44 42 00 6c 6f 67 00 00 00 00 00 00 00 00 iaDB.log....
...
...
```

#

### Interpretation of First 19 Bytes of the Event (the Event Header)

* a4 85 9e 59 [4] Timestamp => 59 9e 85 a4 => 1503561124 = 2017-08-24 09:52:04
* 0f [1] Event Type = 0x0f = FORMAT_DESCRIPTION_EVENT
* 8c 27 00 00 [4] Server_id => 00 00 27 8c = 10124
* f5 00 00 00 [4] Event length => 00 00 00 f5 => 245
* f9 00 00 00 [4] Next Event pos => 00 00 00 f9 => 249 (pos 4 + event size)
* 00 00 [2] Event flags = 0