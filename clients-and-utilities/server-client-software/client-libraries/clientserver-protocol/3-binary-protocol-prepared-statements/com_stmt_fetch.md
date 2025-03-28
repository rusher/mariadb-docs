# COM_STMT_FETCH

Fetch rows from a prepared statement.

A [COM_STMT_EXECUTE](com_stmt_execute.md) with a non-zero cursor flag must have been successfully executed before any COM_STMT_FETCH commands can be executed.

#

### Fields

* [int<1>](/en/protocol-field-types/#fixed-length-integers) 0x1C COM_STMT_FETCH header.
* [int<4>](/en/protocol-field-types/#fixed-length-integers) statement id.
* [int<4>](/en/protocol-field-types/#fixed-length-integers) number of rows to fetch.

#

### Response

Returns one or more [binary result set rows](../4-server-response-packets/resultset-row.md#binary-resultset-row) followed by an [EOF packet](https://mariadb.com/kb/en/library/eof_packet/).