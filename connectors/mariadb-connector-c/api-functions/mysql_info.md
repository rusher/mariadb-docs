# mysql\_info

## Syntax

```c
const char * mysql_info(MYSQL * mysql);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

The mysql\_info() function returns a string providing information about the last query executed. The nature of this string is provided below:

Table 1. Possible mysql\_info return values

| Query type                                                                                                                                                                                                            | Example result string                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| Query type                                                                                                                                                                                                            | Example result string                        |
| [INSERT INTO...SELECT...](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert)                                       | Records: 100 Duplicates: 0 Warnings: 0       |
| [INSERT INTO...VALUES (...),(...),(...)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/insert)                        | Records: 3 Duplicates: 0 Warnings: 0         |
| [LOAD DATA INFILE ...](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) | Records: 1 Deleted: 0 Skipped: 0 Warnings: 0 |
| [ALTER TABLE ...](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-definition/alter)                                                                         | Records: 3 Duplicates: 0 Warnings: 0         |
| [UPDATE ...](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/update)                                                    | Rows matched: 40 Changed: 40 Warnings: 0     |

{% hint style="info" %}
Queries which do not fall into one of the preceding formats are not supported (e.g. [SELECT ...](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/select)). In these situations mysql\_info() will return an empty string.
{% endhint %}

## See also

* [mysql\_affected\_rows()](mysql_affected_rows.md)
* [mysql\_warning\_count()](mysql_warning_count.md)

{% @marketo/form formid="4316" %}
