
# ColumnStore Audit Plugin

 
1. [Introduction "Introduction"](#introduction)
1. [Installation "Installation"](#installation)
1. [Enabling the audit plugin "Enabling the audit plugin"](#enabling-the-audit-plugin)



# Introduction


MariaDB server includes an optional [Audit Plugin](../../../server/reference/plugins/mariadb-audit-plugin/release-notes-mariadb-audit-plugin/mariadb-audit-plugin-113-release-notes.md) that enables logging and tracking of all user access and statements. This is included and can be enabled for ColumnStore


# Installation


To enable the audit plugin for the currently running instance (but no across restarts) run the following as mcsmysql with the default root account:


```
INSTALL PLUGIN server_audit 
SONAME 'server_audit.so';
```


To have this persist across restarts edit the ColumnStore my.cnf file (example shown for root install):


```
$ vi /usr/local/mariadb/columnstore/mysql/my.cnf
[mysqld]
... 
plugin_load=server_audit=server_audit.so
```


For more details see the [audit plugin installation guide](../../../server/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-installation.md)


# Enabling the audit plugin


To enable audit logging the following global variable must be set to ON:


```
SET GLOBAL server_audit_logging=ON;
```


To ensure this persists across restarts edit the ColumnStore my.cnf file (example shown for root install):


```
$ vi /usr/local/mariadb/columnstore/mysql/my.cnf
[server]
... 
server_audit_logging=ON
```


This will enable logging to the file /usr/local/mariadb/columnstore/mysql/db/server_audit.log. For example:


```
20170914 17:31:24,centos,root,localhost,11,114,QUERY,loans,'SELECT grade, AVG(loan_amnt) avg, FROM loanstats GROUP BY grade ORDER BY grade',0
```


To have the log entries written to syslog the global variable server_audit_output_type should be changed from 'file' to 'syslog'. In this case the 'syslog_info' entry contains the ColumnStore server instance name, for example:


```
Sep 14 17:46:51 centos mysql-server_auditing: columnstore-1 centos,root,localhost,11,117,QUERY,loans,'SELECT grade, AVG(loan_amnt) avg,FROM loanstats GROUP BY grade ORDER BY grade',0
```


For additional configuration and customization options see the [Audit Plugin](../../../server/reference/plugins/mariadb-audit-plugin/release-notes-mariadb-audit-plugin/mariadb-audit-plugin-113-release-notes.md) documentation.

