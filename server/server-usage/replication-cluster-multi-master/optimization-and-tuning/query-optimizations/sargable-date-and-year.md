
# Sargable DATE and YEAR

Starting from [MariaDB 11.1](../../../../../release-notes/mariadb-community-server/what-is-mariadb-111.md), conditions in the form


```
YEAR(indexed_date_col) CMP const_value
DATE(indexed_date_col) CMP const_value
```

are sargable, provided that


* CMP is any of `<code>=</code>`, `<code><=></code>`, `<code><</code>`, `<code><=</code>`, `<code>></code>`, `<code>>=</code>` .
* `<code>indexed_date_col</code>` has a type of `<code>DATE</code>`, `<code>DATETIME</code>` or `<code>TIMESTAMP</code>` and is a part of some index.


One can swap the left and right hand sides of the equality: `<code>const_value CMP {DATE|YEAR}(indexed_date_col)</code>` is also handled.


Sargable here means that the optimizer is able to use such conditions to construct access methods, estimate their selectivity, or use them to perform partition pruning.


## Implementation


Internally, the optimizer rewrites the condition to an equivalent condition which doesn't use `<code>YEAR</code>` or `<code>DATE</code>` functions.


For example, `<code>YEAR(date_col)=2023</code>` is rewritten into 
`<code>date_col between '2023-01-01' and '2023-12-31'</code>`.


Similarly, `<code>DATE(datetime_col) <= '2023-06-01'</code>` is rewritten into 
`<code>datetime_col <= '2023-06-01 23:59:59'</code>`.


## Controlling the Optimization


The optimization is always ON, there is no Optimizer Switch flag to control it.


## Optimizer Trace


The rewrite is logged as `<code>date_conds_into_sargable</code>` transformation. Example:


```
{
            "transformation": "date_conds_into_sargable",
            "before": "cast(t1.datetime_col as date) <= '2023-06-01'",
            "after": "t1.datetime_col <= '2023-06-01 23:59:59'"
          },
```

## References


* [MDEV-8320](https://jira.mariadb.org/browse/MDEV-8320): Allow index usage for DATE(datetime_column) = const

