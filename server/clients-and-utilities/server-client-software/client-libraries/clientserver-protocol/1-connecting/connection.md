
# Connecting

Connection is done by many exchanges:


* (Create socket)
* If first byte from server is 0xFF: 

  * packet is an [ERR_Packet](../4-server-response-packets/err_packet.md), socket has to be closed
* else 

  * Packet is an [Initial handshake packet](#initial-handshake-packet)
  * If SSL/TLS connection

    * Client sends [SSLRequest packet](#sslrequest-packet) and switches to SSL mode for sending and receiving the following messages:
  * Client sends [Handshake response packet](#handshake-response-packet)
  * Server sends either:

    * An OK packet in case of success [OK_Packet](../4-server-response-packets/ok_packet.md)
    * An error packet in case of error [ERR_Packet](../4-server-response-packets/err_packet.md)
    * Authentication switch 

      * If the client or server doesn't have PLUGIN_AUTH capability:

        * Server sends 0xFE byte
        * Client sends old_password
      * else

        * Server sends [Authentication switch request](#authentication-switch-request)
        * Client may have many exchange with the server according to the [Plugin](#plugin-list).
      * Authentication switch ends with server sending either [OK_Packet](../4-server-response-packets/ok_packet.md) or [ERR_Packet](../4-server-response-packets/err_packet.md)





### Initial Handshake Packet



* [int<1>](../protocol-data-types.md#fixed-length-integers) protocol version
* [string<NUL>](../protocol-data-types.md#null-terminated-strings) server version (MariaDB server version for 10.X versions is by default prefixed by "5.5.5-". [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110) and later versions do not have a "5.5.5-" default prefix)
* [int<4>](../protocol-data-types.md#fixed-length-integers) connection id
* [string<8>](../protocol-data-types.md#fixed-length-strings) authentication plugin data (1st part)
* [string<1>](../protocol-data-types.md#fixed-length-strings) reserved byte
* [int<2>](../protocol-data-types.md#fixed-length-integers) server capabilities (1st part)
* [int<1>](../protocol-data-types.md#fixed-length-integers) server default collation
* [int<2>](../protocol-data-types.md#fixed-length-integers) status flags
* [int<2>](../protocol-data-types.md#fixed-length-integers) server capabilities (2nd part)
* if (server_capabilities & PLUGIN_AUTH) 

  * [int<1>](../protocol-data-types.md#fixed-length-integers) plugin data length
* else

  * [int<1>](../protocol-data-types.md#fixed-length-integers) 0x00
* [string<6>](../protocol-data-types.md#fixed-length-strings) filler
* if (server_capabilities & CLIENT_MYSQL) 

  * [string<4>](../protocol-data-types.md#fixed-length-strings) filler
* else

  * [int<4>](../protocol-data-types.md#fixed-length-integers) server capabilities 3rd part . MariaDB specific flags /* [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) or later */
* if (server_capabilities & CLIENT_SECURE_CONNECTION)

  * [string<n>](../protocol-data-types.md#fixed-length-strings) authentication plugin data 2nd part . Length = max(12, plugin data length - 9)
  * [string<1>](../protocol-data-types.md#fixed-length-strings) reserved byte
* if (server_capabilities & PLUGIN_AUTH) 

  * [string<NUL>](../protocol-data-types.md#null-terminated-strings) authentication plugin name






### Client Handshake Response


If the client requests a TLS/SSL connection, first response will be an SSL connection request packet, then a handshake response packet. If no TLS is required, client send directly a handshake response packet.


#### SSLRequest Packet



* [int<4>](../protocol-data-types.md#fixed-length-integers) client capabilities
* [int<4>](../protocol-data-types.md#fixed-length-integers) max packet size
* [int<1>](../protocol-data-types.md#fixed-length-integers) client's default character set and collation
* [string<19>](../protocol-data-types.md#fixed-length-strings) reserved
* if not (server_capabilities & CLIENT_MYSQL)

  * [int<4>](../protocol-data-types.md#fixed-length-integers) extended client capabilities
* else

  * [string<4>](../protocol-data-types.md#fixed-length-strings) reserved






#### ZERO-CONFIGURATION SSL ENCRYPTION


Automatic Encrypted Connections ([MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-11-4-series/what-is-mariadb-114)+):


Previously, failed SSL connections due to self-signed certificates prevented communication. [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-11-4-series/what-is-mariadb-114)+ introduces a secondary validation method that works for all servers.


##### What Happens When SSL Validation Fails?


Even without a valid SSL certificate, the connector can still authenticate by remembering the server's fingerprint (unique identifier). However, it needs to confirm the connection is secure.


##### Verifying a Secure Connection:


The confirmation method depends on the connection type. When using secure MitM-proof methods, like Unix sockets, connector can automatically validate the connection. Otherwise, a shared secret is used.


##### Shared Secret for Secure Connection:


The shared secret is only used if the authentication plugin password is hashable (e.g., mysql_native_password , client_ed25519 or parsec) and not empty.


It's calculated by hashing the user's hash password with the authentication seed and the server fingerprint.


Password hash is generated depending on authentication plugin:


* ed25519 : identical to password encryption
* native password : identical to password encryption
* parsec: ext-salt + raw ed25519 public key


##### Server 11.4+ Confirmation Details:


For servers running [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-11-4-series/what-is-mariadb-114) or later, the final confirmation packet contains:


* [int<1>](../protocol-data-types.md#fixed-length-integers) encryption (actually only 0x01 = SHA256 encryption)
* [byte<EOF>](../protocol-data-types.md#end-of-file-length-bytes) shared secret.


##### Matching the Shared Secret:


If the calculated shared secret matches the received one, the SSL connection is considered valid (host validation is not needed). Otherwise, the connection must be closed for security reasons.





#### Handshake Response Packet



* [int<4>](../protocol-data-types.md#fixed-length-integers) client capabilities
* [int<4>](../protocol-data-types.md#fixed-length-integers) max packet size
* [int<1>](../protocol-data-types.md#fixed-length-integers) client's default character set and collation
* [string<19>](../protocol-data-types.md#fixed-length-strings) reserved
* if not (server_capabilities & CLIENT_MYSQL)

  * [int<4>](../protocol-data-types.md#fixed-length-integers) extended client capabilities
* else

  * [string<4>](../protocol-data-types.md#fixed-length-strings) reserved
* [string<NUL>](../protocol-data-types.md#null-terminated-strings) username
* if (password)

  * if (server_capabilities & PLUGIN_AUTH_LENENC_CLIENT_DATA) 

    * [string<lenenc>](../protocol-data-types.md#length-encoded-strings) authentication data
  * else if (server_capabilities & CLIENT_SECURE_CONNECTION) 

    * [int<1>](../protocol-data-types.md#fixed-length-integers) length of authentication response
    * [string<fix>](../protocol-data-types.md#fixed-length-strings) authentication response (length is indicated by previous field)
  * else

    * [string<NUL>](../protocol-data-types.md#null-terminated-strings) authentication response null ended
* else

  * string<1>\0 (empty password)
* if (server_capabilities & CLIENT_CONNECT_WITH_DB)

  * [string<NUL>](../protocol-data-types.md#null-terminated-strings) default database name
* if (server_capabilities & CLIENT_PLUGIN_AUTH)

  * [string<NUL>](../protocol-data-types.md#null-terminated-strings) authentication plugin name
* if (server_capabilities & CLIENT_CONNECT_ATTRS)

  * [int<lenenc>](../protocol-data-types.md#length-encoded-integers) size of connection attributes
  * while packet has remaining data

    * [string<lenenc>](../protocol-data-types.md#length-encoded-strings) key
    * [string<lenenc>](../protocol-data-types.md#length-encoded-strings) value



### Server Response to Handshake Response Packet


The server responds with an [OK_packet](../4-server-response-packets/ok_packet.md), an [ERR_packet](../4-server-response-packets/err_packet.md) or an Authentication Switch Request packet.


#### Authentication Switch Request


(If client and server support CLIENT_AUTH capability)



* [int<1>](../protocol-data-types.md#fixed-length-integers) 0xFE : Authentication switch request header
* [string<NUL>](../protocol-data-types.md#null-terminated-strings) authentication plugin name
* [byte<EOF>](../protocol-data-types.md#end-of-file-length-bytes) authentication plugin data






### Plugin List





#### mysql_old_password Plugin


*deprecated*
send a 8 byte encrypted password


authentication plugin data format :



* [byte<8>](../protocol-data-types.md#fixed-length-bytes) 8-byte seed



Client response :



* [string<NUL>](../protocol-data-types.md#null-terminated-strings) old format encrypted password






#### mysql_clear_password Plugin


Since password is transmitted in clear, this has be used only when using SSL connection


send clear password to server


Client response :



* [string<NUL>](../protocol-data-types.md#null-terminated-strings) password without encryption






#### mysql_native_password Plugin


SHA-1 encrypted password with server seed


authentication plugin data format :



* [string<NUL>](../protocol-data-types.md#null-terminated-strings) seed



Client response :



* [byte<EOF>](../protocol-data-types.md#end-of-file-length-bytes) sha1 encrypted password



The password is encrypted with: `SHA1( password ) ^ SHA1( seed + SHA1( SHA1( password ) ) )`





#### dialog Plugin (PAM)


Interactive exchanges to permit fill passwords - for example for 2-Step authentication.


authentication plugin data format :



* [byte<1>](../protocol-data-types.md#fixed-length-bytes) password type
* [string<EOF>](../protocol-data-types.md#end-of-file-length-strings) prompt message



The server can send one or many requests. For each of them, the client must display this prompt message to the user, to permit the user to type requested information, then send it to the server in [string<NUL>](../protocol-data-types.md#null-terminated-strings) format. Password type indicate answer format ( 2 means "read the input with the echo enabled", 4 means "password-like input, echo disabled")


First authentication format (from authentication switch packet) can be empty since 10.4.


This end when server send an [EOF_Packet](../4-server-response-packets/eof_packet.md), [OK_Packet](../4-server-response-packets/ok_packet.md) or [ERROR_packet](https://mariadb.com/kb/en/ERROR_packet).





#### auth_gssapi_client Plugin


gssapi implementation


authentication plugin data format :



* [string<NUL>](../protocol-data-types.md#null-terminated-strings) serverPrincipalName (UTF-8 format)
* [string<NUL>](../protocol-data-types.md#null-terminated-strings) mechanisms (UTF-8 format)



Client must exchange packet with server until having a mutual [GSSAPI](https://en.wikipedia.org/wiki/Generic_Security_Services_Application_Program_Interface) authentication.
The only difference compared to standard client-server GSSAPI authentication is that exchanges contain standard protocol with packet headers.





#### client_ed25519 Plugin


The ed25519 plugin uses the Elliptic Curve Digital Signature Algorithm to securely store users' passwords and to authenticate users. 
It has been Implemented in the server since [MariaDB 10.1.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10122-release-notes).


See [plugin description](../../../../../reference/plugins/authentication-plugins/authentication-plugin-ed25519.md).


The server sends a random nonce that the client signs.


authentication plugin data format :



* [byte<EOF>](../protocol-data-types.md#end-of-file-length-bytes) seed



Client response :



* [byte<EOF>](../protocol-data-types.md#end-of-file-length-bytes) ed25519 encrypted password






#### parsec Plugin


authentication plugin data format :



* [string<32>](../protocol-data-types.md#null-terminated-strings) server nonce



Client has to send an empty packet to request "ext-salt".


Format of ext-salt is



* [string<1>](../protocol-data-types.md#fixed-length-strings) 'P' (denotes KDF algorithm = PBKDF2)
* [byte<1>](../protocol-data-types.md#fixed-length-bytes) iteration factor. number of iterations correspond to 1024 << iteration factor (0x0 means 1024, 0x1 means 2048, etc.)
* [byte<EOF>](../protocol-data-types.md#end-of-file-length-bytes) salt



client must then :


* generate derived key = hash password with PBKDF2 ( sha512 digest) with iteration number and salt from ext-salt.
* generate a client 32 bytes nonce
* generate the signature with ed25519 of an array concatenation of server nonce + client nonce with the generated derived key as private key.


Client response :



* [byte<32>](../protocol-data-types.md#fixed-length-bytes) client nonce
* [byte<64>](../protocol-data-types.md#fixed-length-bytes) signature






### Capabilities


Server and Client have different capabilities, here is the possibles values. 
client with capabilities CLIENT_MYSQL + CONNECT_WITH_DB will have a value of 9 (1 + 8).



|   |   |   |
| --- | --- | --- |
| CLIENT_MYSQL | 1 | Set by older MariaDB versions. [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) leaves this bit unset to permit MariaDB identification and indicate support for extended capabilities. (MySQL named this CLIENT_LONG_PASSWORD) |
| FOUND_ROWS | 2 |  |
| CONNECT_WITH_DB | 8 | One can specify db on connect |
| COMPRESS | 32 | Can use compression protocol |
| LOCAL_FILES | 128 | Can use LOAD DATA LOCAL |
| IGNORE_SPACE | 256 | Ignore spaces before '(' |
| CLIENT_PROTOCOL_41 | 1 << 9 | 4.1 protocol |
| CLIENT_INTERACTIVE | 1 << 10 |
| SSL | 1 << 11 | Can use SSL |
| TRANSACTIONS | 1 << 13 |
| SECURE_CONNECTION | 1 << 15 | 4.1 authentication |
| MULTI_STATEMENTS | 1 << 16 | Enable/disable multi-stmt support |
| MULTI_RESULTS | 1 << 17 | Enable/disable multi-results |
| PS_MULTI_RESULTS | 1 << 18 | Enable/disable multi-results for PrepareStatement |
| PLUGIN_AUTH | 1 << 19 | Client supports plugin authentication |
| CONNECT_ATTRS | 1 << 20 | Client send connection attributes |
| PLUGIN_AUTH_LENENC_CLIENT_DATA | 1 << 21 | Enable authentication response packet to be larger than 255 bytes |
| CLIENT_CAN_HANDLE_EXPIRED_PASSWORDS | 1 << 22 | Client can handle expired passwords |
| CLIENT_SESSION_TRACK | 1 << 23 | Enable/disable session tracking in OK_Packet |
| CLIENT_DEPRECATE_EOF | 1 << 24 | EOF_Packet deprecation : * OK_Packet replace EOF_Packet in end of Resulset when in text format * EOF_Packet between columns definition and resultsetRows is deleted |
| CLIENT_OPTIONAL_RESULTSET_METADATA | 1 << 25 | Not use for MariaDB |
| CLIENT_ZSTD_COMPRESSION_ALGORITHM | 1 << 26 | Support zstd protocol compression |
| CLIENT_CAPABILITY_EXTENSION | 1 << 29 | Reserved for future use. (Was CLIENT_PROGRESS Client support progress indicator before 10.2) |
| CLIENT_SSL_VERIFY_SERVER_CERT | 1 << 30 | Client verify server certificate. deprecated, client have options to indicate if server certifiate must be verified |
| CLIENT_REMEMBER_OPTIONS | 1 << 31 |
| MARIADB_CLIENT_PROGRESS | 1 << 32 | Client support progress indicator (since 10.2) |
| MARIADB_CLIENT_COM_MULTI | 1 << 33 | Permit COM_MULTI protocol |
| MARIADB_CLIENT_STMT_BULK_OPERATIONS | 1 << 34 | Permit bulk insert |
| MARIADB_CLIENT_EXTENDED_METADATA | 1 << 35 | Add extended metadata information |
| MARIADB_CLIENT_CACHE_METADATA | 1 << 36 | Permit skipping metadata |
| MARIADB_CLIENT_BULK_UNIT_RESULTS | 1 << 37 | when enable, indicate that Bulk command can use STMT_BULK_FLAG_SEND_UNIT_RESULTS flag that permit to return a result-set of all affected rows and auto-increment values |






### Native Password Authentication


The 20 byte string 'seed' is calculated by concatenating scramble first part (8 bytes) and scramble second part from [Initial handshake packet](#initial-handshake-packet). After that, the client calculates a password hash using the password and seed by using ^ (bitwise xor), + (string concatenation) and SHA1 as follows:


SHA1( passwd) ^ SHA1( seed + SHA1( SHA1( passwd ) ) )

