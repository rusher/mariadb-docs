# CLOSE

## Syntax

```
CLOSE cursor_name
```

## Description

This statement closes a previously [opened](open.md) cursor. The cursor must have been previously opened or else an error occurs.

If not closed explicitly, a cursor is closed at the end of the\
compound statement in which it was declared.

See [Cursor Overview](cursor-overview.md) for an example.

## See Also

* [Cursor Overview](cursor-overview.md)
* [DECLARE CURSOR](declare-cursor.md)
* [OPEN cursor\_name](open.md)
* [FETCH cursor\_name](fetch.md)
* [Cursors in Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/comparison/sql_modeoracle)

GPLv2 fill\_help\_tables.sql
