# mysql\_stmt\_free\_result

## Syntax

```c
my_bool mysql_stmt_free_result(MYSQL_STMT * stmt);
```

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).

## Description

Frees stored result memory of a prepared statement. Returns void.

## See Also

* [mysql\_stmt\_store\_result()](mysql_stmt_store_result.md)


{% @marketo/form formid="4316" %}
