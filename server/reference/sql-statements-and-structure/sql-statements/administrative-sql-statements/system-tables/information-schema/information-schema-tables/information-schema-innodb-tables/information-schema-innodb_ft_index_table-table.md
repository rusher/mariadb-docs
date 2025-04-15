# Information Schema INNODB_FT_INDEX_TABLE Table

The [Information Schema](/en/information_schema/) `INNODB_FT_INDEX_TABLE` table contains information about InnoDB [fulltext indexes](/en/full-text-indexes/). To avoid re-organizing the fulltext index each time a change is made, which would be very expensive, new changes are stored separately and only integrated when an [OPTIMIZE TABLE](../../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/optimize-table.md) is run. See the [INNODB_FT_INDEX_CACHE](information-schema-innodb_ft_index_cache-table.md) table.

The `SUPER` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table, and it also requires the [innodb_ft_aux_table](../../../../../../../storage-engines/innodb/innodb-system-variables.md#innodb_ft_aux_table) system variable to be set.

It has the following columns:

| Column | Description |
| --- | --- |
| Column | Description |
| WORD | Word from the text of a column with a fulltext index. Words can appear multiple times in the table, once per DOC_ID and POSITION combination. |
| FIRST_DOC_ID | First document ID where this word appears in the index. |
| LAST_DOC_ID | Last document ID where this word appears in the index. |
| DOC_COUNT | Number of rows containing this word in the index. |
| DOC_ID | Document ID of the newly added row, either an appropriate ID column or an internal InnoDB value. |
| POSITION | Position of this word instance within the DOC_ID, as an offset added to the previous POSITION instance. |

Note that for `OPTIMIZE TABLE` to process InnoDB fulltext index data, the [innodb_optimize_fulltext_only](innodb-server-system-variables#innodb_optimize_fulltext_only) system variable needs to be set to `1`. When this is done, and an `OPTIMIZE TABLE` statement run, the [INNODB_FT_INDEX_CACHE](information-schema-innodb_ft_index_cache-table.md) table will be emptied, and the `INNODB_FT_INDEX_TABLE` table will be updated.

#

# Examples

```
SELECT * FROM INNODB_FT_INDEX_TABLE;
Empty set (0.00 sec)

SET GLOBAL innodb_optimize_fulltext_only =1;

OPTIMIZE TABLE test.ft_innodb;
+----------------+----------+----------+----------+
| Table | Op | Msg_type | Msg_text |
+----------------+----------+----------+----------+
| test.ft_innodb | optimize | status | OK |
+----------------+----------+----------+----------+

SELECT * FROM INNODB_FT_INDEX_TABLE;
+------------+--------------+-------------+-----------+--------+----------+
| WORD | FIRST_DOC_ID | LAST_DOC_ID | DOC_COUNT | DOC_ID | POSITION |
+------------+--------------+-------------+-----------+--------+----------+
| and | 4 | 5 | 2 | 4 | 0 |
| and | 4 | 5 | 2 | 5 | 0 |
| arrived | 4 | 4 | 1 | 4 | 20 |
| ate | 1 | 5 | 2 | 1 | 4 |
| ate | 1 | 5 | 2 | 5 | 8 |
| everybody | 1 | 1 | 1 | 1 | 8 |
| goldilocks | 4 | 4 | 1 | 4 | 9 |
| hungry | 3 | 3 | 1 | 3 | 8 |
| pear | 5 | 5 | 1 | 5 | 14 |
| she | 5 | 5 | 1 | 5 | 4 |
| then | 4 | 4 | 1 | 4 | 4 |
| wicked | 2 | 2 | 1 | 2 | 4 |
| witch | 2 | 2 | 1 | 2 | 11 |
+------------+--------------+-------------+-----------+--------+----------+
```