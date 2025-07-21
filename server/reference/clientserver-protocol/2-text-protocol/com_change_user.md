
# COM_CHANGE_USER

COM_CHANGE_USER resets the connection and re-authenticates with the given credentials. The packet is identical to the authentication packet in the connection handshake.


#### Fields



* [int<1>](../protocol-data-types.md#fixed-length-integers) 0x11 : COM_CHANGE_USER header
* [string<NUL>](../protocol-data-types.md#null-terminated-strings) username
* if (server_capabilities & CLIENT_SECURE_CONNECTION) 

  * [int<1>](../protocol-data-types.md#fixed-length-integers) length of authentication response
  * string authentication response
* else

  * [string<NUL>](../protocol-data-types.md#null-terminated-strings) authentication response
* [string<NUL>](../protocol-data-types.md#null-terminated-strings) default schema name
* [int<2>](../protocol-data-types.md#fixed-length-integers) client character collation
* if (server_capabilities & CLIENT_PLUGIN_AUTH)

  * [string<NUL>](../protocol-data-types.md#null-terminated-strings) authentication plugin name
* if (server_capabilities & CLIENT_CONNECT_ATTRS)

  * [int<lenenc>](../protocol-data-types.md#length-encoded-integers) size of connection attributes
  * loop:

    * [string<lenenc>](../protocol-data-types.md#length-encoded-strings) key
    * [string<lenenc>](../protocol-data-types.md#length-encoded-strings) value



#### Response


Server response is like [connection authentication](../1-connecting/connection.md) :


* An OK packet in case of success [OK_Packet](../4-server-response-packets/ok_packet.md).
* An error packet in case of error [ERR_Packet](../4-server-response-packets/err_packet.md).
* Authentication switch 

  * If the client or server doesn't have PLUGIN_AUTH capability:

    * Server sends 0xFE byte .
    * Client sends old_password.
  * else

    * Server sends [Authentication switch request](#authentication-switch-request).
    * Client may have many exchanges with the server according to the [Plugin](#plugin-list).
  * Authentication switch ends with server sending either [OK_Packet](../4-server-response-packets/ok_packet.md) or [ERR_Packet](../4-server-response-packets/err_packet.md).


If the authentication fails more than three times, all future `COM_CHANGE_USER` commands on the connection will return
the `#08S01 Unknown command` error. This is an anti-brute-force mechanism designed to prevent rapid guessing of passwords.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
