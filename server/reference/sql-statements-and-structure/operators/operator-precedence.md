
# Operator Precedence

The precedence is the order in which the SQL operators are evaluated.


The following list shows the SQL operator precedence. Operators that appear first in the list have a higher precedence. Operators which are listed together have the same precedence.


* `[INTERVAL](../sql-statements/built-in-functions/date-time-functions/date-and-time-units.md)`
* `[BINARY](../sql-statements/built-in-functions/string-functions/binary-operator.md)`, `[COLLATE](../../data-types/string-data-types/character-sets/setting-character-sets-and-collations.md#literals)`
* `[!](../../mariadb-internals/mariadb-internals-documentation-query-optimizer/notes-when-an-index-cannot-be-used.md)`
* `[-](arithmetic-operators/subtraction-operator-.md)` (unary minus), [bitwise not](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/bitwise-not.md) () (unary bit inversion)
* `||` (string concatenation)
* `[^](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/bitwise-xor.md)`
* `[*](../sql-statements/built-in-functions/numeric-functions/multiplication-operator.md)`, `[/](../sql-statements/built-in-functions/numeric-functions/division-operator.md)`, `[DIV](../sql-statements/built-in-functions/numeric-functions/div.md)`, `[%](arithmetic-operators/modulo-operator.md)`, `[MOD](../sql-statements/built-in-functions/numeric-functions/mod.md)`
* `[-](arithmetic-operators/subtraction-operator-.md)`, `[+](../sql-statements/built-in-functions/numeric-functions/addition-operator.md)`
* `[<<](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/shift-left.md)`, `[>>](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/shift-right.md)`
* `[&](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/bitwise_and.md)`
* `[|](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/bitwise-or.md)`
* `[LIKE](../sql-statements/built-in-functions/string-functions/like.md)`, `[REGEXP](../sql-statements/built-in-functions/string-functions/regular-expressions-functions/regexp.md)`, `[IN](../../../../columnstore/columnstore-getting-started/preparing-and-installing-mariadb-columnstore-11x/installing-and-configuring-a-multi-server-columnstore-system-11x.md)`
* `[BETWEEN](comparison-operators/between-and.md)`
* `[=](../geographic-geometric-features/geometry-relations/equals.md)` (comparison), `[<=>](comparison-operators/null-safe-equal.md)`, `[>=](comparison-operators/greater-than-or-equal.md)`, `[>](comparison-operators/greater-than-or-equal.md)`, `[<=](comparison-operators/less-than-or-equal.md)`, `[<](comparison-operators/less-than.md)`, `[<>](comparison-operators/not-equal.md)`, `[!=](comparison-operators/not-equal.md)`, `[IS](../geographic-geometric-features/geometry-properties/isclosed.md)`
* `[NOT](../../mariadb-internals/mariadb-internals-documentation-query-optimizer/notes-when-an-index-cannot-be-used.md)`
* `[&&](logical-operators/and.md)`, `[AND](logical-operators/and.md)`
* `[XOR](logical-operators/xor.md)`
* `[||](../sql-statements/built-in-functions/string-functions/ord.md)` (logical or), `[OR](../sql-statements/built-in-functions/string-functions/ord.md)`
* `[=](assignment-operators/assignment-operators-assignment-operator.md)` (assignment), `[:=](assignment-operators/assignment-operators-assignment-operator.md)`


Functions precedence is always higher than operators precedence.


In this page `CASE` refers to the [CASE operator](../sql-statements/built-in-functions/control-flow-functions/case-operator.md), not to the [CASE statement](../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/case-statement.md)`.`


If the `HIGH_NOT_PRECEDENCE` [SQL_MODE](../../../server-management/variables-and-modes/sql-mode.md) is set, `NOT` has the same precedence as `!`.


The `||` operator's precedence, as well as its meaning, depends on the `PIPES_AS_CONCAT` [SQL_MODE](../../../server-management/variables-and-modes/sql-mode.md) flag: if it is on, `||` can be used to concatenate strings (like the [CONCAT()](../sql-statements/built-in-functions/string-functions/concat_ws.md) function) and has a higher precedence.


The `=` operator's precedence depends on the context - it is higher when `=` is used as a comparison operator.


[Parenthesis](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/parentheses.md) can be used to modify the operators precedence in an expression.


## Short-circuit evaluation


The `AND`, `OR`, `&&` and `||` operators support short-circuit evaluation. This means that, in some cases, the expression on the right of those operators is not evaluated, because its result cannot affect the result. In the following cases, short-circuit evaluation is used and `x()` is not evaluated:


* `FALSE AND x()`
* `FALSE && x()`
* `TRUE OR x()`
* `TRUE || x()`
* `NULL BETWEEN x() AND x()`


Note however that the short-circuit evaluation does *not* apply to `NULL AND x()`. Also, `BETWEEN`'s right operands are not evaluated if the left operand is `NULL`, but in all other cases all the operands are evaluated.


This is a speed optimization. Also, since functions can have side-effects, this behavior can be used to choose whether execute them or not using a concise syntax:


```
SELECT some_function() OR log_error();
```
