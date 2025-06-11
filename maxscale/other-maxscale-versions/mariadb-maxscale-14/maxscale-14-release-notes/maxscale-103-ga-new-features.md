# MaxScale 1.0.3 GA New Features

1.0.3 GA

This document details the changes in version 1.0.3 since the release of the 1.0.2 Release Candidate of the MaxScale product.

## New Features

No new features have been introduced since the released candidate was released.

## Bug Fixes

A number of bug fixes have been applied between the 0.6 alpha and this alpha release. The table below lists the bugs that have been resolved. The details for each of these may be found in bugs.mariadb.com.

|     |                                                                                                                                                                  |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID  | Summary                                                                                                                                                          |
| 644 | Buffered that were cloned using the gwbuf\_clone routine failed to initialise the buffer lock structure correctly.                                               |
| 643 | Recursive filter definitions in the configuration file could cause MaxScale to loop                                                                              |
| 665 | An access to memory that had already been freed could be made within the MaxScale core                                                                           |
| 664 | MySQL Authentication code could access memory that had already been freed.                                                                                       |
| 673 | MaxScale could crash if it had an empty user table and the MaxAdmin show dbusers command was run                                                                 |
| 670 | The tee filter could lose statement on the branch service if the branch service was significantly slower at executing statements compared with the main service. |
| 653 | Memory corruption could occur with extremely long hostnames in the mysql.user table.                                                                             |
| 657 | If the branch service of a tee filter shutdown unexpectedly then MaxScale could fail                                                                             |
| 654 | Missing quotes in MaxAdmin show dbusers command could cause MaxAdmin to crash                                                                                    |
| 677 | A race condition existed in the tee filter client reply handling                                                                                                 |
| 658 | The readconnroute router did not correctly close sessions when a backend database failed                                                                         |
| 662 | MaxScale startup hangs if no backend servers respond                                                                                                             |
| 676 | MaxScale writes a log entry, "Write to backend failed. Session closed." when changing default database via readwritesplit with max\_slave\_connections != 100%   |
| 650 | Tee filter does not correctly detect missing branch service                                                                                                      |
| 645 | Tee filter can hang MaxScale if the read/write splitter is used                                                                                                  |
| 678 | Tee filter does not always send full query to branch service                                                                                                     |
| 679 | A shared pointer in the service was leading to misleading service states                                                                                         |
| 680 | The Read/Write Splitter can not load users if there are no databases available at startup                                                                        |
| 681 | The Read/Write Splitter could crash is the value of max\_slave\_connections was set to a low percentage and only a small number of backend servers are available |

## Known Issues

There are a number bugs and known limitations within this version of MaxScale, the most serious of this are listed below.

* The SQL construct "LOAD DATA LOCAL INFILE" is not fully supported.
* The Read/Write Splitter is a little too strict when it receives errors from slave servers during execution of session commands. This can result in sessions being terminated in situation in which MaxScale could recover without terminating the sessions.
* MaxScale can not manage authentication that uses wildcard matching in hostnames in the mysql.user table of the backend database. The only wildcards that can be used are in IP address entries.
* When users have different passwords based on the host from which they connect MaxScale is unable to determine which password it should use to connect to the backend database. This results in failed connections and unusable usernames in MaxScale.

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

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
