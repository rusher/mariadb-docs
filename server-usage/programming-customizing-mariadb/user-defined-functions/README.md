# User-Defined Functions

A user-defined function (UDF) is a historical way to extend MariaDB with a new function that works similar to a native (built-in) MariaDB function such as [ABS( )](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/numeric-functions/abs.md) or [CONCAT( )](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/string-functions/concat.md). It was introduced in 1998 and is generally limited to supporting features that existed at that time.

Statements making use of user-defined functions are not [safe for replication](/en/unsafe-statements-for-replication/).

For an example, see `sql/udf_example.cc` in the source tree. For a collection of existing UDFs go to the [UDF Repository on GitHub](https://github.com/orgs/mysqludf/repositories).

There are alternative ways to add a new function: a native function, which requires modifying and compiling the server source code; a [function plugin](https://app.gitbook.com/s/iJPrPCGi329TSR8WIXJW/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/mariadb-internals-documentation/development-writing-plugins-for-mariadb#function-plugins); or a [stored function](/en/stored-functions/).