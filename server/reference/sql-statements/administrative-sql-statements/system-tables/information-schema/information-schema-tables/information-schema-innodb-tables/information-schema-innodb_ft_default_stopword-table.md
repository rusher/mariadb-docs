# Information Schema INNODB\_FT\_DEFAULT\_STOPWORD Table

The [Information Schema](../../) `INNODB_FT_DEFAULT_STOPWORD` table contains a list of default [stopwords](../../../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/full-text-index-stopwords.md) used when creating an InnoDB [fulltext index](../../../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/).

The `PROCESS` [privilege](../../../../../account-management-sql-statements/grant.md) is required to view the table.

It has the following column:

| Column | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Column | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| VALUE  | Default [stopword](../../../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/full-text-index-stopwords.md) for an InnoDB [fulltext index](../../../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/). Setting either the [innodb\_ft\_server\_stopword\_table](../../../../../../storage-engines/innodb/innodb-system-variables.md) or the [innodb\_ft\_user\_stopword\_table](../../../../../../storage-engines/innodb/innodb-system-variables.md) system variable will override this. |

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

CC BY-SA / Gnu FDL
