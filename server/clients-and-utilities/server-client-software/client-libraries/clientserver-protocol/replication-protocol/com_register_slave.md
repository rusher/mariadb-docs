# COM_REGISTER_SLAVE

This command is sent by the slave server in order to start MariaDB replication and should be sent before requesting binlog events with [COM_BINLOG_DUMP](com_binlog_dump.md).

The payload is:

* [uint<1>](../protocol-data-types.md#fixed-length-bytes) command (COM_REGISTER_SLAVE = 0x15)
* [uint<4>](../protocol-data-types.md#fixed-length-bytes) Slave server_id
* [uint<1>](../protocol-data-types.md#fixed-length-bytes) Slave hostname length
* [string<n>](../protocol-data-types.md#fixed-length-bytes) Hostname
* [uint<1>](../protocol-data-types.md#fixed-length-bytes) Slave username len
* [string<n>](../protocol-data-types.md#fixed-length-bytes) Username
* [uint<1>](../protocol-data-types.md#fixed-length-bytes) Slave password len
* [string<n>](../protocol-data-types.md#fixed-length-bytes) Slave password
* [uint<2>](../protocol-data-types.md#fixed-length-bytes) Slave connection port
* [uint<4>](../protocol-data-types.md#fixed-length-bytes) Replication rank
* [uint<4>](../protocol-data-types.md#fixed-length-bytes) Master server id

**Note**:

* Slave hostname, slave user, slave password and slave port are usually not set.
Some slave [replication parameters](/en/replication-and-binary-log-server-system-variables/) can be used for such settings (report_host, report_port etc).
* Replication rank is not set.
* Master server id is not set as well.

#

### Example of COM_REGISTER_SLAVE

The slave server is configured with:

* server-id=10101
* report-host=slave_n_1
* report-port=23241

```
1b 00 00 00 15 75 27 00 00 09 73 6c 61 76 65 5f .....u'...slave_
 6e 5f 31 00 00 c9 5a 00 00 00 00 00 00 00 00 n_1...Z.......
```

We can see from the example:

* server_id [4] = 75 27 00 00 => 10101
* hostname_len [1] = 09
* hostname[n] = slave_n_1 (9 bytes)
* username len [1] = 0 (not set)
* password len [1] = 0 (not set)
* slave port [2] = c9 5a => 23241
* rank [4] = 0
* master server id = 0