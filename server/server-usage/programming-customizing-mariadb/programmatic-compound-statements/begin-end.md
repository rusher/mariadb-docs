
# BEGIN END

## Syntax


```
[begin_label:] BEGIN [NOT ATOMIC]
    [statement_list]
END [end_label]
```


`NOT ATOMIC` is required when used outside of a [stored procedure](../stored-routines/stored-procedures/README.md). Inside stored procedures or within an anonymous block, `BEGIN` alone starts a new anonymous block.


## Description


`BEGIN ... END` syntax is used for writing compound statements. A compound statement can contain multiple statements, enclosed by the `BEGIN` and `END` keywords. statement_list represents a list of one or more statements, each
terminated by a semicolon (i.e., `;`) statement delimiter. statement_list is
optional, which means that the empty compound statement (`BEGIN END`) is
legal.


Note that `END` will perform a commit. If you are running in [autocommit](../../replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#autocommit) mode, every statement will be committed separately. If you are not running in `autocommit` mode, you must execute a [COMMIT](../../../ref/sql-statements-and-structure/sql-statements/transactions/commit.md) or [ROLLBACK](../../../ref/sql-statements-and-structure/sql-statements/transactions/rollback.md) after `END` to get the database up to date.


Use of multiple statements requires that a client is able to send statement strings containing the ; statement delimiter. This is handled in the [mysql](https://mariadb.com/kb/en/mysql-command-line_client) command-line client with the [DELIMITER](../../../clients-and-utilities/mariadb-client/delimiters.md) command.
Changing the `;` end-of-statement delimiter (for example, to
`//`) allows `;` to be used in a program body.


A compound statement within a [stored program](../stored-routines/README.md) can be
[labeled](labels.md). `end_label` cannot be given unless `begin_label` also is present. If both are present, they must be the same.


`BEGIN ... END` constructs can be nested. Each block can define its own variables, a `CONDITION`, a `HANDLER` and a [CURSOR](programmatic-compound-statements-cursors/README.md), which don't exist in the outer blocks. The most local declarations override the outer objects which use the same name (see example below).


The declarations order is the following:


* [DECLARE local variables](declare-variable.md);
* [DECLARE CONDITIONs](declare-condition.md);
* [DECLARE CURSORs](programmatic-compound-statements-cursors/declare-cursor.md);
* [DECLARE HANDLERs](declare-handler.md);


Note that `DECLARE HANDLER` contains another `BEGIN ... END` construct.


Here is an example of a very simple, anonymous block:


```
BEGIN NOT ATOMIC
SET @a=1;
CREATE TABLE test.t1(a INT);
END|
```

Below is an example of nested blocks in a stored procedure:


```
CREATE PROCEDURE t( )
BEGIN
   DECLARE x TINYINT UNSIGNED DEFAULT 1;
   BEGIN
      DECLARE x CHAR(2) DEFAULT '02';
       DECLARE y TINYINT UNSIGNED DEFAULT 10;
       SELECT x, y;
   END;
   SELECT x;
END;
```

In this example, a [TINYINT](../../../ref/data-types/data-types-numeric-data-types/tinyint.md) variable, `x` is declared in the outter block. But in the inner block `x` is re-declared as a [CHAR](../../../ref/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/charset.md) and an `y` variable is declared. The inner [SELECT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) shows the "new" value of `x`, and the value of `y`. But when x is selected in the outer block, the "old" value is returned. The final [SELECT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) doesn't try to read `y`, because it doesn't exist in that context.


## See Also


* [Using compound statements outside of stored programs](using-compound-statements-outside-of-stored-programs.md)
* [Changes in Oracle mode from MariaDB 10.3](../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md)

