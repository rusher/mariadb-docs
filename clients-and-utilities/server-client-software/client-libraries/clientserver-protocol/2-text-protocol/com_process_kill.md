# COM_PROCESS_KILL

Forces the server to terminate a specified connection.

#

### Fields

* [int<1>](/en/protocol-field-types/#fixed-length-integers) 0xC COM_PROCESS_KILL
* [int<4>](/en/protocol-field-types/#fixed-length-integers) process id

#

### Response

[OK Packet](../4-server-response-packets/ok_packet.md) or [ERR Packet](../4-server-response-packets/err_packet.md)