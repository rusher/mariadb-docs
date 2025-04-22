
# LOAD_FILE

## Syntax


```
LOAD_FILE(file_name)
```


## Description


Reads the file and returns the file contents as a string. To use this function, the file must be located on the server host, you must specify the full path name to the file, and you must have the FILE privilege. The file must be readable by all and it must be less than the size, in bytes, of the [max_allowed_packet](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_allowed_packet) system variable. If the [secure_file_priv](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#secure_file_priv) system variable is set to a non-empty directory name, the file to be loaded must be located in that directory.


If the file does not exist or cannot be read because one of the preceding conditions is not satisfied, the function returns NULL.


Since [MariaDB 5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1), the [character_set_filesystem](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_filesystem) system variable has controlled interpretation of file names that are given as literal strings.


Statements using the LOAD_FILE() function are not [safe for statement based replication](../../../../../server-usage/replication-cluster-multi-master/standard-replication/unsafe-statements-for-statement-based-replication.md). This is because the slave will execute the LOAD_FILE() command itself. If the file doesn't exist on the slave, the function will return NULL.


## Examples


```
UPDATE t SET blob_col=LOAD_FILE('/tmp/picture') WHERE id=1;
```

## See Also


* [SELECT INTO DUMPFILE](../../data-manipulation/selecting-data/select-into-dumpfile.md)

