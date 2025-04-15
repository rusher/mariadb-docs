
# mariadb-test Overview


## The Basics


At its core, mariadb-test is very simple. The client program `<code>mariadb-test</code>`
executes a *test file* and compares the produced output with the *result
file*. If the files match, the test is passed; otherwise the test has failed.
This approach can be used to test any SQL statement, as well as other
executables (with the `<code>exec</code>` command).


The complete process of testing is governed and monitored by 
the *mariadb-test-run.pl* driver script, or *mtr* for short (for convenience,
`<code>mtr</code>` is created as a symbolic link to `<code>mariadb-test-run.pl</code>`). The mtr script
is responsible for preparing the test environment, creating a list of all tests
to run, running them, and producing the report at the end. It can run many
tests in parallel, execute tests in an order which minimizes server restarts
(as they are slow), run tests in a debugger or under valgrind or strace, and so
on.


Test files are located in *suites*. A *suite* is a directory which contains
test files, result files, and optional configuration files. The mtr looks for
suites in the `<code>mariadb-test/suite</code>` directory, and in the `<code>mariadb-test</code>`
subdirectories of plugins and storage engine directories. For example, the
following are all valid suite paths:


```
mariadb-test/suite/rpl
```


```
mariadb-test/suite/handler
```


```
storage/example/mariadb-test/demo
```


```
plugin/auth_pam/mariadb-test/pam
```


In almost all cases, the suite directory name is the suite name. A notable
historical exception is the *main* suite, which is located directly in the
`<code>mariadb-test</code>` directory.


Test files have a `<code>.test</code>` extension and can be placed directly in the suite
directory (for example, `<code>mariadb-test/suite/handler/interface.test</code>`) or in the
`<code>t</code>` subdirectory (e.g. `<code>mariadb-test/suite/rpl/t/rpl_alter.test</code>` or
`<code>mariadb-test/t/grant.test</code>`). Similarly, result files have the `<code>.result</code>`
extension and can be placed either in the suite directory or in the `<code>r</code>`
subdirectory.


A test file can include other files (with the `<code>source</code>` command). These
included files can have any name and may be placed anywhere, but customarily
they have a `<code>.inc</code>` extension and are located either in the suite directory or
in the `<code>inc</code>` or `<code>include</code>` subdirectories (for example,
`<code>mariadb-test/suite/handler/init.inc</code>` or
`<code>mariadb-test/include/start_slave.inc</code>`).


Other files which affect testing, while not being tests themselves, are:


* `<code>disabled.def</code>`
* `<code>suite.opt</code>`
* other `<code>*.opt</code>` files
* `<code>my.cnf</code>`
* other `<code>*.cnf</code>` files
* `<code>combinations</code>`
* other `<code>*.combinations</code>` files
* `<code>suite.pm</code>`
* `<code>*.sh</code>` files
* `<code>*.require</code>` files
* `<code>*.rdiff</code>` files
* `<code>valgrind.supp</code>`


See [Auxiliary files](mariadb-test-auxiliary-files.md) for details on these.


## Overlays


In addition to regular suite directories, mtr supports *overlays*.
An *overlay* is a directory with the same name as an existing suite, but
which is located in a storage engine or plugin directory. For example,
`<code>storage/myisam/mariadb-test/rpl</code>` could be a *myisam* overlay of the *rpl*
suite in `<code>mariadb-test/suite/rpl</code>`. And
`<code>plugin/daemon_example/mariadb-test/demo</code>` could be a *daemon_example* overlay
of the *demo* suite in `<code>storage/example/mariadb-test/demo</code>`. As a special
exception, an overlay of the main suite, should be called `<code>main</code>`, as in
`<code>storage/pbxt/mariadb-test/main</code>`.


An overlay is like a second transparent layer in a graphics editor. It can
obscure, extend, or modify the background image. Also, one may notice that an
overlay is very close to a *UnionFS*, but implemented in perl inside mtr.


An overlay can replace almost any file in the overlaid suite, or add new files.
For example, if some overlay of the main suite contains a
`<code>include/have_innodb.inc</code>` file, then all tests that include it will see and
use the overlaid version. Or, an overlay can create a `<code>t/create.opt</code>` file
(even though the main suite does not have such a file), and `<code>create.test</code>`
will be executed with the specified additional options.


But adding an overlay never affects how the original suite is executed. That
is, mtr always executes the original suite as if no overlay was present. And
then, additionally, it executes a combined "union" of the overlay and the
original suite. When doing that, mtr takes care to avoid re-executing tests
that are not changed in the overlay. For example, creating `<code>t/create.opt</code>` in
the overlay of the main suite will only cause `<code>create.test</code>` to be executed in
the overlay. But creating `<code>suite.opt</code>` affects all tests
— and it will cause all tests to be re-executed with
the new options.


## Combinations


In certain cases it makes sense to run a specific test or a group of tests
several times with different server settings. This can be done using
so-called *combinations*. Combinations are groups of settings that are used
alternatively. A combinations file defines these alternatives using `<code>my.cnf</code>`
syntax, for example


```
[row]
binlog-format=row

[stmt]
binlog-format=statement

[mix]
binlog-format=mixed
```

And all tests where this combinations file applies will be run three times:
once for the combination called "row", and `<code>--binlog-format=row</code>` on the
server command line, once for the "stmt" combination, and once for the "mix"
combination.


More than one combinations file may be applicable to a given test file. In this
case, mtr will run the test for all possible combinations of the given
combinations. A test that uses replication (three combinations as above) and
innodb (two combinations - innodb and xtradb), will be run six times.


## Sample Output


Typical mtr output looks like this


```
==============================================================================
TEST                                  WORKER RESULT   TIME (ms) or COMMENT
--------------------------------------------------------------------------
rpl.rpl_row_find_row_debug                [ skipped ]  Requires debug build
main-pbxt.connect                         [ skipped ]  No PBXT engine
main-pbxt.mysqlbinlog_row                 [ disabled ]  test expects a non-transactional engine
rpl.rpl_savepoint 'mix,xtradb'            w2 [ pass ]    238
rpl.rpl_stm_innodb 'innodb_plugin,row'    w1 [ skipped ]  Neither MIXED nor STATEMENT binlog format
binlog.binlog_sf 'stmt'                   w2 [ pass ]      7
unit.dbug                                 w2 [ pass ]      1
maria.small_blocksize                     w1 [ pass ]     23
sys_vars.autocommit_func3 'innodb_plugin' w1 [ pass ]      5
sys_vars.autocommit_func3 'xtradb'        w1 [ pass ]      6
main.ipv6                                 w1 [ pass ]    131
...
```

Every test is printed as "suitename.testname", and a suite name may include an
overlay name (like in `<code>main-pbxt</code>`). After the test name, mtr prints
combinations that were applied to this test, if any.


A similar syntax can be used on the mtr command line to specify what tests to
run:



| $ ./mtr innodb | $ ./mtr main.innodb | $ ./mtr main-pbxt.innodb | $ ./mtr main-.innodb | $ ./mtr main.innodb,xtradb | $ ./mtr --suite=rpl | $ ./mtr --suite=mroonga/storage |
| --- | --- | --- | --- | --- | --- | --- |
| $ ./mtr innodb | search for innodb test in every suite from the default list, and run all that was found. |
| $ ./mtr main.innodb | run the innodb test from the main suite |
| $ ./mtr main-pbxt.innodb | run the innodb test from the pbxt overlay of the main suite |
| $ ./mtr main-.innodb | run the innodb test from the main suite and all its overlays. |
| $ ./mtr main.innodb,xtradb | run the innodb test from the main suite, only in the xtradb combination |
| $ ./mtr --suite=rpl | Run all test in the rpl suite (found in the suite/rpl directory) |
| $ ./mtr --suite=mroonga/storage | Run all test in the mroonga/wrapper suite (found in the storage/mroonga/mysql-test/mroonga/storage directory) |



## Plugin Support


The mtr driver has special support for MariaDB plugins.


First, on startup it copies or symlinks all dynamically-built plugins into
`<code>var/plugins</code>`. This allows one to have many plugins loaded at the same time.
For example, one can load Federated and InnoDB engines together. Also, mtr
creates environment variables for every plugin with the corresponding plugin
name. For example, if the InnoDB engine was built, `<code>$HA_INNODB_SO</code>` will be
set to `<code>ha_innodb.so</code>` (or `<code>ha_innodb.dll</code>` on Windows). And the test can
safely use the corresponding environment variable on all platforms to refer to
a plugin file; it will always have the correct platform-dependent extension.


Second, when combining server command-line options (which may come from many
different sources) into one long list before starting `<code>mariadbd</code>`, mtr treats
`<code>--plugin-load</code>` specially. Normal server semantics is to use the latest value
of any particular option on the command line. If one starts the server with,
for example, `<code>--port=2000 --port=3000</code>`, the server will use the last value
for the port, that is 3000. To allow different `<code>.opt</code>` files to require
different plugins, mtr goes through the assembled server command line, and
joins all `<code>--plugin-load</code>` options into one. Additionally it removes all empty
`<code>--plugin-load</code>` options. For example, suppose a test is affected by three
`<code>.opt</code>` files which contain, respectively:


```
--plugin-load=$HA_INNODB_SO
```

```
--plugin-load=$AUTH_PAM_SO
```

```
--plugin-load=$HA_EXAMPLE_SO
```

...and, let's assume the Example engine was not built (`<code>$HA_EXAMPLE_SO</code>` is
empty). Then the server will get:


```
--plugin-load=ha_innodb.so:auth_pam.so
```

instead of


```
--plugin-load=ha_innodb.so --plugin-load=auth_pam.so --plugin-load=
```

Third, to allow plugin sources to be simply copied into the `<code>plugin/</code>` or
`<code>storage/</code>` directories, and still not affect existing tests (even if new
plugins are statically linked into the server), mtr automatically disables all
optional plugins on server startup. A plugin is optional if it can be disabled
with the corresponding `<code>--skip-XXX</code>` server command-line option. Mandatory
plugins, like MyISAM or MEMORY, do not have `<code>--skip-XXX</code>` options (e.g. there
is no `<code>--skip-myisam</code>` option). This mtr behavior means that no plugin,
statically or dynamically built, has any effect on the server unless it was
explicitly enabled. A convenient way to enable a given plugin *XXX* for
specific tests is to create a `<code>have_XXX.opt</code>` file which contains the
necessary command-line options, and a `<code>have_XXX.inc</code>` file which checks
whether a plugin was loaded. Then any test that needs this plugin can source
the `<code>have_XXX.inc</code>` file and have the plugin loaded automatically.


## mtr communication procedure


`<code>mtr</code>` is first creating the server socket (`<code>master</code>`).


After that, `<code>workers</code>` are created using `<code>fork()</code>`.


For each worker `<code>run_worker()</code>` function is called, which is executing the following:


* creates a new socket to connect to `<code>server_port</code>` obtained from the `<code>master</code>`
* initiate communication with the `<code>master</code>` using `<code>START</code>` command
* `<code>master</code>` sends first test from list of tests supplied by the user and immediately sends command `<code>TESTCASE</code>` to the `<code>worker</code>`
* `<code>worker</code>` gets command `<code>TESTCASE</code>` and processes test case, by calling `<code>run_testcase()</code>` function which starts(/restarts if needed) the server and sends `<code>TESTRESULT</code>` (in case of restart `<code>WARNINGS</code>` command is issued to the `<code>master</code>` in case some warnings/error logs are found)
* `<code>master</code>` accepts `<code>TESTRESULT</code>` command and run `<code>mtr_report_test()</code>` function which check does the test fail and also generates the new command `<code>TESTCASE</code>` if some new test case exist
* If there is no other test case `<code>master</code>` sends `<code>BYE</code>` command which gets accepted by the `<code>worker</code>` which is properly closing the connection.

