
# Optimizer Debugging With GDB

Some useful things for debugging optimizer code.


## Useful Print Functions


* `<code>dbug_print_item()</code>` prints the contents of an `<code>Item</code>` object into a buffer and returns pointer to it.
* `<code>dbug_print_sel_arg()</code>` prints an individual `<code>SEL_ARG</code>` object (NOT the whole graph or tree) and returns pointer to the buffer holding the printout.
* `<code>dbug_print_table_row</code>` prints the current row buffer of the given table.
* There are more `<code>dbug_print_XX</code>` functions for various data structures


## Printing the Optimizer Trace


The optimizer trace is collected as plain text.
One can print the contents of the trace collected so far as follows:


```
printf "%s\n", thd->opt_trace->current_trace->current_json->output.str.Ptr
```

Starting from 11.0, there is `<code>dbug_print_opt_trace()</code>` function which one call from gdb.


## Printing Current Partial Join Prefix


`<code>best_access_path()</code>` is a function that adds another table to the join prefix.


When in or around that function, the following can be useful:


A macro to print the join prefix already constructed:


```
define bap_print_prefix
  set $i=0
  while ($i < idx)
    p join->positions[$i++].table->table->alias.Ptr
  end
end
```

## Other Settings


* May need to set [innodb_fatal_semaphore_wait_threshold](../../storage-engines/innodb/innodb-system-variables.md#innodb_fatal_semaphore_wait_threshold) to be high enough?


## Other development topics


### mtr tests


In order to get innodb to have stable statistics, use this in the test:


```
--source include/innodb_stable_estimates.inc
```

Also consider `<code>set global innodb_max_purge_lag_wait=0;</code>` 
(TODO: how these two compare?)


### Coding guidelines


Run this to get your patch auto-formatted according to our coding style in `<code>.clang-format</code>` :


```
git diff -U0 --no-color --relative HEAD^ | clang-format-diff -p1 -i
```

## See Also


* [How to collect large optimizer traces](mariadb-internals-documentation-optimizer-trace/how-to-collect-large-optimizer-traces.md)

