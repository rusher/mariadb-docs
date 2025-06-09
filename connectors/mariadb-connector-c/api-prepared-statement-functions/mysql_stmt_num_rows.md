# mysql\_stmt\_num\_rows

## Syntax

```c
unsigned long long mysql_stmt_num_rows(MYSQL_STMT * stmt);
```

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).

## Description

Returns the number of rows in the result set. The use of mysql\_stmt\_num\_rows() depends on whether or not you used [mysql\_stmt\_store\_result()](mysql_stmt_store_result.md) to buffer the entire result set in the statement handle.

{% hint style="info" %}
If you use [mysql\_stmt\_store\_result()](mysql_stmt_store_result.md), mysql\_stmt\_num\_rows() may be called immediately.
{% endhint %}

## See Also

* [mysql\_stmt\_store\_result()](mysql_stmt_store_result.md)

{% @marketo/form formid="4316" %}
