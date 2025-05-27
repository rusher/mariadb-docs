# DES\_DECRYPT

DES\_DECRYPT has been deprecated from [MariaDB 10.10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/mariadb-10100-release-notes), and will be removed in a future release.

## Syntax

```
DES_DECRYPT(crypt_str[,key_str])
```

## Description

Decrypts a string encrypted with `[DES_ENCRYPT()](des_encrypt.md)`. If an error occurs,\
this function returns `NULL`.

This function works only if MariaDB has been configured with [TLS\
support](../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md).

If no `key_str` argument is given, `DES_DECRYPT()` examines the first byte\
of the encrypted string to determine the DES key number that was used\
to encrypt the original string, and then reads the key from the DES\
key file to decrypt the message. For this to work, the user must have\
the SUPER privilege. The key file can be specified with the`--des-key-file` server option.

If you pass this function a `key_str` argument, that string is used as\
the key for decrypting the message.

If the `crypt_str` argument does not appear to be an encrypted string,\
MariaDB returns the given crypt\_str.

GPLv2 fill\_help\_tables.sql
