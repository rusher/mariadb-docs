
# EXECUTE Statement

## Syntax


```
EXECUTE stmt_name
    [USING expression[, expression] ...]
```


## Description


After preparing a statement with `[PREPARE](prepare-statement.md)`, you execute it with an
`EXECUTE` statement that refers to the prepared statement name. If the
prepared statement contains any parameter markers, you must supply a
`USING` clause that lists user variables containing the values to be
bound to the parameters. Parameter values can be supplied only by user
variables, and the `USING` clause must name exactly as many variables as
the number of parameter markers in the statement.


You can execute a given prepared statement multiple times, passing
different variables to it or setting the variables to different values
before each execution.


If the specified statement has not been PREPAREd, an error similar to the following is produced:


```
ERROR 1243 (HY000): Unknown prepared statement handler (stmt_name) given to EXECUTE
```

`EXECUTE` with expression as parameters was introduced in [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes). Prior to that one could only use variables (@var_name) as parameters.


## Example


See [example in PREPARE](prepare-statement.md#example).


## See Also


* [EXECUTE IMMEDIATE](execute-immediate.md)


GPLv2 fill_help_tables.sql

