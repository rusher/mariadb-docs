
# ROLLBACK

The `<code>ROLLBACK</code>` statement rolls back (ends) a transaction, destroying any changes to SQL-data so that they never become visible to subsequent transactions. The required syntax for the `<code>ROLLBACK</code>` statement is as follows.


```
ROLLBACK [ WORK ] [ AND [ NO ] CHAIN ] 
[ TO [ SAVEPOINT ] {<savepoint name> | <simple target specification>} ]
```

The `<code>ROLLBACK</code>` statement will either end a transaction, destroying all data changes that happened during any of the transaction, or it will just destroy any data changes that happened since you established a savepoint. The basic form of the `<code>ROLLBACK</code>` statement is just the keyword `<code>ROLLBACK</code>` (the keyword `<code>WORK</code>` is simply noise and can be omitted without changing the effect).


The optional `<code>AND CHAIN</code>` clause is a convenience for initiating a new transaction as soon as the old transaction terminates. If `<code>AND CHAIN</code>` is specified, then there is effectively nothing between the old and new transactions, although they remain separate. The characteristics of the new transaction will be the same as the characteristics of the old one — that is, the new transaction will have the same access mode, isolation level and diagnostics area size (we'll discuss all of these shortly) as the transaction just terminated. The `<code>AND NO CHAIN</code>` option just tells your DBMS to end the transaction — that is, these four SQL statements are equivalent:


```
ROLLBACK; 
ROLLBACK WORK; 
ROLLBACK AND NO CHAIN; 
ROLLBACK WORK AND NO CHAIN;
```

All of them end a transaction without saving any transaction characteristics. The only other options, the equivalent statements:


```
ROLLBACK AND CHAIN;
ROLLBACK WORK AND CHAIN;
```

both tell your DBMS to end a transaction, but to save that transaction's characteristics for the next transaction.


`<code>ROLLBACK</code>` is much simpler than `<code>COMMIT</code>`: it may involve no more than a few deletions (of Cursors, locks, prepared SQL statements and log-file entries). It's usually assumed that `<code>ROLLBACK</code>` can't fail, although such a thing is conceivable (for example, an encompassing transaction might reject an attempt to `<code>ROLLBACK</code>` because it's lining up for a `<code>COMMIT</code>`).


`<code>ROLLBACK</code>` cancels all effects of a transaction. It does not cancel effects on objects outside the DBMS's control (for example the values in host program variables or the settings made by some SQL/CLI function calls). But in general, it is a convenient statement for those situations when you say "oops, this isn't working" or when you simply don't care whether your temporary work becomes permanent or not.


Here is a moot question. If all you've been doing is `<code>SELECT</code>`s, so that there have been no data changes, should you end the transaction with `<code>ROLLBACK</code>` or `<code>COMMIT</code>`? It shouldn't really matter because both `<code>ROLLBACK</code>` and `<code>COMMIT</code>` do the same transaction-terminating job. However, the popular conception is that `<code>ROLLBACK</code>` implies failure, so after a successful series of `<code>SELECT</code>` statements the convention is to end the transaction with `<code>COMMIT</code>` rather than `<code>ROLLBACK</code>`.


MariaDB (and most other DBMSs) supports rollback of SQL-data change statements, but not of SQL-Schema statements. This means that if you use any of `<code>CREATE</code>`, `<code>ALTER</code>`, `<code>DROP</code>`, `<code>GRANT</code>`, `<code>REVOKE</code>`, you are implicitly committing at execution time.


```
INSERT INTO Table_2 VALUES(5); 
DROP TABLE Table_3 CASCADE; 
ROLLBACK;
```

The result will be that both the `<code>INSERT</code>` and the `<code>DROP</code>` will go through as separate transactions so the `<code>ROLLBACK</code>` will have no effect.

