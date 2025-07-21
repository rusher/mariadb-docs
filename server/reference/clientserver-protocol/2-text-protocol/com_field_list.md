# COM\_FIELD\_LIST

**Warning**: This command is deprecated and not used by MariaDB connectors any more. Please use the SQL statements [SHOW COLUMNS](../../sql-statements/administrative-sql-statements/show/show-columns.md) or [SELECT FROM INFORMATION\_SCHEMA.COLUMNS](../../system-tables/information-schema/information-schema-tables/information-schema-columns-table.md) instead.

#### Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) 0x04 : COM\_FIELD\_LIST Header

#### Response

* n [resultset row](../4-server-response-packets/resultset-row.md)
* [EOF\_Packet](../4-server-response-packets/eof_packet.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
