
# Buildbot Database Schema

This page describes the database schema used by Buildbot to save results from test runs.


The idea is to be able to use this data from outside of Buildbot for things like additional web pages presenting test results, or search/data mining facilities for searching for test failures.


## Accessing the database


The plan is to make remote database connections available to community members. For this, we need to set up a slave host replicating the master Buildbot database (which would in any case be good to isolate the running Buildbot from possibly high load from queries).


However, for now the database access is only available locally on the machine (hasky) running the buildbot master.


## Schema


The most current information about the schema used is available in the file `buildbot/process/mtrlogobserver.py` in the Buildbot sources. As the code evolves and more kinds of information is made available in the database, the schema might be extended, but the schema description in the source code should always be up-to-date.


### The `test_run` table


This table has one row for every test run that Buildbot does. Thus, each row corresponds to one cell in the [[waterfall](https://askmonty.org/buildbot/waterfall) Waterfall display]. The format of the table is as follows:


```
CREATE TABLE test_run(
    id INT PRIMARY KEY AUTO_INCREMENT,
    branch VARCHAR(100),
    revision VARCHAR(32) NOT NULL,
    platform VARCHAR(100) NOT NULL,
    dt TIMESTAMP NOT NULL,
    bbnum INT NOT NULL,
    typ VARCHAR(32) NOT NULL,
    info VARCHAR(255),
    KEY (branch, revision),
    KEY (dt),
    KEY (platform, bbnum)
) ENGINE=innodb
```

* id: Primary key, just an auto_increment id.
* branch: This is the name of the bzr branch of the test run.
* revision: The Bzr revision number tested.
* platform: The name of the builder that ran the test.
* dt: Date when the buildbot run was started.
* bbnum: The Buildbot '''build number''' which together with `platform` uniquely identifies a build within Buildbot.
* typ: Concise abbreviation describing the kind of test. For example `pr` for --ps-protocol with row based replication, or `nm` for normal run with mixed-mode replication.
* info: Short textual description of the kind of test run.


### The `test_failure` table


This table has one row for every test failure encountered:


```
CREATE TABLE test_failure(
    test_run_id INT NOT NULL,
    test_name VARCHAR(100) NOT NULL,
    test_variant VARCHAR(16) NOT NULL,
    info_text VARCHAR(255),
    failure_text TEXT,
    PRIMARY KEY (test_run_id, test_name, test_variant)
) ENGINE=innodb
```

* test_run_id: This identifies the test run in which the test failure occured (eg. it is a foreign key to `id` in table `test_run`).
* test_name: The name of the test that failed, eg. `main.information_schema`.
* test_variant: Some tests are run multiple times in different variants. Ie. many replication tests are run under both statement-based, mixed-mode, and row-based replication. The variant will be 'stmt', 'mix', or 'row' accordingly. For tests that do not have multiple variants, the value will be the empty string (ie. not a NULL value).
* info_text: This is a short description that mysql-test-run.pl sometimes gives for some kinds of test failures (for example "timeout").
* failure_text: This is the entire output from mysql-test-run.pl concerning this test failure. It usually contains the diff against the result file, a stacktrace for a crash, etc. This is useful to run `<span class="k">LIKE</span>
` queries against when searching for test failures similar to one being investigated.


### The `test_warnings` table


This table holds information about test problems that were detected after a test case ran, during server restart (typically by finding an error or warning message in the server error log files). A typical example of this is a memory leak or a crash during server shutdown.


Such a failure can not be attributed to a specific test case, as it could be caused by any of the tests run against the server since last restart, or could even be a general problem not caused by any test case. Instead, for each occurence, this table provides a list of names of the tests that were run by the server prior to detecting the error or warning.


```
CREATE TABLE test_warnings(
    test_run_id INT NOT NULL,
    list_id INT NOT NULL,
    list_idx INT NOT NULL,
    test_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (test_run_id, list_id, list_idx)
) ENGINE=innodb
```

* test_run_id: Identifies the corresponding row in table <code>test_run</code>.
* list_id: This is a counter for occurences of warnings within each test run (ie. it starts over from 0 again for each different value of <code>test_run_id</code>).
* list_idx: This is a counter for each test name (ie. it starts over from 0 again for each different value of <code>test_run_id</code> ''and'' <code>list_id</code>).
* test_name: The name of the test run by the server prior to seeing the warning.


## Sample queries


Show all platforms that failed for a particular revision of a particular branch:


```
select platform
  from test_run r
where branch = 'mysql-6.0-testing2'
  and revision = '2819'
  and (exists (select * from test_failure f where f.test_run_id = r.id)
    or exists (select * from test_warnings w where w.test_run_id = r.id));
```

Find failures similar to a given failure being investigated:


```
select branch, revision, platform, test_name, test_variant, failure_text
  from  test_failure f
  inner join test_run r on (f.test_run_id = r.id)
  where failure_text LIKE "%--protocol=TCP' failed%";
```

Check which branches a specific kind of failure has occured in:


```
select branch, count(*)
  from test_failure f
  inner join test_run r on (f.test_run_id = r.id)
  where failure_text LIKE "%--protocol=TCP' failed%"
  group by branch;
```

Find all test runs where a given test was run against a server that later had warnings in the error log, and also count the number of occurences of this event in each run:


```
select branch, revision, platform, count(*)
  from test_warnings w
  inner join test_run r on (w.test_run_id = r.id)
  where test_name = 'rpl.rpl_plugin_load'
  group by r.id;
```
