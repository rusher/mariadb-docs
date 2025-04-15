
# INSERT - Default & Duplicate Values


## Default Values


If the `<code>[SQL_MODE](../../../../../server-management/variables-and-modes/sql-mode.md)</code>` contains `<code>STRICT_TRANS_TABLES</code>` and you are [inserting](../../built-in-functions/string-functions/insert-function.md) into a transactional table (like InnoDB), or if the SQL_MODE contains `<code>STRICT_ALL_TABLES</code>`, all `<code>NOT NULL</code>` columns which do not have a `<code>DEFAULT</code>` value (and are not [AUTO_INCREMENT](../../../../storage-engines/innodb/auto_increment-handling-in-innodb.md)) must be explicitly referenced in `<code>INSERT</code>` statements. If not, an error like this is produced:


```
ERROR 1364 (HY000): Field 'col' doesn't have a default value
```

In all other cases, if a `<code>NOT NULL</code>` column without a `<code>DEFAULT</code>` value is not referenced, an empty value will be inserted (for example, 0 for `<code>INTEGER</code>` columns and '' for `<code>CHAR</code>` columns). See [NULL Values in MariaDB:Inserting](../../../../data-types/null-values.md) for examples.


If a `<code>NOT NULL</code>` column having a `<code>DEFAULT</code>` value is not referenced, `<code>NULL</code>` will be inserted.


If a `<code>NULL</code>` column having a `<code>DEFAULT</code>` value is not referenced, its default value will be inserted. It is also possible to explicitly assign the default value using the `<code>DEFAULT</code>` keyword or the `<code>[DEFAULT()](../../built-in-functions/secondary-functions/information-functions/default.md)</code>` function.


If the `<code>DEFAULT</code>` keyword is used but the column does not have a `<code>DEFAULT</code>` value, an error like this is produced:


```
ERROR 1364 (HY000): Field 'col' doesn't have a default value
```

## Duplicate Values


By default, if you try to insert a duplicate row and there is a `<code>UNIQUE</code>` index, `<code>INSERT</code>` stops and an error like this is produced:


```
ERROR 1062 (23000): Duplicate entry 'dup_value' for key 'col'
```

To handle duplicates you can use the [IGNORE](ignore.md) clause, [INSERT ON DUPLICATE KEY UPDATE](insert-on-duplicate-key-update.md) or the [REPLACE](../../built-in-functions/string-functions/replace-function.md) statement. Note that the IGNORE and DELAYED options are ignored when you use [ON DUPLICATE KEY UPDATE](insert-on-duplicate-key-update.md).


## See Also


* [INSERT](../../built-in-functions/string-functions/insert-function.md)
* [INSERT DELAYED](insert-delayed.md)
* [INSERT SELECT](insert-select.md)
* [HIGH_PRIORITY and LOW_PRIORITY](../changing-deleting-data/high_priority-and-low_priority.md)
* [Concurrent Inserts](concurrent-inserts.md)
* [INSERT IGNORE](insert-ignore.md)
* [INSERT ON DUPLICATE KEY UPDATE](insert-on-duplicate-key-update.md)

