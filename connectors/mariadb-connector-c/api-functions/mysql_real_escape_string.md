# mysql\_real\_escape\_string

## Syntax

```c
unsigned long mysql_real_escape_string(MYSQL * mysql,
                                       char * to,
                                       const char * from,
                                       unsigned long);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `to` - buffer for the encoded string. The size of this buffer must be length \* 2 + 1 bytes: in worst case every character of the from string needs to be escaped. Additionally a trailing 0 character will be appended.
* `from` - a string which will be encoded by mysql\_real\_escape\_string().
* `long` - the length of the `from` string.

## Description

This function is used to create a legal SQL string that you can use in an SQL statement. The given string is encoded to an escaped SQL string, taking into account the current character set of the connection.

Returns the length of the encoded (to) string.

{% @marketo/form formid="4316" %}
