
# COM_STMT_RESET

Resets a prepared statement on the client and server to state after preparing.


### Fields



* [int<1>](../protocol-data-types.md#fixed-length-integers) 0x1A COM_STMT_RESET header
* [int<4>](../protocol-data-types.md#fixed-length-integers) Statement id



#### Response


[ERR_Packet](../4-server-response-packets/err_packet.md) or [OK_Packet](../4-server-response-packets/ok_packet.md)


#### Example



```
05 00 00 00 1A 04 00 00 00
```




CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
