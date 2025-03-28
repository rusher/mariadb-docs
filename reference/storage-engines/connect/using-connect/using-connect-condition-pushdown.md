# Using CONNECT - Condition Pushdown

The [ODBC](/en/connect-table-types-odbc-table-type-accessing-tables-from-other-dbms/), [JDBC](/en/connect-jdbc-table-type-accessing-tables-from-other-dbms/), [MYSQL](/en/connect-table-types-mysql-table-type-accessing-mysqlmariadb-tables/), [TBL](/en/connect-table-types-tbl-table-type-table-list/) and WMI table types use engine condition pushdown in order to restrict the number of rows returned by the RDBS source or the WMI component.

The CONDITION_PUSHDOWN argument used in old versions of CONNECT is no longer needed because CONNECT uses condition pushdown unconditionally.