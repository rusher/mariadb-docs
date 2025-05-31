# Worklog Quality Checklist Template

The purpose of this template is to produce individual checklists for testing\
individual Worklogs. Using a checklist ensures that all WLs are treated equally\
and that all important points are addressed and tested, or at least considered\
when clearing the WL for merging into a stable release.

## Inputs

_This section lists all sources of information which can be used as inputs to the testing process. The goal is to gather comprehensive information before creating a testing plan_

### Usage scenario

_Summarize here the intended use for the feature_

### Design, architecture and specification

* WorkLog number and title:
  * If there is no Worklog, create one or ask one to be created
* Are HLS and LLS present?
  * If the HLS or LLS sections are missing, add them or ask that they are created
* Reviewer name:
  * Testing suggestions and concerns should be obtained by the reviewer
* Customer requirements:
  * Make yourself familiar with any requirements or documents supplied by the customer
* Other implementations:
  * Make yourself familiar with other implementations of the feature in other database products or flavors of MySQL

### Testability and observability

* Does the feature have an on/off switch?
  * An on/off switch is required in at least the following situations:
    * A RQG comparison test will be performed in order to validate the feature;
    * The feature may cause a performance degradation for certain queries or usage scenarios;
    * The feature is experimental or of interest to a small number of users;
* Is the operation of the feature observable?
  * Does the feature leave any traces in SHOW STATUS or EXPLAIN, or in the logs?

### The patch

* List of modified files:
  * Obtain a list of all modified files from the version control system, to serve as a starting point for identifying areas of risk within the server or potential interactions with other features. A larger number of modified files may indicate larger risk of unforseen interactions;
* Review comments:
  * Paste a link to the review and read it for any concerns that the reviewer may have raised
* MTR tests:
  * Does the patch include enough MTR tests?
* DGCov output:
  * Generate a report or obtain it from a developer and make sure it is acceptable for all parties

### Feedback from interested parties

* Feedback from developer:
  * Paste here any useful information provided by the developer in informal discussions, emails or chat
  * Make sure any concerns raised by the developer are recorded in this document
* Feedback from reviewer:
  * Paste here any discussions with the reviewer related to concerns, risks or testing, if not included in the formal review comments for the patch itself
* Feedback from customer:
  * Summarize here any relevant discussions with the customer

### Query Patterns

_If the feature relates to the optimization of a particular set of queries, provide here examples that were extracted from the sources of information listed above, in particular the Worklog and any MTR test cases provided with the patch_

## Risks

_This section lists any risks inherent to the Worklog, as identified by reviewing the inputs mentioned_

### Refactoring

* Areas that have been refactored:
  * List areas that have been refactored in order to accommodate the new functionality

### Interactions

* Areas of potential interaction:
  * List areas in the server that may have an interaction with the feature
* Does the feature contain engine-specific code, hooks or hacks?
  * List any engine-specific considerations there may be
* Does the feature define a new API?
* Does the feature relate to transactions or transactional integrity?
  * If yes, is testing required on all storage engines, or using cross-engine transactions or binlog involvement?
* Does the feature relate to any of the core server features?
  * Do we need to test with views, triggers, stored procedures, functions, events, partitions, foreign keys, time zones

### Upgrade/Downgrade

* Does the feature change any on-disk formats?
  * If yes, testing would be required that upgrading to the new format works properly
* Does the feature change the format of the system tables in the `mysql` database?
  * If yes, testing would be required to make sure that any upgrade/downgrade scripts are able to handle the change gracefully
* Does the feature change or retire or deprecate any mysqld configuration options?
  * List options here
* Is downgrade to be supported?
  * If using the new feature makes the database non-downgradable, this must be a conscious design decision

### User-visible changes

* Does the feature change the mysql protocol?
  * If yes, full connectors testing is required to make sure the change is compatible
* Does the feature change any result formatting or data types?
  * If yes, testing via the `mysql` client is required to verify that the new format or data type properly arrives at the client
* Does the feature change the syntax or the output of a `SHOW` command?
  * If yes, clients, connectors and tools that issue that `SHOW` command and process its output should be tested
* Does the feature change anything with respect to `INFORMATION_SCHEMA` and `PERFORMANCE_SCHEMA` ?

### Performance and Optimizer

* Does the feature have any performance implications?
  * Is the feature expected to deliver any performance improvement?
  * Is the feature feared to have a performance impact?
* Does the feature interact with the Optimizer or indexes?
  * Does the feature change anything related to indexes or data stored in them?
  * Does the feature change anything with respect to any optimizations?

### Replication

_Does the feature generate or transmit data that may be sent or processed by the slave or tools such as `mysqlbinlog`?_

* Which binary log formats should be tested?
  * Certain optimizations or scenarios may only trigger for a particular binary log mode
* Are existing replication RQG grammars sufficient to trigger the new code?
* Do we need to test DDL in replication, log rotation and such?
* Does the change affect the master as well, or just the slave? Is a transactional integrity test indicated?
* Do we need to simulate replication failures, server restarts and such?
* Do we need to test cloning new slaves from scratch, binary log replay and other replication maintenance activities?
* Do we need to cover exotic data types, overly large records, statements that are only safe in a particular binlog mode, etc?

### Extreme conditions and corner case

* Does the feature deal with extreme conditions and corner cases?
  * e.g. huge values, huge tables, huge row lengths, blobs, high concurrencies
* Is any form of stress testing indicated for the feature?
  * Does the feature have any thread interactions, locking or concurrency mechanisms?

## Testing Plan

_This section identifies the testing that will be performed based on the risks identified above_

### Additional MTR tests

_Describe any MTR tests that will be implemented in addition to the ones already present in the patch_

### RQG tests

* Are new Random Query Generator grammars required?
  * If existing grammars do not cover the new feature
* Are new Validators or Reporters required?
  * If the existing RQG validation code can not verify the proper operation of the feature
* RQG tests lines to run:
  * provide actual RQG command lines, along with a description of the desired effect

### Manual testing

_Describe any manual testing that will be performed involving connectors, clients or installers_

### Benchmarks and stress tests

_Describe any benchmarks and stress tests that will be performed. Include the exact parameters and command lines that will be used_

## Hand-off

_This section identifies final checks to be performed on the test content when it is delivered_

### Requirements for MTR tests

* Are all new mysqld options, SHOW STATUS variables, I\_S tables and such\
  covered with an MTR test?
* Are all new error messages covered with a test?
* Is code coverage acceptable to all parties involved?

### Requirements for Random Query Generator tests

* Has the proper set of RQG grammars been chosen or created?
* Do we have a .CC file listing all interesting mysqld options and RQG\
  variants, in order to run a combinations test? Was the CC file pushed into\
  RQG's LP repository?
* Has an at least 24-hour combination test been run?
* Was code coverage run on the RQG test?
* Were all new grammars and Perl modules pushed into the RQG LP repository?
* Were the RQG tests prepared to be buildbot-ready, as opposed to manually-monitored?
* Does the test include any safeguards against false negatives?
  * e.g. all queries generated are bad, which causes no actual replication, which is still reported as test success
* Are the tests running stably and green in the feature tree's BuildBot?
* Are any bug reports missing reproducible test cases, core files, RQG command\
  lines and the like?

### Requirements for Code Coverage

_This makes it much faster to review code as one knows what it tested and what one needs to review more carefully_

* Ideally all code should be tested by MTR;
* If code can only be reproduced by an RQG test or other external test,\
  sufficient information must be provided in the Worklog for the test to be\
  reproducible;
* All code should either be tested or reviewed and marked with `/* purecov inspected */`
* Code that is suspected to be unreachable should have an DBUG\_ASSERT(0) and be\
  marked with /\* purecov: deadcode \*/.
* Was an MTR code coverage report for the feature tree generated by\
  i7.stoev.org/lcov?
* Has the dgcov coverage tool been run?
* Are there any notable regressions in the code coverage?
* Was code coverage run on the RQG tests alone, along with an effort to\
  increase it?
* Is the code covered by comments?

### Requirements for the code trees

* Was the stable tree merged into the feature tree recently?
* Were all RQG tests pushed into lp:randgen and documented on the RQG manual\
  pages?
* Were all RQG or other automatable tests installed in BuildBot?
* Is the feature tree BuildBot green?

### Requirements for closing the Worklog as complete

* Was the Worklog updated with information on the testing performed?
* Was the QA check box in the Worklog ticked?
* Were all related bugs on Launchpad closed? This includes A) bugs that were\
  tagged to belong to the feature tree, B) bugs assigned to the developer\
  regardless of tree, C) bugs assigned to the tester and D) and orphan bugs\
  just hanging around the same theme or time frame;
* Did the WL complete the entire review procedure, including any back-and-forth\
  emails?
* Has the new feature been documented?

## See also

* [RQG Documentation](https://github.com/RQG/RQG-Documentation/wiki/Category:RandomQueryGenerator)
* [RQG Performance Comparisons](benchmarks-and-long-running-tests/benchmarks/rqg-performance-comparisons.md)
* [RQG Extensions for MariaDB Features](rqg-extensions-for-mariadb.md)
* [Optimizer Quality](optimizer-quality.md)
* [QA Tools](qa-tools.md)

CC BY-SA / Gnu FDL
