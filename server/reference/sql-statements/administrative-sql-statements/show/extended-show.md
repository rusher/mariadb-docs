
# Extended Show

The following `[SHOW](README.md)` statements can be extended by using a `WHERE` clause and a `LIKE` clause to refine the results:


* [SHOW CHARACTER SET](show-character-set.md)
* [SHOW COLLATION](show-collation.md)
* [SHOW COLUMNS](show-columns.md)
* [SHOW DATABASES](show-databases.md)
* [SHOW FUNCTION STATUS](show-function-status.md)
* [SHOW INDEX](show-index.md)``
* [SHOW OPEN TABLES](show-open-tables.md)
* [SHOW PACKAGE STATUS](show-package-status.md)
* [SHOW PACKAGE BODY STATUS](show-package-body-status.md)
* [SHOW INDEX](show-index.md)
* [SHOW PROCEDURE STATUS](show-procedure-status.md)
* [SHOW STATUS](show-status.md)
* [SHOW TABLE STATUS](show-table-status.md)
* [SHOW TABLES](show-tables.md)
* [SHOW TRIGGERS](show-triggers.md)
* [SHOW VARIABLES](show-variables.md)


As with a regular `[SELECT](../../data-manipulation/selecting-data/select.md)`, the `WHERE` clause can be used for the specific columns returned, and the `[LIKE](../../built-in-functions/string-functions/like.md)` clause with the regular wildcards.


## Examples


```
SHOW TABLES;
+----------------------+
| Tables_in_test       |
+----------------------+
| animal_count         |
| animals              |
| are_the_mooses_loose |
| aria_test2           |
| t1                   |
| view1                |
+----------------------+
```

Showing the tables beginning with *a* only.


```
SHOW TABLES WHERE Tables_in_test LIKE 'a%';
+----------------------+
| Tables_in_test       |
+----------------------+
| animal_count         |
| animals              |
| are_the_mooses_loose |
| aria_test2           |
+----------------------+
```

Variables whose name starts with *aria* and with a valued of greater than 8192:


```
SHOW VARIABLES WHERE Variable_name LIKE 'aria%' AND Value >8192;
+------------------------------+---------------------+
| Variable_name                | Value               |
+------------------------------+---------------------+
| aria_checkpoint_log_activity | 1048576             |
| aria_log_file_size           | 1073741824          |
| aria_max_sort_file_size      | 9223372036853727232 |
| aria_pagecache_buffer_size   | 134217728           |
| aria_sort_buffer_size        | 134217728           |
+------------------------------+---------------------+
```

Shortcut, just returning variables whose name begins with *aria*.


```
SHOW VARIABLES LIKE 'aria%';
+------------------------------------------+---------------------+
| Variable_name                            | Value               |
+------------------------------------------+---------------------+
| aria_block_size                          | 8192                |
| aria_checkpoint_interval                 | 30                  |
| aria_checkpoint_log_activity             | 1048576             |
| aria_force_start_after_recovery_failures | 0                   |
| aria_group_commit                        | none                |
| aria_group_commit_interval               | 0                   |
| aria_log_file_size                       | 1073741824          |
| aria_log_purge_type                      | immediate           |
| aria_max_sort_file_size                  | 9223372036853727232 |
| aria_page_checksum                       | ON                  |
| aria_pagecache_age_threshold             | 300                 |
| aria_pagecache_buffer_size               | 134217728           |
| aria_pagecache_division_limit            | 100                 |
| aria_recover                             | NORMAL              |
| aria_repair_threads                      | 1                   |
| aria_sort_buffer_size                    | 134217728           |
| aria_stats_method                        | nulls_unequal       |
| aria_sync_log_dir                        | NEWFILE             |
| aria_used_for_temp_tables                | ON                  |
+------------------------------------------+---------------------+
```


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
