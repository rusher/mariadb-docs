
# UNLOCK TABLES

## Syntax


```
UNLOCK TABLES
```


## Description


`UNLOCK TABLES` explicitly releases any table locks held by the
current session. See `[LOCK TABLES](lock-tables.md)` for more information.


In addition to releasing table locks acquired by the `[LOCK TABLES](lock-tables.md)` statement, the `UNLOCK TABLES` statement also releases the global read lock acquired by the `FLUSH TABLES WITH READ LOCK` statement. The `FLUSH TABLES WITH READ LOCK` statement is very useful for performing backups. See `[FLUSH](../administrative-sql-statements/flush-commands/flush-tables-for-export.md)` for more information about `FLUSH TABLES WITH READ LOCK`.

