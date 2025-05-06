
# ColumnStore User Defined Functions

 
1. [Introduction "Introduction"](#introduction)
1. [Developing a user defined function "Developing a user defined function"](#developing-a-user-defined-function) 

  1. [MariaDB server UDF implementation "MariaDB server UDF implementation"](#mariadb-server-udf-implementation)
  1. [ColumnStore distributed UDF implementation "ColumnStore distributed UDF implementation"](#columnstore-distributed-udf-implementation)
  1. [Deploying and using a UDF "Deploying and using a UDF"](#deploying-and-using-a-udf)





## Introduction


MariaDB provides extensibility support through user defined functions. For more details on the MariaDB server framework see the [user-defined-functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/programming-customizing-mariadb/user-defined-functions/) article. This documentation applies to MariaDB ColumnStore version 1.0.10 and above.


MariaDB ColumnStore provides scale out query processing and as such requires a separate distributed implementation of each SQL function. This allows for the function application to happen on each PM server node providing distributed scale out performance.


Thus, to fully implement a user defined function for MariaDB ColumnStore requires implementing 2 different API's:


* The MariaDB server UDF API: This allows utilization on all storage engines and is the implementation used if applied in the select list.
* The ColumnStore distributed UDF API: This enables distributed execution of where clause and group by usage of the function and will be pushed down to PM nodes for execution where possible.


MariaDB ColumnStore supports user defined function implementations in C/C++. User defined aggregate and window functions are not supported in ColumnStore 1.0.


## Developing a user defined function


The development kit can be found under the [utils/udfsdk](https://github.com/mariadb-corporation/mariadb-columnstore-engine/tree/master/utils/udfsdk) directory of the mariadb-columnstore-engine source tree. To develop a user defined function requires you to set up a development environment and be comfortable with c++ development. To setup a ColumnStore development environment please follow the instructions on dependencies in the [ColumnStore server fork](https://github.com/mariadb-corporation/mariadb-columnstore-server) repository.


Three main files will need to be modified in order to add a new UDF:


* udfmysql.cpp : mariadb server UDF implementation
* udfsdk.h : class headers.
* udfsdk.cpp : distributed columnstore UDF implementation.


Two reference implementations are provided to provide guidance on creating your own functions:


* MCS_IsNull : this illustrates a simple one argument function providing the ability to return a Boolean if the expression parameter is null
* MCS_Add: this illustrates a simple 2 argument function to illustrate adding 2 values and return the sum.


It is simplest to copy these and adapt to your needs. There are no system dependencies on the included reference implementations so these can be removed to simplify the class files if preferred.


### MariaDB server UDF implementation


Three functions are required to be implemented (for more details see [user-defined-functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/programming-customizing-mariadb/user-defined-functions/)):


* x_init : perform any parameter validation or setup such as memory allocation.
* x : perform the actual function implementation.
* x_deinit : perform any clean up tasks such as deallocating memory
where 'x' is the function name.


### ColumnStore distributed UDF implementation


The function name and class must be registered in order to be recognized and used by the ColumnStore primitive processor. This is done by adding a line to perform the registration in the *UDFSDK::UDFMap()* function in the file **udfsdk.cpp**:


```
FuncMap UDFSDK::UDFMap() const
{
	FuncMap fm;
	
	// first: function name
	// second: Function pointer
	// please use lower case for the function name. Because the names might be 
	// case-insensitive in MariaDB depending on the setting. In such case,
	// the function names passed to the interface is always in lower case.
	fm["mcs_add"] = new MCS_add();
	fm["mcs_isnull"] = new MCS_isnull();

	return fm;
}
```


For any new user defined functions add a new entry into the FuncMap object mapping the name to the udf class.


The UDF class should be defined in file **udfsdk.h** and implemented in file **udfsdk.cpp**. It is easiest to adapt the example classes for new instance but each class must implement the *funcexp::Func* C++ class definition:


* constructor: any initialization necessary
* destructor: any de-initialization.
* getOperationType: this performs parameter validation and returns the result data type.
* get<DATATYPE>Val : computes and returns the value of the user defined function for each given return datatype.


The code changes can be built using make within the directory **utils/udfsdk**, this will create the following libraries in the same directory:


* libudf_mysql.so.1.0.0
* libudfsdk.so.1.0.0


containing the compiled code


### Deploying and using a UDF


The 2 libraries created above must be deployed to the **/usr/local/mariadb/columnstore/lib** directory (or equivalent lib directory in a non root install) replacing the existing files. Symbolic links in the mariadb server directory point to these but should be validated. Run the following as root from the **utils/udfsdk** directory in the build tree (specifying a password to restartSystem if needed for a multi server cluster):


```
$ cp libudf_mysql.so.1.0.0 libudfsdk.so.1.0.0 /usr/local/mariadb/columnstore/lib/
$ ls -l /usr/local/mariadb/columnstore/mysql/lib/plugin/libudf_mysql.so
lrwxrwxrwx. 1 root root 56 Jul 19 09:47 /usr/local/mariadb/columnstore/mysql/lib/plugin/libudf_mysql.so -> /usr/local/mariadb/columnstore/lib/libudf_mysql.so.1.0.0
```


Repeat this for each ColumnStore UM and PM node in the cluster and then restart ColumnStore to make the libraries available.


After restarting the system the UDF must be registered with the MariaDB server to be usable:


```
$ mcsmysql
    > create function mcs_add returns integer soname 'libudf_mysql.so';
```


The function *mcs_add* can then be used. Verify that it can be used both in the select list and where clause for correct installation:


```
MariaDB [test]> create function mcs_add returns integer soname 'libudf_mysql.so';
Query OK, 0 rows affected (0.01 sec)

MariaDB [test]> create table t1(i1 int, i2 int) engine=columnstore;
Query OK, 0 rows affected (0.58 sec)

MariaDB [test]> insert into t1 values (1,1), (2,2);
Query OK, 2 rows affected (0.24 sec)
Records: 2  Duplicates: 0  Warnings: 0

MariaDB [test]> select i1, i2, mcs_add(i1,i2) sum from t1;
+------+------+------+
| i1   | i2   | sum  |
+------+------+------+
|    1 |    1 |    2 |
|    2 |    2 |    4 |
+------+------+------+
2 rows in set (0.05 sec)

MariaDB [test]> select i1, i2 from t1 where mcs_add(i1,i2) = 4;
+------+------+
| i1   | i2   |
+------+------+
|    2 |    2 |
+------+------+
1 row in set (0.02 sec)
```


CC BY-SA / Gnu FDL

