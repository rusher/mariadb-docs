
# COM_RESET_CONNECTION

COM_RESET_CONNECTION Resets a connection without re-authentication.


This will :


* rollback any open transaction
* reset transaction isolation level
* reset session variables
* delete user variables
* remove temporary tables
* remove all PREPARE statement


Database will NOT be reset to initial value.


### Fields



* [int<1>](../protocol-data-types.md#fixed-length-integers) 0x1f : COM_RESET_CONNECTION Header



### Response


[ERR_Packet](../4-server-response-packets/err_packet.md) or [OK_Packet](../4-server-response-packets/ok_packet.md)


CC BY-SA / Gnu FDL

