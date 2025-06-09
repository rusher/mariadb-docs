# mysql\_stmt\_execute

## Syntax

```c
int mysql_stmt_execute(MYSQL_STMT * stmt);
```

* `stmt` - A statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).

## Description

Executes a prepared statement which was previously prepared by [mysql\_stmt\_prepare()](mysql_stmt_prepare.md). When executed any parameter markers which exist will automatically be replaced with the appropriate data.

Returns zero on success, non-zero on failure.

{% hint style="info" %}
If the statement is [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/update), [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/delete), or [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert), the total number of affected rows can be determined by using the mysql\_stmt\_affected\_rows() function. Likewise, if the query yields a result set the mysql\_stmt\_fetch() function is used.
{% endhint %}

## See Also

* [mariadb\_stmt\_execute\_direct()](mariadb_stmt_execute_direct.md)
* [mysql\_stmt\_prepare()](mysql_stmt_prepare.md)
* [mysql\_stmt\_bind\_param()](mysql_stmt_bind_param.md)
* [mysql\_stmt\_next\_result()](mysql_stmt_next_result.md)

{% @marketo/form formid="4316" %}
