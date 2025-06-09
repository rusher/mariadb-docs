
# Aggregate Functions as Window Functions

It is possible to use [aggregate functions](../../aggregate-functions/README.md) as window functions. An aggregate function used as a window function must have the `OVER` clause. For example, here's [COUNT()](../../aggregate-functions/count.md) used as a window function:


```
select COUNT(*) over  (order by column) from table;
```

MariaDB currently allows these aggregate functions to be used as window functions:


* [AVG](../../aggregate-functions/avg.md)
* [BIT_AND](../../aggregate-functions/bit_and.md)
* [BIT_OR](../../aggregate-functions/bit_or.md)
* [BIT_XOR](../../aggregate-functions/bit_xor.md)
* [COUNT](../../aggregate-functions/count.md)
* [MAX](../../aggregate-functions/max.md)
* [MIN](../../aggregate-functions/min.md)
* [STD](../../aggregate-functions/std.md)
* [STDDEV](../../aggregate-functions/stddev.md)
* [STDDEV_POP](../../aggregate-functions/stddev_pop.md)
* [STDDEV_SAMP](../../aggregate-functions/stddev_samp.md)
* [SUM](../../aggregate-functions/sum.md)
* [VAR_POP](../../aggregate-functions/var_pop.md)
* [VAR_SAMP](../../aggregate-functions/var_samp.md)
* [VARIANCE](../../aggregate-functions/variance.md)


CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
