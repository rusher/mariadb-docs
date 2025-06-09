# mysql\_error

## Syntax

```c
const char * mysql_error(MYSQL * mysql);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Returns the last error message for the most recent function call that can succeed or fail. If no error occurred an empty string is returned.

## See also

* [mysql\_errno()](mysql_errno.md)
* [mysql\_sqlstate()](mysql_sqlstate.md).

{% @marketo/form formid="4316" %}
