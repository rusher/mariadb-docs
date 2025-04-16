
# RETURN

## Syntax


```
RETURN expr
```

The `RETURN` statement terminates execution of a [stored function](../stored-routines/stored-functions/README.md) and
returns the value *`expr`* to the function caller. There must be at least
one `RETURN` statement in a stored function. If the function has multiple exit points, all exit points must have a `RETURN`.


This statement is not used in [stored procedures](../stored-routines/stored-procedures/README.md), [triggers](../triggers-events/triggers/triggers-and-implicit-locks.md), or [events](../triggers-events/event-scheduler/events.md). [LEAVE](leave.md) can be used instead.


The following example shows that `RETURN` can return the result of a [scalar subquery](../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/joins-subqueries/subqueries/subqueries-scalar-subqueries.md):


```
CREATE FUNCTION users_count() RETURNS BOOL
   READS SQL DATA
BEGIN
   RETURN (SELECT COUNT(DISTINCT User) FROM mysql.user);
END;
```
