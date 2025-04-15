
# VALUES / VALUE

## Syntax


```
VALUE(col_name)
```

## Description


In an [INSERT ... ON DUPLICATE KEY UPDATE](../../../data-manipulation/inserting-loading-data/insert-on-duplicate-key-update.md) statement, you can use the `<code>VALUES(col_name)</code>` function in the [UPDATE](../../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md) clause to refer to column values from the [INSERT](../../string-functions/insert-function.md) portion of the statement. In other words, `<code>VALUES(col_name)</code>` in the `<code>UPDATE</code>` clause refers to the value of col_name that would be inserted, had no duplicate-key conflict occurred. This function is especially useful in multiple-row inserts.


The `<code>VALUES()</code>` function is meaningful only in `<code>INSERT ... ON DUPLICATE KEY UPDATE</code>` statements and returns `<code>NULL</code>` otherwise.


This function was renamed to `<code>VALUE()</code>`, because it's incompatible with the standard Table Value Constructors syntax.


The `<code>VALUES()</code>` function can still be used but only in `<code>INSERT ... ON DUPLICATE KEY UPDATE</code>` statements; it's a syntax error otherwise.


## Examples


```
INSERT INTO t (a,b,c) VALUES (1,2,3),(4,5,6)
    ON DUPLICATE KEY UPDATE c=VALUE(a)+VALUE(b);
```
