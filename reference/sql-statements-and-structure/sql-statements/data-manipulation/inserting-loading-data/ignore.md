# IGNORE

The `IGNORE` option tells the server to ignore some common errors.

`IGNORE` can be used with the following statements:

* [DELETE](../changing-deleting-data/delete.md)
* [INSERT](../../../../../server-usage/programming-customizing-mariadb/views/inserting-and-updating-with-views.md) (see also [INSERT IGNORE](insert-ignore.md))
* [LOAD DATA INFILE](load-data-into-tables-or-index/load-data-infile.md)
* [UPDATE](../changing-deleting-data/update.md)
* [ALTER TABLE](../../data-definition/alter/alter-table.md)
* [CREATE TABLE ... SELECT](../../data-definition/create/create-tablespace.md#create-select)
* [INSERT ... SELECT](insert-select.md)

The logic used:

* Variables out of ranges are replaced with the maximum/minimum value.

* [SQL_MODEs](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/mariadb-releases/compatibility-differences/sql_modemssql) `STRICT_TRANS_TABLES`, `STRICT_ALL_TABLES`, `NO_ZERO_IN_DATE`, `NO_ZERO_DATE` are ignored.

* Inserting `NULL` in a `NOT NULL` field will insert 0 ( in a numerical
 field), 0000-00-00 ( in a date field) or an empty string ( in a character
 field).

* Rows that cause a duplicate key error or break a foreign key constraint are
 not inserted, updated, or deleted.

The following errors are ignored:

| Error number | Symbolic error name | Description |
| --- | --- | --- |
| Error number | Symbolic error name | Description |
| 1022 | ER_DUP_KEY | Can't write; duplicate key in table '%s' |
| 1048 | ER_BAD_NULL_ERROR | Column '%s' cannot be null |
| 1062 | ER_DUP_ENTRY | Duplicate entry '%s' for key %d |
| 1242 | ER_SUBQUERY_NO_1_ROW | Subquery returns more than 1 row |
| 1264 | ER_WARN_DATA_OUT_OF_RANGE | Out of range value for column '%s' at row %ld |
| 1265 | WARN_DATA_TRUNCATED | Data truncated for column '%s' at row %ld |
| 1292 | ER_TRUNCATED_WRONG_VALUE | Truncated incorrect %s value: '%s' |
| 1366 | ER_TRUNCATED_WRONG_VALUE_FOR_FIELD | Incorrect integer value |
| 1369 | ER_VIEW_CHECK_FAILED | CHECK OPTION failed '%s.%s' |
| 1451 | ER_ROW_IS_REFERENCED_2 | Cannot delete or update a parent row |
| 1452 | ER_NO_REFERENCED_ROW_2 | Cannot add or update a child row: a foreign key constraint fails (%s) |
| 1526 | ER_NO_PARTITION_FOR_GIVEN_VALUE | Table has no partition for value %s |
| 1586 | ER_DUP_ENTRY_WITH_KEY_NAME | Duplicate entry '%s' for key '%s' |
| 1591 | ER_NO_PARTITION_FOR_GIVEN_VALUE_SILENT | Table has no partition for some existing values |
| 1748 | ER_ROW_DOES_NOT_MATCH_GIVEN_PARTITION_SET | Found a row not matching the given partition set |

Ignored errors normally generate a warning.

A property of the `IGNORE` clause consists in causing transactional engines and non-transactional engines (like InnoDB and Aria) to behave the same way. For example, normally a multi-row insert which tries to violate a `UNIQUE` contraint is completely rolled back on InnoDB, but might be partially executed on Aria. With the `IGNORE` clause, the statement will be partially executed in both engines.

Duplicate key errors also generate warnings. The [OLD_MODE](/kb/en/old_mode/) server variable can be used to prevent this.