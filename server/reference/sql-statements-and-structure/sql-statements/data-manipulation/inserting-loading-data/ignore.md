
# IGNORE

The `<code>IGNORE</code>` option tells the server to ignore some common errors.


`<code>IGNORE</code>` can be used with the following statements:


* [DELETE](../changing-deleting-data/delete.md)
* [INSERT](../../built-in-functions/string-functions/insert-function.md) (see also [INSERT IGNORE](insert-ignore.md))
* [LOAD DATA INFILE](load-data-into-tables-or-index/load-data-infile.md)
* [UPDATE](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md)
* [ALTER TABLE](../../data-definition/alter/alter-tablespace.md)
* [CREATE TABLE ... SELECT](../../../vectors/create-table-with-vectors.md#create-select)
* [INSERT ... SELECT](insert-select.md)


The logic used:


* Variables out of ranges are replaced with the maximum/minimum value.


* [SQL_MODEs](../../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modemssql.md) `<code>STRICT_TRANS_TABLES</code>`, `<code>STRICT_ALL_TABLES</code>`, `<code>NO_ZERO_IN_DATE</code>`, `<code>NO_ZERO_DATE</code>` are ignored.


* Inserting `<code>NULL</code>` in a `<code>NOT NULL</code>` field will insert 0 ( in a numerical
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


A property of the `<code>IGNORE</code>` clause consists in causing transactional engines and non-transactional engines (like InnoDB and Aria) to behave the same way. For example, normally a multi-row insert which tries to violate a `<code>UNIQUE</code>` contraint is completely rolled back on InnoDB, but might be partially executed on Aria. With the `<code>IGNORE</code>` clause, the statement will be partially executed in both engines.


Duplicate key errors also generate warnings. The [OLD_MODE](../../../../../server-management/variables-and-modes/old-mode.md) server variable can be used to prevent this.

