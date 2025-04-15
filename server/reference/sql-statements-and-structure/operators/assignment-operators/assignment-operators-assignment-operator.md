# Assignment Operator (=)

#

# Syntax

```
identifier = expr
```

#

# Description

The equal sign is used as both an assignment operator in certain contexts, and as a [comparison operator](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/equality-propagation-optimization.md). When used as assignment operator, the value on the right is assigned to the variable (or column, in some contexts) on the left.

Since its use can be ambiguous, unlike the [:= assignment operator](assignment-operators-assignment-operator.md), the *`=`* assignment operator cannot be used in all contexts, and is only valid as part of a [SET](../../../../server-usage/replication-cluster-multi-master/standard-replication/setting-up-replication.md) statement, or the SET clause of an [UPDATE](../../sql-statements/data-manipulation/changing-deleting-data/update.md) statement

This operator works with both [user-defined variables](../../sql-language-structure/user-defined-variables.md) and [local variables](../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/declare-variable.md).

#

# Examples

```
UPDATE table_name SET x = 2 WHERE x > 100;
```

```
SET @x = 1, @y := 2;
```

#

# See Also

* [Operator Precedence](../operator-precedence.md)