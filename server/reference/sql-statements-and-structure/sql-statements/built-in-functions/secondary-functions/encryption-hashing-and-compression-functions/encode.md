
# ENCODE

## Syntax


```
ENCODE(str,pass_str)
```

## Description


ENCODE is not considered cryptographically secure, and should not be used for password encryption.


Encrypt `str` using `pass_str` as the password. To decrypt the result, use
`[DECODE()](decode.md)`.


The result is a binary string of the same length as `str`.


The strength of the encryption is based on how good the random generator is.


It is not recommended to rely on the encryption performed by the ENCODE function. Using a salt value (changed when a password is updated) will improve matters somewhat, but for storing passwords, consider a more cryptographically secure function, such as [SHA2()](sha2.md).


## Examples


```
ENCODE('not so secret text', CONCAT('random_salt','password'))
```


GPLv2 fill_help_tables.sql

