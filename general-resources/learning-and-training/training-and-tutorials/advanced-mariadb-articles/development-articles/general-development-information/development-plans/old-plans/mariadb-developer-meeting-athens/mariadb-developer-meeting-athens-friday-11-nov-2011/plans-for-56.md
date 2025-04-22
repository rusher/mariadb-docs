
# Plans for 5.6

The information on this page is obsolete. Current information can be found on the **[Plans for 10x](../../plans-for-103.md)** page.
 
Also see the following blog posts:

* [](https://blog.mariadb.org/what-comes-in-between-mariadb-now-and-mysql-5-6/)


* [](https://blog.mariadb.org/explanation-on-mariadb-10-0/)




The following is a list of features considered for 5.6.


As soon as 5.3/5.5 is declared gamma we have to decode who will work on what
features for 5.6. All features that has a designed developer who agrees to get
the thing done in a given timeline will be considered as a 5.6 feature. Then
we will also create a new kb page with the to-be-done features.


The items below that have a name after them are already allocated to a
developer.


If you want to be part of developing any of these features, get
[an account](https://kb.askmonty.org/v/about) and add your name after the
feature you are interested in. You can also add new features to this list or
to the [worklog](../../../../../tools/worklog.md).


## [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3)


Features which will be in [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3) (instead of waiting until 5.6 to add them).


* Storage independent test suite (add to 5.3)
* OpenGIS: create required tables: GeometryColumns, related views. (Holyfoot) (move to 5.3)
* OpenGIS: stored procedure AddGeometryColumn (Holyfoot) (move to 5.3)


## [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)


Features which will be in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) (instead of waiting until 5.6 to add them).


* Present in MySQL 5.5: Performance Schema

  * what do we want to do with it, embrace it, extend it?
  * or it is better to have more SHOW commands and INFORMATION_SCHEMA tables?
  * are going to use Facebook's user stats/index stats patch or create a PERFORMANCE_SCHEMA-based solution? (MP + Percona)
  * Not much we can do to improve it for 5.6


* FB request: log all SQL errors (Holyfoot to do in 5.5); [MWL#177](https://askmonty.org/worklog/?tid=177)
* FB request: EXPLAIN the *actual* plan on a *running* statement; no progress indicators and numbers are needed; [MWL#182](https://askmonty.org/worklog/?tid=182) (In Progress) (spetrunia)
* Thread pool (Wlad) (5.5)
* Memory tables: VARCHAR and BLOB support (Have sponsor; Will be implemented for 5.5) (monty)
* Plugins by Sergey: INSTALL PLUGIN * ([MWL#77](https://askmonty.org/worklog/?tid=77)) (done but not pushed) (will be in 5.5) (sergey)
* LGPL/BSD client library (MP) (done in 5.5)

  * Need to build it outside the tree as a separate package that people can use


## [MariaDB 5.6](/kb/en/what-is-mariadb-56/) Definite


Features which will definitely be in [MariaDB 5.6](/kb/en/what-is-mariadb-56/)


* FB request: Better monitoring for replication (FB has patch; MP will add) (kristian) (for 5.5 or 5.6)
* Aria: Concurrent UPDATE & DELETE. [MWL#235](https://askmonty.org/worklog/?tid=235) (Have partial sponsor) (monty) (will do before April)
* Aria: Segmented key cache for Aria (igor) (definitely before 5.7)
* Aria: Fast next not same (monty) (will be done for 5.6)
* From MySQL 5.6: Global transaction ID, so the slave state becomes recoverable, and facilitate automatic moving a slave to a new master across multi-level hierarchies.


## [MariaDB 5.6](/kb/en/what-is-mariadb-56/) High Probability


Features which have a high probability of being in [MariaDB 5.6](/kb/en/what-is-mariadb-56/)


* Performance: More scalable query cache under higher concurrency (Sanja) (maybe)

  * Allow stale data (Sanja) (maybe)


## [MariaDB 5.6](/kb/en/what-is-mariadb-56/) Rolling


Features which will be added when they are ready.


* Parameterized Views
* Percona patches (Monty & Sanja) (rolling feature)


## Will skip for 5.6


Features which will not be added to [MariaDB 5.6](/kb/en/what-is-mariadb-56/).


* Community Request: prevent full scans from running at all above a certain table size;

  * is existing `max-join-size` variable sufficient or more granula control is needed?
* Optimizer: Implement UNION ALL without usage of a temporary table (nice to have) (wait for sponsor)
* Federated: Generic query pushdown
* Federated: Apply it to federated
* Federated: Timour's old list of tasks (Timour)
* Table functions (Timour) (after 5.6)
* Refactoring: do_select refactoring to remove if's and make each code group (like end_select) smaller (small speedup and cleaner code)


## Uncategorized


Features which have not been categorized into the above categories.


### OpenGIS compliance


* OpenGIS: prefill the spatial_ref_sys table. (Holyfoot)
* OpenGIS: Add possible III-rd coordinate (Altitude). (Holyfoot)
* OpenGIS: Distance3D, related optimization.
* OpenGIS: Precise math coordinates instead of DOUBLE-s.


### GIS-Optimizer


* optimize simple queries with Intersects(), Within, Distance()<X
* add Distance_sphere() and the related optimization.


### Online operations


* Extension to bigger datatype (var)char(n) (n+x)
* Online extension of any NUMERIC datatype ; Like ALTER tinyint -> smallint
* Extend ENUM done need more visibility
* Alter comment (Monty)
* Online Add and drop index (Drop is easy to implement MyISAM/ARIA)
* Online OPTIMIZE
* Online ANALYSE
* Add ALTER ONLINE TABLE (Done by Monty: Syntax added in 5.3; When ONLINE is used, one gets an error if the ALTER TABLE can't be done online)
* Look at patch for online backport sent to maria-developers


### COMPATIBILITY & USABILITY


* Date & time embedded timezone (Need sponsor)
* IPV6 native type

  * Functions ; Functions exists in public patch (MP)
  * Datatype ;Old patch exists
* Extended timestamp > 2038
* 1M tables Information schema (MP will investigate)
* 1M users requirements

  * Roles
* mysql.* in any engine
* LOG tables in a log_schema schema
* User Ldap Authentification like Drizzle
* Make openssl hash functions available for user. (Bank will sponsor)
* Query logging and summary per query [MWL#179](https://askmonty.org/worklog/?tid=179)
* Auditing for specific user (to general log)
* Flush and reload variables from my.cnf


### Replication


* Replication filters, like `--replicate-do-db` and friends, need to be possible to change dynamically, without having to restart the server. Having to stop the slave should ideally also not be needed, but is less of a problem.
* Transactional storage of slave state, rather than file-based master.info and relay-log.info . So the slave can recover consistently after a crash.
* Support in global transaction ID for master_pos_wait()
* Hooks around rotation of the binlog, so user can configure shell commands
 when a new log is started and when it is ended. The command must be run
 asynchroneously, and get the old and new log file name as arguments.
* Reduce fsyncs from 3 to 1 in group commit with binary log ([MWL#164](https://askmonty.org/worklog/?tid=164))
* Parallel applying of binary log in slave ([MWL#169](https://askmonty.org/worklog/?tid=169))
* Replication APIs, as per [MWL#107](https://askmonty.org/worklog/?tid=107) (Needs sponsor)

  * Most important [MWL#120](https://askmonty.org/worklog/?tid=120) and [MWL#133](https://askmonty.org/worklog/?tid=133), for obtaining and applying events.
  * Then a mechanism for prioritizing transactions.
* Multi source (Slave can have multiple masters). [MWL#201](https://askmonty.org/worklog/?tid=201). There is a partial sponsorship for this already. (Monty and Kristian)


### Statistics and monitoring


* Strategic direction: Enterprise monitoring

  * graphing and data aggregation tools, server monitoring, etc.
  * customer has reported that Merlin is inadequate, should we enter into
this market? (MonYog, SkySQL, Percona, Oli Sennhauser, Open Query etc is doing tools)


* QA request: better EXPLAIN (HIGH priority; MP; Spetrunia)

  * required in order to debug performance issues in queries without knowing
the query or the data;
  * the customer will only provide EXPLAIN and SHOW output, we need to debug
based on that; (need examples)
  * Perhaps optimizer trace is what we need


* QA request: engine independent PERSISTENT TABLE STATISTICS (Igor)

  * required to ensure repeatable query execution for InnoDB;
  * may allow various statistics to be reported by the server regardless of engine;
  * able to simulate different sized tables


* U/C at Oracle: OPTIMIZER tracing 
spetrunia: report actual estimates, and all decisions of the optimizer,
including why an index was *not* picked, etc.

  * want to change for 5.7


* FB request: more options for controlling the slow query log [MWL#181](https://askmonty.org/worklog/?tid=181) (Holyfoot will check)

  * sample one out of every N queries or transactions ; with N ~ 99 (Patch by FB; Will be changed to use AUDIT)
* idea: collect statistics per query text, or normalized query text and report;


* request by community: progress bar for SELECT;

  * how to estimate the total running time of the query;
  * Percona has [support for this](https://www.mysqlperformanceblog.com/2011/03/13/percona-server-and-xtrabackup-weekly-news-march-12th)
  * 5.3 has progress reporting for SHOW PROGRESS PROCESSLIST; SHOW QUERY PROGRESS; and LOAD DATA
.
* FB request: limit total temptable size on the server (MP) [MWL#183](https://askmonty.org/worklog/?tid=183)


* FB patch: Admission Control (MP) (seriously considered to be done) (wlad)

  * limit number of concurrently running queries per user;
  * if all user queries are blocked, allow a few more queries to join;


* Integration with log watching tools

  * alter log formats to make them compatible with tools;
  * include logwatch mysql-specific config file in packages/distributions;


**a counter for the total number of bytes read by I/O thread that does not rotate on log rotation;** "seconds behind real master" to report the actual time the slave I/O thread is behind (MP will look into this)


* FB patch: report the time spent in individual phases of query processing (MP)


### Optimizer


* Put cost related constants into variables (will be done) (timour)

  * Automatic tuning of cost constants for specific setup (SSD / TAPE)
* Make optimizer switch more user friendly (Sanja and Spetrunia) (will be done)
* Cost model cleanup (Don't assume things are B-trees) (timour)

  * Consistent cost interface trough handler methods


* Persistent data statistics (Igor)
* Grace HASH join (Need sponsor)
* Sort merge join (Need sponsor)
* Better item_equal (Igor & Monty)

  * missing item_equal for ORDER BY and GROUP BY
* Less fetches of data pages.

  * can use whenever you have many-to-many relationships between two tables
  * use to try to minimize data access
  * it's like INDEX INTERSECTION


### Performance:


* Performance: Better multi CPU performance above 16 cores (Work with Intel)
* Performance: Predictive parser to replace yacc based ; 5 % speedup for simpler queries
* Performance: Faster WHERE (a,b) in ((1,2),(2,3)...huge list...) (customer request)
* Performance: Faster VIEW (Not open frm & parse query for every access); Speed up simple view handling 2x


### Aria


* MIN/MAX indexes
* Index withing key pages to speed up lookup on compressed key pages.


### User friendly features


* Better/safer upgrade (?)
* Better option files in distributions.
* UNIQUE CONSTRAINT for BLOB ([MWL#139](https://askmonty.org/worklog/?tid=139)) (medium)


### Other things


* Enhance RQG to test for query correctness and performance on production workloads during upgrade ([MWL#178](https://askmonty.org/worklog/?tid=178)) (prototype done, need to get outside users to verify the code)


### Plugins by Sergey


* Plugins by Sergey: query rewrite ([MWL#144](https://askmonty.org/worklog/?tid=144))
* Plugins by Sergey: full-text search engine plugin ([MWL#143](https://askmonty.org/worklog/?tid=143))
* Plugins by Sergey: Plugin Loader ([MWL#162](https://askmonty.org/worklog/?tid=162))
* Plugins by Sergey: smaller, nice to have, tasks:

  * show plugins soname ... ([MWL#80](https://askmonty.org/worklog/?tid=80))
  * mutex/condition service ([WL#83](https://askmonty.org/worklog/?tid=83))
  * duplicate plugin names ([MWL#79](https://askmonty.org/worklog/?tid=79))
  * create a charset service ([MWL#81](https://askmonty.org/worklog/?tid=81))

