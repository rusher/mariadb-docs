
# MariaDB Plans - Statistics and Monitoring

**Note:** This page is obsolete. The information is old, outdated, or otherwise currently incorrect. We are keeping the page for historical reasons only. **Do not** rely on the information in this article.



Notes from the Statistics and Monitoring group:


* Strategic direction: Enterprise monitoring

  * graphing and data aggregation tools, server monitoring, etc.
  * customer has reported that Merlin is inadequate, should we enter into
this market?


* QA request: better EXPLAIN:

  * required in order to debug performance issues in queries without knowing
the query or the data;
  * the customer will only provide EXPLAIN and SHOW output, we need to debug
based on that;


* QA request: PERSISTENT TABLE STATISTICS

  * required to ensure repeatable query execution for InnoDB;
  * may allow various statistics to be reported by the server regardless of
engine;


* U/C at Oracle: OPTIMIZER tracing
spetrunia: report actual estimates, and all decisions of the optimizer,
including why an index was *not* picked, etc.


* Developed by Serg for [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3): Phone Home
todo: make a web page on mariadb.org showing the results from the data
being collected;
pstoev: do we need to allow people to run their own reporting servers;


* Present in MySQL 5.5: Performance Schema

  * what do we want to do with it, embrace it, extend it?
  * or it is better to have more SHOW commands and INFORMATION_SCHEMA tables?
  * are going to use Facebook's user stats/index stats patch or create a
PERFORMANCE_SCHEMA-based solution?


* FB request: log all SQL errors

  * serg: possible via AUDIT plugin, must back-port audit infrastructure from
MySQL 5.5


* FB request: more options for controlling the slow query log

  * sample one out of every N queries or transactions ; with N ~ 99
  * filter queries based on rows examined, I/O performed, total lock wait
time;


* idea: collect statistics per query text, or normalized query text and
report;


* FB request: EXPLAIN the *actual* plan on a *running* statement; no
progress indicators and numbers are needed;


* request by community: progress bar for queries such as LOAD DATA and
SELECT;

  * something like SHOW PROGRESS PROCESSLIST ; SHOW QUERY PROGRESS;
  * what numbers are to be reported? time to elapsed, time to completion,
number of rows processed?
  * how to estimate the total runing time of the query;


* FB request: limit total temptable size on the server; Already available
per-query, but per-server needed;


* FB patch: Admission Control

  * limit number of concurrently running queries per user;
  * if all user queries are blocked, allow a few more queries to join;


* Kurt: Integration with log watching tools

  * alter log formats to make them compatible with tools;
  * include logwatch mysql-specific config file in packages/distributions;


* FB request: Better monitoring for replication:

  * seconds_behind_master computation is incorrect, sometimes is zero
  * a counter for the total number of bytes read by I/O thread that does not
rotate on log rotation;
  * "seconds behind real master" to report the actual time the slave I/O
thread is behind;


* community request: prevent full scans from running at all above a certain
table size;

  * is existing max-join-size variable sufficient or more granula control is
needed?


* FB patch: report the time spent in individual phases of query processing

