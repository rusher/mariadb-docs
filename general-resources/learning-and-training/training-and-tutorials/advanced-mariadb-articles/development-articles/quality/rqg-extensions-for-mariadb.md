
# RQG Extensions for MariaDB


All recent reasonably stable changes can be found in [our Github repository](https://github.com/MariaDB/randgen). The link points to the master branch; there are other branches created for more specific cases.


While all described changes were made in order to test MariaDB code, many of them are applicable to other MySQL flavors as well.


## Galera Mode


A set of changes to support running RQG tests with multi-master Galera replication, implemented to test [MariaDB Galera cluster](../../../../../../server/reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md).


The top-level script `<code>runall-new.pl</code>` got a new option --galera, which takes a string value. The string can be a combination of 'm' or 's', where each symbol represents a Galera node. 'm' stands for 'master', and 's' stands for 'slave'.


The new module `<code>GaleraMySQLd.pm</code>` implements cluster initialization and startup. It is only interested in the number of nodes.


Internals are adapted to the multi-master or mixed mode:


* instead of executing data generation on each started server, it is only executed on the first 'master';
* test flow is executed on each 'master' (but not on 'slaves');
* no result comparison is performed after each query, the flow runs independently, but at the end, if no other errors were encountered, `<code>runall-new.pl</code>` performs dump comparison in the usual manner.


Also, a sample grammar and data template are provided in `<code>conf/galera</code>`, they are slightly modified versions of conf/engines/engine_stress.yy and engine_stress.zz, adapted for Galera taking into account its limitations (e.g. no `<code>LOCK</code>`).


*Note: `<code>GaleraMySQLd.pm</code>` has defaults for everything mandatory but `<code>wsrep_provider</code>`. If you run the test with more than 1 node, you need to provide the value on the command line in the usual manner (`<code>--mysqld=--wsrep-provider=...</code>`), otherwise the test fail with the corresponding error message.*


So, if you provide


```
--galera=mms --mysqld=--wsrep-provider=<path to Galera library>
```

3 nodes will be started, and Galera replication will be set up between them; the data will be generated on the first node; the test flow will be executed on the first and second nodes; at the end of the test, data dump from each node will be taken and compared; node vardirs will be placed under `<code><vardir>/node0</code>`, `<code><vardir>/node1</code>`, `<code><vardir>/node2</code>`.


## CheckFieldValue Validator


A grammar can set requirements on results of a query through a specifically formatted comment. If the validator finds a comment which matches the template, it performs the requested check. The validation is defined in the comment itself: it says which field in which row in the result set should be checked, and provides the condition (currently simple numeric comparisons: `<code>=</code>`, `<code><</code>`, `<code>></code>`, `<code><=</code>`, `<code>>=</code>`).


It allows to do simple verification without implementing a special validator.


Example:


A query in the grammar file


```
SELECT COUNT(*), MAX(`pk`) FROM _table /* Validate 2 > 10 for row all*/;
```

The comment means "Check that the value in field 2 is greater than 10 for all rows" (for this query "all rows" is overkill, it could just as well be "row 1").


Assuming that there is a table with not more than 10 rows, the validator will produce the error:


```
ERROR: For query 'SELECT COUNT(*), MAX(`pk`) FROM `BB` /* Validate 2 > 10 for row 1*/' on row 1 result 10 does not meet the condition > 10
Full row: [1] : 1; [2] : 10;
```

The exit code for this failure is `<code>STATUS_REQUIREMENT_UNMET</code>`.


*Usage example: investigation of the sporadic failure [MDEV-4578](https://jira.mariadb.org/browse/MDEV-4578)*


## MariadbGtidCrashSafety Reporter


The reporter was created to test slave crash-safety with [MariaDB implementation of GTID](../../../../../../server/server-usage/replication-cluster-multi-master/standard-replication/gtid.md). It is similar to [SlaveCrashRecovery reporter](#slavecrashrecovery-reporter), but is adjusted to check GTID-specific aspects:


* it restarts the slave with --skip-slave-start, and executes


```
CHANGE MASTER .. MASTER_USE_GTID=current_pos;
STOP SLAVE;
```

So, regardless how the replication was set up initially, after the first crash/restart it will start using GTID for sure;


* while the slave is running, and also before a crash and after restart the reporter checks `<code>gtid*</code>` variables and the contents of the system table `<code>mysql.gtid_slave_pos</code>` and verifies basic consistency of the data, e.g. watches that GTID seq_no constantly grows.


## SlaveCrashRecovery Reporter


The reporter can be used to test crash-safety of replication.


It is a periodic reporter, every 30 seconds it kills the slave server using `<code>SIGKILL</code>`, and immediately restarts it on the old data directory, with the same parameters as before. On server restart, the reporter checks that the server and the replication started all right.


The reporter itself does not check consistency of the data, but it can be used together with `<code>ReplicationConsistency</code>` reporter.


It is supposed to be used with `<code>runall-new.pl</code>`, so that the server is started without MTR involvement.


*Usage example: testing of [GTID in MariaDB 10.0](../../../../../../server/server-usage/replication-cluster-multi-master/standard-replication/gtid.md)*


## BinlogConsistency Reporter


The reporter checks that the contents of the binary log correctly reflects the contents of the server.


After the main test flow is finished, the reporter creates a data dump of the server, stores its binary logs, shuts down the server, starts a new one with the same parameters, but on a clean data directory, replays the binary logs into it, creates a dump of the new server, and compares two dumps.


It is to be used with `<code>runall-new.pl</code>`.


*Usage example: testing of binlog changes in [MariaDB 10.0](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) (e.g. [MDEV-181](https://jira.mariadb.org/browse/MDEV-181), [MDEV-232](https://jira.mariadb.org/browse/MDEV-232))*


## CrashRecovery Reporter


The idea is very much the same as in the old Recovery reporter: crash the server at the end of the test, restart it and make sure it started all right, and the data is not corrupted. The main difference is that the old reporter restarts the server in a hardcoded pre-defined manner, which limits its use. Instead, CrashRecovery reporter starts the server with the same set of options as the initial one, which imitates a more realistic scenario, and also allows to use it on non-default InnoDB configurations.


It is to be used with `<code>runall-new.pl</code>`


## LimitRowsExamined Transformer


The transformer was developed for testing new [LIMIT ROWS EXAMINED](../../../../../../server/server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/limit-rows-examined.md) functionality added in [MariaDB 5.5](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md). It can be used in the usual way, by providing its name in the `<code>--transformers</code>` list.


The transformer checks whether the original query already contains a `<code>ROWS EXAMINED</code>` clause. If it does not, it adds the clause either after the `<code>LIMIT</code>` clause, or at the end of the query. In any case (even if `<code>ROWS EXAMINED</code>` was already there), the transformer returns the following sequence of statements:


* `<code>FLUSH STATUS</code>`
* <the query with `<code>ROWS EXAMINED</code>`>
* <a query which sums up status variables related to examined rows>


The result of the main query is checked to be a subset of the original query's result set. The sum of status variables is checked to be not greater than the limit provided in the `<code>ROWS EXAMINED</code>` clause, plus a margin. The margin is configured in the transformer.


If the result of the transformed query appears not to be a subset of the original result set, `<code>STATUS_LENGTH_MISMATCH</code>` is returned.


If the sum of status variables is greater than the maximum allowed value, `<code>STATUS_REQUIREMENT_UNMET</code>` is returned.


Note: Status values `<code>STATUS_REQUIREMENT_UNMET</code>` and `<code>STATUS_REQUIREMENT_UNMET_SELECT</code>` were added to `<code>Constants.pm</code>`.


## ShowExplain Validator


The validator was developed for testing the new functionality [SHOW EXPLAIN](../../../../../../server/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-explain.md) introduced in [MariaDB 10.0](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md).


The validator checks that the output of `<code>SHOW EXPLAIN</code>` correlates with the output of traditional `<code>EXPLAIN</code>` executed for the same query. It also tries to filter out known expected mismatches between the produced plans.


## Comparison of VIEW Algorithms


RQG already provided `<code>--views[=<view type>]</code>` option, which means that in addition to the normal data generation, views of the requested types will be added and used in the test flow. However, you could only create views of the same type on servers that you were comparing. Now there are `<code>--views1</code>` and `<code>--views2</code>` options, which work the same way as `<code>--basedir1</code>`/`<code>--basedir2</code>`, `<code>--mysqld1</code>`/`<code>--mysqld2</code>`, etc. The backward compatibility is preserved, so you can still use `<code>--views</code>` which will be applied to both servers unless there is `<code>--views1</code>` or `<code>--views2</code>` to override it.


The change was made in `<code>gentest.pl</code>` and both `<code>runall.pl</code>` and `<code>runall-new.pl</code>`.


*Usage example: testing of MERGE view extension in [MariaDB 10.0](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) ([MDEV-3862](https://jira.mariadb.org/browse/MDEV-3862))*


## Multiple Redefining Grammars


RQG allows to provide `<code>--redefine=<grammar file></code>` option to override or add rules to the main grammar. Sometimes you have a redefining grammar for a feature, and another redefining grammar for an engine, and yet another redefining grammar for a specific version, and combining them makes the number of grammars to grow uncontrollably. The simple change has been made to allow providing several redefining grammars at once, e.g.:


```
runall.pl ... --redefine=memory_engine_redefine.yy --redefine=binlog_format_stmt_redefine.yy --redefine=legacy_version_redefine.yy
```

*Warning: It is better not to allow them to override each other, since the result can be unexpected (that is, they should define different sets of rules)*


The change was made in `<code>gentest.pl</code>` and both `<code>runall.pl</code>` and `<code>runall-new.pl</code>`.


## New Grammar Keywords _basetable and _view


The RQG keyword _table means any table or view from the test dataset. Often it's good enough, but sometimes it badly increases the number of erroneous statements. Now tables and views can be differentiated in a grammar depending on what the goal is: _table can still be used for both tables and views, while _basetable will only pick tables, and _view will only pick views.


Example:


If you create the following rule in your grammar


```
alter:
        ALTER TABLE _table ENGINE=MyISAM;
```

and you are running the test with views, you will be getting lots of `<code>ER_WRONG_OBJECT</code>` errors ("is not BASE TABLE"). It is hardly the goal, so you can improve the grammar by changing it to


```
alter:
        ALTER TABLE _basetable ENGINE=MyISAM;
```

This way the rule will only pick "real" tables. 
Of course, if you still want to pick views sometimes, as a sanity check that there is no crash or anything, you can make the rule a bit more complicated, but much better tuned than it was, e.g.


```
alter:
        ALTER TABLE alter_object ENGINE=MyISAM;

alter_object:
        _basetable | _basetable | _basetable | _basetable | _basetable | _view ;
```

## See Also


* [RQG Documentation](https://github.com/RQG/RQG-Documentation/wiki/Category:RandomQueryGenerator)
* [RQG Performance Comparisons](benchmarks-and-long-running-tests/benchmarks/rqg-performance-comparisons.md)
* [Optimizer Quality](optimizer-quality.md)
* [QA Tools](qa-tools.md)
* [Worklog Quality Checklist Template](worklog-quality-checklist-template.md)

