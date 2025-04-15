
# LOOP

## Syntax


```
[begin_label:] LOOP
    statement_list
END LOOP [end_label]
```


## Description


`<code>LOOP</code>` implements a simple loop construct, enabling repeated execution
of the statement list, which consists of one or more statements, each
terminated by a semicolon (i.e., `<code>;</code>`) statement delimiter. The statements
within the loop are repeated until the loop is exited; usually this is
accomplished with a [LEAVE](leave.md) statement.


A `<code>LOOP</code>` statement can be [labeled](labels.md). `<code>end_label</code>` cannot be given unless
`<code>begin_label</code>` also is present. If both are present, they must be the
same.


See [Delimiters](../../../clients-and-utilities/mariadb-client/delimiters.md) in the [mariadb](../../../clients-and-utilities/mariadb-client/README.md) client for more on delimiter usage in the client.


## See Also


* [LOOP in Oracle mode](../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md)
* [ITERATE](iterate.md)
* [LEAVE](leave.md)
* [FOR Loops](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/sys-schema/sys-schema-stored-functions/format_statement.md)

