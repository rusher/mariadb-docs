
# format_path

## Syntax


```
sys.format_path(path)
```

## Description


`format_path` is a [stored function](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) available with the [Sys Schema](../README.md) that, given a path, returns a modified path after replacing subpaths matching the values of various system variables with the variable name.


The system variables that are matched are, in order:


* [datadir](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#datadir)
* [tmpdir](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#tmpdir)
* [slave_load_tmpdir](../../../../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#slave_load_tmpdir)
* [innodb_data_home_dir](../../../../../../storage-engines/innodb/innodb-system-variables.md#innodb_data_home_dir)
* [innodb_log_group_home_dir](../../../../../../storage-engines/innodb/innodb-system-variables.md#innodb_log_group_home_dir)
* [innodb_undo_directory](../../../../../../storage-engines/innodb/innodb-system-variables.md#innodb_undo_directory)
* [basedir](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#basedir)


## Examples


```
SELECT @@tmpdir;
+------------------------------------+
| @@tmpdir                           |
+------------------------------------+
| /home/ian/sandboxes/msb_10_8_2/tmp |
+------------------------------------+

SELECT sys.format_path('/home/ian/sandboxes/msb_10_8_2/tmp/testdb.ibd');
+------------------------------------------------------------------+
| sys.format_path('/home/ian/sandboxes/msb_10_8_2/tmp/testdb.ibd') |
+------------------------------------------------------------------+
| @@tmpdir/testdb.ibd                                              |
+------------------------------------------------------------------+
```


CC BY-SA / Gnu FDL

