# SET Variable

#

# Syntax

```
SET var_name = expr [, var_name = expr] ...
```

#

# Description

The `SET` statement in [stored programs](/kb/en/stored-programs-and-views/) is an extended version of the general `[SET](../../replication-cluster-multi-master/standard-replication/setting-up-replication.md)` statement. Referenced variables may be ones declared inside a stored program, global system variables, or user-defined variables.

The `SET` statement in stored programs is implemented as part of the
pre-existing [SET](../../replication-cluster-multi-master/standard-replication/setting-up-replication.md) syntax. This allows an extended syntax of `SET a=x, 
b=y, ...` where different variable types (locally declared variables,
global and session server variables, user-defined variables) can be
mixed. This also allows combinations of local variables and some
options that make sense only for system variables; in that case, the
options are recognized but ignored.

`SET` can be used with both [local variables](declare-variable.md) and [user-defined variables](../../../reference/sql-statements-and-structure/sql-language-structure/user-defined-variables.md).

When setting several variables using the columns returned by a query, `[SELECT INTO](../../../reference/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/select-into-outfile.md)` should be preferred.

To set many variables to the same value, the `[LAST_VALUE( )](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/information-functions/last_value.md)` function can be used.

Below is an example of how a user-defined variable may be set:

```
SET @x = 1;
```

#

# See Also

* [SET](../../replication-cluster-multi-master/standard-replication/setting-up-replication.md)
* [SET STATEMENT](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/set-commands/set-statement.md)
* [DECLARE Variable](declare-variable.md)