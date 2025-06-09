# mysql\_kill

## Syntax

```c
int mysql_kill(MYSQL * mysql,
               unsigned long);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `long` - process id

## Description

This function is used to ask the server to kill a MariaDB thread specified by the processid parameter. This value must be retrieved by [SHOW PROCESSLIST](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-processlist). If trying to kill the own connection [mysql\_thread\_id()](mysql_thread_id.md) should be used.

Returns 0 on success, otherwise nonzero.

{% hint style="info" %}
To stop a running command without killing the connection use [KILL QUERY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/kill). The mysql\_kill() function only kills a connection, it doesn't free any memory - this must be done explicitly by calling [mysql\_close()](mysql_close.md).
{% endhint %}

## See also

* [mysql\_thread\_id()](mysql_thread_id.md)
* [mysql\_close()](mysql_close.md)
* [mariadb\_cancel()](mariadb_cancel.md)


{% @marketo/form formid="4316" %}
