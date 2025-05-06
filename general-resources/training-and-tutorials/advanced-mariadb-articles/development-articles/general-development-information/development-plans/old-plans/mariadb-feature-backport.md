
# MariaDB Feature Backport

**Note:** This page is obsolete. The information is old, outdated, or otherwise currently incorrect. We are keeping the page for historical reasons only. **Do not** rely on the information in this article.



## Some background


If case you didn't know:


### What features were in 6.0


Features that were in 6.0 and that we can rescue from there and provide value
for the users:


* MRR+BKA

  * There are known bugs in the implementation of MRR/InnoDB (but not in
 MRR/Maria or MRR/MyISAM) which has caused Oracle to request a patch that
 disables MRR/InnoDB, which SergeyP has given them this May.
  * BKA itself was used by a customer with a proprietary engine, and also by
 NDB, so can be assumed tested.


*note: unless said otherwise, by MRR we mean MRR and ICP, everywhere*


* The first two batches of subquery optimizations:
* [MySQL Worklog #2980](https://dev.mysql.com/worklog/task/?id=2980): Subquery optimization: Semijoin

  * [MySQL Worklog #3740](https://dev.mysql.com/worklog/task/?id=3740): Subquery optimization: Semijoin: Pull-out of inner tables
  * [MySQL Worklog #3741](https://dev.mysql.com/worklog/task/?id=3741): Subquery optimization: Semijoin: Duplicate elimination strategy
  * [MySQL Worklog #3750](https://dev.mysql.com/worklog/task/?id=3750): Subquery optimization: Semijoin: First-match strategy
  * [MySQL Worklog #3751](https://dev.mysql.com/worklog/task/?id=3751): Subquery optimization: Semijoin: Inside-out strategy
* [MySQL Worklog #1110](https://dev.mysql.com/worklog/task/?id=1110): Subquery optimization: Materialization
* [MySQL Worklog #3985](https://dev.mysql.com/worklog/task/?id=3985): Subquery optimization: smart choice between semi-join and
 materialization


* Semi-join optimizations, including semi-join materialization has issues:

  * The "outer join and semi-join problem"
  * The different-datatypes-comparison problem


* Subquery optimizations rely on the following WLs to be present in the tree:

  * [MySQL Worklog #4165](https://dev.mysql.com/worklog/task/?id=4165) Prepared statements: validation
  * [MySQL Worklog #4166](https://dev.mysql.com/worklog/task/?id=4166) Prepared statements: automatic re-prepare


### Related unfinished 6.x tasks


There are also unfinished tasks, in various degrees of public availability and readyness:


* [MySQL Worklog #3485](https://dev.mysql.com/worklog/task/?id=3485): Subquery optimization: FROM (SELECT) (Evgen)
* [MySQL Worklog #4389](https://dev.mysql.com/worklog/task/?id=4389): Subquery optimizations: Make IN optimizations also handle EXISTS (Roy Lyseng)
* [MySQL Worklog #3830](https://dev.mysql.com/worklog/task/?id=3830): Subquery optimization: Materialization: Partial matching of tuples with NULL components (Timour)


* [MySQL Worklog #4800](https://dev.mysql.com/worklog/task/?id=4800): Optimizer trace/debugger
* : (this is an utitlity task that might be useful for implementation of some
 of the other WLs. SergeyP has already ported it to MariaDB for such utility
 purposes, but its code is not ready for being pushed yet.


### Directions for improvement


Some (but not all) of the following might be needed to make a well-rounded
release:


* [No WL]: Single table "UPDATE/DELETE one_table WHERE
 subquery_predicate"<br/>such query will not be executed by semi-join runtime.
 Ironically, multi-table UPDATE/DELETEs will be, so not multi-table UPDATEs
 may work faster than single-table.
* [MySQL Worklog #3341](https://dev.mysql.com/worklog/task/?id=3341): Subquery optimization: Shortcut the evaluation as soon as there is a match
* [MySQL Worklog #1117](https://dev.mysql.com/worklog/task/?id=1117): Subquery optimization: Avoid recalculating subquery if external fields have not changed
* [MySQL Worklog #4614](https://dev.mysql.com/worklog/task/?id=4614): Subquery optimization: Materialization: avoid double subquery materialization
* [MySQL Worklog #3490](https://dev.mysql.com/worklog/task/?id=3490): Subquery optimization: Subqueries and multiple columns comparison with ALL
* [MySQL Worklog #4690](https://dev.mysql.com/worklog/task/?id=4690): Insideout order for materialized non-semijoin subqueries at top-level of the WHERE
* [MySQL Worklog #3808](https://dev.mysql.com/worklog/task/?id=3808): Subquery optimization: Materialize and use as ranges for MRR scan of outer tables
* [MySQL Worklog #4245](https://dev.mysql.com/worklog/task/?id=4245): Subquery optimization: FirstMatch strategy for anti-semi-join
* [MySQL Worklog #3489](https://dev.mysql.com/worklog/task/?id=3489): Subquery optimization: Subquery and loose index scan
* [MySQL Worklog #4691](https://dev.mysql.com/worklog/task/?id=4691): Subqueries: No-startup-cost execution for SJ-Materialization-Scan
* [No WL#]: Support ORDER BY .. LIMIT clause within a subquery (a quite common user request).


* [No WL]: Make the join optimizer take BKA into account


## Feature-wise plan for 5.4


The following is the "Igor's list":


```
1. MRR/ICP
 ---------------
 WL#2474: Batched range read handler functions
 WL#2475: Batched range read functions for MyISAM/InnoDB
 2. BKA
 ---------
 WL #2771: Usage of multi_read_range in nested loop join
 3. Metadata integrity
 -------------------------
 WL #4284 (bug #989): Transactional DDL locking
 WL#4165: Prepared statements: validation
 WL#4166: Prepared statements: automatic re-prepare
 4. Subqueries
 -----------------
 4.1 Materialization of non-correlated IN subqueries
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 WL #1110: Materialization
 WL #4614: Materialization: avoid double subquery materialization
 WL #4690: Insideout order for materialized non-semijoin subqueries at top-level  of the WHERE
 4.2. Semi-joins
 ~~~~~~~~~~~
 WL #3740: Subquery optimization: Semijoin: Pull-out of inner tables
 WL #3741: Subquery optimization: Semijoin: Duplicate elimination strategy
 WL #3750: Subquery optimization: Semijoin: Duplicate elimination strategy
 WL #3751: Subquery optimization: Semijoin: Inside-out strategy
 4.3. Smart choice between materialization and semi-join
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 WL #3985: Subquery optimization: smart choice between semi-join and
 materialization
 4.4. Derived tables
 ~~~~~~~~~~~~~~
 WL #3485: Subquery optimization: FROM (SELECT) 
 4.5. EXISTs convertible to IN
 ~~~~~~~~~~~~~~~~~~~~~~
 WL #4389: Make IN optimizations also handle EXISTS
 4.6. Materialization for non-correlated NOT IN subqueries
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 WL #3830: Materialization: Partial matching of tuples with NULL components
 
 4.7. Direct evaluation of subqueries with caching
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 WL #3341: Shortcut the evaluation as soon as there is a match
 WL #1117: Avoid recalculating subquery if external fields have not changed
```

[MySQL Worklog #4614](https://dev.mysql.com/worklog/task/?id=4614) and [MySQL Worklog #4690](https://dev.mysql.com/worklog/task/?id=4690) are considered droppable.


## Plan for action (committed)


### General considerations


It seems to be infeasible to take mysql-6.0 and fix it until it has release
quality. We'll have to do it other way around: start from mariadb-5.2 codebase
and pull features to there, one by one. This process will be called "backport".


### Backport MRR/BKA (SergeyP)


MRR/BKA has been there for longer time than other features and so is more
stable and so is a natural candidate for the first step.


Needed actions:


* Backport MRR/BKA code

  * According to Igor, code at SQL layer should be easy to move
  * Code inside MyISAM and Maria should be easily movable
  * TODO what to do about MRR/NDB? We need to get it to compile at least.
  * The trickest engine is InnoDB/XtraDB

    * will need to take changes that we've made to InnoDB and apply them to
 XtraDB (TODO will Percona accept that? Or we'll have to maintain
 patches-to-patches?)
* We'll also need to fix the known MRR/InnoDB bugs


After MRR has been pushed, it received a number of code cleanups, bugfixes, and
interface adjustments (motivated by BKA and NDB/Falcon implementations). This
means that there is no single MRR patch, instead one should go through
revisions and cherry-pick MRR-related patches (one of the ways to narrow down
the number of revisions: most (all?) MRR fixes were made by sergefp@mysql.com,


with exception of this fix:


```
2726 Guilhem Bichot    2009-03-13
      Fix for multiple symptoms sharing the same cause:
      BUG#42297 Maria: crash in multi-range-read code
      BUG#42298 Maria: SELECT with join returns no rows
      ...
```

In addition to backport, we need the following adjustments:


* Let DS-MRR support clustered primary keys (needed when using BKA).
* Remove conditions used for key access from the condition pushed to
 index (We sometimes get "Using index condition" where there was no "Using
 where") Considered done as we're unable to find any examples for
 this.
* Introduce a separate @@optimizer_switch flag for turning on/out
 ICP. DONE.
* Rename multi_range_read_info_const() to look like it is not a part of MRR
 interface


All of the above is filed as [MWL#67](https://askmonty.org/worklog/?tid=67):
[index.pl?tid=67](https://askmonty.org/worklog/Server-Sprint/index.pl?tid=67)


#### Milestone BKA-1: BKA backported


After the above is done, BKA will work in [MariaDB 5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2) codebase in the same way
as it worked in MySQL 6.0, but without MRR/InnoDB bugs.


### Subquery optimization: Efficient NOT IN execution with NULL (Timour)


Implement [index.pl?tid=68](https://askmonty.org/worklog/Server-Sprint/index.pl?tid=68)


## Plan for action (planned)


### Step: Take BKA into account in join optimizer (SergeyP or Igor)


Implement this item


* [No WL]: Make the join optimizer account for BKA.


According to Igor:


Within this milestone, assume a certain join_cache_level setting (it is likely
the estimates will be so rough that it won't matter)


TODO: clarify if this includes making the choice between doing MRR scan and
then filesorting vs doing non-MRR scan but not having to sort.


#### Milestone BKA-2: BKA with cost-based optimization


After the above is done, we'll have MRR/BKA with cost-based optimization.


### Step: Subqueries, start: backport and bugfixing


This step includes backporting all pushed 6.0's subquery optimizations and
fixing open wrong-result or crash bugs, including addressing of these
problems:


* Semi-join optimizations, including semi-join materialization has issues:

  * The "outer join and semi-join problem"
  * The different-datatypes-comparison problem


At the moment it seems the preferred course of action is to first fix the bugs
and then backport.


#### Milestone SUBQ-GET-ON-TRACK


After the above is done, we'll be able to assume that we "got on track" with
subquery development and will be able to proceed further in many directions.


NOTE: it is not fully known what we'll discover when this milestone is
reacheed. Perhaps, we'll discover that subquery cost model needs some 
adjustments (but there's always a way out, penalize all non-5.1 plans so that 
the 5.1 plan wins in near competitions and thus there are no regressions).


### Step: FROM subqueries


After the semi-join subqueries are done, the biggest and most annoying gap in
subquery optimizations will be poor FROM subquery handling. Thus, the next
item is to take the available code for


* [MySQL Worklog #3485](https://dev.mysql.com/worklog/task/?id=3485): Subquery optimization: FROM (SELECT)


and finish that.


#### Milestone SUBQ-FROM-SUBQUERIES


* This milestone adds [MySQL Worklog #3485](https://dev.mysql.com/worklog/task/?id=3485).


(is there really sense to have a linear plan that extends further than this?
 Let's reach this point and release?)


### Step: More subqueries 1


This is a step that has high ROI, can be done more-or-less indepdendently of 
the other work, and doesn't require in-depth knowlege of new subquery 
code/features:


* [MySQL Worklog #1117](https://dev.mysql.com/worklog/task/?id=1117): Subquery optimization: Avoid recalculating subquery if external 
 fields have not changed


this can be passed over to somebody who haven't worked with subquery code
before.


(note: this task has a natural extension: create and use a cache of 
external_field_values->subquery_result mappings.


Btw, certain nose-trunk databases do not seem to handle this case.


### Step: More subqueries 2


Another separate, high-ROI item:


* [MySQL Worklog #3341](https://dev.mysql.com/worklog/task/?id=3341): Subquery optimization: Shortcut the evaluation as soon as there is a match


(TODO check if that's really that WL entry).


(note: after "More subqueries #1/#2 we'll also need [MySQL Worklog #3830](https://dev.mysql.com/worklog/task/?id=3830) before we could
count non-WHERE clause subqueries as covered).


### Step: Backport Metadata integrity code (Timour)


Backport the following:


```
WL #2771: Usage of multi_read_range in nested loop join
 3. Metadata integrity
 -------------------------
 WL #4284 (bug #989): Transactional DDL locking
 WL#4165: Prepared statements: validation
 WL#4166: Prepared statements: automatic re-prepare
```


CC BY-SA / Gnu FDL

