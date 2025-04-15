# COM_QUERY

With the COM_QUERY command, the client sends the server an SQL statement to be executed immediately.

#

## Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) 0x03 : COM_QUERY header
* [string<EOF>](../protocol-data-types.md#end-of-file-length-strings) SQL statement

The SQL statement should be properly escaped. The escape character is usually a backslash '\' = 0x5c. However, if the status flag returned by the last [OK Packet](../4-server-response-packets/ok_packet.md#status-flag) had NO_BACKSLASH_ESCAPES bit set then the escape character is a single quote(' = 0x60)

If the escape character is a backslash, the following characters are escaped:

* single quote (' = 0x60)
* back slash (\ = 0x5c)
* double quote (" = 0x22)
* null character (0x00)

If the escape character is a single quote, only the single quote (' = 0x60) can be escaped.

#

## Response

The server can answer with 4 different responses that can be differentiated by the first byte (packet header):

* 0xFF - [ERR_Packet](../4-server-response-packets/err_packet.md) if any error occurs.
* 0x00 - [OK_Packet](../4-server-response-packets/ok_packet.md) when query execution works without resultset.
* 0xFB - [LOCAL_INFILE Packet](/en/local_infile-packet/) if the query was "LOCAL INFILE ...".
* Or a [Resultset](../4-server-response-packets/resultset-row.md), when the query returns results (in case of a SELECT query for example).

#

## Example

| 1b 00 00 00 03 44 52 4f 50 20 54 41 42 4c 45 20 | .....DROP TABLE |
| 49 46 20 45 58 49 53 54 53 20 62 75 6c 6b 31 | IF EXISTS bulk1 |