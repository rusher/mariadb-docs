
# COM_STMT_CLOSE

Closes a previously prepared statement.


### Direction


Client to server.


### Implemented by


* [mysql_stmt_close()](../../../../../../connectors/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_close.md)
* [mysql_stmt_prepare()](../../../../../../connectors/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_prepare.md)


### Fields



* [int<1>](../protocol-data-types.md#fixed-length-integers) 0x19 COM_STMT_CLOSE header
* [int<4>](../protocol-data-types.md#fixed-length-integers) Statement id



#### Example


05 00 00 00 19 04 00 00 00 


#### Response


No response from server.

