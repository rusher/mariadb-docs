# COM_SET_OPTION

Enables or disables server option.

#

### Fields

* [int<1>](/en/protocol-field-types/#fixed-length-integers) 0x1B COM_SET_OPTION
* [int<2>](/en/protocol-field-types/#fixed-length-integers) option

#

#### Options

| Constant | Value |
| MYSQL_OPTION_MULTI_STATEMENTS_ON | 0 |
| MYSQL_OPTION_MULTI_STATEMENTS_OFF | 1 |

#

### Response

[EOF Packet](../4-server-response-packets/eof_packet.md) on success or [ERR packet](../4-server-response-packets/err_packet.md).