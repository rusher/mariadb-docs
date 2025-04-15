
# CLOSE

## Syntax


```
CLOSE cursor_name
```


## Description


This statement closes a previously [opened](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/qa-datasets/openstreetmap-dataset.md) cursor. The cursor must have been previously opened or else an error occurs.


If not closed explicitly, a cursor is closed at the end of the
compound statement in which it was declared.


See [Cursor Overview](cursor-overview.md) for an example.


## See Also


* [Cursor Overview](cursor-overview.md)
* [DECLARE CURSOR](declare-cursor.md)
* [OPEN cursor_name](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/qa-datasets/openstreetmap-dataset.md)
* [FETCH cursor_name](fetch.md)
* [Cursors in Oracle mode](../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md)

