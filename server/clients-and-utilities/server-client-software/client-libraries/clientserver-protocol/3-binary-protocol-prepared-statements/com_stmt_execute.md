
# COM_STMT_EXECUTE

Executes a previously prepared statement.


If specific data is large, it can be sent separately prior to this command (see [COM_STMT_SEND_LONG_DATA](com_stmt_send_long_data.md)).


If a statement is re-executed without changing the bind types, the types do not need to be sent to the server again.


### Direction


Client to server.


### Fields



* [int<1>](../protocol-data-types.md#fixed-length-integers) 0x17 : COM_STMT_EXECUTE header
* [int<4>](../protocol-data-types.md#fixed-length-integers) [statement id](#statement-id)
* [int<1>](../protocol-data-types.md#fixed-length-integers) flags:
* [int<4>](../protocol-data-types.md#fixed-length-integers) Iteration count (always 1)
* if (param_count > 0)

  * byte<(param_count + 7)/8> [null bitmap](#null-bitmap)
  * byte<1>: send type to server (0 / 1)
  * if (send type to server)

    * for each parameter :

      * byte<1>: [field type](../4-server-response-packets/result-set-packets.md)
      * byte<1>: [parameter flag](#parameter-flag)
  * for each parameter (i.e param_count times)

    * if parameter is not null

      * byte<n> [binary parameter value](#binary-parameter-encoding)



### Statement Id


Statement id is the identifier of the prepared statement (from [COM_STMT_PREPARE answer](com_stmt_prepare.md#com_stmt_prepare_ok))


#### Specific "-1" statement id value


Since MariaDB server version 10.2, value -1 (0xFFFFFFFF) can be used to indicate to use the last statement prepared on current connection if no COM_STMT_PREPARE has fail since.


This permit pipelining :


* send COM_STMT_PREPARE + COM_STMT_EXECUTE with statement id -1
* read COM_STMT_PREPARE + COM_STMT_EXECUTE response


In case COM_STMT_PREPARE returns an error, COM_STMT_EXECUTE will return an error that statement id -1 is unknown. This permits to avoid much of the network latency.


### Flag



|   |   |
| --- | --- |
| 0 | no cursor |
| 1 | read only |
| 2 | cursor for update |
| 4 | scrollable cursor |



#### Cursors


If the flags of the COM_STMT_EXECUTE request a cursor to be opened, the returned result will only contain the column definitions and the EOF that terminates it and the resultset rows are fetched using separate COM_STMT_FETCH commands.


Whether a cursor is actually opened is indicated by the SERVER_STATUS_CURSOR_EXISTS bit in the first EOF packet in the response to the COM_STMT_EXECUTE. If it is **not** set in, no cursor is opened and a normal resultset is returned.


### Parameter flag


parameter type flag byte:



|   |   |
| --- | --- |
| 128 | unsigned |



### NULL-Bitmap


The NULL-Bitmap indicates if parameters are null (one bit per parameter). If the parameter is NULL, the bit is set in the bitmap and the parameter value is not sent.


The size in bytes of the NULL-bitmap can be calculated with: `(parameter number + 7) / 8`


### Binary parameter encoding


The encoding of the COM_STMT_EXECUTE parameters are the same as the encoding of the [binary resultsets](../4-server-response-packets/result-set-packets.md#field-types).


### COM_STMT_EXECUTE response


The server can answer with 3 different responses:


* 0xff: [ERR_Packet](../4-server-response-packets/err_packet.md) if any errors occur.
* 0x00: [OK_packet](../4-server-response-packets/ok_packet.md) when query execution works without resultset.
* one (or more) [Resultset](../4-server-response-packets/result-set-packets.md), when query execution return rows (in case of SELECT query for example).


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
