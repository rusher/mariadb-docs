
# BENCHMARK

## Syntax


```
BENCHMARK(count,expr)
```

## Description


The BENCHMARK() function executes the expression `<code>expr</code>` repeatedly `<code>count</code>`
times. It may be used to time how quickly MariaDB processes the
expression. The result value is always 0. The intended use is from
within the [mariadb client](../../../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md), which reports query execution times.


## Examples


```
SELECT BENCHMARK(1000000,ENCODE('hello','goodbye'));
+----------------------------------------------+
| BENCHMARK(1000000,ENCODE('hello','goodbye')) |
+----------------------------------------------+
|                                            0 |
+----------------------------------------------+
1 row in set (0.21 sec)
```
