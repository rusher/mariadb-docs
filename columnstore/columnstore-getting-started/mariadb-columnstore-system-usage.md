
# MariaDB ColumnStore System Usage

 
1. [Non-root user MariaDB ColumnStore Admin console "Non-root user MariaDB ColumnStore Admin console"](#non-root-user-mariadb-columnstore-admin-console)
1. [MariaDB ColumnStore aliases "MariaDB ColumnStore aliases"](#mariadb-columnstore-aliases)
1. [mcsadmin "mcsadmin"](#mcsadmin) 

  1. [Shutting down the system "Shutting down the system"](#shutting-down-the-system)
  1. [Stopping the system "Stopping the system"](#stopping-the-system)
  1. [Starting the system or modules "Starting the system or modules"](#starting-the-system-or-modules)
  1. [Restarting the system "Restarting the system"](#restarting-the-system)
1. [Logging into MariaDB ColumnStore MariaDB console "Logging into MariaDB ColumnStore MariaDB console"](#logging-into-mariadb-columnstore-mariadb-console) 

  1. [MariaDB Root user password "MariaDB Root user password"](#mariadb-root-user-password)
1. [Example MariaDB ColumnStore database setup "Example MariaDB ColumnStore database setup"](#example-mariadb-columnstore-database-setup)
1. [Importing data into MariaDB ColumnStore "Importing data into MariaDB ColumnStore"](#importing-data-into-mariadb-columnstore) 

  1. [Configuring_to_use_UTF-8_Character_sets "Configuring_to_use_UTF-8_Character_sets"](#configuring_to_use_utf-8_character_sets)
1. [Configuring to use UTF-8 Character sets "Configuring to use UTF-8 Character sets"](#configuring-to-use-utf-8-character-sets)
1. [Importing UTF-8 data "Importing UTF-8 data"](#importing-utf-8-data)





Once the MariaDB ColumnStore system installation has been completed, these are some of the basic commands to access the MariaDB ColumnStore Admin and MySQL Console


## Non-root user MariaDB ColumnStore Admin console


The MariaDB ColumnStore Admin console that is run from the command line console as root user can be 
setup to be run for a non-root user, if you choose to do so.


This would require a change in the /etc/sudoers file.


After this line:


```
# %wheel	ALL=(ALL)	NOPASSWD: ALL
```

Add, where 'user' is the non-root username:


```
user	  ALL=(ALL)       NOPASSWD: /usr/local/mariadb/columnstore/bin/mcsadmin
```

To run the command, you would need to enter the full path or you can setup the alias's by entering the following command:


```
.  /usr/local/mariadb/columnstore/bin/columnstoreAlias
```

Now you can run both console commands for a non-root user account: 'mcsmysql' and 'mcsadmin'


NOTE: The same setup can be done for other commands like 'cpimport'.


## MariaDB ColumnStore aliases


To configure the MariaDB ColumnStore Aliases, run the following:


```
. /usr/local/mariadb/columnstore/bin/columnstoreAlias
```

Note: This script will also be added to the /root/.bash_profile. The following alias will be created after running the Alias:


```
mcsmysql = /usr/local/mariadb/columnstore/mysql/bin/mysql 
  --defaults-file=/usr/local/mariadb/columnstore/mysql/my.cnf 
  -u root
```

mcsmysql: Launches the MariaDB ColumnStore MySQL Console


```
mcsadmin = /usr/local/mariadb/columnstore/bin/mcsadmin
```

mcsadmin: Launches the MariaDB ColumnStore Admin Console


## mcsadmin


The MariaDB ColumnStore Management Console allows you to configure, monitor, and manage
the MariaDB ColumnStore system and servers. For more detailed information, see [MariaDB ColumnStore Administrative Console](../managing-columnstore/managing-columnstore-system/columnstore-administrative-console.md).


These 2 examples will provide a full command list


```
mcsadmin help
```

Or


```
mcsadmin
mcsadmin> help
```

To get a verbose help on a specific command, enter:


```
mcsadmin help getsysteminfo
```

NOTE: You can also short-cut commands, both of these do the same command:


```
mcsadmin getsysteminfo
mcsadmin getsystemi
```

Check system status


```
mcsadmin getsystemstatus

getsystemstatus Tue Jan 12 08:07:02 2012
System mymcs1
System and Module statuses
Component    Status                    Last Status Change
------------ ----------------------   ------------------------
System       ACTIVE                    Mon Jan 11 17:54:46 2012
Module pm1   ACTIVE                    Mon Jan 11 17:54:45 2012
```

Check system info, which provides process status


```
mcsadmin getsysteminfo
```

### Shutting down the system


When you perform a shutdown, all MariaDB ColumnStore processes are stopped. This
command would be used mainly when performing software upgrades.


To shutdown the system:


* From the MariaDB ColumnStore Console, type shutdownSystem
* Press y


```
mcsadmin shutdownSystem y
```

### Stopping the system


Stopping the system stops the application processes. The platform process that
supports the Management Console and System Alarms remain active. If you want to
stop the system or server and immediately start the processes again (typically if the
system or a server hangs), you can restart the system or servers as shown in the
section “Restarting the system”.


To stop the system:


* From the MariaDB ColumnStore Console, type stopSystem
* Press y


```
mcsadmin stopSystem y
```

### Starting the system or modules


You can start the system or module application processes with the following
commands:


To start the system after a stopSystem:


* From the MariaDB ColumnStore Console, type startSystem


```
mcsadmin startSystem
```

To start the system after a shutdownSystem:


If its a multi-server system and ssh-keys are not configured between the servers, you will be required to provide
the user password for the other servers. If ssh-keys are configured, then password parameter isn't required


* From the MariaDB ColumnStore Console, type startSystem


```
mcsadmin startSystem 'user-password'
```

### Restarting the system


When you want to stop and immediately start application processes, you can perform
a restart. You restart the system or modules application processes with the following
commands:


To restart the system:


* From the MariaDB ColumnStore Console, type restartSystem


```
mcsadmin restartSystem
```

## Logging into MariaDB ColumnStore MariaDB console


a Linux prompt:


```
mcsmysql [optional database name]
```

### MariaDB Root user password


When a MariaDB Root user password is configured, do the following to access the MariaDB console:


```
mcsmysql -p'password' [optional database name]
```

Setup this file in the user account where MariaDB ColumnStore was installed, .my.cnf
So for root user install, it would be /root/.my.cnf


```
[client] 
   user            = root
   password        = 'password'
```

Make sure the permissions are set appropriately:


```
# chmod 0600 /root/.my.cnf
```

[password-security-user.html](https://dev.mysql.com/doc/refman/5.7/en/password-security-user.html)


IMPORTANT - If there is no MariaDB Root user password set, make sure there is no .my.cnf file. This could cause failures in install and upgrades if this file exist when no password is set.


## Example MariaDB ColumnStore database setup


Once logged into mcsmysql:


```
create database mcs;
use mcs;
create table idbtest(col1 int, col2 int) engine=columnstore;
show create table idbtest;
insert into idbtest values (1, 2);
insert into idbtest values (3, 4);
select * from idbtest;
```

## Importing data into MariaDB ColumnStore


While MariaDB ColumnStore supports multiple ways to get data into the database
(individual insert, batch insert, load data infile and import), the most efficient manner
to load significant amounts of data into MariaDB ColumnStore is through the import
utility.


* A delimited import file should be created to match the table that you want to import data to similar to the following. In this example, the file will be saved as idbtest.tbl:


```
100|1001|
200|2002|
```

* Save/place this file in a directory
* From that same directory, import the rows:


```
/usr/local/mariadb/columnstore/bin/cpimport mcs idbtest idbtest.tbl
```

#### `<code>Configuring_to_use_UTF-8_Character_sets</code>`


## Configuring to use UTF-8 Character sets


MariaDB Columnstore has the ability to support UTF-8 character sets. This profile may be set as a default 
for the instance or set at the session level.


Please refer to the SQL Syntax Guide for the setting UTF-8 profile at the session level.


To set UTF-8 profile at the instance level, specify the following in my.cnf and the Columnstore.xml files.


my.cnf
 To configure the MariaDB Locale language, modify the my.cnf file (/usr/local/mariadb/columnstore/mysql):


```
[client]
default-character-set=utf8
[mysqld]
character-set-server=utf8
collation-server=utf8_general_ci
init-connect='SET NAMES utf8'
```

Columnstore.xml


To configure the ColumnStore Locale language, modify the Columnstore.xml files (/usr/local/mariadb/columnstore/etc)


```
<SystemConfig>
   <SystemLang>en_US.utf8</SystemLang>
```

where value is a valid locale for the operating system. The recommended setting is en_US.utf8.


Alternatively, you can set the value as follows


```
/usr/local/mariadb/columnstore/bin/setConfig SystemConfig SystemLang en_US.utf8
```

Any tables containing UTF-8 data must have the default character set specified as 'utf8', for example:


```
create table airports (
code char(3),
airport varchar(100),
city varchar(50),
state char(50),
country char(100),
latitude float,
longitude float
) engine=columnstore default character set=utf8;
```

## Importing UTF-8 data


When using the cpimport utility, the input file must be converted to UTF-8 data. The
Linux program iconv is one utility to convert it.


```
iconv -f ISO-8859-1 -t UTF-8 < input.txt > output.txt
```
