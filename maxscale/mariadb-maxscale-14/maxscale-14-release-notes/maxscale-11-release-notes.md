
# MaxScale 1.1 Release Notes

# MariaDB MaxScale 1.1 Release Notes


## 1.1 GA


This document details the changes in version 1.1 since the release of the 1.0.5 GA Release of the MaxScale product.


## New Features


### High Performance Binlog Relay


Replicate Binlog from the master to slave through MaxScale as simplified relay server for reduced network load and disaster recovery


### Database Firewall Filter


Block queries based on columns in the query, where condition, query type(select, insert, delete, update), presence of wildcard in column selection, regular expression match and time of the query


### Schema Sharding Router


Route to databases sharded by schema without application level knowledge of shard configuration


### Hint based routing


Pass hints in the SQL statement to influence the routing decision based on replication lag or time out


### Named Server Routing


Routing to a named server if incoming query matches a regular expression


### Canonical Query logging


Convert incoming queries to canonical form and push the query and response into RabbitMQ Broker for a RabbitMQ Client to later retrieve from


### Nagios Plugin


Plugin scripts for monitoring MaxScale status and performance from a Nagios Server


### Notification Service


Receive notification of security update and patches tailored to your MaxScale configuration


### MySQL NDB cluster support


Connection based routing to MySQL NDB clusters


### Updated installation path


MaxScale is now installed into `/usr/local/mariadb-maxscale`


## Bug Fixes


A number of bug fixes have been applied between the 1.0.5 GA and this GA release. The table below lists the bugs that have been resolved. The details for each of these may be found in [MXS](https://jira.mariadb.org/projects/MXS) or in the former [bugs.mariadb.com](https://bugs.mariadb.com) Bug database


|   |   |
| --- | --- |
| ID | Summary |
| MXS-80 | "show sessions" can crash MaxScale |
| MXS-79 | schemarouter hangs if client connects with empty database |
| MXS-78 | "USE" statement gives unpredictable/unexpected results |
| MXS-76 | core/dbusers.c needs better error messages |
| MXS-74 | Crash when no arguments given to on_queries clause |
| MXS-72 | dbfwfilter on_queries clause appears to be ignored |
| MXS-71 | dbfwfilter at_times clause seems to erroneously block user |
| MXS-68 | Wrong rule name in dbfwfilter leads to MaxScale crash |
| MXS-65 | Omitting <any|all|strict_all> in users directive causes crash in libdbfwfilter.so(link_rules) |
| MXS-63 | Maxkeys and Maxpasswd log to /tpm |
| MXS-57 | MaxScale should write a message to the error log when config is not found |
| MXS-54 | Write failed auth attempt to trace log |
| MXS-50 | Removing 1.0.5 RPM gives error about /etc/ld.so.conf.d/maxscale.conf |
| MXS-47 | Session freeze when small tail packet |
| MXS-5 | Possible memory leak in readwritesplit router |
| 736 | Memory leak while doing read/write splitting |
| 733 | Init-script deletes bin/maxscale |
| 732 | Build is broken: CentOS/RHEL 5 and SLES 11 |
| 730 | Regex filter and shorter than original replacement queries MaxScale |
| 729 | PDO prepared statements bug introduced in Maxscale 1.0.5 |
| 721 | Documentation suggests SIGTERM to re-read config file |
| 716 | $this->getReadConnection()->query('SET @id = 0;'); |
| 709 | "COPYRIGHT LICENSE README SETUP" files go to /usr/local/mariadb-maxscale/ after 'make package' |
| 704 | "make testall" returns success status (exit code 0) even on failures |
| 698 | Using invalid parameter in many maxadmin commands causes MaxScale to fail |
| 693 | Freeing tee filter's orphaned sessions causes a segfault when embedded server closes |
| 690 | CPU/architecture is hardcoded into debian/rules |
| 686 | TestService fails because of the modules used in it aren't meant for actual use |
| 677 | Race condition in tee filter clientReply |
| 676 | "Write to backend failed. Session closed." when changing default database via readwritesplit with max_slave_connections != 100% |
| 673 | MaxScale crashes if "Users table data" is empty and "show dbusers" is executed in maxadmin |
| 670 | Tee filter: statement router loses statements when other router gets enough ahead |
| 665 | Core: accessing freed memory when session is closed |
| 659 | MaxScale doesn't shutdown if none of the configured services start |
| 648 | use database is sent forever with tee filter to a readwrite split service |
| 620 | enable_root_user=true generates errors to error log |
| 612 | Service was started although no users could be loaded from database |
| 600 | RWSplit: if session command fails in some backend, it is not dropped from routing session |
| 587 | Hint filter don't work if listed before regex filter in configuration file |
| 579 | serviceStartProtocol test crashes |
| 506 | Don't write to shm/tmpfs by default without telling and without a way to override it |
| 503 | TOC in the bundled PDFs doesn't link to actual sections |
| 457 | Please provide a list of build dependencies for building MaxScale |
| 361 | file_exists() *modifies* the file it checks for??? |
| 338 | Log manager spread down feature is disabled |
| 159 | Memory leak. Dbusers are loaded into memory but not unloaded |


## Known Issues


There are a number bugs and known limitations within this version of MaxScale, the most serious of this are listed below.


* The Read/Write Splitter is a little too strict when it receives errors from slave servers during execution of session commands. This can result in sessions being terminated in situation in which MaxScale could recover without terminating the sessions.
* MaxScale can not manage authentication that uses wildcard matching in hostnames in the mysql.user table of the backend database. The only wildcards that can be used are in IP address entries.
* When users have different passwords based on the host from which they connect MaxScale is unable to determine which password it should use to connect to the backend database. This results in failed connections and unusable usernames in MaxScale.
* Service init script is missing after upgrade from 1.0 in RPM-based system. Can be fixed by reinstalling the package ('yum reinstall maxscale' or 'rpm -i --force /maxscale-1.1.rpm')
* Binlog Router Plugin is compatible with MySQL 5.6
 Binlog Router Plugin currently does not work for MariaDB 5.5 and MariaDB 10.0
* LONGBLOG are currently not supported.
* Galera Cluster variables, such as @@wsrep_node_name, are not resolved by the embedded MariaDB parser.
* The Database Firewall filter does not support multi-statements. Using them will result in an error being sent to the client.


## Packaging


Both RPM and Debian packages are available for MaxScale in addition to the tar based releases previously distributed we now provide


* CentOS/RedHat 5
* CentOS/RedHat 6
* CentOS/RedHat 7
* Debian 6
* Debian 7
* Ubuntu 12.04 LTS
* Ubuntu 13.10
* Ubuntu 14.04 LTS
* Fedora 19
* Fedora 20
* OpenSuSE 13
* SuSE Linux Enterprise 11
* SuSE Linux Enterprise 12


CC BY-SA / Gnu FDL

