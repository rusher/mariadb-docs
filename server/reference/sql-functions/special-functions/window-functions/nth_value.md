
# NTH_VALUE

## Syntax


```
NTH_VALUE (expr[, num_row]) OVER ( 
  [ PARTITION BY partition_expression ] 
  [ ORDER BY order_list ]
)
```


## Description


The `NTH_VALUE` function returns the value evaluated at row number `num_row` of the window frame, starting from 1, or NULL if the row does not exist.


CC BY-SA / Gnu FDL

