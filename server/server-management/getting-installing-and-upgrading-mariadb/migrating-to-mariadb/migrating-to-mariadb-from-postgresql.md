
# Migrating to MariaDB from PostgreSQL

There are many different ways to migrate from [PostgreSQL](https://www.postgresql.org/) to MariaDB. This article will discuss some of those options.



## MariaDB's CONNECT Storage Engine


MariaDB's [CONNECT](../../../../connectors/mariadb-connector-nodejs/connector-nodejs-pipelining.md) storage engine can be used to migrate from PostgreSQL to MariaDB. There are two primary ways that this can be done.


See [Loading the CONNECT Storage Engine](../../../reference/storage-engines/connect/installing-the-connect-storage-engine.md) for information on how to install the CONNECT storage engine.


### Tables with ODBC table_type


The CONNECT storage engine allows you to create tables that refer to tables on an external server, and it can fetch the data using a compatible [ODBC](https://en.wikipedia.org/wiki/Open_Database_Connectivity) driver. PostgreSQL does have a freely available ODBC driver called `<code>[psqlODBC](https://odbc.postgresql.org/)</code>`. Therefore, if you install `<code>psqlODBC</code>` on the MariaDB Server, and then configure the system's ODBC framework (such as [unixODBC](https://www.unixodbc.org/)), then the MariaDB server will be able to connect to the remote PostgreSQL server. At that point, you can create tables with the `<code>[ENGINE=CONNECT](../../../reference/sql-statements-and-structure/vectors/create-table-with-vectors.md#storage-engine)</code>` and `<code>[table_type=ODBC](../../../reference/storage-engines/connect/connect-table-types/connect-odbc-table-type-accessing-tables-from-another-dbms.md)</code>` table options set, so that you can access the PostgreSQL tables from MariaDB.


See [CONNECT ODBC Table Type: Accessing Tables From Another DBMS](../../../reference/storage-engines/connect/connect-table-types/connect-odbc-table-type-accessing-tables-from-another-dbms.md) for more information on how to do that.


Once the remote table is setup, you can migrate the data to local tables very simply. For example:


```
CREATE TABLE psql_tab (
   id int,
   str varchar(50)
) ENGINE = CONNECT
table_type=ODBC
tabname='tab'
connection='DSN=psql_server';

CREATE TABLE tab (
   id int,
   str varchar(50)
) ENGINE = InnoDB;

INSERT INTO tab SELECT * FROM psql_tab;
```

### Tables with JDBC table_type


The CONNECT storage engine allows you to create tables that refer to tables on an external server, and it can fetch the data using a compatible [JDBC](https://en.wikipedia.org/wiki/Java_Database_Connectivity) driver. PostgreSQL does have a freely available [JDBC driver](https://jdbc.postgresql.org/). If you install this JDBC driver on the MariaDB server, then the MariaDB server will be able to connect to the remote PostgreSQL server via JDBC. At that point, you can create tables with the `<code>[ENGINE=CONNECT](../../../reference/sql-statements-and-structure/vectors/create-table-with-vectors.md#storage-engine)</code>` and `<code>[table_type=JDBC](../../../reference/storage-engines/connect/connect-table-types/connect-odbc-table-type-accessing-tables-from-another-dbms.md)</code>` table options set, so that you can access the PostgreSQL tables from MariaDB.


See [CONNECT JDBC Table Type: Accessing Tables from Another DBMS](../../../reference/storage-engines/connect/connect-table-types/connect-jdbc-table-type-accessing-tables-from-another-dbms.md) for more information on how to do that.


Once the remote table is setup, you can migrate the data to local tables very simply. For example:


```
CREATE TABLE psql_tab (
   id int,
   str varchar(50)
) ENGINE = CONNECT
table_type=JDBC
tabname='tab'
connection='jdbc:postgresql://psql_server/db1';

CREATE TABLE tab (
   id int,
   str varchar(50)
) ENGINE = InnoDB;

INSERT INTO tab SELECT * FROM psql_tab;
```

## PostgreSQL's Foreign Data Wrappers


PostgreSQL's [foreign data wrappers](https://wiki.postgresql.org/wiki/Foreign_data_wrappers) can also be used to migrate from PostgreSQL to MariaDB.


### mysql_fdw


[mysql_fdw](https://github.com/EnterpriseDB/mysql_fdw) allows you to create a table in PostgreSQL that actual refers to a remote MySQL or MariaDB server. Since MySQL and MariaDB are compatible at the protocol level, this should also support MariaDB.


The foreign data wrapper also supports writes, so you should be able to write to the remote MariaDB table to migrate your PostgreSQL data. For example:


```
CREATE TABLE tab (
   id int,
   str text
);

INSERT INTO tab VALUES (1, 'str1');

CREATE SERVER mariadb_server
   FOREIGN DATA WRAPPER mysql_fdw
   OPTIONS (host '10.1.1.101', port '3306');

CREATE USER MAPPING FOR postgres
   SERVER mariadb_server
   OPTIONS (username 'foo', password 'bar');

CREATE FOREIGN TABLE mariadb_tab (
   id int,
   str text
)
SERVER mariadb_server
OPTIONS (dbname 'db1', table_name 'tab');

INSERT INTO mariadb_tab SELECT * FROM tab;
```

## PostgreSQL's COPY TO


PostgreSQL's `<code>[COPY TO](https://www.postgresql.org/docs/current/sql-copy.html)</code>` allows you to copy the data from a PostgreSQL table to a text file. This data can then be loaded into MariaDB with `<code>[LOAD DATA INFILE](../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md)</code>`.


## MySQL Workbench


MySQL Workbench has a [migration feature](https://www.mysql.com/products/workbench/migrate/) that requires an [ODBC](https://en.wikipedia.org/wiki/Open_Database_Connectivity) driver. PostgreSQL does have a freely available ODBC driver called `<code>[psqlODBC](https://odbc.postgresql.org/)</code>`.


See [Set up and configure PostgreSQL ODBC drivers for the MySQL Workbench Migration Wizard](https://mysqlworkbench.org/2012/11/set-up-and-configure-postgresql-odbc-drivers-for-the-mysql-workbench-migration-wizard/) for more information.


## Known Issues


### Migrating Functions and Procedures


PostgreSQL's [functions](https://www.postgresql.org/docs/current/sql-createfunction.html) and [procedures](https://www.postgresql.org/docs/11/sql-createprocedure.html) use a language called `<code>[PL/pgSQL](https://www.postgresql.org/docs/current/plpgsql.html)</code>`. This language is quite different than the default `<code>SQL/PSM</code>` language used for MariaDB's [stored procedures](../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md). `<code>PL/pgSQL</code>` is more similar to `<code>PL/PSQL</code>` from Oracle, so you may find it beneficial to try migrate with `<code>[SQL_MODE=ORACLE](../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md)</code>` set.


## See also


* [Set up and configure PostgreSQL ODBC drivers for the MySQL Workbench Migration Wizard](https://mysqlworkbench.org/2012/11/set-up-and-configure-postgresql-odbc-drivers-for-the-mysql-workbench-migration-wizard/)

