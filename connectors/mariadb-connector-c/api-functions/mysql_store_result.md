# mysql\_store\_result

## Syntax

```c
MYSQL_RES * mysql_store_result(MYSQL * mysql);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Returns a buffered resultset from the last executed query.

{% hint style="info" %}
mysql\_store\_result() returns NULL in case an error occured or if the query didn't return data (e.g. when executing an [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert) or [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/update) query.

[mysql\_field\_count()](mysql_field_count.md) indicates if there will be a result set available.

The memory allocated by mysql\_store\_result() needs to be released by calling the function [mysql\_free\_result()](mysql_free_result.md).
{% endhint %}

## See also

* [mysql\_use\_result()](mysql_use_result.md)
* [mysql\_real\_query()](mysql_real_query.md)
* [mysql\_field\_count()](mysql_field_count.md)


{% @marketo/form formId="4316" %}
