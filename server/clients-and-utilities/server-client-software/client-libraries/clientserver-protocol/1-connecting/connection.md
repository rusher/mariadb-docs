# Connecting

Connection is done by many exchanges:

* (Create socket)
* If first byte from server is 0xFF:
  * packet is an [ERR\_Packet](../4-server-response-packets/err_packet.md), socket has to be closed
* else
  * Packet is an [Initial handshake packet](connection.md#initial-handshake-packet)
  * If SSL/TLS connection
    * Client sends [SSLRequest packet](connection.md#sslrequest-packet) and switches to SSL mode for sending and receiving the following messages:
  * Client sends [Handshake response packet](connection.md#handshake-response-packet)
  * Server sends either:
    * An OK packet in case of success [OK\_Packet](../4-server-response-packets/ok_packet.md)
    * An error packet in case of error [ERR\_Packet](../4-server-response-packets/err_packet.md)
    * Authentication switch
      * If the client or server doesn't have PLUGIN\_AUTH capability:
        * Server sends 0xFE byte
        * Client sends old\_password
      * else
        * Server sends [Authentication switch request](connection.md#authentication-switch-request)
        * Client may have many exchange with the server according to the [Plugin](connection.md#plugin-list).
      * Authentication switch ends with server sending either [OK\_Packet](../4-server-response-packets/ok_packet.md) or [ERR\_Packet](../4-server-response-packets/err_packet.md)

### Initial Handshake Packet

* [int<1>](../protocol-data-types.md#fixed-length-integers) protocol version
* [string](../protocol-data-types.md#null-terminated-strings) server version (MariaDB server version for 10.X versions is by default prefixed by "5.5.5-". [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110) and later versions do not have a "5.5.5-" default prefix)
* [int<4>](../protocol-data-types.md#fixed-length-integers) connection id
* [string<8>](../protocol-data-types.md#fixed-length-strings) authentication plugin data (1st part)
* [string<1>](../protocol-data-types.md#fixed-length-strings) reserved byte
* [int<2>](../protocol-data-types.md#fixed-length-integers) server capabilities (1st part)
* [int<1>](../protocol-data-types.md#fixed-length-integers) server default collation
* [int<2>](../protocol-data-types.md#fixed-length-integers) status flags
* [int<2>](../protocol-data-types.md#fixed-length-integers) server capabilities (2nd part)
* if (server\_capabilities & PLUGIN\_AUTH)
  * [int<1>](../protocol-data-types.md#fixed-length-integers) plugin data length
* else
  * [int<1>](../protocol-data-types.md#fixed-length-integers) 0x00
* [string<6>](../protocol-data-types.md#fixed-length-strings) filler
* if (server\_capabilities & CLIENT\_MYSQL)
  * [string<4>](../protocol-data-types.md#fixed-length-strings) filler
* else
  * [int<4>](../protocol-data-types.md#fixed-length-integers) server capabilities 3rd part . MariaDB specific flags /\* [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) or later \*/
* if (server\_capabilities & CLIENT\_SECURE\_CONNECTION)
  * [string](../protocol-data-types.md#fixed-length-strings) authentication plugin data 2nd part . Length = max(12, plugin data length - 9)
  * [string<1>](../protocol-data-types.md#fixed-length-strings) reserved byte
* if (server\_capabilities & PLUGIN\_AUTH)
  * [string](../protocol-data-types.md#null-terminated-strings) authentication plugin name

### Client Handshake Response

If the client requests a TLS/SSL connection, first response will be an SSL connection request packet, then a handshake response packet. If no TLS is required, client send directly a handshake response packet.

#### SSLRequest Packet

* [int<4>](../protocol-data-types.md#fixed-length-integers) client capabilities
* [int<4>](../protocol-data-types.md#fixed-length-integers) max packet size
* [int<1>](../protocol-data-types.md#fixed-length-integers) client's default character set and collation
* [string<19>](../protocol-data-types.md#fixed-length-strings) reserved
* if not (server\_capabilities & CLIENT\_MYSQL)
  * [int<4>](../protocol-data-types.md#fixed-length-integers) extended client capabilities
* else
  * [string<4>](../protocol-data-types.md#fixed-length-strings) reserved

#### ZERO-CONFIGURATION SSL ENCRYPTION

Automatic Encrypted Connections ([MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/what-is-mariadb-114)+):

Previously, failed SSL connections due to self-signed certificates prevented communication. [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/what-is-mariadb-114)+ introduces a secondary validation method that works for all servers.

**What Happens When SSL Validation Fails?**

Even without a valid SSL certificate, the connector can still authenticate by remembering the server's fingerprint (unique identifier). However, it needs to confirm the connection is secure.

**Verifying a Secure Connection:**

The confirmation method depends on the connection type. When using secure MitM-proof methods, like Unix sockets, connector can automatically validate the connection. Otherwise, a shared secret is used.

**Shared Secret for Secure Connection:**

The shared secret is only used if the authentication plugin password is hashable (e.g., mysql\_native\_password , client\_ed25519 or parsec) and not empty.

It's calculated by hashing the user's hash password with the authentication seed and the server fingerprint.

Password hash is generated depending on authentication plugin:

* ed25519 : identical to password encryption
* native password : identical to password encryption
* parsec: ext-salt + raw ed25519 public key

**Server 11.4+ Confirmation Details:**

For servers running [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/what-is-mariadb-114) or later, the final confirmation packet contains:

* [int<1>](../protocol-data-types.md#fixed-length-integers) encryption (actually only 0x01 = SHA256 encryption)
* [byte](../protocol-data-types.md#end-of-file-length-bytes) shared secret.

**Matching the Shared Secret:**

If the calculated shared secret matches the received one, the SSL connection is considered valid (host validation is not needed). Otherwise, the connection must be closed for security reasons.

#### Handshake Response Packet

* [int<4>](../protocol-data-types.md#fixed-length-integers) client capabilities
* [int<4>](../protocol-data-types.md#fixed-length-integers) max packet size
* [int<1>](../protocol-data-types.md#fixed-length-integers) client's default character set and collation
* [string<19>](../protocol-data-types.md#fixed-length-strings) reserved
* if not (server\_capabilities & CLIENT\_MYSQL)
  * [int<4>](../protocol-data-types.md#fixed-length-integers) extended client capabilities
* else
  * [string<4>](../protocol-data-types.md#fixed-length-strings) reserved
* [string](../protocol-data-types.md#null-terminated-strings) username
* if (password)
  * if (server\_capabilities & PLUGIN\_AUTH\_LENENC\_CLIENT\_DATA)
    * [string](../protocol-data-types.md#length-encoded-strings) authentication data
  * else if (server\_capabilities & CLIENT\_SECURE\_CONNECTION)
    * [int<1>](../protocol-data-types.md#fixed-length-integers) length of authentication response
    * [string](../protocol-data-types.md#fixed-length-strings) authentication response (length is indicated by previous field)
  * else
    * [string](../protocol-data-types.md#null-terminated-strings) authentication response null ended
* else
  * string<1>\0 (empty password)
* if (server\_capabilities & CLIENT\_CONNECT\_WITH\_DB)
  * [string](../protocol-data-types.md#null-terminated-strings) default database name
* if (server\_capabilities & CLIENT\_PLUGIN\_AUTH)
  * [string](../protocol-data-types.md#null-terminated-strings) authentication plugin name
* if (server\_capabilities & CLIENT\_CONNECT\_ATTRS)
  * [int](../protocol-data-types.md#length-encoded-integers) size of connection attributes
  * while packet has remaining data
    * [string](../protocol-data-types.md#length-encoded-strings) key
    * [string](../protocol-data-types.md#length-encoded-strings) value

### Server Response to Handshake Response Packet

The server responds with an [OK\_packet](../4-server-response-packets/ok_packet.md), an [ERR\_packet](../4-server-response-packets/err_packet.md) or an Authentication Switch Request packet.

#### Authentication Switch Request

(If client and server support CLIENT\_AUTH capability)

* [int<1>](../protocol-data-types.md#fixed-length-integers) 0xFE : Authentication switch request header
* [string](../protocol-data-types.md#null-terminated-strings) authentication plugin name
* [byte](../protocol-data-types.md#end-of-file-length-bytes) authentication plugin data

### Plugin List

#### mysql\_old\_password Plugin

_deprecated_\
send a 8 byte encrypted password

authentication plugin data format :

* [byte<8>](../protocol-data-types.md#fixed-length-bytes) 8-byte seed

Client response :

* [string](../protocol-data-types.md#null-terminated-strings) old format encrypted password

#### mysql\_clear\_password Plugin

{% hint style="danger" %}
Since password is transmitted in clear, this has be used only when using SSL connection
{% endhint %}

send clear password to server

Client response :

* [string](../protocol-data-types.md#null-terminated-strings) password without encryption

#### mysql\_native\_password Plugin

SHA-1 encrypted password with server seed

authentication plugin data format :

* [string](../protocol-data-types.md#null-terminated-strings) seed

Client response :

* [byte](../protocol-data-types.md#end-of-file-length-bytes) sha1 encrypted password

The password is encrypted with: `SHA1( password ) ^ SHA1( seed + SHA1( SHA1( password ) ) )`

#### dialog Plugin (PAM)

Interactive exchanges to permit fill passwords - for example for 2-Step authentication.

authentication plugin data format :

* [byte<1>](../protocol-data-types.md#fixed-length-bytes) password type
* [string](../protocol-data-types.md#end-of-file-length-strings) prompt message

The server can send one or many requests. For each of them, the client must display this prompt message to the user, to permit the user to type requested information, then send it to the server in [string](../protocol-data-types.md#null-terminated-strings) format. Password type indicate answer format ( 2 means "read the input with the echo enabled", 4 means "password-like input, echo disabled")

First authentication format (from authentication switch packet) can be empty since 10.4.

This end when server send an [EOF\_Packet](../4-server-response-packets/eof_packet.md), [OK\_Packet](../4-server-response-packets/ok_packet.md) or [ERROR\_packet](https://mariadb.com/kb/en/ERROR_packet).

#### auth\_gssapi\_client Plugin

gssapi implementation

authentication plugin data format :

* [string](../protocol-data-types.md#null-terminated-strings) serverPrincipalName (UTF-8 format)
* [string](../protocol-data-types.md#null-terminated-strings) mechanisms (UTF-8 format)

Client must exchange packet with server until having a mutual [GSSAPI](https://en.wikipedia.org/wiki/Generic_Security_Services_Application_Program_Interface) authentication.\
The only difference compared to standard client-server GSSAPI authentication is that exchanges contain standard protocol with packet headers.

#### client\_ed25519 Plugin

The ed25519 plugin uses the Elliptic Curve Digital Signature Algorithm to securely store users' passwords and to authenticate users.\
It has been Implemented in the server since [MariaDB 10.1.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10122-release-notes).

See [plugin description](../../../../../reference/plugins/authentication-plugins/authentication-plugin-ed25519.md).

The server sends a random nonce that the client signs.

authentication plugin data format :

* [byte](../protocol-data-types.md#end-of-file-length-bytes) seed

Client response :

* [byte](../protocol-data-types.md#end-of-file-length-bytes) ed25519 encrypted password

#### parsec Plugin

authentication plugin data format :

* [string<32>](../protocol-data-types.md#null-terminated-strings) server nonce

Client has to send an empty packet to request "ext-salt".

Format of ext-salt is

* [string<1>](../protocol-data-types.md#fixed-length-strings) 'P' (denotes KDF algorithm = PBKDF2)
* [byte<1>](../protocol-data-types.md#fixed-length-bytes) iteration factor. number of iterations correspond to 1024 << iteration factor (0x0 means 1024, 0x1 means 2048, etc.)
* [byte](../protocol-data-types.md#end-of-file-length-bytes) salt

client must then :

* generate derived key = hash password with PBKDF2 ( sha512 digest) with iteration number and salt from ext-salt.
* generate a client 32 bytes nonce
* generate the signature with ed25519 of an array concatenation of server nonce + client nonce with the generated derived key as private key.

Client response :

* [byte<32>](../protocol-data-types.md#fixed-length-bytes) client nonce
* [byte<64>](../protocol-data-types.md#fixed-length-bytes) signature

### Capabilities

Server and Client have different capabilities, here is the possibles values.\
client with capabilities CLIENT\_MYSQL + CONNECT\_WITH\_DB will have a value of 9 (1 + 8).

|                                         |         |                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CLIENT\_MYSQL                           | 1       | Set by older MariaDB versions. [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) leaves this bit unset to permit MariaDB identification and indicate support for extended capabilities. (MySQL named this CLIENT\_LONG\_PASSWORD) |
| FOUND\_ROWS                             | 2       |                                                                                                                                                                                                                                                                                                                                                          |
| CONNECT\_WITH\_DB                       | 8       | One can specify db on connect                                                                                                                                                                                                                                                                                                                            |
| COMPRESS                                | 32      | Can use compression protocol                                                                                                                                                                                                                                                                                                                             |
| LOCAL\_FILES                            | 128     | Can use LOAD DATA LOCAL                                                                                                                                                                                                                                                                                                                                  |
| IGNORE\_SPACE                           | 256     | Ignore spaces before '('                                                                                                                                                                                                                                                                                                                                 |
| CLIENT\_PROTOCOL\_41                    | 1 << 9  | 4.1 protocol                                                                                                                                                                                                                                                                                                                                             |
| CLIENT\_INTERACTIVE                     | 1 << 10 |                                                                                                                                                                                                                                                                                                                                                          |
| SSL                                     | 1 << 11 | Can use SSL                                                                                                                                                                                                                                                                                                                                              |
| TRANSACTIONS                            | 1 << 13 |                                                                                                                                                                                                                                                                                                                                                          |
| SECURE\_CONNECTION                      | 1 << 15 | 4.1 authentication                                                                                                                                                                                                                                                                                                                                       |
| MULTI\_STATEMENTS                       | 1 << 16 | Enable/disable multi-stmt support                                                                                                                                                                                                                                                                                                                        |
| MULTI\_RESULTS                          | 1 << 17 | Enable/disable multi-results                                                                                                                                                                                                                                                                                                                             |
| PS\_MULTI\_RESULTS                      | 1 << 18 | Enable/disable multi-results for PrepareStatement                                                                                                                                                                                                                                                                                                        |
| PLUGIN\_AUTH                            | 1 << 19 | Client supports plugin authentication                                                                                                                                                                                                                                                                                                                    |
| CONNECT\_ATTRS                          | 1 << 20 | Client send connection attributes                                                                                                                                                                                                                                                                                                                        |
| PLUGIN\_AUTH\_LENENC\_CLIENT\_DATA      | 1 << 21 | Enable authentication response packet to be larger than 255 bytes                                                                                                                                                                                                                                                                                        |
| CLIENT\_CAN\_HANDLE\_EXPIRED\_PASSWORDS | 1 << 22 | Client can handle expired passwords                                                                                                                                                                                                                                                                                                                      |
| CLIENT\_SESSION\_TRACK                  | 1 << 23 | Enable/disable session tracking in OK\_Packet                                                                                                                                                                                                                                                                                                            |
| CLIENT\_DEPRECATE\_EOF                  | 1 << 24 | EOF\_Packet deprecation : \* OK\_Packet replace EOF\_Packet in end of Resulset when in text format \* EOF\_Packet between columns definition and resultsetRows is deleted                                                                                                                                                                                |
| CLIENT\_OPTIONAL\_RESULTSET\_METADATA   | 1 << 25 | Not use for MariaDB                                                                                                                                                                                                                                                                                                                                      |
| CLIENT\_ZSTD\_COMPRESSION\_ALGORITHM    | 1 << 26 | Support zstd protocol compression                                                                                                                                                                                                                                                                                                                        |
| CLIENT\_CAPABILITY\_EXTENSION           | 1 << 29 | Reserved for future use. (Was CLIENT\_PROGRESS Client support progress indicator before 10.2)                                                                                                                                                                                                                                                            |
| CLIENT\_SSL\_VERIFY\_SERVER\_CERT       | 1 << 30 | Client verify server certificate. deprecated, client have options to indicate if server certifiate must be verified                                                                                                                                                                                                                                      |
| CLIENT\_REMEMBER\_OPTIONS               | 1 << 31 |                                                                                                                                                                                                                                                                                                                                                          |
| MARIADB\_CLIENT\_PROGRESS               | 1 << 32 | Client support progress indicator (since 10.2)                                                                                                                                                                                                                                                                                                           |
| MARIADB\_CLIENT\_COM\_MULTI             | 1 << 33 | Permit COM\_MULTI protocol                                                                                                                                                                                                                                                                                                                               |
| MARIADB\_CLIENT\_STMT\_BULK\_OPERATIONS | 1 << 34 | Permit bulk insert                                                                                                                                                                                                                                                                                                                                       |
| MARIADB\_CLIENT\_EXTENDED\_METADATA     | 1 << 35 | Add extended metadata information                                                                                                                                                                                                                                                                                                                        |
| MARIADB\_CLIENT\_CACHE\_METADATA        | 1 << 36 | Permit skipping metadata                                                                                                                                                                                                                                                                                                                                 |
| MARIADB\_CLIENT\_BULK\_UNIT\_RESULTS    | 1 << 37 | when enable, indicate that Bulk command can use STMT\_BULK\_FLAG\_SEND\_UNIT\_RESULTS flag that permit to return a result-set of all affected rows and auto-increment values                                                                                                                                                                             |

### Native Password Authentication

The 20 byte string 'seed' is calculated by concatenating scramble first part (8 bytes) and scramble second part from [Initial handshake packet](connection.md#initial-handshake-packet). After that, the client calculates a password hash using the password and seed by using ^ (bitwise xor), + (string concatenation) and SHA1 as follows:

SHA1( passwd) ^ SHA1( seed + SHA1( SHA1( passwd ) ) )

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
