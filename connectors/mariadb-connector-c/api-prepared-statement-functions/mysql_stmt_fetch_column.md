# mysql\_stmt\_fetch\_column

## Syntax

```c
int mysql_stmt_fetch_column(MYSQL_STMT * stmt,
                            MYSQL_BIND * bind_arg,
                            unsigned int column,
                            unsigned long offset);
```

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).
* `bind_arg` - a pointer to a MYSQL\_BIND structure.
* `column` - number of column, first column is numbered zero.
* `offset` - offset at which to begin retrieving data.

## Description

This function can be used to fetch large data of a single column in pieces. Returns zero on success, non-zero on failure.

{% hint style="info" %}
The size of the buffer is specified within MYSQL\_BIND structure.
{% endhint %}

## See Also

* [mysql\_stmt\_fetch()](mysql_stmt_fetch.md)
* [mysql\_stmt\_send\_long\_data()](mysql_stmt_send_long_data.md)


{% @marketo/form formId="4316" %}
