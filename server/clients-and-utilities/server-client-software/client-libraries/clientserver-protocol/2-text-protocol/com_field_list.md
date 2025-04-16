
# COM_FIELD_LIST

**Warning**: This command is deprecated and not used by MariaDB connectors any more. Please use the SQL statements [SHOW COLUMNS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-columns.md) or [SELECT FROM INFORMATION_SCHEMA.COLUMNS](../../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-columns-table.md) instead.


#### Fields



* [int<1>](../protocol-data-types.md#fixed-length-integers) 0x04 : COM_FIELD_LIST Header



#### Response


* n [resultset row](../4-server-response-packets/resultset-row.md)
* [EOF_Packet](../4-server-response-packets/eof_packet.md)

<span></span>
