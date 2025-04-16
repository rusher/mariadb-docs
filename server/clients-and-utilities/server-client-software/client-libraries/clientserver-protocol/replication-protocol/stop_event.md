
# STOP_EVENT

The master server writes the event to the [binary log](../../../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) when it shuts down or when resuming after a mysqld process crash.


A new binary log file is always created but there is no ROTATE_EVENT.


STOP_EVENT is then the last written event after clean shutdown or resuming a crash.


this event is never sent to slave servers.


### Header


* Event header with EventType set to STOP_EVENT (0x03).
* Event header NextPos set to EOF
* No special flags added.


### Fields


* The event has no data


### Example With CRC32 (Last 4 Bytes)


Event size = header[19] + 0 bytes data + 4 CRC32 = 23


```
3a b8 15 5a 03 01 00 00  00 17 00 00 00 09 0c 00  ..Z............
00 00 00 4e 99 ee 2c                              ...N..,
```

<span></span>
