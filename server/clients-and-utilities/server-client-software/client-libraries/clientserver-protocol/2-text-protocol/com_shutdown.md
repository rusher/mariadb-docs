
# COM_SHUTDOWN

Shuts down the server. To execute this command the SHUTDOWN privilege is required.


#### Fields



* [int<1>](../protocol-data-types.md) 0x0A COM_SHUTDOWN
* [int<1>](../protocol-data-types.md) option



##### Options



|   |   |
| --- | --- |
| Constant | Value |
| SHUTDOWN_DEFAULT | 0 |



#### Response


[OK Packet](../4-server-response-packets/ok_packet.md) or [ERR packet](../4-server-response-packets/err_packet.md).


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
