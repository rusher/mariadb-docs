
# COM_STMT_BULK_EXECUTE

Executes a bulk insert of a previously prepared statement.


A command that returns a resultset will return an error (Error packet).


### Direction


Client to server.


### Fields



* [int<1>](../protocol-data-types.md#fixed-length-integers) 0xfa : COM_STMT_BULK_EXECUTE header
* [int<4>](../protocol-data-types.md#fixed-length-integers) statement id
* [int<2>](../protocol-data-types.md#fixed-length-integers) [bulk flags](#bulk-flags)
* if (bulk_flag & SEND_TYPES_TO_SERVER)

  * for each parameter :

    * byte<1>: [field type](../4-server-response-packets/result-set-packets.md)
    * byte<1>: [parameter type flag](#parameter-type-flag)
* until end of packet

  * for each parameter (i.e param_count times)

    * byte<1>: [parameter indicator](#parameter-indicator)
    * if indicator == NONE

      * byte<n> : binary parameter value



### Flags


#### bulk flags



|   |   |   |
| --- | --- | --- |
| SEND_UNIT_RESULTS | 64 | Return generated affected rows and auto-increment IDs as a resultset (only when server supports MARIADB_CLIENT_BULK_UNIT_RESULTS capability) |
| SEND_TYPES_TO_SERVER | 128 | Send types to server |



#### parameter type flag:



|   |   |
| --- | --- |
| 128 | unsigned |



#### parameter indicator



|   |   |   |
| --- | --- | --- |
| 0 | NONE | Value follow |
| 1 | NULL | Value is null |
| 2 | DEFAULT | For INSERT/UPDATE, value is default |
| 3 | IGNORE | Value is default for insert, Is ignored for update |



### COM_STMT_BULK_EXECUTE response


The server can answer with 3 different responses:


* 0xff: [ERR_Packet](../4-server-response-packets/err_packet.md) if any errors occur.
* 0x00: [OK_packet](../4-server-response-packets/ok_packet.md) when query execution works without resultset.
* a resultset containing affected rows and auto-increment IDs when bulk flag SEND_UNIT_RESULTS is set

