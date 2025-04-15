
# NTH_VALUE

## Syntax


```
NTH_VALUE (expr[, num_row]) OVER ( 
  [ PARTITION BY partition_expression ] 
  [ ORDER BY order_list ]
)
```


## Description


The `<code>NTH_VALUE</code>` function returns the value evaluated at row number `<code>num_row</code>` of the window frame, starting from 1, or NULL if the row does not exist.

