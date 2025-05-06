
# CACHE INDEX

## Syntax


```
CACHE INDEX                      
  tbl_index_list [, tbl_index_list] ...
  IN key_cache_name                    

tbl_index_list:
  tbl_name [[INDEX|KEY] (index_name[, index_name] ...)]
```

## Description


The `CACHE INDEX` statement assigns table indexes to a specific key
cache. It is used only for [MyISAM](../../../storage-engines/myisam-storage-engine/README.md) tables.


A default key cache exists and cannot be destroyed. To create more key caches, the [key_buffer_size](../../../storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size) server system variable.


The associations between tables indexes and key caches are lost on server restart. To recreate them automatically, it is necessary to configure caches in a [configuration file](../../../../server-management/getting-installing-and-upgrading-mariadb/mariadbd-configuration-files-and-groups.md) and include some `CACHE INDEX` (and optionally `[LOAD INDEX](../data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-index.md)`) statements in the init file.


## Examples


The following statement assigns indexes from the tables t1, t2, and t3
to the key cache named hot_cache:


```
CACHE INDEX t1, t2, t3 IN hot_cache;
+---------+--------------------+----------+----------+
| Table   | Op                 | Msg_type | Msg_text |
+---------+--------------------+----------+----------+
| test.t1 | assign_to_keycache | status   | OK       |
| test.t2 | assign_to_keycache | status   | OK       |
| test.t3 | assign_to_keycache | status   | OK       |
+---------+--------------------+----------+----------+
```

## Implementation (for MyISAM)


Normally CACHE INDEX should not take a long time to execute. Internally it's implemented the following way:


* Find the right key cache (under LOCK_global_system_variables)
* Open the table with a TL_READ_NO_INSERT lock.
* Flush the original key cache for the given file (under key cache lock)
* Flush the new key cache for the given file (safety)
* Move the file to the new key cache (under file share lock)


The only possible long operations are getting the locks for the table and flushing the original key cache, if there were many key blocks for the file in it.


We plan to also add CACHE INDEX for Aria tables if there is a need for this.


GPLv2 fill_help_tables.sql

