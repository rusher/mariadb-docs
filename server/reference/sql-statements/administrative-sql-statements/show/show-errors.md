# SHOW ERRORS

## Syntax

```
SHOW ERRORS [LIMIT [offset,] row_count]
SHOW ERRORS [LIMIT row_count OFFSET offset]
SHOW COUNT(*) ERRORS
```

## Description

This statement is similar to [SHOW WARNINGS](show-warnings.md), except that instead of\
displaying errors, warnings, and notes, it displays only errors.

The `LIMIT` clause has the same syntax as for the[SELECT](../../data-manipulation/selecting-data/select.md) statement.

The `SHOW COUNT(*) ERRORS` statement displays the number of\
errors. You can also retrieve this number from the [error\_count](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#error_count) variable.

```
SHOW COUNT(*) ERRORS;
SELECT @@error_count;
```

The value of [error\_count](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#error_count) might be greater than the number of messages displayed by [SHOW WARNINGS](show-warnings.md) if the [max\_error\_count](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_error_count) system variable is set so low that not all messages are stored.

For a list of MariaDB error codes, see [MariaDB Error Codes](broken-reference).

## Examples

```
SELECT f();
ERROR 1305 (42000): FUNCTION f does not exist

SHOW COUNT(*) ERRORS;
+-----------------------+
| @@session.error_count |
+-----------------------+
|                     1 |
+-----------------------+

SHOW ERRORS;
+-------+------+---------------------------+
| Level | Code | Message                   |
+-------+------+---------------------------+
| Error | 1305 | FUNCTION f does not exist |
+-------+------+---------------------------+
```

GPLv2 fill\_help\_tables.sql
