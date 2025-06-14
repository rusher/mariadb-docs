# DECLARE CURSOR

## Syntax

Until [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107)

```
DECLARE cursor_name CURSOR [(cursor_formal_parameter[,...])] FOR select_statement

cursor_formal_parameter:
    name type [collate clause]
```

From [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108)

```
DECLARE cursor_name CURSOR [(cursor_formal_parameter[,...])] FOR select_statement

cursor_formal_parameter:
    [IN] name type [collate clause]
```

## Description

This statement declares a [cursor](./). Multiple cursors may be declared in a [stored program](../../../../server-usage/stored-routines/), but each cursor in a given block must have a unique name.

`select_statement` is not executed until the [OPEN](open.md) statement is executed. It is important to remember this if the query produces an error, or calls functions which have side effects.

A `SELECT` associated to a cursor can use variables, but the query itself cannot be a variable, and cannot be dynamically composed. The `SELECT` statement cannot have an `INTO` clause.

Cursors must be declared before [HANDLERs](../declare-handler.md), but after local variables and [CONDITIONs](../declare-condition.md).

### Parameters

Cursors can have parameters. This is a non-standard SQL extension. Cursor parameters can appear in any part of the DECLARE CURSOR select\_statement where a stored procedure variable is allowed (select list, WHERE, HAVING, LIMIT etc).

### IN

**MariaDB starting with** [**10.8.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes)

From [MariaDB 10.8.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes) preview release, the `IN` qualifier is supported in the `cursor_formal_parameter` part of the syntax.

See [Cursor Overview](cursor-overview.md) for an example.

## See Also

* [Cursor Overview](cursor-overview.md)
* [OPEN cursor\_name](open.md)
* [FETCH cursor\_name](fetch.md)
* [CLOSE cursor\_name](close.md)
* [Cursors in Oracle mode](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/programmatic-compound-statements/programmatic-compound-statements-cursors/broken-reference/README.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
