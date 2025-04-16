
# SPIDER_BG_DIRECT_SQL

## Syntax


```
SPIDER_BG_DIRECT_SQL('sql', 'tmp_table_list', 'parameters')
```

## Description


Executes the given SQL statement in the background on the remote server, as defined in the parameters listing. If the query returns a result-set, it sttores the results in the given temporary table. When the given SQL statement executes successfully, this function returns the number of called UDF's. It returns `0` when the given SQL statement fails.


This function is a [UDF](../../../../server-usage/programming-customizing-mariadb/user-defined-functions/user-defined-functions-security.md) installed with the [Spider](spider_copy_tables.md) storage engine.


## Examples


```
SELECT SPIDER_BG_DIRECT_SQL('SELECT * FROM example_table',  '', 
   'srv "node1", port "8607"') AS "Direct Query";
+--------------+
| Direct Query | 
+--------------+
|            1 |
+--------------+
```

## Parameters


#### `error_rw_mode`


* Description: Returns empty results on network error.

  * `0` : Return error on getting network error.
  * `1`: Return 0 records on getting network error.
* Default Table Value: `0`
* DSN Parameter Name: `erwm`


## See also


* [SPIDER_DIRECT_SQL](spider_direct_sql.md)

