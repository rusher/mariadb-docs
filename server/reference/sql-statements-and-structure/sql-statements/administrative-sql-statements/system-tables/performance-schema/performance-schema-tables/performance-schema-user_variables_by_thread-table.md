
# Performance Schema user_variables_by_thread Table


##### MariaDB starting with [10.5.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)
The `user_variables_by_thread` table was added in [MariaDB 10.5.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md).


The `user_variables_by_thread` table contains information about [user-defined variables](../../../../../sql-language-structure/user-defined-variables.md) and the threads that defined them.


[TRUNCATE TABLE](../../../../table-statements/truncate-table.md) cannot be performed on the table.


The table contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| THREAD_ID | The thread identifier of the session in which the variable is defined. |
| VARIABLE_NAME | The variable name, without the leading @ character. |
| VARIABLE_VALUE | The variable value |



## Example


```
SET @var = 0;

SELECT * FROM user_variables_by_thread;
+-----------+---------------+----------------+
| THREAD_ID | VARIABLE_NAME | VARIABLE_VALUE |
+-----------+---------------+----------------+
|        11 | var           | 0              |
+-----------+---------------+----------------+
```

## See Also


* [User-defined variables](../../../../../sql-language-structure/user-defined-variables.md)
* [Information Schema USER_VARIABLES Table](../../information-schema/information-schema-tables/information-schema-user_variables-table.md)

