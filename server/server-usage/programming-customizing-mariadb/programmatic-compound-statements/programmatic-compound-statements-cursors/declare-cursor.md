
# DECLARE CURSOR

## Syntax


Until [MariaDB 10.7](../../../../../release-notes/mariadb-community-server/what-is-mariadb-107.md)


```
DECLARE cursor_name CURSOR [(cursor_formal_parameter[,...])] FOR select_statement

cursor_formal_parameter:
    name type [collate clause]
```

From [MariaDB 10.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-108.md)


```
DECLARE cursor_name CURSOR [(cursor_formal_parameter[,...])] FOR select_statement

cursor_formal_parameter:
    [IN] name type [collate clause]
```


## Description


This statement declares a [cursor](README.md). Multiple cursors may be declared in a [stored program](../../stored-routines/README.md), but each cursor in a given block must have a unique name.


`<code>select_statement</code>` is not executed until the [OPEN](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/qa-datasets/openstreetmap-dataset.md) statement is executed. It is important to remember this if the query produces an error, or calls functions which have side effects.


A `<code>SELECT</code>` associated to a cursor can use variables, but the query itself cannot be a variable, and cannot be dynamically composed. The `<code>SELECT</code>` statement cannot have an `<code>INTO</code>` clause.


Cursors must be declared before [HANDLERs](../declare-handler.md), but after local variables and [CONDITIONs](../declare-condition.md).


### Parameters


Cursors can have parameters. This is a non-standard SQL extension. Cursor parameters can appear in any part of the DECLARE CURSOR select_statement where a stored procedure variable is allowed (select list, WHERE, HAVING, LIMIT etc).


### IN



##### MariaDB starting with [10.8.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes.md)
From [MariaDB 10.8.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes.md) preview release, the `<code>IN</code>` qualifier is supported in the `<code>cursor_formal_parameter</code>` part of the syntax.


See [Cursor Overview](cursor-overview.md) for an example.


## See Also


* [Cursor Overview](cursor-overview.md)
* [OPEN cursor_name](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/qa-datasets/openstreetmap-dataset.md)
* [FETCH cursor_name](fetch.md)
* [CLOSE cursor_name](close.md)
* [Cursors in Oracle mode](../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md)

