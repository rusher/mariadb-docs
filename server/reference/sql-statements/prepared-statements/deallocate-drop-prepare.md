
# DEALLOCATE / DROP PREPARE

## Syntax


```
{DEALLOCATE | DROP} PREPARE stmt_name
```

## Description


To deallocate a prepared statement produced with `[PREPARE](prepare-statement.md)`, use a
`DEALLOCATE PREPARE` statement that refers to the prepared statement
name.


A prepared statement is implicitly deallocated when a new `PREPARE` command is issued. In that case, there is no need to use `DEALLOCATE`.


Attempting to execute a prepared statement after deallocating it
results in an error, as if it was not prepared at all:


```
ERROR 1243 (HY000): Unknown prepared statement handler (stmt_name) given to EXECUTE
```

If the specified statement has not been PREPAREd, an error similar to the following will be produced:


```
ERROR 1243 (HY000): Unknown prepared statement handler (stmt_name) given to DEALLOCATE PREPARE
```

## Example


See [example in PREPARE](prepare-statement.md#example).


## See Also


* [PREPARE Statement](prepare-statement.md)
* [EXECUTE Statement](execute-statement.md)
* [EXECUTE IMMEDIATE](execute-immediate.md)


GPLv2 fill_help_tables.sql


{% @marketo/form formId="4316" %}
