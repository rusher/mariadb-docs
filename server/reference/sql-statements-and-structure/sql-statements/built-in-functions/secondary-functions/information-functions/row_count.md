
# ROW_COUNT

## Syntax


```
ROW_COUNT()
```

## Description


ROW_COUNT() returns the number of rows updated, inserted or deleted
by the preceding statement. This is the same as the row count that the
mariadb client displays and the value from the [mysql_affected_rows()](../../../../../../../connectors/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_affected_rows.md) C
API function.


Generally:


* For statements which return a result set (such as [SELECT](../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md), [SHOW](../../../administrative-sql-statements/show/show-procedure-code.md), [DESC](../../../administrative-sql-statements/describe.md) or [HELP](../../../administrative-sql-statements/help-command.md)), returns -1, even when the result set is empty. This is also true for administrative statements, such as [OPTIMIZE](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/optimize-table.md).
* For DML statements other than [SELECT](../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) and for [ALTER TABLE](../../../../../../../general-resources/learning-and-training/training-and-tutorials/beginner-mariadb-articles/altering-tables-in-mariadb.md), returns the number of affected rows.
* For DDL statements (including [TRUNCATE](../../../table-statements/truncate-table.md)) and for other statements which don't return any result set (such as [USE](../../../../../../../general-resources/learning-and-training/training-and-tutorials/beginner-mariadb-articles/useful-mariadb-queries.md), [DO](../../../../../../../general-resources/company-and-community/contributing-participating/donate-to-the-foundation.md), [SIGNAL](../../../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/signal.md) or [DEALLOCATE PREPARE](../../../prepared-statements/deallocate-drop-prepare.md)), returns 0.


For [UPDATE](../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md), affected rows is by default the number of rows that were actually changed. If the CLIENT_FOUND_ROWS flag to [mysql_real_connect()](../../../../../../../connectors/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_real_connect.md) is specified when connecting to mariadbd, affected rows is instead the number of rows matched by the WHERE clause.


For [REPLACE](../../string-functions/replace-function.md), deleted rows are also counted. So, if REPLACE deletes a row and adds a new row, ROW_COUNT() returns 2.


For [INSERT ... ON DUPLICATE KEY](../../../data-manipulation/inserting-loading-data/insert-on-duplicate-key-update.md), values returned are as follows:


* 0: an existing row is set to its current values, and the CLIENT_FOUND_ROWS is not set
* 1: the values are inserted as a new row, or an existing row is set to its current values, and the CLIENT_FOUND_ROWS is set
* 2: an existing row is updated with new values


ROW_COUNT() does not take into account rows that are not directly deleted/updated by the last statement. This means that rows deleted by foreign keys or triggers are not counted.


**Warning:** You can use ROW_COUNT() with prepared statements, but you need to call it after EXECUTE, not after [DEALLOCATE PREPARE](../../../prepared-statements/deallocate-drop-prepare.md), because the row count for allocate prepare is always 0.


**Warning:** When used after a [CALL](../../../stored-routine-statements/call.md) statement, this function returns the number of rows affected by the last statement in the procedure, not by the whole procedure.


**Warning:** After [INSERT DELAYED](../../../data-manipulation/inserting-loading-data/insert-delayed.md), ROW_COUNT() returns the number of the rows you tried to insert, not the number of the successful writes.


This information can also be found in the [diagnostics area](../../../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/programmatic-compound-statements-diagnostics/diagnostics-area.md).


Statements using the ROW_COUNT() function are not [safe for statement-based replication](../../../../../../server-usage/replication-cluster-multi-master/standard-replication/unsafe-statements-for-statement-based-replication.md).


## Examples


```
CREATE TABLE t (A INT);

INSERT INTO t VALUES(1),(2),(3);

SELECT ROW_COUNT();
+-------------+
| ROW_COUNT() |
+-------------+
|           3 |
+-------------+

DELETE FROM t WHERE A IN(1,2);

SELECT ROW_COUNT(); 
+-------------+
| ROW_COUNT() |
+-------------+
|           2 |
+-------------+
```

Example with prepared statements:


```
SET @q = 'INSERT INTO t VALUES(1),(2),(3);';

PREPARE stmt FROM @q;

EXECUTE stmt;
Query OK, 3 rows affected (0.39 sec)
Records: 3  Duplicates: 0  Warnings: 0

SELECT ROW_COUNT();
+-------------+
| ROW_COUNT() |
+-------------+
|           3 |
+-------------+
```

## See Also


* [FOUND_ROWS()](found_rows.md)

