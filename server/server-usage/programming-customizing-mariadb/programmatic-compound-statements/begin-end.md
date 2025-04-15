
# BEGIN END

## Syntax


```
[begin_label:] BEGIN [NOT ATOMIC]
    [statement_list]
END [end_label]
```


`<code>NOT ATOMIC</code>` is required when used outside of a [stored procedure](../stored-routines/stored-procedures/README.md). Inside stored procedures or within an anonymous block, `<code>BEGIN</code>` alone starts a new anonymous block.


## Description


`<code>BEGIN ... END</code>` syntax is used for writing compound statements. A compound statement can contain multiple statements, enclosed by the `<code>BEGIN</code>` and `<code>END</code>` keywords. statement_list represents a list of one or more statements, each
terminated by a semicolon (i.e., `<code>;</code>`) statement delimiter. statement_list is
optional, which means that the empty compound statement (`<code>BEGIN END</code>`) is
legal.


Note that `<code>END</code>` will perform a commit. If you are running in [autocommit](../../replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#autocommit) mode, every statement will be committed separately. If you are not running in `<code>autocommit</code>` mode, you must execute a [COMMIT](../../../reference/sql-statements-and-structure/sql-statements/transactions/commit.md) or [ROLLBACK](../../../reference/sql-statements-and-structure/sql-statements/transactions/rollback.md) after `<code>END</code>` to get the database up to date.


Use of multiple statements requires that a client is able to send statement strings containing the ; statement delimiter. This is handled in the [mysql](https://mariadb.com/kb/en/mysql-command-line_client) command-line client with the [DELIMITER](../../../clients-and-utilities/mariadb-client/delimiters.md) command.
Changing the `<code>;</code>` end-of-statement delimiter (for example, to
`<code class="highlight fixed" style="white-space:pre-wrap">//</code>`) allows `<code>;</code>` to be used in a program body.


A compound statement within a [stored program](../stored-routines/README.md) can be
[labeled](labels.md). `<code>end_label</code>` cannot be given unless `<code>begin_label</code>` also is present. If both are present, they must be the same.


`<code>BEGIN ... END</code>` constructs can be nested. Each block can define its own variables, a `<code>CONDITION</code>`, a `<code>HANDLER</code>` and a [CURSOR](programmatic-compound-statements-cursors/README.md), which don't exist in the outer blocks. The most local declarations override the outer objects which use the same name (see example below).


The declarations order is the following:


* [DECLARE local variables](declare-variable.md);
* [DECLARE CONDITIONs](declare-condition.md);
* [DECLARE CURSORs](programmatic-compound-statements-cursors/declare-cursor.md);
* [DECLARE HANDLERs](declare-handler.md);


Note that `<code>DECLARE HANDLER</code>` contains another `<code>BEGIN ... END</code>` construct.


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

In this example, a [TINYINT](../../../reference/data-types/data-types-numeric-data-types/tinyint.md) variable, `<code>x</code>` is declared in the outter block. But in the inner block `<code>x</code>` is re-declared as a [CHAR](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/charset.md) and an `<code>y</code>` variable is declared. The inner [SELECT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) shows the "new" value of `<code>x</code>`, and the value of `<code>y</code>`. But when x is selected in the outer block, the "old" value is returned. The final [SELECT](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md) doesn't try to read `<code>y</code>`, because it doesn't exist in that context.


## See Also


* [Using compound statements outside of stored programs](using-compound-statements-outside-of-stored-programs.md)
* [Changes in Oracle mode from MariaDB 10.3](../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md)

