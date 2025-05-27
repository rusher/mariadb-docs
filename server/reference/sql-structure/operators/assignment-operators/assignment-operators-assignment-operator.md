# Assignment Operator (=)

## Syntax

```
identifier = expr
```

## Description

The equal sign is used as both an assignment operator in certain contexts, and as a [comparison operator](../comparison-operators/equal.md). When used as assignment operator, the value on the right is assigned to the variable (or column, in some contexts) on the left.

Since its use can be ambiguous, unlike the [:= assignment operator](assignment-operator.md), the _`=`_ assignment operator cannot be used in all contexts, and is only valid as part of a [SET](../../../sql-statements/administrative-sql-statements/set-commands/set.md) statement, or the SET clause of an [UPDATE](../../../sql-statements/data-manipulation/changing-deleting-data/update.md) statement

This operator works with both [user-defined variables](../../sql-language-structure/user-defined-variables.md) and [local variables](../../../../server-usage/programmatic-compound-statements/declare-variable.md).

## Examples

```
UPDATE table_name SET x = 2 WHERE x > 100;
```

```
SET @x = 1, @y := 2;
```

## See Also

* [Operator Precedence](../operator-precedence.md)

CC BY-SA / Gnu FDL
