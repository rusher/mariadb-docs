
# DES_DECRYPT

DES_DECRYPT has been deprecated from [MariaDB 10.10.0](../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-10-series/mariadb-10100-release-notes.md), and will be removed in a future release.


## Syntax


```
DES_DECRYPT(crypt_str[,key_str])
```

## Description


Decrypts a string encrypted with `<code>[DES_ENCRYPT()](des_encrypt.md)</code>`. If an error occurs,
this function returns `<code>NULL</code>`.


This function works only if MariaDB has been configured with [TLS
support](../../../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md).


If no `<code>key_str</code>` argument is given, `<code>DES_DECRYPT()</code>` examines the first byte
of the encrypted string to determine the DES key number that was used
to encrypt the original string, and then reads the key from the DES
key file to decrypt the message. For this to work, the user must have
the SUPER privilege. The key file can be specified with the
`<code>--des-key-file</code>` server option.


If you pass this function a `<code>key_str</code>` argument, that string is used as
the key for decrypting the message.


If the `<code>crypt_str</code>` argument does not appear to be an encrypted string,
MariaDB returns the given crypt_str.

