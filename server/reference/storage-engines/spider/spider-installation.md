
# Spider Installation

The Spider storage engine supports partitioning and XA transactions, and allows tables of different MariaDB instances to be handled as if they were on the same instance.


To use Spider, you need two or more instances of MariaDB, typically running on separate hosts. The Spider node is the MariaDB server that receives queries from your application. It then processes these queries, connecting to one or more data nodes. The data nodes are the MariaDB servers that actually store the table data.


In order for this to work, you need to configure the data nodes to accept queries from the Spider node and you need to configure the Spider node to use the data nodes as remote storage.


You don't need to install any additional packages to use it, but it does require some configuration.



## Configuring Data Nodes


Spider deployments use data nodes to store the actual table data. In order for a MariaDB server to operate as a data node for Spider, you need to create a table or tables on which to store the data and configure the server to accept client connections from the Spider node.


For instance, first create the table:


```
CREATE TABLE test.spider_example (
   id INT PRIMARY KEY AUTO_INCREMENT,
   name VARCHAR(50)
) ENGINE=InnoDB;
```

Next, create a user for the Spider node and set a password for that user. For the sake of the example, assume the Spider node is at the IP address 192.168.1.1:


```
CREATE USER spider@192.168.1.1;

SET PASSWORD FOR spider@192.168.1.1 = PASSWORD('passwd');
```

Then grant the `spider` user privileges on the example table.


```
GRANT ALL ON test.spider_example TO spider@192.168.1.1;
```

The data node is now ready for use. You can test it by attempting to connect the MariaDB client to the data from the Spider node. For instance, assuming the data node is at the IP address 192.168.1.5, SSH into the Spider node then try to establish a client connection.


```
$ mysql -u spider -p -h 192.168.1.5 test -e "SHOW TABLES;"

+----------------+
| Tables_in_test |
+----------------+
| spider_example |
+----------------+
```

## Install Spider on Spider Node


The Spider storage engine must be installed on the Spider node. The Spider node is the MariaDB server that receives queries for the table, (in this case `test.spider_example`). It then uses the Spider storage engine to connect to the tables on the data nodes to retrieve data and return the result-set.


To install the Spider storage engine, complete the installation process shown below.


### Step 1: Install Spider Package (Debian/Ubuntu)


On Debian and Ubuntu, the Spider storage engine is installed via a separate `mariadb-plugin-spider` package. To install the package via APT, execute the following command:


```
$ sudo apt install mariadb-plugin-spider
```

On other Linux distributions, the Spider storage engine is installed with MariaDB Server.


### Step 2a: Load the Spider Plugin ([MariaDB 10.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md) and Later)


With [MariaDB 10.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md) and later, the Spider storage engine can be loaded as a normal plugin, and Spider automatically creates its dependencies. There are two primary ways to load the plugin.


The plugin can be loaded dynamically without a server restart by executing `INSTALL SONAME` or `INSTALL PLUGIN`:


```
INSTALL SONAME "ha_spider";
```

Alternatively, the plugin can be loaded by adding `plugin_load_add=ha_spider` to a configuration file:


```
<<quote>>
[mariadb]
...
plugin_load_add = "ha_spider"
<</quote>>
```

If the plugin is loaded in a configuration file, then the server will load the plugin after the server has been restarted.


Loading the plugin also creates a series of new tables in the `mysql` database, including:



| table name | added version |
| --- | --- |
| table name | added version |
| spider_xa | [MariaDB 10.0.4](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1004-release-notes.md) |
| spider_xa_member | [MariaDB 10.0.4](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1004-release-notes.md) |
| spider_xa_failed_log | [MariaDB 10.0.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1005-release-notes.md) |
| spider_tables | [MariaDB 10.0.4](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1004-release-notes.md) |
| spider_link_mon_servers | [MariaDB 10.0.4](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1004-release-notes.md) |
| spider_link_failed_log | [MariaDB 10.0.4](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1004-release-notes.md) |
| spider_table_position_for_recovery | [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md) |
| spider_table_sts | [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md) |
| spider_table_crd | [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md) |



### Step 2b: Load the Spider Plugin ([MariaDB 10.3](../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md) and Before)


With [MariaDB 10.3](../../../../release-notes/mariadb-community-server/what-is-mariadb-103.md) and before, the Spider storage engine can be loaded by executing the included `install_spider.sql` script:


```
$ mysql --user root --password < /usr/share/mysql/install_spider.sql
```

Running this configuration script also creates a series of new tables in the `mysql` database, including:



| table name | added version |
| --- | --- |
| table name | added version |
| spider_xa | [MariaDB 10.0.4](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1004-release-notes.md) |
| spider_xa_member | [MariaDB 10.0.4](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1004-release-notes.md) |
| spider_xa_failed_log | [MariaDB 10.0.5](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1005-release-notes.md) |
| spider_tables | [MariaDB 10.0.4](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1004-release-notes.md) |
| spider_link_mon_servers | [MariaDB 10.0.4](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1004-release-notes.md) |
| spider_link_failed_log | [MariaDB 10.0.4](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1004-release-notes.md) |
| spider_table_position_for_recovery | [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md) |
| spider_table_sts | [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md) |
| spider_table_crd | [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md) |



### Step 3: Verify Loading of the Spider Plugin


You can verify that the Spider plugin has been loaded by querying the `information_schema.ENGINES` table:


```
SELECT ENGINE, SUPPORT
FROM information_schema.ENGINES
WHERE ENGINE = 'SPIDER';

+--------------------+---------+
| ENGINE             | SUPPORT |
+--------------------+---------+
| SPIDER             | YES     |
+--------------------+---------+
```

If the Spider plugin is not loaded, then the query will not return any results.


## Configuring Spider Nodes


With the data node or data nodes configured, you can set up the Spider node to use them. The Spider node is the MariaDB server that receives queries for the table, (in this case `test.spider_example`). It then uses the Spider storage engine to connect to the tables on the data nodes to retrieve data and return the result-set.


### Configure the Server


In order to connect the Spider node to the data nodes, you may issue a `[CREATE SERVER](../../sql-statements-and-structure/sql-statements/data-definition/create/create-server.md)` statement for each data node. You can then use the server definition in creating the Spider table.


```
CREATE SERVER dataNode1 FOREIGN DATA WRAPPER mysql
OPTIONS (
   HOST '192.168.1.5',
   DATABASE 'test',
   USER 'spider',
   PASSWORD 'passwd',
   PORT 3306);
```

In the event that you need to modify or replace this server after setting up the Spider table, remember to issue a `[FLUSH](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)` statement to update the server definition.


```
FLUSH TABLES;
```

Alternatively, you could also choose not to create a server, but specify the connection info in the spider table creation.


### Create the Table


With the data nodes set up and the Spider node configured for use, you can create the Spider table. The Spider table must have the same column definitions as the tables on the data nodes. Spider can be configured through table parameters passed to the `COMMENT` or `CONNECTION` option.


```
CREATE TABLE test.spider_example (
   id INT PRIMARY KEY AUTO_INCREMENT,
   name VARCHAR(50)
) ENGINE=Spider
COMMENT='wrapper "mysql", srv "dataNode1", table "spider_example"';
```

This configures Spider to use the server `dataNode1`, (defined above), as a remote table. Any data you write to this table is actually stored on the MariaDB server at 192.168.1.5.


Alternatively, starting from [MariaDB 10.8.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-1081-release-notes.md), one could specify spider table parameters using table options:


```
CREATE TABLE test.spider_example (
   id INT PRIMARY KEY AUTO_INCREMENT,
   name VARCHAR(50)
) ENGINE=Spider
REMOTE_SERVER=dataNode1 REMOTE_TABLE=spider_example;
```
