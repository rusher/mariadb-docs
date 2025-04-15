
# Information Schema MROONGA_STATS Table

The [Information Schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>MROONGA_STATS</code>` table only exists if the [Mroonga](../../../../../../storage-engines/mroonga/mroonga-user-defined-functions/mroonga_snippet_html.md) storage engine is installed, and contains information about its activities.



| Column | Description |
| --- | --- |
| Column | Description |
| VERSION | Mroonga version. |
| rows_written | Number of rows written into Mroonga tables. |
| rows_read | Number of rows read from all Mroonga tables. |



This table always contains 1 row.

