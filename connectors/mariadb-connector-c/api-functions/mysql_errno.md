# mysql\_errno

## Syntax

```c
unsigned int mysql_errno(MYSQL * mysql);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Returns the last [error code](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-code-reference) for the most recent function call that can succeed or fail. Zero means no error occurred.

{% hint style="info" %}
Client error messages are listed in errmsg.h header file, server error messages are listed in mysqld\_error.h header file of the server source distribution.
{% endhint %}

## See also

* [mysql\_error()](mysql_error.md)
* [mysql\_sqlstate()](mysql_sqlstate.md)

{% @marketo/form formid="4316" %}
