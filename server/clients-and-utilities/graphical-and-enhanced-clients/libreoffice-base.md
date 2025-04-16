
# LibreOffice Base

[LibreOffice Base](https://www.libreoffice.org/discover/base/) is an open source RDBMS (relational database management system) front-end tool to create and manage various databases.


## Preparing the ODBC Connection


First, make sure to prepare MariaDB Connector/ODBC as explained in [MariaDB Connector/ODBC](../../../connectors/mariadb-connector-odbc/about-mariadb-connector-odbc.md).


That includes:


* Download [the latest MariaDB Connector/ODBC](https://mariadb.com/downloads/#connectors)
* Copy the shared library libmaodbc.so to /usr/lib/[multi-arch]
* Install the unixodbc, unixodbc-dev, openssh-client, odbcinst packages
* Create a template file for the [ODBC driver](../../../connectors/mariadb-connector-odbc/creating-a-data-source-with-mariadb-connectorodbc.md#configuring-mariadb-connectorodbc-as-a-unixodbc-driver-on-linux). A sample “MariaDB_odbc_driver_template.ini” could be:



|   |
| --- |
| [MariaDB ODBC 3.1 Driver] |
| Description = MariaDB Connector/ODBC v.3.1 |
| Driver = /usr/lib/x86_64-linux-gnu/libmaodbc.so |



* Install the ODBC driver from the template file by running:


```
$ sudo odbcinst -i -d -f MariaDB_odbc_driver_template.ini
odbcinst: Driver installed. Usage count increased to 1. 
    Target directory is /etc
```

Verify successful installation in */etc/odbcinst.ini* file (this path is obtained by the config info */-j*/ option, where drivers are installed in that predefined location).


```
$ odbcinst -j
unixODBC 2.3.6
DRIVERS............: /etc/odbcinst.ini
SYSTEM DATA SOURCES: /etc/odbc.ini
FILE DATA SOURCES..: /etc/ODBCDataSources
USER DATA SOURCES..: /home/anel/.odbc.ini
SQLULEN Size.......: 8
SQLLEN Size........: 8
SQLSETPOSIROW Size.: 8

$ cat /etc/odbcinst.ini 
[MariaDB ODBC 3.1 Driver]
Description=MariaDB Connector/ODBC v.3.1
Driver=/usr/lib/x86_64-linux-gnu/libmaodbc.so
UsageCount=1
```

* Create a template file for the [Data Source Name (DSN)](../../../connectors/mariadb-connector-odbc/creating-a-data-source-with-mariadb-connectorodbc.md#configuring-a-dsn-with-unixodbc-on-linux). A sample “MariaDB_odbc_data_source_template.ini” could be:



|   |
| --- |
| [MariaDB-server] |
| Description=MariaDB server |
| Driver=MariaDB ODBC 3.1 Driver |
| SERVER=localhost |
| USER=anel |
| PASSWORD= |
| DATABASE=test |
| PORT=3306 |



* Install data source:


```
odbcinst -i -s -h -f MariaDB_odbc_data_source_template.ini
```

* Verify successful installation in the /.odbc.ini file


```
$ cat ~/.odbc.ini 
[MariaDB-server]
Description=MariaDB server
Driver=MariaDB ODBC 3.1 Driver
SERVER=MariaDB
USER=anel
PASSWORD=
DATABASE=test
PORT=3306
```

* Verify successful installation also using the [isql](../../../connectors/mariadb-connector-odbc/creating-a-data-source-with-mariadb-connectorodbc.md#verifying-a-dsn-configuration-with-unixodbc-on-linux) utility, for example:


```
$ isql MariaDB-server
+---------------------------------------+
| Connected!                            |
|                                       |
| sql-statement                         |
| help [tablename]                      |
| quit                                  |
|                                       |
+---------------------------------------+
SQL> show tables;
+--------------------------------------------------------------------------+
| Tables_in_test                                                           |
+--------------------------------------------------------------------------+
| Authors                                                                  |
| tbl_names                                                                |
| webposts                                                                 |
| webusers                                                                 |
+--------------------------------------------------------------------------+
SQLRowCount returns 4
4 rows fetched
```

## Start with LibreOffice Base


Start Libreoffice Base from the terminal by running *lobase* (make sure to install the *libreoffice-base* package if needed). The default option is to create a new database, which is *HSQLDB*. In order to connect to a running MariaDB server, choose *“Connect to an existing database”* and choose *“ODBC”* driver as shown below:


![librebase_1](../../.gitbook/assets/libreoffice-base/+image/librebase_1.png "librebase_1")


After that, choose DSN (the one that we created in the previous step) and click *“Next”*:


![librebase_2](../../.gitbook/assets/libreoffice-base/+image/librebase_2.png "librebase_2")


Provide a user name (and password if needed) and again check the connection (with the *“Test Connection”* button) and click *“Next”*:


![librebase_3](../../.gitbook/assets/libreoffice-base/+image/librebase_3.png "librebase_3")


After that, we have options to register the database. Registration in this sense means that the database is viewable by other LibreOffice modules (like *LibreOffice Calc* and *LibreOffice Writer*). So this step is optional. In this example, we will save as *“fosdem21_mariadb.odb”*. See [Using a Registered Database](#using-a-registered-database).


![librebase_4](../../.gitbook/assets/libreoffice-base/+image/librebase_4.png "librebase_4")


It opens the following window:


![librebase_5](../../.gitbook/assets/libreoffice-base/+image/librebase_5.png "librebase_5")


It consists of three windows/panels:


1. “Database” window with the options

  1. "Tables",
  1. "Queries",
  1. "Forms",
  1. "Reports".
1. "Tasks window (dependent on what is selected in the “Database” window). When “Tables” is selected, the options are:

  1. "Create Table in Design View",
  1. "Use Wizard to Create Table" and
  1. "Create View".
1. "Tables" window - shows list of tables that are created.


As we can see, there are system tables in the *“mysql”* database as well as *“test”* database.


Let’s say we create a table using the REST API from JSON data from [posts](https://jsonplaceholder.typicode.com/posts), and another table using the same mechanism from [users](https://jsonplaceholder.typicode.com/users), and let’s call them *webposts* and *webusers*. In order to do so, we have to enable the **CONNECT** storage engine plugin and start with REST_API. See more in the [CONNECT - Files Retrieved Using Rest Queries](../../reference/storage-engines/connect/connect-table-types/connect-files-retrieved-using-rest-queries.md) article.


The queries we need to run in MariaDB are:


```
CREATE TABLE webusers ENGINE=CONNECT TABLE_TYPE=JSON
  HTTP='http://jsonplaceholder.typicode.com/users';

CREATE TABLE webposts ENGINE=CONNECT TABLE_TYPE=JSON
  HTTP='http://jsonplaceholder.typicode.com/posts';
```

The result in LibreOffice Base will be as shown below:


![librebase_6](../../.gitbook/assets/libreoffice-base/+image/librebase_6.png "librebase_6")


Double clicking on the table opens a new window with the data displayed to inspect:


![librebase_7](../../.gitbook/assets/libreoffice-base/+image/librebase_7.png "librebase_7")


To create the table from the *“Tasks”* window, use the option *“Create Table in Design View”*, where one can specify specific field names and types as shown:


![librebase_8](../../.gitbook/assets/libreoffice-base/+image/librebase_8.png "librebase_8")


From the “Tasks” window one can create a table using the option *“Use Wizard to Create Table”* to create some sample tables.


One can fill the data in the existing table, or create and define the new table from the *LibreOffice Calc* module with simple copy-paste (in the *"Tasks"* window).


## Using a Registered Database


Other modules can use the registered database, for example, open *"LibreOffice Calc"* and go to *"Tools"*, *"Options"* and you will see the *"odb"* file we registered when starting *"LibreOffice Base"*.

