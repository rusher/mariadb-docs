
# Information Schema TABLE_CONSTRAINTS Table

The [Information Schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>TABLE_CONSTRAINTS</code>` table contains information about tables that have [constraints](../../../../data-definition/constraint.md).


It has the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| CONSTRAINT_CATALOG | Always def. |
| CONSTRAINT_SCHEMA | Database name containing the constraint. |
| CONSTRAINT_NAME | Constraint name. |
| TABLE_SCHEMA | Database name. |
| TABLE_NAME | Table name. |
| CONSTRAINT_TYPE | Type of constraint; one of UNIQUE, PRIMARY KEY, FOREIGN KEY or CHECK. |



The [REFERENTIAL_CONSTRAINTS](information-schema-referential_constraints-table.md) table has more information about foreign keys.

