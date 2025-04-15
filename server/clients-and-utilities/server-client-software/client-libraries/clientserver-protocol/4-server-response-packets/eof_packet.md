
# EOF_Packet

The eof packet marks the end of a resultset and returns status and warnings.


When testing for an EOF packet, the packet size must be less than 9 bytes in length. 
Resultset can send data that begins with a 0xfe byte, but then the packet length will be greater than 9.


#### Fields



* [int<1>](../protocol-data-types.md#fixed-length-integers) 0xfe : EOF header
* [int<2>](../protocol-data-types.md#fixed-length-integers) warning count
* [int<2>](../protocol-data-types.md#fixed-length-integers) [server status](ok_packet.md#server-status-flag)





