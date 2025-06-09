# Code Coverage

We are working on getting more of the MariaDB source covered by our\
mysql-test-run (MTR) test suite. This is an ongoing (and slow) task as there is\
still a lot of old code with not very good coverage.

## Goals for new code

For new code in MariaDB, we aim much higher:

The goals are:

1. All new lines of code should ideally be tested by MTR.
2. Code which cannot reasonably be tested by MTR needs to be tested by another\
   tool and those code lines marked with /\* purecov: tested \*/.

* In this case the tool used for testing should be documented in the[worklog](../tools/worklog.md) entry for the code or in the commit message.

1. Code that can't reasonably be tested (such as error conditions) should be\
   marked with '/\* purecov: inspected \*/' so that a reviewer of the code can\
   easily spot this code.
2. Code that is suspected to be deadcode should have a 'DBUG\_ASSERT(0)' or be\
   marked with '/\* purecov: deadcode \*/' so that we have a chance to notice if\
   the code is ever executed.

The reason we are using 'purecov' to mark lines is an attribution to the[purecov](https://mariadb.com/kb/en/ftp://ftp.software.ibm.com/software/rational/docs/v2002/dev_tools/purecov/html/ht_intro_pc.htm)\
tool we originally used for code coverage in the early years of MySQL.

## Markers

The recommended markers are:

`/* purecov: tested */`

* For code lines that are tested by something other than\
  mysql-test-run:

`/* purecov: inspected */`

* For code lines that are hard to test but for which one has read the line\
  multiple times to ensure it is correct. A code reviewer should also\
  inspect these lines with care as they have not been properly tested.

`/* purecov: deadcode */`

* For code lines that one suspects will never be called. Having this marker\
  allows us to generate a warning during mysql-test-run code coverage if\
  this line is executed.

The comment must be placed on the line/lines that are affected.

For code blocks larger than 1 line one can use the block syntax:

```
/* purecov: begin tested */
....
/* purecov: end */
```

## Running mysql-test-run with gcov

### Prerequisites

1. First make sure that gcov 4.9 is installed.Older versions of the gocv library (lgcov) can't\
   handle running several instances of a program in parallel. This causes the generated .gov files to not\
   contain all executed lines when running mysql-test-run with the --parallel option or running test that starts several mysqld servers, like replication or spider tests.
2. Compile MariaDB with BUILD/compile-pentium64-gcov (if your machine does not\
   have a pentium CPU, hack this script, or just live with the pentium-specific stuff)

### Running mysql-test-run

To be able to see the level of coverage within the current test suite, do the\
following:

1. In the mysql-test directory, run this\
   command: `./mysql-test-run -gcov`
2. To see which lines are not yet covered, look at `source_file_name.gcov` in\
   the source tree. In [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1) or below it's in the CMakeFiles directory where the object files are stored. In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) it's stored together with the source files.
3. Think hard about a test case which will cover those lines that are not tested, and write one.

## Tools

* You can use the [code-coverage-with-dgcov/dgcov tool](https://mariadb.com/kb/en/code-coverage-with-dgcov/dgcov_tool) to check the coverage for the new code. This is especially written and maintained for MariaDB.
* For code coverage you also use the [lcov](https://fedora13.selfip.org/lcov/) tool.

## Code coverage in buildbot

[buildbot](../tools/buildbot/), the MariaDB build system, is doing [automatic coverage testing for each push](https://buildbot.askmonty.org/buildbot/builders/kvm-dgcov-jaunty-i386).

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
