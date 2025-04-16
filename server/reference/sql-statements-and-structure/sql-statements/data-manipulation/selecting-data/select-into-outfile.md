
# SELECT INTO OUTFILE

## Syntax


```
SELECT ... INTO OUTFILE 'file_name'
        [CHARACTER SET charset_name]
        [export_options]

export_options:
    [{FIELDS | COLUMNS}
        [TERMINATED BY 'string']
        [[OPTIONALLY] ENCLOSED BY 'char']
        [ESCAPED BY 'char']
    ]
    [LINES
        [STARTING BY 'string']
        [TERMINATED BY 'string']
    ]
```


## Description


`SELECT INTO OUTFILE` writes the resulting rows to a file, and allows the use of column and row terminators to specify a particular output format. The default is to terminate fields with tabs (`\t`) and lines with newlines (`\n`).


The file must not exist. It cannot be overwritten. A user needs the [FILE](../../account-management-sql-commands/grant.md#global-privileges) privilege to run this statement. Also, MariaDB needs permission to write files in the specified location. If the [secure_file_priv](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#secure_file_priv) system variable is set to a non-empty directory name, the file can only be written to that directory.


The `[LOAD DATA INFILE](../inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md)` statement complements `SELECT INTO OUTFILE`.


### Character-sets


The `CHARACTER SET` clause specifies the [character set](../../../../data-types/string-data-types/character-sets/README.md) in which the results are to be written. Without the clause, no conversion takes place (the binary character set). In this case, if there are multiple character sets, the output will contain these too, and may not easily be able to be reloaded.


In cases where you have two servers using different character-sets, using `SELECT INTO OUTFILE` to transfer data from one to the other can have unexpected results. To ensure that MariaDB correctly interprets the escape sequences, use the `CHARACTER SET` clause on both the `SELECT INTO OUTFILE` statement and the subsequent `[LOAD DATA INFILE](../inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md)` statement.


## Example


The following example produces a file in the CSV format:


```
SELECT customer_id, firstname, surname from customer
  INTO OUTFILE '/exportdata/customers.txt'
  FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
  LINES TERMINATED BY '\n';
```

The following ANSI syntax is also supported for simple `SELECT` without `UNION`


```
SELECT customer_id, firstname, surname INTO OUTFILE '/exportdata/customers.txt'
  FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  FROM customers;
```

If you want to use the ANSI syntax with `UNION` or similar construct you have to use the syntax:


```
SELECT  * INTO OUTFILE "/tmp/skr3" FROM (SELECT * FROM t1 UNION SELECT * FROM t1);
```

## See Also


* [SELECT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)
* [LOAD_DATA()](../../built-in-functions/string-functions/load_file.md) function
* [LOAD DATA INFILE](../inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md)
* [SELECT INTO Variable](../../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/selectinto.md)
* [SELECT INTO DUMPFILE](select-into-dumpfile.md)

