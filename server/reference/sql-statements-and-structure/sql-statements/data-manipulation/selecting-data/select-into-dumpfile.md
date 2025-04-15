
# SELECT INTO DUMPFILE


## Syntax


```
SELECT ... INTO DUMPFILE 'file_path'
```

## Description


`<code>SELECT ... INTO DUMPFILE</code>` is a [SELECT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) clause which writes the resultset into a single unformatted row, without any separators, in a file. The results will not be returned to the client.


*file_path* can be an absolute path, or a relative path starting from the data directory. It can only be specified as a [string literal](../../../sql-language-structure/string-literals.md), not as a variable. However, the statement can be dynamically composed and executed as a prepared statement to work around this limitation.


This statement is binary-safe and so is particularly useful for writing [BLOB](../../../../data-types/string-data-types/blob.md) values to file. It can be used, for example, to copy an image or an audio document from the database to a file.


The file must not exist. It cannot be overwritten. A user needs the [FILE](../../account-management-sql-commands/grant.md#global-privileges) privilege to run this statement. Also, MariaDB needs permission to write files in the specified location. If the [secure_file_priv](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#secure_file_priv) system variable is set to a non-empty directory name, the file can only be written to that directory.


Since [MariaDB 5.1](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md), the [character_set_filesystem](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_filesystem) system variable has controlled interpretation of file names that are given as literal strings.


## Example


```
SELECT _utf8'Hello world!' INTO DUMPFILE '/tmp/world';

SELECT LOAD_FILE('/tmp/world') AS world;
+--------------+
| world        |
+--------------+
| Hello world! |
+--------------+
```

## See Also


* [SELECT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)
* [LOAD_FILE()](../../built-in-functions/string-functions/load_file.md)
* [SELECT INTO Variable](../../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/selectinto.md)
* [SELECT INTO OUTFILE](select-into-outfile.md)

