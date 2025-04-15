
# LAST_INSERT_ID

## Syntax


```
LAST_INSERT_ID(), LAST_INSERT_ID(expr)
```


## Description


LAST_INSERT_ID() (no arguments) returns
the first automatically generated value successfully inserted for an
[AUTO_INCREMENT](../../../../../storage-engines/innodb/auto_increment-handling-in-innodb.md) column as a result of the most recently executed INSERT
statement. The value of LAST_INSERT_ID() remains unchanged if no rows
are successfully inserted.


If one gives an argument to LAST_INSERT_ID(), then it will return the value of the expression and
the next call to LAST_INSERT_ID() will return the same value. The value will also be sent to the client
and can be accessed by the [mysql_insert_id](../../../../../../../connectors/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_insert_id.md) function.


For example, after inserting a row that generates an AUTO_INCREMENT
value, you can get the value like this:


```
SELECT LAST_INSERT_ID();
+------------------+
| LAST_INSERT_ID() |
+------------------+
|                9 |
+------------------+
```

You can also use LAST_INSERT_ID() to delete the last inserted row:


```
DELETE FROM product WHERE id = LAST_INSERT_ID();
```

If no rows were successfully inserted, LAST_INSERT_ID() returns 0.


One can also use [INSERT...RETURNING](../../../data-manipulation/inserting-loading-data/insertreturning.md) for this purpose.


The value of LAST_INSERT_ID() will be consistent across all versions
if all rows in the [INSERT](../../string-functions/insert-function.md) or [UPDATE](../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md) statement were successful.


The currently executing statement does not affect the value of
LAST_INSERT_ID(). Suppose that you generate an AUTO_INCREMENT value
with one statement, and then refer to LAST_INSERT_ID() in a
multiple-row INSERT statement that inserts rows into a table with its
own AUTO_INCREMENT column. The value of LAST_INSERT_ID() will remain
stable in the second statement; its value for the second and later
rows is not affected by the earlier row insertions. (However, if you
mix references to LAST_INSERT_ID() and LAST_INSERT_ID(expr), the
effect is undefined.)


If the previous statement returned an error, the value of
LAST_INSERT_ID() is undefined. For transactional tables, if the
statement is rolled back due to an error, the value of
LAST_INSERT_ID() is left undefined. For manual [ROLLBACK](../../../transactions/rollback.md), the value of
LAST_INSERT_ID() is not restored to that before the transaction; it
remains as it was at the point of the ROLLBACK.


Within the body of a stored routine (procedure or function) or a
trigger, the value of LAST_INSERT_ID() changes the same way as for
statements executed outside the body of these kinds of objects. The
effect of a stored routine or trigger upon the value of
LAST_INSERT_ID() that is seen by following statements depends on the
kind of routine:


* If a [stored procedure](../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md) executes statements that change the value of LAST_INSERT_ID(), the new value will be seen by statements that follow the procedure call.


* For [stored functions](../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) and [triggers](../../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/triggers-and-implicit-locks.md) that change the value, the value is restored when the function or trigger ends, so following statements will not see a changed value.


## Examples


```
CREATE TABLE t (
  id INTEGER UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
  f VARCHAR(1)) 
ENGINE = InnoDB;

INSERT INTO t(f) VALUES('a');

SELECT LAST_INSERT_ID();
+------------------+
| LAST_INSERT_ID() |
+------------------+
|                1 |
+------------------+

INSERT INTO t(f) VALUES('b');

INSERT INTO t(f) VALUES('c');

SELECT LAST_INSERT_ID();
+------------------+
| LAST_INSERT_ID() |
+------------------+
|                3 |
+------------------+

INSERT INTO t(f) VALUES('d'),('e');

SELECT LAST_INSERT_ID();
+------------------+
| LAST_INSERT_ID() |
+------------------+
|                4 |
+------------------+

SELECT * FROM t;
+----+------+
| id | f    |
+----+------+
|  1 | a    |
|  2 | b    |
|  3 | c    |
|  4 | d    |
|  5 | e    |
+----+------+

SELECT LAST_INSERT_ID(12);
+--------------------+
| LAST_INSERT_ID(12) |
+--------------------+
|                 12 |
+--------------------+

SELECT LAST_INSERT_ID();
+------------------+
| LAST_INSERT_ID() |
+------------------+
|               12 |
+------------------+

INSERT INTO t(f) VALUES('f');

SELECT LAST_INSERT_ID();
+------------------+
| LAST_INSERT_ID() |
+------------------+
|                6 |
+------------------+

SELECT * FROM t;
+----+------+
| id | f    |
+----+------+
|  1 | a    |
|  2 | b    |
|  3 | c    |
|  4 | d    |
|  5 | e    |
|  6 | f    |
+----+------+

SELECT LAST_INSERT_ID(12);
+--------------------+
| LAST_INSERT_ID(12) |
+--------------------+
|                 12 |
+--------------------+

INSERT INTO t(f) VALUES('g');

SELECT * FROM t;
+----+------+
| id | f    |
+----+------+
|  1 | a    |
|  2 | b    |
|  3 | c    |
|  4 | d    |
|  5 | e    |
|  6 | f    |
|  7 | g    |
+----+------+
```

## See Also


* [mysql_insert_id](../../../../../../../connectors/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_insert_id.md)
* [AUTO_INCREMENT](../../../../../storage-engines/innodb/auto_increment-handling-in-innodb.md)
* [AUTO_INCREMENT handling in InnoDB](../../../../../storage-engines/innodb/auto_increment-handling-in-innodb.md)
* [Sequences](../../../../sequences/README.md) - an alternative to auto_increment
* [INSERT...RETURNING](../../../data-manipulation/inserting-loading-data/insertreturning.md)

