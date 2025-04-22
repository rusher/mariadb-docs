
# Authentication Plugin - PARSEC


##### MariaDB starting with [11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116)
The PARSEC Authentication Plugin was introduced in [MariaDB 11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116). It is intended to be the default in a future release.


The PARSEC (Password Authentication using Response Signed with Elliptic Curve) authentication plugin uses salted passwords, key derivation, extensible password storage format, and both server- and client-side scrambles.


It signs the response with ed25519, but it uses stock unmodified ed25519 as provided by OpenSSL/WolfSSL/GnuTLS.


### Description


* the KDF function is pbkdf2 (supported by everything, including [windows native](https://learn.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptderivekeypbkdf2), Java, javascript, PHP, .NET
* parameters to the pbkdf2 are stored in with authentication plugin data : hash function (SHA512,SHA256), iteration count, salt, key_length, together with derived key = PBKDF2(func, password, salt, iteration_count, key_length)
* number of iterations is a power of 2, greater than 9
* the algorithm is ed25519, "hash" is the public key generated using ed25519 from the PBKDF2(password)


The authentication string, stored by the server, is


```
concat('P', conv(log2(iterations)-10, 10, 62), ':', base64(salt), ':', base64(hash))
```

for example `P0:WW9sXaaL/o:vubFBzIrapbfHct1/J72dnUryz5VS7lA6XHH8sIx4TI`


* it consists of colon-separated fields
* first field is 'P' (denotes KDF algorithm = PBKDF2) and the number of iterations, '0' means 1024, '1' means 2048, etc
* then salt
* then the password hash


first two fields together are called below *ext-salt*, extended salt.


#### Login Process, Packet Exchange


1. Server sends an [Authentication Switch Request](../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/1-connecting/connection.md#authentication-switch-request) with a 32-byte random scramble
1. Client sends an empty packet to the server to request the [ext-salt](../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/1-connecting/connection.md#parsec-plugin)
1. Server sends the [ext-salt](../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/1-connecting/connection.md#parsec-plugin) to the client
1. Client sends the random 32-byte scramble, and the concat(server scramble, client scramble) ed25519-signed by a secret key generated from the PBKDF2(password, ext-salt)
1. Server replies with ["ok"](../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/4-server-response-packets/ok_packet.md) or ["access denied"](../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/4-server-response-packets/err_packet.md)


### Installing


```
install soname 'auth_parsec';
```

### Example


```
create user test1@'%' identified via parsec using PASSWORD('pwd');
```
