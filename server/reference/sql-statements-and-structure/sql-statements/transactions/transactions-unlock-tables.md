
# UNLOCK TABLES

## Syntax


```
UNLOCK TABLES
```


## Description


`<code>UNLOCK TABLES</code>` explicitly releases any table locks held by the
current session. See `<code>[LOCK TABLES](lock-tables.md)</code>` for more information.


In addition to releasing table locks acquired by the `<code>[LOCK TABLES](lock-tables.md)</code>` statement, the `<code>UNLOCK TABLES</code>` statement also releases the global read lock acquired by the `<code>FLUSH TABLES WITH READ LOCK</code>` statement. The `<code>FLUSH TABLES WITH READ LOCK</code>` statement is very useful for performing backups. See `<code>[FLUSH](../administrative-sql-statements/flush-commands/flush-tables-for-export.md)</code>` for more information about `<code>FLUSH TABLES WITH READ LOCK</code>`.

