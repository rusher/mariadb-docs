
# INET_NTOA

## Syntax


```
INET_NTOA(expr)
```

## Description


Given a numeric IPv4 network address in network byte order (4 or 8 byte),
returns the dotted-quad representation of the address as a string.


## Examples


```
SELECT INET_NTOA(3232235777);
+-----------------------+
| INET_NTOA(3232235777) |
+-----------------------+
| 192.168.1.1           |
+-----------------------+
```

192.168.1.1 corresponds to 3232235777 since 192 x 2563 + 168 x 256 2 + 1 x 256 + 1 = 3232235777


## See Also


* [INET6_NTOA()](inet6_ntoa.md)
* [INET_ATON()](inet_aton.md)


GPLv2 fill_help_tables.sql

