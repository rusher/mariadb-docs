
# PREPARE Statement

## Syntax


```
PREPARE stmt_name FROM preparable_stmt
```


## Description


The `<code class="fixed" style="white-space:pre-wrap">PREPARE</code>` statement prepares a statement and assigns it a name,
`<code class="fixed" style="white-space:pre-wrap">stmt_name</code>`, by which to refer to the statement later. Statement names
are not case sensitive. `<code class="fixed" style="white-space:pre-wrap">preparable_stmt</code>` is either a string literal or a [user variable](../../sql-language-structure/user-defined-variables.md) (not a [local variable](../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/declare-variable.md), an SQL expression or a subquery) that contains the text of the statement. The text must 
represent a single SQL statement, not multiple statements. Within the
statement, "?" characters can be used as parameter markers to indicate
where data values are to be bound to the query later when you execute
it. The "?" characters should not be enclosed within quotes, even if
you intend to bind them to string values. Parameter markers can be used
only where expressions should appear, not for SQL keywords,
identifiers, and so forth.


The scope of a prepared statement is the session within which it is
created. Other sessions cannot see it.


If a prepared statement with the given name already exists, it is
deallocated implicitly before the new statement is prepared. This means
that if the new statement contains an error and cannot be prepared, an
error is returned and no statement with the given name exists.


Prepared statements can be PREPAREd and [EXECUTEd](execute-statement.md) in a stored procedure, but not in a stored function or trigger. Also, even if the statement is PREPAREd in a procedure, it will not be deallocated when the procedure execution ends.


A prepared statement can access [user-defined variables](../../sql-language-structure/user-defined-variables.md), but not [local variables](../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/declare-variable.md) or procedure's parameters.


If the prepared statement contains a syntax error, PREPARE will fail. As a side effect, stored procedures can use it to check if a statement is valid. For example:


```
CREATE PROCEDURE `test_stmt`(IN sql_text TEXT)
BEGIN
        DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN
                SELECT CONCAT(sql_text, ' is not valid');
        END;
        SET @SQL := sql_text;
        PREPARE stmt FROM @SQL;
        DEALLOCATE PREPARE stmt;
END;
```

The [FOUND_ROWS()](../built-in-functions/secondary-functions/information-functions/found_rows.md) and [ROW_COUNT()](../built-in-functions/secondary-functions/information-functions/row_count.md) functions, if called immediatly after EXECUTE, return the number of rows read or affected by the prepared statements; however, if they are called after DEALLOCATE PREPARE, they provide information about this statement. If the prepared statement produces errors or warnings, [GET DIAGNOSTICS](../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/programmatic-compound-statements-diagnostics/get-diagnostics.md) return information about them. DEALLOCATE PREPARE shouldn't clear the [diagnostics area](../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/programmatic-compound-statements-diagnostics/diagnostics-area.md), unless it produces an error.


A prepared statement is executed with `<code>[EXECUTE](execute-statement.md)</code>` and released 
with `<code>[DEALLOCATE PREPARE](deallocate-drop-prepare.md)</code>`.


The [max_prepared_stmt_count](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_prepared_stmt_count) server system variable determines the number of allowed prepared statements that can be prepared on the server. If it is set to 0, prepared statements are not allowed. If the limit is reached, an error similar to the following will be produced:


```
ERROR 1461 (42000): Can't create more than max_prepared_stmt_count statements 
  (current value: 0)
```

### Oracle Mode


In [Oracle mode](../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md), `<code>PREPARE stmt FROM 'SELECT :1, :2'</code>` is used, instead of `<code>?</code>`.


## Permitted Statements



##### MariaDB starting with [10.6.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1062-release-notes.md)
All statements can be prepared, except [PREPARE](prepare-statement.md), [EXECUTE](execute-statement.md), and [DEALLOCATE / DROP PREPARE](deallocate-drop-prepare.md).


Prior to this, not all statements can be prepared. Only the following SQL commands are permitted:


* [ALTER TABLE](../data-definition/alter/alter-tablespace.md)
* [ANALYZE TABLE](../table-statements/analyze-table.md)
* [BINLOG](../../../../../maxscale/mariadb-maxscale-14/maxscale-14-routers/binlogrouter.md)
* [CACHE INDEX](../administrative-sql-statements/cache-index.md)
* [CALL](../stored-routine-statements/call.md)
* [CHANGE MASTER](../administrative-sql-statements/replication-statements/change-master-to.md)
* [CHECKSUM {TABLE | TABLES}](../table-statements/checksum-table.md)
* [COMMIT](../transactions/commit.md)
* {[CREATE](../data-definition/create/create-database.md) | [DROP](../data-definition/drop/drop-database.md)} DATABASE
* {[CREATE](../data-definition/create/create-index.md) | [DROP](../data-definition/drop/drop-index.md)} INDEX
* {[CREATE](../../vectors/create-table-with-vectors.md) | [RENAME](../data-definition/rename-table.md) | [DROP](../data-definition/drop/drop-tablespace.md)} TABLE
* {[CREATE](../account-management-sql-commands/create-user.md) | [RENAME](../account-management-sql-commands/rename-user.md) | [DROP](../account-management-sql-commands/drop-user.md)} USER
* {[CREATE](../../../../server-usage/programming-customizing-mariadb/views/create-view.md) | [DROP](../../../../server-usage/programming-customizing-mariadb/views/drop-view.md)} VIEW
* [DELETE](../data-manipulation/changing-deleting-data/delete.md)
* [DESCRIBE](../administrative-sql-statements/describe.md)
* [DO](../../../../../general-resources/company-and-community/contributing-participating/donate-to-the-foundation.md)
* [EXPLAIN](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/outdated-pages/explain-formatjson-in-mysql.md)
* [FLUSH](../administrative-sql-statements/flush-commands/flush-tables-for-export.md) {TABLE | TABLES | TABLES WITH READ LOCK | HOSTS | PRIVILEGES | LOGS | STATUS | 
 MASTER | SLAVE | DES_KEY_FILE | USER_RESOURCES | [QUERY CACHE](../administrative-sql-statements/flush-commands/flush-query-cache.md) | TABLE_STATISTICS | 
 INDEX_STATISTICS | USER_STATISTICS | CLIENT_STATISTICS}
* [GRANT](../account-management-sql-commands/grant.md)
* [INSERT](../built-in-functions/string-functions/insert-function.md)
* INSTALL {[PLUGIN](../administrative-sql-statements/plugin-sql-statements/install-plugin.md) | [SONAME](../administrative-sql-statements/plugin-sql-statements/install-soname.md)}
* [HANDLER READ](../../nosql/handler/handler-commands.md)
* [KILL](../administrative-sql-statements/kill.md)
* [LOAD INDEX INTO CACHE](../data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-index.md)
* [OPTIMIZE TABLE](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/optimize-table.md)
* [REPAIR TABLE](../table-statements/repair-table.md)
* [REPLACE](../built-in-functions/string-functions/replace-function.md)
* [RESET](../administrative-sql-statements/replication-statements/reset-master.md) {[MASTER](../administrative-sql-statements/replication-statements/reset-master.md) | [SLAVE](../administrative-sql-statements/replication-statements/reset-replica.md) | [QUERY CACHE](../administrative-sql-statements/replication-statements/reset-master.md)}
* [REVOKE](../account-management-sql-commands/revoke.md)
* [ROLLBACK](../transactions/rollback.md)
* [SELECT](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)
* [SET](../../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md)
* [SET GLOBAL SQL_SLAVE_SKIP_COUNTER](../administrative-sql-statements/replication-statements/set-global-sql_slave_skip_counter.md)
* [SET ROLE](../account-management-sql-commands/set-role.md)
* [SET SQL_LOG_BIN](../administrative-sql-statements/set-commands/set-sql_log_bin.md)
* [SET TRANSACTION ISOLATION LEVEL](../transactions/set-transaction.md)
* [SHOW EXPLAIN](../administrative-sql-statements/show/show-explain.md)
* SHOW {[DATABASES](../administrative-sql-statements/show/show-databases.md) | [TABLES](../administrative-sql-statements/show/show-tables.md) | [OPEN TABLES](../administrative-sql-statements/show/show-open-tables.md) | [TABLE STATUS](../administrative-sql-statements/show/show-table-status.md) | [COLUMNS](../administrative-sql-statements/show/show-columns.md) | [INDEX](../administrative-sql-statements/show/show-index.md) | [TRIGGERS](../administrative-sql-statements/show/show-triggers.md) | 
 [EVENTS](../administrative-sql-statements/show/show-events.md) | [GRANTS](../administrative-sql-statements/show/show-grants.md) | [CHARACTER SET](../administrative-sql-statements/show/show-character-set.md) | [COLLATION](../administrative-sql-statements/show/show-collation.md) | [ENGINES](../administrative-sql-statements/show/show-events.md) | [PLUGINS [SONAME](../administrative-sql-statements/show/show-plugins-soname.md)] | [PRIVILEGES](../administrative-sql-statements/show/show-privileges.md) | 
 [PROCESSLIST](../administrative-sql-statements/show/show-processlist.md) | [PROFILE](../administrative-sql-statements/show/show-profile.md) | [PROFILES](../administrative-sql-statements/show/show-profiles.md) | [VARIABLES](../administrative-sql-statements/show/show-variables.md) | [STATUS](../administrative-sql-statements/show/show-status.md) | [WARNINGS](../administrative-sql-statements/show/show-warnings.md) | [ERRORS](../administrative-sql-statements/show/show-errors.md) | 
 [TABLE_STATISTICS](../administrative-sql-statements/show/show-table-statistics.md) | [INDEX_STATISTICS](../administrative-sql-statements/show/show-index-statistics.md) | [USER_STATISTICS](../administrative-sql-statements/show/show-user-statistics.md) | [CLIENT_STATISTICS](../administrative-sql-statements/show/show-client-statistics.md) | [AUTHORS](../administrative-sql-statements/show/show-authors.md) | 
 [CONTRIBUTORS](../administrative-sql-statements/show/show-contributors.md)}
* SHOW CREATE {[DATABASE](../administrative-sql-statements/show/show-create-database.md) | [TABLE](../administrative-sql-statements/show/show-create-table.md) | [VIEW](../administrative-sql-statements/show/show-create-view.md) | [PROCEDURE](../administrative-sql-statements/show/show-create-procedure.md) | [FUNCTION](../administrative-sql-statements/show/show-create-function.md) | [TRIGGER](../administrative-sql-statements/show/show-create-trigger.md) | [EVENT](../administrative-sql-statements/show/show-create-event.md)}
* SHOW {[FUNCTION](../administrative-sql-statements/show/show-function-code.md) | [PROCEDURE](../administrative-sql-statements/show/show-procedure-code.md)} CODE
* [SHOW BINLOG EVENTS](../administrative-sql-statements/show/show-binlog-events.md)
* [SHOW SLAVE HOSTS](../administrative-sql-statements/show/show-replica-hosts.md)
* SHOW {MASTER | BINARY} LOGS
* SHOW {MASTER | SLAVE | TABLES | INNODB | FUNCTION | PROCEDURE} STATUS
* SLAVE {[START](../administrative-sql-statements/replication-statements/start-replica.md) | [STOP](../administrative-sql-statements/replication-statements/stop-replica.md)}
* [TRUNCATE TABLE](../table-statements/truncate-table.md)
* [SHUTDOWN](../administrative-sql-statements/shutdown.md)
* UNINSTALL {PLUGIN | SONAME}
* [UPDATE](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md)


Synonyms are not listed here, but can be used. For example, DESC can be used instead of DESCRIBE.


[Compound statements](../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/using-compound-statements-outside-of-stored-programs.md) can be prepared too.


Note that if a statement can be run in a stored routine, it will work even if it is called by a prepared statement. For example, [SIGNAL](../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/signal.md) can't be directly prepared. However, it is allowed in [stored routines](../../../../server-usage/programming-customizing-mariadb/stored-routines/README.md). If the x() procedure contains SIGNAL, you can still prepare and execute the 'CALL x();' prepared statement.


PREPARE supports most kinds of expressions as well, for example:


```
PREPARE stmt FROM CONCAT('SELECT * FROM ', table_name);
```

When PREPARE is used with a statement which is not supported, the following error is produced:


```
ERROR 1295 (HY000): This command is not supported in the prepared statement protocol yet
```

## Example


```
create table t1 (a int,b char(10));
insert into t1 values (1,"one"),(2, "two"),(3,"three");
prepare test from "select * from t1 where a=?";
set @param=2;
execute test using @param;
+------+------+
| a    | b    |
+------+------+
|    2 | two  |
+------+------+
set @param=3;
execute test using @param;
+------+-------+
| a    | b     |
+------+-------+
|    3 | three |
+------+-------+
deallocate prepare test;
```

Since identifiers are not permitted as prepared statements parameters, sometimes it is necessary to dynamically compose an SQL statement. This technique is called *dynamic SQL*). The following example shows how to use dynamic SQL:


```
CREATE PROCEDURE test.stmt_test(IN tab_name VARCHAR(64))
BEGIN
	SET @sql = CONCAT('SELECT COUNT(*) FROM ', tab_name);
	PREPARE stmt FROM @sql;
	EXECUTE stmt;
	DEALLOCATE PREPARE stmt;
END;

CALL test.stmt_test('mysql.user');
+----------+
| COUNT(*) |
+----------+
|        4 |
+----------+
```

Use of variables in prepared statements:


```
PREPARE stmt FROM 'SELECT @x;';

SET @x = 1;

EXECUTE stmt;
+------+
| @x   |
+------+
|    1 |
+------+

SET @x = 0;

EXECUTE stmt;
+------+
| @x   |
+------+
|    0 |
+------+

DEALLOCATE PREPARE stmt;
```

## See Also


* [Out parameters in PREPARE](out-parameters-in-prepare.md)
* [EXECUTE Statement](execute-statement.md)
* [DEALLOCATE / DROP Prepared Statement](deallocate-drop-prepare.md)
* [EXECUTE IMMEDIATE](execute-immediate.md)
* [Oracle mode from MariaDB 10.3](../../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md)

