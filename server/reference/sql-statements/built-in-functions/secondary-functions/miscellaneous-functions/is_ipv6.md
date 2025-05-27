# IS\_IPV6

## Syntax

```
IS_IPV6(expr)
```

## Description

Returns 1 if the expression is a valid IPv6 address specified as a string, otherwise returns 0. Does not consider IPv4 addresses to be valid IPv6 addresses.

## Examples

```
SELECT IS_IPV6('48f3::d432:1431:ba23:846f');
+--------------------------------------+
| IS_IPV6('48f3::d432:1431:ba23:846f') |
+--------------------------------------+
|                                    1 |
+--------------------------------------+
1 row in set (0.02 sec)

SELECT IS_IPV6('10.0.1.1');
+---------------------+
| IS_IPV6('10.0.1.1') |
+---------------------+
|                   0 |
+---------------------+
```

## See Also

* [INET6](../../../../data-types/string-data-types/inet6.md) data type
* [INET6\_ATON](inet6_aton.md)
* [INET6\_NTOA](inet6_ntoa.md)

CC BY-SA / Gnu FDL
