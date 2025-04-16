
# Information Schema KEY_COLUMN_USAGE Table

The [Information Schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `KEY_COLUMN_USAGE` table shows which key columns have constraints.


It contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| CONSTRAINT_CATALOG | Always def. |
| CONSTRAINT_SCHEMA | Database name of the constraint. |
| CONSTRAINT_NAME | Name of the constraint (PRIMARY for the primary key). |
| TABLE_CATALOG | Always #def. |
| TABLE_SCHEMA | Database name of the column constraint. |
| TABLE_NAME | Table name of the column constraint. |
| COLUMN_NAME | Column name of the constraint. |
| ORDINAL_POSITION | Position of the column within the constraint. |
| POSITION_IN_UNIQUE_CONSTRAINT | For [foreign keys](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/foreign-keys.md), the position in the unique constraint. |
| REFERENCED_TABLE_SCHEMA | For foreign keys, the referenced database name. |
| REFERENCED_TABLE_NAME | For foreign keys, the referenced table name. |
| REFERENCED_COLUMN_NAME | For foreign keys, the referenced column name. |



## Example


```
SELECT * FROM information_schema.KEY_COLUMN_USAGE LIMIT 1 \G
********************** 1. row **********************
           CONSTRAINT_CATALOG: def
            CONSTRAINT_SCHEMA: my_website
              CONSTRAINT_NAME: PRIMARY
                TABLE_CATALOG: def
                 TABLE_SCHEMA: users
                  COLUMN_NAME: user_id
             ORDINAL_POSITION: 1
POSITION_IN_UNIQUE_CONSTRAINT: NULL
      REFERENCED_TABLE_SCHEMA: NULL
        REFERENCED_TABLE_NAME: NULL
       REFERENCED_COLUMN_NAME: NULL
```

## See Also


* [Finding Tables Without Primary Keys](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/getting-started-with-indexes.md#finding-tables-without-primary-keys)

