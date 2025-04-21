
# User-Defined Functions Calling Sequences


The functions described in [Creating User-defined Functions](creating-user-defined-functions.md) are expanded on this page. They are declared as follows:


## Simple Functions


### x()


If x() returns an integer, it is declared as follows:


```
long long x(UDF_INIT *initid, UDF_ARGS *args,
              char *is_null, char *error);
```

If x() returns a string (DECIMAL functions also return string values), it is declared as follows:


```
char *x(UDF_INIT *initid, UDF_ARGS *args,
          char *result, unsigned long *length,
          char *is_null, char *error);
```

If x() returns a real, it is declared as follows:


```
double x(UDF_INIT *initid, UDF_ARGS *args,
              char *is_null, char *error);
```

### x_init()


```
my_bool x_init(UDF_INIT *initid, UDF_ARGS *args, char *message);
```

### x_deinit()


```
void x_deinit(UDF_INIT *initid);
```

### Description


*initid* is a parameter passed to all three functions that points to a *UDF_INIT* structure, used for communicating information between the functions. Its structure members are:


* my_bool maybe_null

  * maybe_null should be set to 1 if x_init can return a NULL value, Defaults to 1 if any arguments are declared maybe_null.
* unsigned int decimals

  * Number of decimals after the decimal point. The default, if an explicit number of decimals is passed in the arguments to the main function, is the maximum number of decimals, so if 9.5, 9.55 and 9.555 are passed to the function, the default would be three (based on 9.555, the maximum). If there are no explicit number of decimals, the default is set to 31, or one more than the maximum for the DOUBLE, FLOAT and DECIMAL types. This default can be changed in the function to suit the actual calculation.
* unsigned int max_length

  * Maximum length of the result. For integers, the default is 21. For strings, the length of the longest argument. For reals, the default is 13 plus the number of decimals indicated by initid->decimals. The length includes any signs or decimal points. Can also be set to 65KB or 16MB in order to return a BLOB. The memory remains unallocated, but this is used to decide on the data type to use if the data needs to be temporarily stored.
* char *ptr

  * A pointer for use as required by the function. Commonly, initid->ptr is used to communicate allocated memory, with x_init() allocating the memory and assigning it to this pointer, x() using it, and x_deinit() de-allocating it.
* my_bool const_item

  * Should be set to 1 in x_init() if x() always returns the same value, otherwise 0.


## Aggregate Functions


### x_clear()


*x_clear()* is a required function for aggregate functions, and is declared as follows:


```
void x_clear(UDF_INIT *initid, char *is_null, char *error);
```

It is called when the summary results need to be reset, that is at the beginning of each new group. but also to reset the values when there were no matching rows.


*is_null* is set to point to CHAR(0) before calling x_clear().


In the case of an error, you can store the value to which the error argument points (a single-byte variable, not a string string buffer) in the variable.


### x_reset()


*x_reset()* is declared as follows:


```
void x_reset(UDF_INIT *initid, UDF_ARGS *args,
               char *is_null, char *error);
```

It is called on finding the first row in a new group. Should reset the summary variables, and then use *UDF_ARGS* as the first value in the group's internal summary value. The function is not required if the UDF interface uses *x_clear()*.


### x_add()


*x_add()* is declared as follows:


```
void x_add(UDF_INIT *initid, UDF_ARGS *args,
             char *is_null, char *error);
```

It is called for all rows belonging to the same group, and should be used to add the value in *UDF_ARGS* to the internal summary variable.


### x_remove()


*x_remove()* was added in [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104) and is declared as follows (same as *x_add()*):


```
void x_remove(UDF_INIT* initid, UDF_ARGS* args,
               char* is_null, char *error );
```

It adds more efficient support of aggregate UDFs as [window functions](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/window-functions/README.md). *x_remove()* should "subtract" the row (reverse *x_add()*). In [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104) aggregate UDFs will work as WINDOW functions without *x_remove()* but it will not be so efficient.


If *x_remove()* supported (defined) detected automatically.

