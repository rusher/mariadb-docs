
# UPDATE

## Syntax


Single-table syntax:


```
UPDATE [LOW_PRIORITY] [IGNORE] table_reference 
  [PARTITION (partition_list)]
  [FOR PORTION OF period FROM expr1 TO expr2]
  SET col1={expr1|DEFAULT} [,col2={expr2|DEFAULT}] ...
  [WHERE where_condition]
  [ORDER BY ...]
  [LIMIT row_count]
```

Multiple-table syntax:


```
UPDATE [LOW_PRIORITY] [IGNORE] table_references
    SET col1={expr1|DEFAULT} [, col2={expr2|DEFAULT}] ...
    [WHERE where_condition]
```


## Description


For the single-table syntax, the `UPDATE` statement updates
columns of existing rows in the named table with new values. The
`SET` clause indicates which columns to modify and the values
they should be given. Each value can be given as an expression, or the keyword
`DEFAULT` to set a column explicitly to its default value. The
`WHERE` clause, if given, specifies the conditions that identify
which rows to update. With no `WHERE` clause, all rows are
updated. If the [ORDER BY](../selecting-data/order-by.md) clause is specified, the rows are
updated in the order that is specified. The [LIMIT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/limitationsdifferences-with-a-mariadb-server-compiled-for-debugging.md) clause
places a limit on the number of rows that can be updated.


Both clauses can be used with multiple-table updates. Prior to [MariaDB 10.3](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md), for the multiple-table syntax, `UPDATE` updates rows in each table named in table_references that satisfy the conditions. In this case,
[ORDER BY](../selecting-data/order-by.md) and [LIMIT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/limitationsdifferences-with-a-mariadb-server-compiled-for-debugging.md) could not be used.


An `UPDATE` can also reference tables which are located in different databases; see [Identifier Qualifiers](../../../sql-language-structure/identifier-qualifiers.md) for the syntax.


`where_condition` is an expression that evaluates to true for
each row to be updated.


`table_references` and `where_condition` are as
specified as described in [SELECT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md).


For single-table updates, assignments are evaluated in left-to-right order, while for multi-table updates, there is no guarantee of a particular order. If the `SIMULTANEOUS_ASSIGNMENT` [sql_mode](../../../../../server-management/variables-and-modes/sql-mode.md) is set, UPDATE statements evaluate all assignments simultaneously.


You need the `UPDATE` privilege only for columns referenced in
an `UPDATE` that are actually updated. You need only the
[SELECT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) privilege for any columns that are read but
not modified. See [GRANT](../../account-management-sql-commands/grant.md).


The `UPDATE` statement supports the following modifiers:


* If you use the `LOW_PRIORITY` keyword, execution of
 the `UPDATE` is delayed until no other clients are reading from
 the table. This affects only storage engines that use only table-level
 locking (MyISAM, MEMORY, MERGE). See [HIGH_PRIORITY and LOW_PRIORITY clauses](high_priority-and-low_priority.md) for details.
* If you use the `IGNORE` keyword, the update statement does 
 not abort even if errors occur during the update. Rows for which
 duplicate-key conflicts occur are not updated. Rows for which columns are
 updated to values that would cause data conversion errors are updated to the
 closest valid values instead.


### PARTITION


See [Partition Pruning and Selection](../../../../../server-management/partitioning-tables/partition-pruning-and-selection.md) for details.


### FOR PORTION OF


See [Application Time Periods - Updating by Portion](../../../temporal-tables/application-time-periods.md#updating-by-portion).


### UPDATE Statements With the Same Source and Target


UPDATE statements may have the same source and target.
For example, given the following table:


```
DROP TABLE t1;
CREATE TABLE t1 (c1 INT, c2 INT);
INSERT INTO t1 VALUES (10,10), (20,20);

UPDATE t1 SET c1=c1+1 WHERE c2=(SELECT MAX(c2) FROM t1);

SELECT * FROM t1;
+------+------+
| c1   | c2   |
+------+------+
|   10 |   10 |
|   21 |   20 |
+------+------+
```

## Example


Single-table syntax:


```
UPDATE table_name SET column1 = value1, column2 = value2 WHERE id=100;
```

Multiple-table syntax:


```
UPDATE tab1, tab2 SET tab1.column1 = value1, tab1.column2 = value2 WHERE tab1.id = tab2.id;
```

## See Also


* [How IGNORE works](../inserting-loading-data/ignore.md)
* [SELECT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)
* [ORDER BY](../selecting-data/order-by.md)
* [LIMIT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/limitationsdifferences-with-a-mariadb-server-compiled-for-debugging.md)
* [Identifier Qualifiers](../../../sql-language-structure/identifier-qualifiers.md)

