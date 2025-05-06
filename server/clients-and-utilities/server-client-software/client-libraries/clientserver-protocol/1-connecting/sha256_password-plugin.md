
# sha256_password plugin

SHA256 authentication possible exchanges:


* if connection use SSL (SSLRequest Packet sent)

  * client send a [clear password answer](#client-clear-password-answer)
* else

  * if client doesn't know server RSA public key

    * client sends a [public key request](#public-key-request)
    * server sends a [public key response](#public-key-response)
  * client sends an [RSA encrypted password](#rsa-encrypted-password)
  * ends with server sending either [OK_Packet](../4-server-response-packets/ok_packet.md) , [ERR_Packet](../4-server-response-packets/err_packet.md)


#### Client clear password answer



* [string<NUL>](../protocol-data-types.md#null-terminated-strings) password without encryption






#### Public key request



* [byte<1>](../protocol-data-types.md#fixed-length-bytes) fixed 0x01 value






#### Public key response



* [byte<1>](../protocol-data-types.md#fixed-length-bytes) fixed 0x01 value
* [byte<EOF>](../protocol-data-types.md#end-of-file-length-bytes) public key data






#### RSA encrypted password



* [byte<256>](../protocol-data-types.md#fixed-length-bytes) RSA encrypted password



RSA encrypted value of XOR(password, seed) using server public key (RSA_PKCS1_OAEP_PADDING).





CC BY-SA / Gnu FDL

