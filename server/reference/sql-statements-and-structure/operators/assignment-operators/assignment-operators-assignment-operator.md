
# Assignment Operator (=)

## Syntax


```
identifier = expr
```


## Description


The equal sign is used as both an assignment operator in certain contexts, and as a [comparison operator](../../geographic-geometric-features/geometry-relations/equals.md). When used as assignment operator, the value on the right is assigned to the variable (or column, in some contexts) on the left.


Since its use can be ambiguous, unlike the [:= assignment operator](assignment-operators-assignment-operator.md), the *`=`* assignment operator cannot be used in all contexts, and is only valid as part of a [SET](../../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md) statement, or the SET clause of an [UPDATE](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/tools/buildbot/buildbot-setup/buildbot-setup-for-virtual-machines/buildbot-setup-for-virtual-machines-additional-steps/update-debian-4-mirrors-for-buildbot-vms.md) statement


This operator works with both [user-defined variables](../../sql-language-structure/user-defined-variables.md) and [local variables](../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/declare-variable.md).


## Examples


```
UPDATE table_name SET x = 2 WHERE x > 100;
```

```
SET @x = 1, @y := 2;
```

## See Also


* [Operator Precedence](../operator-precedence.md)

