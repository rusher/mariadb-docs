# COM_STMT_PREPARE

Prepares a statement on the server.

**Not all statements can be prepared**.
See [PREPARE](../../../../../reference/sql-statements-and-structure/sql-statements/prepared-statements/prepare-statement.md#permitted-statements) for a list of statements that can be prepared.

#

## Implemented by

* [mariadb_stmt_execute_direct()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mariadb_stmt_execute_direct)
* [mysql_stmt_prepare()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_prepare)

#

# Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) 0x16 COM_STMT_PREPARE header
* [string<EOF>](../protocol-data-types.md#end-of-file-length-strings) SQL Statement

#

## Example

```
1F 00 00 00 16 53 45 4C 45 43 54 20 2A 20 46 52 .....SELECT * FR
1F 4D 20 74 65 73 74 5F 62 69 6E 64 5F 72 65 73 OM test_bind_res
75 6C 74 ult
```

#

## COM_STMT_PREPARE response

If anything goes wrong, the server will send an [ERR_Packet](../4-server-response-packets/err_packet.md).
If the command succeeds, different packets will be received:

* [COM_STMT_PREPARE_OK](#COM_STMT_PREPARE_OK)
* if number of parameters (count of '?' placeholders) > 0

 * for each parameter:

 * [column definition packet](../4-server-response-packets/resultset-row.md#column-definition-packet)
 * if !DEPRECATE_EOF [eof_packet](../4-server-response-packets/eof_packet.md)
* if prepared statement returns result set and number of result set columns > 0

 * for each column:

 * [column definition packet](../4-server-response-packets/resultset-row.md#column-definition-packet)
 * if !DEPRECATE_EOF [eof_packet](../4-server-response-packets/eof_packet.md)

#

## COM_STMT_PREPARE_OK

* [int<1>](../protocol-data-types.md#fixed-length-integers) 0x00 COM_STMT_PREPARE_OK header
* [int<4>](../protocol-data-types.md#fixed-length-integers) statement id
* [int<2>](../protocol-data-types.md#fixed-length-integers) number of columns in the returned result set (or 0 if statement does not return result set)
* [int<2>](../protocol-data-types.md#fixed-length-integers) number of prepared statement parameters ('?'
placeholders)
* [string<1>](../protocol-data-types.md#fixed-length-strings) -not used-
* [int<2>](../protocol-data-types.md#fixed-length-integers) number of warnings