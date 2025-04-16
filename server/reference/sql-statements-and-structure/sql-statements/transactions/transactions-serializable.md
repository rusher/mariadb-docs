
# SERIALIZABLE

`SERIALIZABLE` is one of the transaction isolation levels. Similar to REPEATABLE READ, but InnoDB implicitly converts all plain SELECT statements to SELECT ... LOCK IN SHARE MODE if autocommit is disabled.


See [SET TRANSACTION#Isolation Levels](set-transaction.md#isolation-levels) for details.

