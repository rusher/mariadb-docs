
# Storage Engine Summit 2010

**Note:** This page is obsolete. The information is old, outdated, or otherwise currently incorrect. We are keeping the page for historical reasons only. **Do not** rely on the information in this article.



Storage Engine Summit is a traditional yearly one-day meeting of Storage Engine
vendors, typically held right after the MySQL User Conference.


In 2010 it was organized by [Monty Program Ab](https://montyprogram.com).


## Location


The [Network Meeting Center](https://www.networkmeetingcenter.com/) - across
the street from the Convention Center. ([map](https://goo.gl/D0ru))


## Date and Time


Friday April 16, 2010 - 9:00 a.m. to 6:30 p.m.


## Audience


Invited were all MySQL/MariaDB Storage Engine vendors and anyone interested in
the MySQL/MariaDB Storage Engine API.


There were about 25 participants from MariaDB, Oracle, and eight storage engine
vendors.


## Meeting Minutes


### Presenting Monty Program Ab 1

Unlike Drizzle, MariaDB will stay fully compatible with MySQL (for a while)
MariaDB is GPL only
**Monty:** But we want to evolve the interface.
**Mikael:** It is a bad idea for MariaDB to compete on new APIs as there is a need for a single standard rather than competing APIs.
**Sergei:** Totally agree, we want to improve the API, but stay compatible
MariaDB 5.2 released, good progress with MariaDB 5.3
We do NRE


### Upcoming changes in the Storage Engine API 2

CREATE TABLE extensions in MariaDB 5.2.0 3
**Question:** Are there per-partition attributes?
**Sergei:** No, it's a bug, we will add them in 5.2.1
Performance Schema in MySQL 5.5 4,5
**Mikael:** InnoDB has added probes for this in MySQL 5.5.4
Transactional LOCK TABLES
**Question:** What if the engine does not support it?
**Sergei:** No problem, it's an optional feature, if not supported MySQL will use old style table locks
Multi Read Range (MRR) and how it is used in Batch Key Access (BKA) 6
**Question:** Isn't it in MySQL 5.1?
**Igor Babaev:** No, the interface in MariaDB 5.3 is different, more generic
Server Services for Plugins 7
**Paul McCullah:** Plugins need some "magic autoconf code" to detect whether libservices should be used (to support both MariaDB 5.1 and 5.2)
Query Fragment Pushdown 8
**Mikael:** It is in MySQL in a working tree
**Sergei:** Yes, but it's we are talking about a much more general approach here


### Discussion: What Storage Engine needs

Query Fragment Pushdown:
Sub-problems:


* Abstract Query Tree (AQT) or query and database model ([MySQL Worklog #4533](https://dev.mysql.com/worklog/task/?id=4533))
* Storage Engine Pushdown API ([MySQL Worklog #4535](https://dev.mysql.com/worklog/task/?id=4535))
* Virtual Tables ([MySQL Worklog #4537](https://dev.mysql.com/worklog/task/?id=4537))
* Query decomposition and optimization for query fragments ([MySQL Worklog #4536](https://dev.mysql.com/worklog/task/?id=4536))
* Cost mode calibration ([MySQL Worklog #4553](https://dev.mysql.com/worklog/task/?id=4553))


**Question:** Some engines has extra knowledge, like for example some materialised views. Would it be possible to make these available as extra tables for the MySQL optimiser?
**Kostja:** *You can already do this today, similar to how the merge tables work*
**Jonas:** *We thought about it when designing for NDB. It is much easier to implement, but the "real" solution is much better.*
**Timour:** *The basic framework is only 30% of the full problem. The main part is the query optimisation, and that can be developed incrementally once the rest of the framework is in place.*
**Comment:** *Storage engines do not want to have to implement their own optimiser inside the engine.*
**Sergei:** *But if there is one, it should be possible to use it.*
**Timour:** *We are trying to implement a general solution that makes multiple engines happy. The optimiser should be cost based rather than rule based to cover a general set of cases well.*
**Comment:** *It should be simple by engines such as Spider, Federated to re-construct an SQL query from the proposed representation.*
Majority feels that Query re-write is not realistic to work on due to dependency on highly complex internal data structures.
Range Pushdown for all columns
**Sergei:** *These can be derived from a query pushdown*
**Comment:** *As a separate feature it's much easier to implement and to use*9
Online Backup
Engines want it
Perhaps backport it from MySQL 6.0 ?
Table discovery enhancements
**Sergei:** *There was a patch from Google Summer of Code that included enhanced discovery. MySQL now works on that feature, using the patch as a starting point.*
Parallel query execution across multiple cores
**Sergei:** *Parallel query execution is a general feature, and although it would be nice to have it, it is not directly relevant to this storage engine summit discussion.*
Support in the optimiser for clustering non-primary keys
HA_EXTRA_WRITE_CAN_IGNORE hint
Consolidate the range query apis
Make sure the range boundaries are always sent to the engine (in order by desc, JT_REF, rnd_*, etc)
Transactional DDL
**Comment:** *We do not really need full transactions, just crash recovery.*
**Monty:** *For partial DDL, what we can do is log DDL changes, to be able to recover things after a crash.*
**Mikael:** *There is this already in 5.1 for partitions. But it is only for partitions, not for the tables.*
Monty is willing to write specs for crash-safe DDL
Smarter "ALTER TABLE"
**Comment:** *Need to fix ALTER TABLE to fully support online operations.*
**Jonas:** *This is already implemented, but currently only in the -telco cluster trees.*
Antony is willing to look into backporting new ALTER TABLE to MariaDB
Fast, engine-specific LOAD DATA
Certain engines are so fast for bulk inserts that server adds too much overhead
Faster export (SELECT ... OUTFILE)
Same as with LOAD DATA
Can be done with a special Protocol class or select_result class ?
Engine-provided SQL commands. EXECUTE COMMAND maybe?
**Comment:** *Want to be able to make/extend SHOW ENGINE xxx STATUS*
**Sergei:** *No need, create an INFORMATION_SCHEMA table instead.*
InnoDB statistics in the slow log
Perhaps, audit api can be used for that ?
Engine independent test suite
**Sergei:** *This was presented by Sun on the Storage Engine Summit last year, but no trace has been seen of it ever since*
Paul described how it is done in Drizzle, an engine can override a .result file
An author of the Spider engine started recently a new project [Engine Independent Test for MySQL](https://launchpad.net/engineindependenttestformysql) - we all can collaborate and extend it
**Comment:** *What about unit tests for the storage engine API?*
Need a unit test that loads a storage engine plugin and exercises every call in it.
**Sergei:** *this is also something that Sun tried to do10*


### Conclusions


Few simple feature requests we can do straight away:


* many clustered keys (not only primary) - [MWL#113](https://askmonty.org/worklog/?tid=113)
* insert ignore ha_extra hint - [MWL#114](https://askmonty.org/worklog/?tid=114)
* consolidating the range query apis
* innodb statistics in the slow log - [MWL#115](https://askmonty.org/worklog/?tid=115)


We will work together to create an engine independent test suite - all engines
will benefit from it.


More complex features are open. Monty Program will be happy to do them as
NREs or discuss alternative ways of collaborating on having them implemented.


### References



1. MariaDB, Monty Program, Collaboration by Henrik Ingo ([slides, odp](https://askmonty.org/w/images/3/3a/MP_intro_SE_summit.odp))
1. Storage Engine API: Beyond 5.1 by Sergei Golubchik ([slides, zipped html](https://askmonty.org/w/images/b/b8/SE_API_Beyond_5.1.maff))
1. CREATE TABLE extension [manual](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/storage-engines-storage-engine-development/engine-defined-new-tablefieldindex-attributes)
1. Performance Schema [manual](https://dev.mysql.com/doc/performance-schema/en/index.html)
1. Marc Alff's
[MySQL
University session](https://forge.mysql.com/wiki/Performance_Schema:_Instrumenting_Code) about the instrumentation.
1. See
slides 10-18 from the Sergey Petrunya's [MySQL UC2010 talk](https://en.oreilly.com/mysql2010/public/schedule/detail/13509)
1. Server Services in the
[MySQL manual](https://dev.mysql.com/doc/refman/5.5/en/plugin-services.html)
1. Query Fragment Pushdown Design by Timour Katchaounov ([slides, pdf](https://askmonty.org/w/images/4/47/Qfpd-query-model-design.pdf))
1. post-conference, a quick patch was made for this functionality: [msg02961.html](https://lists.launchpad.net/maria-developers/msg02961.html)
1. [Storage_Engine_API_Testing_Framework](https://forge.mysql.com/wiki/Storage_Engine_API_Testing_Framework)




CC BY-SA / Gnu FDL

