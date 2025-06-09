# mariadb\_stmt\_fetch\_fields

## Syntax

```c
MYSQL_FIELD *mariadb_stmt_fetch_fields(MYSQL_STMT * stmt);
```

* `stmt` - A statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).

## Description

Returns an array of fields. Each field contains the definition for a column of the result set.\
If the statement doesn't have a result set a NULL pointer will be returned.

This function was added in Connector/C 3.1.0

{% hint style="info" %}
The number of fields can be obtained by [mysql\_stmt\_field\_count()](mysql_stmt_field_count.md)
{% endhint %}

## See Also

* [mysql\_stmt\_field\_count()](mysql_stmt_field_count.md)

{% @marketo/form formid="4316" %}
