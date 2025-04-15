
# Information Schema INNODB_FT_DEFAULT_STOPWORD Table

The [Information Schema](../../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `<code>INNODB_FT_DEFAULT_STOPWORD</code>` table contains a list of default [stopwords](../../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/full-text-index-stopwords.md) used when creating an InnoDB [fulltext index](../../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md).


The `<code>PROCESS</code>` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.


It has the following column:



| Column | Description |
| --- | --- |
| Column | Description |
| VALUE | Default [stopword](../../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/full-text-index-stopwords.md) for an InnoDB [fulltext index](../../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-indexes/full-text-indexes/README.md). Setting either the [innodb_ft_server_stopword_table](../../../../../../../storage-engines/innodb/innodb-system-variables.md) or the [innodb_ft_user_stopword_table](../../../../../../../storage-engines/innodb/innodb-system-variables.md) system variable will override this. |



## Example


```
SELECT * FROM information_schema.INNODB_FT_DEFAULT_STOPWORD\G
*************************** 1. row ***************************
value: a
*************************** 2. row ***************************
value: about
*************************** 3. row ***************************
value: an
*************************** 4. row ***************************
value: are
...
*************************** 36. row ***************************
value: www
```
