
# ColumnStore Distributed Aggregate Functions

MariaDB ColumnStore supports the following aggregate functions, these can be used in the SELECT, HAVING, and ORDER BY clauses of the SQL statement.


| Function | Description |
| --- | --- |
| AVG([DISTINCT] column) | Average value of a numeric (INT variations, NUMERIC, DECIMAL) column |
| CORR(ColumnY, ColumnX) | The correlation coefficient for non-null pairs in a group. |
| COUNT (*, [DISTINCT] column) | The number of rows returned by a query or grouping. All datatypes are supported |
| COVAR_POP(ColumnY, ColumnX) | The population covariance for non-null pairs in a group. |
| COVAR_SAMP(ColumnY, ColumnX) | The sample covariance for non-null pairs in a group. |
| MAX ([DISTINCT] column) | The maximum value of a column. All datatypes are supported. |
| MIN ([DISTINCT] column) | The maximum value of a column. All datatypes are supported. |
| REGR_AVGX(ColumnY, ColumnX) | Average of the independent variable (sum(ColumnX)/N), where N is number of rows processed by the query |
| REGR_AVGY(ColumnY, ColumnX) | Average of the dependent variable (sum(ColumnY)/N), where N is number of rows processed by the query |
| REGR_COUNT(ColumnY, ColumnX) | The total number of input rows in which both column Y and column X are nonnull |
| REGR_INTERCEPT(ColumnY, ColumnX) | The y-intercept of the least-squares-fit linear equation determined by the (ColumnX, ColumnY) pairs |
| REGR_R2(ColumnY, ColumnX) | Square of the correlation coefficient. correlation coefficient is the regr_intercept(ColumnY, ColumnX) for linear model |
| REGR_SLOPE(ColumnY, ColumnX) | The slope of the least-squares-fit linear equation determined by the (ColumnX, ColumnY) pairs |
| REGR_SXX(ColumnY, ColumnX) | REGR_COUNT(y, x) * VAR_POP(x) for non-null pairs. |
| REGR_SXY(ColumnY, ColumnX) | REGR_COUNT(y, x) * COVAR_POP(y, x) for non-null pairs. |
| REGR_SYY(ColumnY, ColumnX) | REGR_COUNT(y, x) * VAR_POP(y) for non-null pairs. |
| STD(), STDDEV(), STDDEV_POP() | The population standard deviation of a numeric (INT variations, NUMERIC, DECIMAL) column |
| STDDEV_SAMP() | The sample standard deviation of a numeric (INT variations, NUMERIC, DECIMAL) column |
| SUM([DISTINCT] column) | The sum of a numeric (INT variations, NUMERIC, DECIMAL) column |
| VARIANCE(), VAR_POP() | The population standard variance of a numeric (INT variations, NUMERIC, DECIMAL) column |
| VAR_SAMP() | The population standard variance of a numeric (INT variations, NUMERIC, DECIMAL) column |


### Note


* Regression functions (REGR_AVGX to REGR_YY), CORR, COVAR_POP and COVAR_SAMP are supported for version 1.2.0 and higher


### Example


An example group by query using aggregate functions is:


```
select year(o_orderdate) order_year, 
avg(o_totalprice) avg_totalprice, 
max(o_totalprice) max_totalprice, 
count(*) order_count 
from orders 
group by order_year 
order by order_year;
```


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
