
# mariadb-test Auxiliary Files


The mariadb-test framework utilizes many other files that affect the testing
process, in addition to test and result files.



## `<code>disabled.def</code>` file


This file can be used to disable certain tests temporarily. For example, if one
test fails and you are working on that, you may want to push the changeset that
disables the test into the test suite so that other tests won't be disturbed by
this failure.


The file contains test names and a comment (that should explain why the test
was disabled), separated by a colon. Lines that start with a hash sign
(`<code>#</code>`) are ignored. A typical `<code>disabled.def</code>` may look like this (note
that a hash sign in the middle of a line does not start a comment):


```
# List of disabled tests
# test name : comment
rpl_redirect : Fails due to bug#49978
events_time_zone  : need to fix the timing
```

During testing, mtr will print disabled tests like this:


```
...
rpl.rpl_redirect              [ disabled ]  Fails due to bug#49978
rpl.events_time_zone          [ disabled ]  need to fix the timing
...
```

This file should be located in the suite directory.



## `<code>suite.opt</code>` file


This file lists server options that will be added to the `<code>mariadbd</code>` command
line for every test of this suite. It can refer to environment variables with
the `<code>$NAME</code>` syntax. Shell meta-characters should be quoted. For example


```
--plugin-load=$AUTH_PAM_SO
--max-connections=40 --net_read_timeout=5
"--replicate-rewrite-db=test->rewrite"
```

Note that options may be put either on one line or on separate lines. It is a
good idea to start an option name with the `<code class="fixed" style="white-space:pre-wrap">--loose-</code>` prefix if
the server may or may not recognize the option depending on the configuration.
An unknown option in the `<code>.opt</code>` file will stop the server from starting, and
the test will be aborted.


This file should be located in the suite directory.



## other `<code>*.opt</code>` files


For every test or include file `<code>somefile.test</code>` or `<code>somefile.inc</code>`, mtr will
look for `<code>somefile.opt</code>`, `<code>somefile-master.opt</code>` and `<code>somefile-slave.opt</code>`.
These files have exactly the same syntax as the `<code>suite.opt</code>` above. Options
from these files will also be added to the server command line (all servers
started for this test, only master, or only slave respectively) for all
affected tests, for example, for all tests that include `<code>somefile.inc</code>`
directly or indirectly.


A typical usage example is `<code>include/have_blackhole.inc</code>` and
`<code>include/have_blackhole.opt</code>`. The latter contains the necessary command-line
options to load the Blackhole storage engine, while the former verifies that
the engine was really loaded. Any test that needs the Blackhole engine needs
only to start from `<code>source include/have_blackhole.inc;</code>` and the engine will
be automatically loaded for the test.



## `<code>my.cnf</code>` file


This is not the `<code>my.cnf</code>` file that tests from this suite will use, but rather
a *template* of it. It will be converted later to an actual `<code>my.cnf</code>`. If a
suite contains no `<code>my.cnf</code>` template, a default template,
— `<code>include/default_my.cnf</code>`
— will be used. Or `<code>suite/rpl/my.cnf</code>` if the test
includes `<code>master-slave.inc</code>` (it's one of the few bits of the old MySQL
`<code>mysql-test-run</code>` magic that we have not removed yet). Typically a suite
template will not contain a complete server configuration, but rather start
from


```
!include include/default_my.cnf
```

and then add the necessary modifications.


The syntax of `<code>my.cnf</code>` template is the same of a normal `<code>my.cnf</code>` file, with
a few extensions and assumptions. They are:


* For any group with the name `<code>[mysqld.<strong>N</strong>]</code>`, where N is a number, mtr
 will start one `<code>mysqld</code>` process. Usually one needs to have
 only `<code>[mysqld.1]</code>` group, and `<code>[mysqld.2]</code>` group for replication tests.


* There can be groups with non-standard names (`<code>[foo]</code>`, `<code>[bar]</code>`, whatever),
 not used by `<code>mysqld</code>`. The `<code>suite.pm</code>` files (see below) may use them
 somehow.


* Values can refer to each other using the syntax `<code>@groupname.optionname</code>`
— these references be expanded as needed. For
 example
```
[mysqld.2]
master-port= @mysqld.1.port
```


* it sets the value of the `<code>master-port</code>` in the `<code>[mysqld.2]</code>` group to the value of `<code>port</code>` in the `<code>[mysqld.1]</code>` group.


* An option name may start with a hash sign `<code>#</code>`. In the
 resulting `<code>my.cnf</code>` it will look like a comment, but it still can be
 referred to. For example:


```
[example]
#location = localhost:@mysqld.1.port
bar = server:@example.#location/data
```

* There is the `<code>[ENV]</code>` group. It sets values for the environment variables.
 For example
```
[ENV]
MASTER_MYPORT = @mysqld.1.port
```


* Also, one can refer to values of environment variables via this
 group:
```
[mysqld.1]
user = @ENV.LOGNAME
```


* There is the `<code>[OPT]</code>` group. It allows to invoke functions and
 generate values. Currently it contains only one option
 — `<code>@OPT.port</code>`. Every time this option is referred
 to in some other group in the `<code>my.cnf</code>` template, a new unique port number
 is generated. It will not match any other port number used by this test run.
 For example
```
[ENV]
SPHINXSEARCH_PORT = @OPT.port
```


This file should be located in the suite directory.



## other `<code>*.cnf</code>` files


For every test file `<code>somefile.test</code>` (but for not included files) mtr will
look for `<code>somefile.cnf</code>` file. If such a file exists, it will be used as a
template instead of suite `<code>my.cnf</code>` or a default `<code>include/default_my.cnf</code>`
templates.



## `<code>combinations</code>` file


The `<code>combinations</code>` file defines few sets of alternative configurations, and
every test in this suite will be run many times - once for every configuration.
This can be used, for example, to run all replication tests in the *rpl*
suite for all three binlog format modes (row, statement, and mixed). A
corresponding `<code>combinations</code>` file would look as
following:


```
[row]
binlog-format=row

[stmt]
binlog-format=statement

[mix]
binlog-format=mixed
```

It uses `<code>my.cnf</code>` file syntax, with groups (where group names define
combination names) and options. But, despite the similarity, it is not a
`<code>my.cnf</code>` template, and it cannot use the templating extentions. Instead,
options from the `<code>combinations</code>` file are added to the server command line. In
this regard, combination file is closer to `<code>suite.opt</code>` file. And just like
it, combination file can use environment variables using the `<code>$NAME</code>` syntax.


Not all tests will necessarily run for all combinations. A particular test may
require to be run only in one specific combination. For example, in
replication, if a test can only be run with the row binlog format, it will have
`<code>--binlog-format=row</code>` in one of the `<code>.opt</code>` files. In this case, mtr will
notice that server command line already has an option that matches one of the
combinations, and will skip all other combinations for this particular test.


The `<code>combinations</code>` file should be located in the suite directory.



## other `<code>*.combinations</code>` files


Just like with the `<code>*.opt</code>` files, mtr will use `<code>somefile.combinations</code>` file
for any `<code>somefile.test</code>` and `<code>somefile.inc</code>` that is used in testing. These
files have exactly the same format as a suite `<code>combinations</code>` file.


This can cause many combination files affecting one test file (if a test
includes two `<code>.inc</code>` files, and both of them have corresponding
`<code>.combinations</code>` files). In this case, mtr will run the test for all
combinations of combinations from both files. In [MariaDB 5.5](../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md), for example,
`<code>rpl_init.inc</code>` adds combinations for row/statement/mixed, and
`<code>have_innodb.inc</code>` adds combinations for innodb/xtradb. Thus any replication
test that uses innodb will be run six times.



## `<code>suite.pm</code>` file


This (optional) file is a perl module. It must declare a
package that inherits from `<code>My::Suite</code>`.


This file must normally end with `<code>bless {}</code>` — that
is it must return an object of that class. It can also return a string
— in this case all tests in the suite will be skipped,
with this string being printed as a reason (for example "PBXT engine was not
compiled").


A suite class can define the following methods:


* `<code>config_files()</code>`
* `<code>is_default()</code>`
* `<code>list_cases()</code>`
* `<code>servers()</code>`
* `<code>skip_combinations()</code>`
* `<code>start_test()</code>`


A `<code>config_files()</code>` method returns a list of additional config files (besides
`<code>my.cnf</code>`), that this suite needs to be created. For every file it specifies a
function that will create it, when given a `<code>My::Config</code>` object. For example:


```
sub config_files {(
    'config.ini' => \&write_ini,
    'new.conf'   => \&do_new
)}
```

A `<code>servers()</code>` method returns a list of processes that needs to be started for
this suite. A process is specified as a [regex, hash] pair. The regular
expression must match a section in the `<code>my.cnf</code>` template (for example,
`<code>qr/mysqld\./</code>` corresponds to all `<code>mysqld</code>` processes), the hash contains
these options:



|   |   |
| --- | --- |
| SORT | a number. Processes are started in the order of increasing SORT values (and stopped in the reverse order). mysqld has number 300. |
| START | a function to start a process. It takes two arguments, My::Config::Group and My::Test. If START is undefined a process will not be started. |
| WAIT | a function to wait for the process to be started. It takes My::Config::Group as an argument. Internally mtr first invokes START for all processes, then WAIT for all started processes. |



```
sub servers {(
    qr/^foo$/ => { SORT => 200,  # start foo before mysqld
                   START => \&start_foo,
                   WAIT => \&wait_foo }
)}
```

See the *sphinx* suite for a working example.


A `<code>list_cases()</code>` method returns a complete list of tests for this suite. By
default it will be the list of files that have `<code>.test</code>` extension, but without
the extension. This list will be filtered by mtr, subject to different mtr
options (`<code>--big-test</code>`, `<code>--start-from</code>`, etc), the suite object does not have
to do it.


A `<code>start_test()</code>` method starts one test process, by default it will be
`<code>mariadb-test</code>`. See the *unit* suite for a working example of
`<code>list_cases()</code>` and `<code>start_test()</code>` methods.


A `<code>skip_combinations()</code>` method returns a hash that maps file names (where
combinations are defined) to a list of combinations that should be skipped. As
a special case, it can disable a complete file by using a string instead of a
hash. For example


```
sub skip_combinations {(
    'combinations' => [ 'mix', 'rpl' ],
    'inc/many.combinations' => [ 'a', 'bb', 'c' ],
    'windows.inc' => "Not on windows",
)}
```

The last line will cause all tests of this suite that include `<code>windows.inc</code>`
to be skipped with the reason being "Not on windows".


An `<code>is_default()</code>` method returns 1 if this particular suite should be run by default, when the `<code>mariadb-test-run.pl</code>` script is run without explicitly specified test suites or test cases.



## `<code>*.sh</code>` files


For every test file `<code>sometest.test</code>` mtr looks for `<code>sometest-master.sh</code>` and
`<code>sometest-slave.sh</code>`. If either of these files is found, it will be run before
the test itself.



## `<code>*.require</code>` files


These files are obsolete. Do not use them anymore. If you need to skip a test
use the `<code>skip</code>` command instead.



## `<code>*.rdiff</code>` files


These files also define what the test result should be. But unlike `<code>*.result</code>`
files, they contain a patch that should be applied to one result file to create
a new result file. This is very useful when a result of some test in one
combination differs slightly from the result of the same test, but in another
combination. Or when a result of a test in an overlay differs from the test
result in the overlayed suite.


It is quite difficult to edit `<code>.rdiff</code>` files to update them after the test
file has changed. But luckily, it is never needed. When a test fails, mtr
creates a `<code>.reject</code>` file. Having it, one can create `<code>.rdiff</code>` file as easy
as (for example)


```
diff -u main/foo.result main/foo.reject > main/foo,comb.rdiff
or
diff -u main/foo.result main/foo,comb.reject > main/foo,comb.rdiff
```

Some example:


```
diff -u main/innodb_ext_key.result main/innodb_ext_key,off.reject > main/innodb_ext_key,off.rdiff

diff -u suite/sys_vars/r/sysvars_server_notembedded.result suite/sys_vars/r/sysvars_server_notembedded,32bit.reject > suite/sys_vars/r/sysvars_server_notembedded,32bit.rdiff
```

Note: This will also add a timestamp in the .rdiff file, so if you are submitting a patch you could remove it manually. If the same .rdiff file is used for multiple combinations, then it would be good to omit in the header that would identify the combination, to allow git to pack the repository better. Example:


```
--- testname.result
+++ testname.reject
```

Because a combination can be part of the `<code>.result</code>` or `<code>.rdiff</code>` file name,
mtr has to look in many different places for a test result. For example,
consider a test `<code>foo.test</code>` in the combination pair `<code>aa,bb</code>`, that is run
in the overlay *rty* of the suite *qwe*, in other words, for the test that
mtr prints as


```
qwe-rty.foo 'aa,bb'                     [ pass ]
```

For this test a result can be in


* either `<code>.rdiff</code>` or `<code>.result</code>` file
* either in the overlay "`<code>rty/</code>`" or in the overlayed suite "`<code>qwe/</code>`"
* with or without combinations in the file name ("`<code>,a</code>`", "`<code>,b</code>`",
 "`<code>,a,b</code>`", or nothing)


which means any of the following 15 file names can be used:


1. `<code>rty/r/foo,aa,bb.result</code>`
1. `<code>rty/r/foo,aa,bb.rdiff</code>`
1. `<code>qwe/r/foo,aa,bb.result</code>`
1. `<code>qwe/r/foo,aa,bb.rdiff</code>`
1. `<code>rty/r/foo,aa.result</code>`
1. `<code>rty/r/foo,aa.rdiff</code>`
1. `<code>qwe/r/foo,aa.result</code>`
1. `<code>qwe/r/foo,aa.rdiff</code>`
1. `<code>rty/r/foo,bb.result</code>`
1. `<code>rty/r/foo,bb.rdiff</code>`
1. `<code>qwe/r/foo,bb.result</code>`
1. `<code>qwe/r/foo,bb.rdiff</code>`
1. `<code>rty/r/foo.result</code>`
1. `<code>rty/r/foo.rdiff</code>`
1. `<code>qwe/r/foo.result</code>`


They are listed, precisely, in the order of preference, and mtr will walk that
list from top to bottom and the first file that is found will be used.


If this found file is a `<code>.rdiff</code>`, mtr continues walking down the list until
the first `<code>.result</code>` file is found. A `<code>.rdiff</code>` is applied to that
`<code>.result</code>`.



## `<code>valgrind.supp</code>` file


This file defines valgrind suppressions, and it is used when mtr is started
with a `<code>--valgrind</code>` option.

