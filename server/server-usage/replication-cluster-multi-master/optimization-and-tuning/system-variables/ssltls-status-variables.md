
# SSL/TLS Status Variables


The status variables listed on this page relate to encrypting data during transfer with the Transport Layer Security (TLS) protocol. Often, the term Secure Socket Layer (SSL) is used interchangeably with TLS, although strictly speaking, the SSL protocol is a predecessor to TLS and is no longer considered secure.


For compatibility reasons, the TLS status variables in MariaDB still use the `<code>Ssl_</code>` prefix, but MariaDB only supports its more secure successors. For more information on SSL/TLS in MariaDB, see [Secure Connections Overview](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md).


Some of these status values are not under the control of the server, but are reporting back settings of the underlying SSL library used by the server.


## Variables


#### `<code>Ssl_accept_renegotiates</code>`


* Description: Number of negotiations needed to establish the TLS connection. The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Ssl_accepts</code>`


* Description: Number of accepted TLS handshakes. The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Ssl_callback_cache_hits</code>`


* Description: Number of sessions retrieved from the session cache. The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Ssl_cipher</code>`


* Description: The TLS cipher currently in use.
* Scope: Global, Session
* Data Type: `<code>string</code>`



#### `<code>Ssl_cipher_list</code>`


* Description: List of the available TLS ciphers.
This is not necessarily the list of ciphers the MariaDB server can actually accept, but rather the list of ciphers supported by the underlying SSL library in general. E.g. some of these may not be compatible with the servers SSL certificate and so can't be used to connect to that server.
* Scope: Global, Session
* Data Type: `<code>string</code>`



#### `<code>Ssl_client_connects</code>`


* Description: Number of TLS handshakes started in client mode. The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Ssl_connect_renegotiates</code>`


* Description: Number of negotiations needed to establish the connection to a TLS-enabled master. The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Ssl_ctx_verify_depth</code>`


* Description: Number of tested TLS certificates in the chain. The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Ssl_ctx_verify_mode</code>`


* Description: Mode used for TLS context verification.The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Ssl_default_timeout</code>`


* Description: Default timeout for TLS, in seconds.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Ssl_finished_accepts</code>`


* Description: Number of successful TLS sessions in server mode. The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Ssl_finished_connects</code>`


* Description: Number of successful TLS sessions in client mode. The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Ssl_server_not_after</code>`


* Description: Last valid date for the server TLS certificate.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: `<code>[MariaDB 10.0](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)</code>`



#### `<code>Ssl_server_not_before</code>`


* Description: First valid date for the server TLS certificate.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`
* Introduced: `<code>[MariaDB 10.0](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)</code>`



#### `<code>Ssl_session_cache_hits</code>`


* Description: Number of TLS sessions found in the session cache. The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Ssl_session_cache_misses</code>`


* Description: Number of TLS sessions not found in the session cache. The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Ssl_session_cache_mode</code>`


* Description: Mode used for TLS caching by the server.
* Scope: Global
* Data Type: `<code>string</code>`



#### `<code>Ssl_session_cache_overflows</code>`


* Description: Number of sessions removed from the session cache because it was full. The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Ssl_session_cache_size</code>`


* Description: Size of the session cache. The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Ssl_session_cache_timeouts</code>`


* Description: Number of sessions which have timed out. The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Ssl_sessions_reused</code>`


* Description: Number of sessions reused. The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Ssl_used_session_cache_entries</code>`


* Description: Current number of sessions in the session cache. The global value can be flushed by `<code>[FLUSH STATUS](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>`.
* Scope: Global
* Data Type: `<code>numeric</code>`



#### `<code>Ssl_verify_depth</code>`


* Description: TLS verification depth.
How many levels within the certificate signing chain the verification should cover. This is not set by the server itself but by the OpenSSL configuration, and will typically show a very large number like 18446744073709551615, basically meaning "always verify the full signing chain up to the root CA"
* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Ssl_verify_mode</code>`


* Description: TLS verification mode.


The OpenSSL verification mode flags in effect on the server side.


The value so far is always 5 when OpenSSL encryption is in effect, and 0 when not using encryption, or when the server is compiled against WolfSSL.


The value 5 is a combination of the `<code>SSL_VERIFY_PEER</code>` and `<code>SSL_VERIFY_CLIENT_ONCE</code>` flags, meaning that the client may send a certificate of its own connect, but will not be asked to send one again later for the duration of the encrypted connection.


The `<code>SSL_VERIFY_FAIL_IF_NO_PEER_CERT</code>` is not used at this point to enforce that the client sends a certificate if the database user was created with `<code>REQUIRE X509</code>`, `<code>REQUIRE ISSUER</code>` or `<code>REQUIRE SUBJECT</code>`, whether a client certificate was indeed sent, and whether it fits additional `<code>REQUIRE</code>` conditions, is checked by the server itself at a later state.


See also [#notes](https://docs.openssl.org/master/man3/SSL_CTX_set_verify/#notes) for a description of the OpenSSL verify mode flags.


* Scope: Global, Session
* Data Type: `<code>numeric</code>`



#### `<code>Ssl_version</code>`


* Description: TLS version in use by the current session, possible values are `<code>TLSv1.0</code>`, `<code>TLSv1.1</code>`, `<code>TLSv1.2</code>` and `<code>TLSv1.3</code>`
* Scope: Global, Session
* Data Type: `<code>string</code>`



## See Also


* [Server Status Variables](server-status-variables.md) - complete list of status variables.
* [Full list of MariaDB options, system and status variables](../../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md)

