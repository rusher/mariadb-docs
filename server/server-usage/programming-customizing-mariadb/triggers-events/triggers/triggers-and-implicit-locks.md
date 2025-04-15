
# Triggers and Implicit Locks

A [trigger](triggers-and-implicit-locks.md) may reference multiple tables, and if a `<code>[LOCK TABLES](../../../../reference/sql-statements-and-structure/sql-statements/transactions/lock-tables.md)</code>` statement is used on one of the tables, other tables may at the same time also implicitly be locked due to the trigger.


If the trigger only reads from the other table, that table will be read locked. If the trigger writes to the other table, it will be write locked. If a table is read-locked for reading via `<code>LOCK TABLES</code>`, but needs to be write-locked because it could be modified by a trigger, a write lock is taken.


All locks are acquired together when the `<code>LOCK TABLES</code>` statement is issued and they are released together on `<code>UNLOCK TABLES</code>`.


## Example


```
LOCK TABLE table1 WRITE
```

Assume `<code>table1</code>` contains the following trigger:


```
CREATE TRIGGER trigger1 AFTER INSERT ON table1 FOR EACH ROW
BEGIN
  INSERT INTO table2 VALUES (1);
  UPDATE table3 SET writes = writes+1
    WHERE id = NEW.id AND EXISTS (SELECT id FROM table4);
END;
```

Not only is `<code>table1</code>` write locked, `<code>table2</code>` and `<code>table3</code>` are also write locked, due to the possible `<code>[INSERT](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/insert-function.md)</code>` and `<code>[UPDATE](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md)</code>`, while `<code>table4</code>` is read locked due to the `<code>[SELECT](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)</code>`.

