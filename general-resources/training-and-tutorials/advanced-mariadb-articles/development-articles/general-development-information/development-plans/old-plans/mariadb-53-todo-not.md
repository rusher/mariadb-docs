
# MariaDB 5.3 TODO not

**Note:** This page is obsolete. The information is old, outdated, or otherwise currently incorrect. We are keeping the page for historical reasons only. **Do not** rely on the information in this article.



This page lists things that were in plans for [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3) but were not included after all. 
For the actual list of things that are still needed before 5.3 release, see [mariadb-53-todo](mariadb-53-todo.md)


# Specific goals


Top-level worklog for all tasks: [MWL#91](https://askmonty.org/worklog/?tid=91)


# TODO per person before 5.3 can go beta


## Sergey Petrunya


In priority order:


## Timour Katchaounov


### Optional tasks


* Possibly: MWL#?? Remove double materialization in materialized subqueries ;In 5.5
* New tasks (moved from [MWL#89](https://askmonty.org/worklog/?tid=89)):

  * implement robust expensive predicate handling (is_expensive), possibly in a separate task
* performance tuning for all WL


## Michael "Monty" Widenius


* mwl#?? VARCHAR and BLOB for HEAP tables (from ebay).

  * Waiting for ok from Ebay to use their code to start working on this.


## Igor Babaev


### [MWL#128](https://askmonty.org/worklog/?tid=128): Implement Block Nested Loop Hash Join


**hash join over attributes with non-binary collation (not started, 1-2 weeks) (not critical)**


### MWL#?? (new)


* Cost-based choice for join buffers (not started, 2 weeks, including review)


### [MWL#106](https://askmonty.org/worklog/?tid=106): Backport optimizations for derived tables and views


The goal of this task is to backport the implementation of the late materialization of derived tables and views and the additional optimizations for derived tables/views from MySQL 6.0 code line to [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3).


* Done in a separate tree, probable requires refactoring.
* Probable problems of merging with other tasks. (1 week)
* Philip should start testing; Timour+Igor to define when bugs should be reported (not to be reported if bugs is also a subquery bug)


## Oleksandr "Sanja" Byelkin


### mwl#??


* Bitmap in tmp table keys ; 1-3 days


## Sergei Golubchik


* review query rewrite plugin contribution
* review Kristian's replication tasks
* [MWL#113](https://askmonty.org/worklog/?tid=113): many clustered keys (not only primary)
* [MWL#114](https://askmonty.org/worklog/?tid=114): insert ignore ha_extra hint
* [MWL#151](https://askmonty.org/worklog/?tid=151): Phone home (done, just needs to be pushed)


## Kristian Nielsen


Tasks which should go in 5.3:


* [MWL#116](https://askmonty.org/worklog/?tid=116): Group commit framework and implementation

  * Code complete, waiting for code review.
  * After review+fixes, need to supply info for documentation.
* [MWL#136](https://askmonty.org/worklog/?tid=136): Cross-engine consistency for START TRANSACTION WITH CONSISTENT SNAPSHOT

  * Code complete, waiting for code review.
  * After review+fixes, need to supply info for documentation.
* [MWL#163](https://askmonty.org/worklog/?tid=163): release of row locks in InnoDB during prepare

  * Code complete, waiting for code review.
  * After review+fixes, need to supply info for documentation.


Tasks which are not critical for 5.3, but could go there:


* PBXT part of [MWL#116](https://askmonty.org/worklog/?tid=116).

  * Waiting for response from Paul McCullagh.
* [MWL#132](https://askmonty.org/worklog/?tid=132): TC plugin

  * Waiting for code review.


# Rolling features


* [MWL#92](https://askmonty.org/worklog/?tid=92): Subqueries backport: fix known semi-join subquery bugs
* Consolidate the range query apis (need more info)
* [MWL#115](https://askmonty.org/worklog/?tid=115): innodb statistics in the slow log
* Tasks in [worklog](https://askmonty.org/worklog/index.pl?virtual=version:Server-5.3)
* mwl#?? Optimized versions of users statistics (from google/facebook).

  * responsible: Monty
  * status: will do if Monty has time after VARCHAR and BLOB task
  * todo: review, change, possibly reimplement, est: 7 days work


# Testing


* Still a lot of open bugs at [Launchpad](https://bugs.launchpad.net/maria).
* More testing to be decided later


CC BY-SA / Gnu FDL

