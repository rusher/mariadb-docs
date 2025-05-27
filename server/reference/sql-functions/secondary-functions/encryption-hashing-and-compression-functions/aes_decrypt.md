# AES\_DECRYPT

## Syntax

```
AES_DECRYPT(crypt_str,key_str)
```

From [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes)

```
AES_ENCRYPT(crypt_str, key_str, [, iv [, mode]])
```

## Description

This function allows decryption of data using the official AES (Advanced Encryption Standard) algorithm. For more information, see the description of [AES\_ENCRYPT()](aes_encrypt.md).

**MariaDB starting with** [**11.2**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112)

From [MariaDB 11.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112), the function supports an initialization vector, and control of the block encryption mode. The default mode is specified by the [block\_encryption\_mode](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#block_encryption_mode) system variable, which can be changed when calling the function with a mode. _mode_ is aes-{128,192,256}-{ecb,cbc,ctr} for example: "AES-128-cbc".\
For modes that require it, the initialization\_vector _iv_ should be 16 bytes (it can be longer, but the extra bytes are ignored). A shorter _iv_, where one is required, results in the function returning NULL. Calling [RANDOM\_BYTES(16)](random_bytes.md) will generate a random series of bytes that can be used for the _iv_.

## Examples

From [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes):

```
SELECT HEX(AES_ENCRYPT('foo', 'bar', '0123456789abcdef', 'aes-128-ctr')) AS x; 
+--------+
| x      |
+--------+
| C57C4B |
+--------+


SELECT AES_DECRYPT(x'C57C4B', 'bar', '0123456789abcdef', 'aes-128-ctr'); 
+------------------------------------------------------------------+
| AES_DECRYPT(x'C57C4B', 'bar', '0123456789abcdef', 'aes-128-ctr') |
+------------------------------------------------------------------+
| foo                                                              |
+------------------------------------------------------------------+
```

GPLv2 fill\_help\_tables.sql
