# mysql\_real\_query

## Syntax

```c
int mysql_real_query(MYSQL * mysql,
                     const char * q,
                     unsigned long);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `query` - a string containing the statement to be performed.
* `long` - length of the string.

## Description

mysql\_real\_query() is the binary safe function for performing a statement on the database server. Returns zero on success, otherwise non-zero.

{% hint style="info" %}
Contrary to the [mysql\_query()](mysql_query.md) function, mysql\_real\_query is binary safe.

To determine if mysql\_real\_query returns a result set use the [mysql\_num\_fields()](mysql_num_fields.md) function.
{% endhint %}

## See also

* [mysql\_query()](mysql_query.md)
* [mysql\_num\_fields()](mysql_num_fields.md)
* [mysql\_use\_result()](mysql_use_result.md)
* [mysql\_store\_result()](mysql_store_result.md)


{% @marketo/form formId="4316" %}
