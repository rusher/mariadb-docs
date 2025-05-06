
# AES_ENCRYPT

## Syntax


```
AES_ENCRYPT(str,key_str)
```

From [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes)


```
AES_ENCRYPT(str, key, [, iv [, mode]])
```

## Description


`AES_ENCRYPT()` and [AES_DECRYPT()](aes_decrypt.md) allow encryption and decryption of
data using the official AES (Advanced Encryption Standard) algorithm, previously known as "Rijndael." Encoding with a 128-bit key length is used (from [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes), this is the default, and can be changed). 128 bits is much faster and is secure enough for most purposes.


`AES_ENCRYPT()` encrypts a string *`str`* using the key *`key_str`*, and returns a binary string.


`AES_DECRYPT()` decrypts the encrypted string and returns the original
string.


The input arguments may be any length. If either argument is NULL, the result of this function is also `NULL`.


Because AES is a block-level algorithm, padding is used to encode uneven length strings and so the result string length may be calculated using this formula:


```
16 x (trunc(string_length / 16) + 1)
```

If `AES_DECRYPT()` detects invalid data or incorrect padding, it returns `NULL`. However, it is possible for `AES_DECRYPT()` to return a non-`NULL` value (possibly garbage) if the input data or the key is invalid.



##### MariaDB starting with [11.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112)
From [MariaDB 11.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112), the function supports an initialization vector, and control of the block encryption mode. The default mode is specified by the [block_encryption_mode](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#block_encryption_mode) system variable, which can be changed when calling the function with a mode. *mode* is aes-{128,192,256}-{ecb,cbc,ctr} for example:  "AES-128-cbc".
AES_ENCRYPT(str, key) can no longer be used in persistent virtual columns (and the like).


## Examples


```
INSERT INTO t VALUES (AES_ENCRYPT('text',SHA2('password',512)));
```

From [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes):


```
SELECT HEX(AES_ENCRYPT('foo', 'bar', '0123456789abcdef', 'aes-256-cbc')) AS x;
+----------------------------------+
| x                                |
+----------------------------------+
| 42A3EB91E6DFC40A900D278F99E0726E |
+----------------------------------+
```

## See Also


* [RANDOM_BYTES()](https://mariadb.com/kb/en/random-bytes) - is a function for generating good encryption keys for AES_ENCRYPT
* [KDF()](kdf.md) - key derivation function is useful if an authentication validation against the value is required without data being able to be decrypted.


GPLv2 fill_help_tables.sql

