# ColumnStore User Defined Aggregate and Window Functions

1. [Introduction "Introduction"](columnstore-user-defined-aggregate-and-window-functions.md#introduction)
2. [Using user defined aggregate functions "Using user defined aggregate functions"](columnstore-user-defined-aggregate-and-window-functions.md#using-user-defined-aggregate-functions)
3. [Developing a new function "Developing a new function"](columnstore-user-defined-aggregate-and-window-functions.md#developing-a-new-function)
4. [Limitations "Limitations"](columnstore-user-defined-aggregate-and-window-functions.md#limitations)

## Introduction

Starting with MariaDB ColumnStore 1.1, the ability to create and use user defined aggregate and window functions is supported in addition to scalar functions. With Columnstore 1.2, multiple parameters are supported. A C++ SDK is provided as well as 3 reference examples that provide additional functions that may be of general use:

* median - mathematical median, equivalent to percentile\_cont(0.5)
* avg\_mode - mathematical mode, i.e. the most frequent value in the set
* ssq - sum of squares, i.e. the sum of each individual number squared in the set

Similar to built-in functions, the SDK supports distributed aggregate execution where as much of the calculation is scaled out across PM nodes and then collected / finalized in the UM node. Window functions (due to the ordering requirement) are only executed at the UM level.

## Using user defined aggregate functions

The reference examples above are included in the standard build of MariaDB ColumnStore and so can be used by registering them as user defined aggregate functions. The same can be done for new functions assuming the instance has the updated libraries included. From a mcsmysql prompt:

```
CREATE AGGREGATE FUNCTION median returns REAL soname 'libudf_mysql.so';
CREATE AGGREGATE FUNCTION avg_mode returns REAL soname 'libudf_mysql.so';
CREATE AGGREGATE FUNCTION ssq returns REAL soname 'libudf_mysql.so';
```

After this these may be used in the same way as any other aggregate or window function like sum:

```
SELECT grade, 
AVG(loan_amnt) avg, 
MEDIAN(loan_amnt) median 
FROM loanstats 
GROUP BY grade 
ORDER BY grade;
```

## Developing a new function

This requires a MariaDB ColumnStore source tree and necessary tools to compile C/C++ code. The SDK and reference examples are available in the [utils/udfsdk](https://github.com/mariadb-corporation/mariadb-columnstore-engine/tree/master/utils/udfsdk) directory of the source tree. This contains the SDK documentation which is also available here:

* [1.2.x UDAF SDK Guide "1.2.x UDAF SDK Guide"](https://github.com/mariadb-corporation/mariadb-columnstore-engine/blob/master/utils/udfsdk/udfsdk.h)

## Limitations

* The implementation of the median and avg\_mode functions will scale in memory consumption to the size of the set of unique values in the aggregation.

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
