
# User-Defined Functions Security

The MariaDB server imposes a number of limitations on [user-defined functions](user-defined-functions-security.md) for security purposes.


* The INSERT privilege for the mysql database is required to run [CREATE FUNCTION](create-function-udf.md), as a record will be added to the [mysql.func-table](../../../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-func-table.md).
* The DELETE privilege for the mysql database is required to run [DROP FUNCTION](drop-function-udf.md) as the corresponding record will be removed from the [mysql.func-table](../../../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-func-table.md).
* UDF object files can only be placed in the plugin directory, as specified by the value of the [plugin_dir](../../replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#plugin_dir) system variable.
* At least one symbol, beyond the required x() - corresponding to an SQL function X()) - is required. These can be x_init(), x_deinit(), xxx_reset(), x_clear() and x_add() functions (see [Creating User-defined Functions](creating-user-defined-functions.md)). The [allow-suspicious-udfs](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md#-allow-suspicious-udfs) mariadbd option (by default unset) provides a workaround, permitting only one symbol to be used. This is not recommended, as it opens the possibility of loading shared objects that are not legitimate user-defined functions.

