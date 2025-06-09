# KDF

**MariaDB starting with** [**11.3**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113)

KDF() is a key derivation function introduced in [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes).

## Syntax

```
KDF(key_str, salt [, {info | iterations} [, kdf_name [, width ]]])
```

## Description

`KDF` is a key derivation function, similar to OpenSSL's EVP\_KDF\_derive(). The purpose of a KDF is to be slow, so if the calculated value is lost/stolen, the original `key_str` is not achievable easily with modern GPU. KDFs are therefore an ideal replacement for password hashes. KDFs can also pad out a password secret to the number of bits used in encryption algorithms.

For generating good encryption keys for [AES\_ENCRYPT](aes_encrypt.md) a less expensive but cryptographically secure function like [RANDOM\_BYTES](random_bytes.md) is recommended.

* kdf\_name is "hkdf" or "pbkdf2\_hmac" (default)
* width (in bits) can be any number divisible by 8, by default it's taken from @@block\_encryption\_mode
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

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
