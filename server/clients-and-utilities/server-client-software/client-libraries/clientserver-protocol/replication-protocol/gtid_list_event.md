
# GTID_LIST_EVENT

Logged in every binlog to record the current [replication](../../../../../server-usage/replication-cluster-multi-master/standard-replication/README.md) state. Consists of the last [GTID](../../../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md) seen for each replication domain.


The Global Transaction ID, [GTID](../../../../../server-usage/replication-cluster-multi-master/standard-replication/gtid.md) for short, consists of three components:


* replication domain ID
* master server ID
* sequence ID


It's represented as three numbers separated with dashes '-'
For example:
`1-1222-1011`


It's usually written after the [Format Description Event](format_description_event.md), if binary log encryption is enabled it is written after the [Start Encryption Event](start_encryption_event.md).


**Note**: In case of encrypted binlog files ([encrypt_binlog](../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md) is set to ON), this event is written just after the [START_ENCRYPTION_EVENT](start_encryption_event.md)


#### Header


* Event type is 163 (0xa3)


#### Fields



* [uint<4>](../protocol-data-types.md#fixed-length-integers) Number of GTIDs
* for (i=0; i < gtid_count; i++)

  * [uint<4>](../protocol-data-types.md#fixed-length-integers) Replication Domain ID
  * [uint<4>](../protocol-data-types.md#fixed-length-integers) Server_ID
  * [uint<8>](../protocol-data-types.md#fixed-length-integers) GTID sequence



The minimum content size for 1 GTID is:
4 + (4 + 4 + 8) * 1 = 20 bytes


### Example With 1 GTID, With CRC32


From the [mysqlbinlog](../../../../mariadb-binlog/README.md) utility:


170824 9:52:04 server id 10124 end_log_pos 292 CRC32 **0xb6d8f0a8** 	Gtid list **[0-10124-3584]**


```
a4 85 9e 59 a3 8c 27 00  00 2b 00 00 00 24 01 00  ...Y..'..+...$..
00 00 00 01 00 00 00 00  00 00 00 8c 27 00 00 00  ............'...
0e 00 00 00 00 00 00 a8  f0 d8 b6                 ..........
```


#### Header, 19 Bytes


* Event Time = a4 85 9e 59 ===> 2017-08-24 9:52:04
* Event Type = a3 => 163
* Server_id = 8c 27 00 00 => 00 00 27 8c => 10124
* Event Size = 2b => 43 (header[19] + 1 GTID(20 bytes) + CRC32[4]
* Next Pos = 24 01 00 00 => 00 00 01 24 => 292
* Flags = 00 => 0


#### Content, Variable Size, is (4 + (4 + 4 + 8 ) * n_GTIDs) Bytes


The content example with one GTID is 20 bytes + 4 bytes CRC32:


* Number of GTIDs[4] = 01 00 00 00 => 1
* GTID[0] replication_domain[4] = 00 00 00 00 => 0
* GTID[0] Server_id[4] = 8c 27 00 00 => 00 00 27 8c => 10124
* GTID[0] Sequence[8] = 00 0e 00 00 00 00 00 00 ===> 3584
* crc32[4] = a8 f0 d8 b6 => b6 d8 f0 a8 => 0xb6d8f0a8


CC BY-SA / Gnu FDL

