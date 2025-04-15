
# OPEN

## Syntax


<= [MariaDB 10.2](../../../../../release-notes/mariadb-community-server/what-is-mariadb-102.md)


```
OPEN cursor_name
```

From [MariaDB 10.3](../../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md)


```
OPEN cursor_name [expression[,...]];
```


## Description


This statement opens a [cursor](README.md) which was previously declared with [DECLARE CURSOR](declare-cursor.md).


The query associated to the DECLARE CURSOR is executed when OPEN is executed. It is important to remember this if the query produces an error, or calls functions which have side effects.


This is necessary in order to [FETCH](fetch.md) rows from a cursor.


See [Cursor Overview](cursor-overview.md) for an example.


## See Also


* [Cursor Overview](cursor-overview.md)
* [DECLARE CURSOR](declare-cursor.md)
* [FETCH cursor_name](fetch.md)
* [CLOSE cursor_name](close.md)
* [Cursors in Oracle mode](../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md)

