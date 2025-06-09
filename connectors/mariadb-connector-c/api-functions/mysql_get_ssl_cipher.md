# mysql\_get\_ssl\_cipher

## Syntax

```c
const char *mysql_get_ssl_cipher(MYSQL *mysql)
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Returns the name of the currently used cipher of the [TLS connection](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview), or NULL for non TLS connections.

## See also

* [mysql\_ssl\_set()](mysql_ssl_set.md)


{% @marketo/form formid="4316" %}
