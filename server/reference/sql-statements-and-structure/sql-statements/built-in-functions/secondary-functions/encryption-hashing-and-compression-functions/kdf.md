
# KDF


##### MariaDB starting with [11.3](../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-113.md)
KDF() is a key derivation function introduced in [MariaDB 11.3.0](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md).


## Syntax


```
KDF(key_str, salt [, {info | iterations} [, kdf_name [, width ]]])
```

## Description


`<code>KDF</code>` is a key derivation function, similar to OpenSSL's EVP_KDF_derive(). The purpose of a KDF is to be slow, so if the calculated value is lost/stolen, the original `<code>key_str</code>` is not achievable easily with modern GPU. KDFs are therefore an ideal replacement for password hashes. KDFs can also pad out a password secret to the number of bits used in encryption algorithms.


For generating good encryption keys for [AES_ENCRYPT](aes_encrypt.md) a less expensive but cryptographically secure function like [RANDOM_BYTES](random_bytes.md) is recommended.


* kdf_name is "hkdf" or "pbkdf2_hmac" (default)
* width (in bits) can be any number divisible by 8, by default it's taken from @@block_encryption_mode
* iterations must be positive, and is 1000 by default


Note that OpenSSL 1.0 doesn't support HKDF, so in this case NULL is returned. This OpenSSL version is still used in SLES 12 and CentOS 7.


## Examples


```
select hex(kdf('foo', 'bar', 'infa', 'hkdf')); 
+----------------------------------------+
| hex(kdf('foo', 'bar', 'infa', 'hkdf')) |
+----------------------------------------+
| 612875F859CFB4EE0DFEFF9F2A18E836       |
+----------------------------------------+
```
