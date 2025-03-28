# Information Schema REFERENTIAL_CONSTRAINTS Table

The [Information Schema](/en/information_schema/) `REFERENTIAL_CONSTRAINTS` table contains information about [foreign keys](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/foreign-keys.md). The single columns are listed in the `[KEY_COLUMN_USAGE](information-schema-key_column_usage-table.md)` table.

It has the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| CONSTRAINT_CATALOG | Always def. |
| CONSTRAINT_SCHEMA | Database name, together with CONSTRAINT_NAME identifies the foreign key. |
| CONSTRAINT_NAME | Foreign key name, together with CONSTRAINT_SCHEMA identifies the foreign key. |
| UNIQUE_CONSTRAINT_CATALOG | Always def. |
| UNIQUE_CONSTRAINT_SCHEMA | Database name, together with UNIQUE_CONSTRAINT_NAME and REFERENCED_TABLE_NAME identifies the referenced key. |
| UNIQUE_CONSTRAINT_NAME | Referenced key name, together with UNIQUE_CONSTRAINT_SCHEMA and REFERENCED_TABLE_NAME identifies the referenced key. |
| MATCH_OPTION | Always NONE. |
| UPDATE_RULE | The Update Rule; one of CASCADE, SET NULL, SET DEFAULT, RESTRICT, NO ACTION. |
| DELETE_RULE | The Delete Rule; one of CASCADE, SET NULL, SET DEFAULT, RESTRICT, NO ACTION. |
| TABLE_NAME | Table name from the TABLE_CONSTRAINTS table. |
| REFERENCED_TABLE_NAME | Referenced key table name, together with UNIQUE_CONSTRAINT_SCHEMA and UNIQUE_CONSTRAINT_NAME identifies the referenced key. |