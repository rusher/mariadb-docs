# MaxScale 1.0.1 Beta New Features

1.0.1 Beta

This document details the changes in version 1.0.1 since the release of the 1.0 beta of the MaxScale product.

## New Features

### CMake build system

Building MaxScale is now easier than ever thanks to the introduction of CMake into the build process. Building with CMake removes the need to edit files, specify directory locations or change build flags, in all but the rarest of the cases, and building with non-standard configurations is a lot easier thanks to the easy configuration of all the build parameters.

Here’s a short list of the most common build parameters,their functions and default values.

|                        |                                                                                                               |                            |
| ---------------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------- |
| Variable               | Purpose                                                                                                       | Default value              |
| INSTALL\_DIR           | Root location of the MaxScale install                                                                         | /usr/local/skysql/maxscale |
| STATIC\_EMBEDDED       | Whether to use the static or the dynamic version of the embedded library                                      | No                         |
| OLEVEL                 | Level of optimization used when compiling                                                                     | No optimization            |
| INSTALL\_SYSTEM\_FILES | If startup scripts should be installed into /etc/init.d and ldconfig configuration files to /etc/ld.so.conf.d | Yes                        |
| BUILD\_TYPE            | The type of the build. ‘None’ for normal, ‘Debug’ for debugging and ‘Optimized’ for an optimized build.       | None                       |

Details on all the configurable parameters and instructions on how to use CMake can be found in the README file.

### Enhancements

The polling mechanism in MaxScale has been modified to overcome a flaw which mean that connections with a heavy I/O load could starve other connections within MaxScale and prevent query execution. This has been resolved with a more fairer event scheduling mechanism within the MaxScale polling subsystem. This has led to improve overall performance in high load situations.

## Bug Fixes

A number of bug fixes have been applied between the 1.0 beta release and this release candidate. The table below lists the bugs that have been resolved. The details for each of these may be found in bugs.skysql.com.

|     |                                                                                                  |
| --- | ------------------------------------------------------------------------------------------------ |
| ID  | Summary                                                                                          |
| 462 | Testall target fails in server/test to invalid MAXSCALE\_HOME path specification                 |
| 467 | max\_slave\_replication lag is not effective after session creation                              |
| 468 | query\_classifier : if parsing fails, parse tree and thread context are freed but used           |
| 469 | rwsplit counts every connection twice in master - connection counts leak                         |
| 466 | hint\_next\_token doesn't detect = pair if there are no spaces around '='                        |
| 470 | Maxscale crashes after a normal query if a query with named hint was used before                 |
| 473 | Entering a hint with route server target as '=(' causes a crash                                  |
| 472 | Using a named hint after its initial use causes a crash                                          |
| 471 | Routing Hints route to server sometimes doesn't work                                             |
| 463 | MaxScale hangs receiving more than 16K in input                                                  |
| 476 | mysql\_common.c:protocol\_archive\_srv\_command leaks memory and accesses freed memory           |
| 479 | Undefined filter reference in maxscale.cnf causes a crash                                        |
| 410 | maxscale.cnf server option is not parsed for spaces                                              |
| 417 | Galera monitor freezes on network failure of a server                                            |
| 488 | SHOW VARIABLES randomly failing with "Lost connection to MySQL server"                           |
| 484 | Hashtable does not always release write lock during add                                          |
| 485 | Hashtable not locked soon enough in iterator get next item                                       |
| 493 | Can have same section name multiple times without warning                                        |
| 510 | Embedded library crashes on a call to free\_embedded\_thd                                        |
| 511 | Format strings in log\_manager.cc should be const char\*                                         |
| 509 | rw-split sensitive to order of terms in field list of SELECT                                     |
| 507 | rw-split router does not send last\_insert\_id() to master                                       |
| 490 | session handling for non-determinstic user variables broken                                      |
| 489 | @@hostname and @@server\_id treated differently from @@wsrep\_node\_address                      |
| 528 | Wrong service name in tee filter crashes maxscale on connect                                     |
| 530 | MaxScale socket permission                                                                       |
| 536 | log\_manager doesn't write buffers to disk in the order they are written                         |
| 447 | Error log is flooded with same warning if there are no slaves present                            |
| 475 | The end comment tag in hints isn't properly detected.                                            |
| 181 | Missing log entry if server not reachable                                                        |
| 486 | Hashtable problems when created with size less than one                                          |
| 516 | maxadmin CLI client sessions are not closed?                                                     |
| 495 | Referring to a nonexisting server in servers=... doesn't even raise a warning                    |
| 538 | maxscale should expose details of "Down" server                                                  |
| 539 | MaxScale crashes in session\_setup\_filters                                                      |
| 494 | The service 'CLI' is missing a definition of the servers that provide the service                |
| 180 | Documentation: No information found in the documentation about firewall settings                 |
| 524 | Connecting to MaxScale from localhost tries matching @127.0.0.1 grant                            |
| 481 | MySQL monitor doesn't set master server if the replication is broken                             |
| 437 | Failure to detect MHA master switch                                                              |
| 541 | Long queries cause MaxScale to block                                                             |
| 492 | In dcb.c switch fallthrough appears to be used without comment                                   |
| 439 | Memory leak in getUsers                                                                          |
| 545 | RWSplit: session modification commands weren't routed to all if executed inside open transaction |
| 543 | RWSplit router statistics counters are not updated correctly                                     |
| 544 | server with weight=0 gets one connection                                                         |
| 525 | Crash when saving post in Wordpress                                                              |
| 533 | Drupal installer hangs                                                                           |
| 497 | Can’t enable debug/trace logs in configuration file                                              |
| 430 | Temporary tables not working in MaxScale                                                         |
| 527 | No signal handler for segfault etc                                                               |
| 546 | Use of weightby router parameter causes error log write                                          |
| 506 | Don’t write shm/tmpfs by default without telling the user or giving a way to override it         |
| 552 | Long argument options to maxadmin and maxscale broke maxadmin commands                           |
| 521 | Many commands in maxadmin client simply hang                                                     |
| 478 | Parallel session command processing fails                                                        |
| 499 | make clean leavessoem .o files behind                                                            |
| 500 | "depend: no such file warnings during make                                                       |
| 501 | log\_manager, query classifier rebuilds unconditionally                                          |
| 502 | log\_manager and query\_classifier builds always rebuild utils                                   |
| 504 | clean rule for Documentation directory in wrong makefile                                         |
| 505 | utils/makefile builds stuff unconditionally, misses "depend" target                              |
| 548 | MaxScale accesses freed client DCB and crashes                                                   |
| 550 | modutil functions process length incorrectly                                                     |

## Packaging

Both RPM and Debian packages are available for MaxScale in addition to the tar based releases previously distributed we now provide

* CentOS/RedHat 5 RPM
* CentOS/RedHat 6 RPM
* Ubuntu 14.04 package

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
