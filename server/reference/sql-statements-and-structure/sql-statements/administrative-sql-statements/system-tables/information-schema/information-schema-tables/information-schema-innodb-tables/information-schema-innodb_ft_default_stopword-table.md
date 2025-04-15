# Information Schema INNODB_FT_DEFAULT_STOPWORD Table

The [Information Schema](/en/information_schema/) `INNODB_FT_DEFAULT_STOPWORD` table contains a list of default [stopwords](/en/stopwords/) used when creating an InnoDB [fulltext index](/en/full-text-indexes/).

The `PROCESS` [privilege](../../../../../account-management-sql-commands/grant.md) is required to view the table.

It has the following column:

| Column | Description |
| --- | --- |
| Column | Description |
| VALUE | Default [stopword](/en/stopwords/) for an InnoDB [fulltext index](/en/full-text-indexes/). Setting either the [innodb_ft_server_stopword_table](/en/xtradbinnodb-server-system-variables/#innodb_ft_server_stopword_table) or the [innodb_ft_user_stopword_table](/en/xtradbinnodb-server-system-variables/#innodb_ft_user_stopword_table) system variable will override this. |

#

# Example

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