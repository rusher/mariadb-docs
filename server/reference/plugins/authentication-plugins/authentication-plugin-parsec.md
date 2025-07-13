# Authentication Plugin - PARSEC

{% hint style="info" %}
This plugin is available from MariaDB 11.6.
{% endhint %}

The `PARSEC` Authentication Plugin is intended to be the default in a future release.

The `PARSEC` (Password Authentication using Response Signed with Elliptic Curve) authentication plugin uses salted passwords, key derivation, extensible password storage format, and both server- and client-side scrambles.

It signs the response with `ed25519`, but it uses stock unmodified `ed25519` as provided by OpenSSL/WolfSSL/GnuTLS.

### Description

* The KDF function is pbkdf2 (supported by everything, including [windows native](https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptderivekeypbkdf2), Java, javascript, PHP, .NET.
* Parameters to the pbkdf2 are stored in with authentication plugin data : hash function (SHA512,SHA256), iteration count, salt, key\_length, together with derived key = `PBKDF2(func, password, salt, iteration_count, key_length).`
* The number of iterations is a power of 2, greater than 9.
* The algorithm is ed25519, "hash" is the public key generated using ed25519 from the PBKDF2(password).

The authentication string, stored by the server, is this:

```c
concat('P', conv(log2(iterations)-10, 10, 62), ':', base64(salt), ':', base64(hash))
```

For example, it looks like this: `P0:WW9sXaaL/o:vubFBzIrapbfHct1/J72dnUryz5VS7lA6XHH8sIx4TI`

* It consists of colon-separated fields.
* The first field is 'P' (denotes KDF algorithm = PBKDF2) and the number of iterations, '0' means 1024, '1' means 2048, etc.
* This is followed by the salt.
* This is followed by the password hash.

The first two fields together are called _ext-salt_, extended salt.

#### Login Process, Packet Exchange

1. The server sends an [Authentication Switch Request](../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/1-connecting/connection.md#authentication-switch-request) with a 32-byte random scramble.
2. The client sends an empty packet to the server to request the [ext-salt](../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/1-connecting/connection.md#parsec-plugin).
3. The server sends the [ext-salt](../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/1-connecting/connection.md#parsec-plugin) to the client.
4. The client sends the random 32-byte scramble, and the `concat(server scramble, client scramble)` ed25519-signed by a secret key generated from the function `PBKDF2(password, ext-salt)`.
5. The server replies with ["ok"](../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/4-server-response-packets/ok_packet.md) or ["access denied"](../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/4-server-response-packets/err_packet.md).

### Installing

```sql
INSTALL SONAME 'auth_parsec';
```

### Example

```sql
CREATE USER test1@'%' IDENTIFIED VIA parsec using PASSWORD('pwd');
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
