# Operator Precedence

The precedence is the order in which the SQL operators are evaluated.

The following list shows the SQL operator precedence. Operators that appear first in the list have a higher precedence. Operators which are listed together have the same precedence.

* `[INTERVAL](../sql-statements/built-in-functions/date-time-functions/date-and-time-units.md)`
* `[BINARY](../sql-statements/built-in-functions/string-functions/binary-operator.md)`, `[COLLATE](../../data-types/string-data-types/character-sets/setting-character-sets-and-collations.md#literals)`
* `[!](logical-operators/not.md)`
* `[-](arithmetic-operators/subtraction-operator-.md)` (unary minus), [bitwise not](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/bitwise-not.md) () (unary bit inversion)
* `||` (string concatenation)
* `[^](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/bitwise-xor.md)`
* `[*](../sql-statements/built-in-functions/numeric-functions/multiplication-operator.md)`, `[/](../sql-statements/built-in-functions/numeric-functions/division-operator.md)`, `[DIV](../sql-statements/built-in-functions/numeric-functions/div.md)`, `[%](arithmetic-operators/modulo-operator.md)`, `[MOD](../sql-statements/built-in-functions/numeric-functions/mod.md)`
* `[-](arithmetic-operators/subtraction-operator-.md)`, `[+](../sql-statements/built-in-functions/numeric-functions/addition-operator.md)`
* `[<<](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/shift-left.md)`, `[>>](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/shift-right.md)`
* `[&](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/bitwise_and.md)`
* `[|](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/bitwise-or.md)`
* `[LIKE](../sql-statements/built-in-functions/string-functions/like.md)`, `[REGEXP](../sql-statements/built-in-functions/string-functions/regular-expressions-functions/regexp.md)`, `[IN](comparison-operators/in.md)`
* `[BETWEEN](comparison-operators/between-and.md)`
* `[=](comparison-operators/equal.md)` (comparison), `[<=>](comparison-operators/null-safe-equal.md)`, `[>=](comparison-operators/greater-than-or-equal.md)`, `[>](comparison-operators/greater-than.md)`, `[<=](comparison-operators/less-than-or-equal.md)`, `[<](comparison-operators/less-than.md)`, `[<>](comparison-operators/not-equal.md)`, `[!=](comparison-operators/not-equal.md)`, `[IS](comparison-operators/is.md)`
* `[NOT](logical-operators/not.md)`
* `[&&](logical-operators/and.md)`, `[AND](logical-operators/and.md)`
* `[XOR](logical-operators/xor.md)`
* `[||](logical-operators/or.md)` (logical or), `[OR](logical-operators/or.md)`
* `[=](assignment-operators/assignment-operators-assignment-operator.md)` (assignment), `[:=](assignment-operators/assignment-operator.md)`

Functions precedence is always higher than operators precedence.

In this page `CASE` refers to the [CASE operator](../sql-statements/built-in-functions/control-flow-functions/case-operator.md), not to the [CASE statement](../../../server-usage/programmatic-compound-statements/case-statement.md)`.`

If the `HIGH_NOT_PRECEDENCE` [SQL\_MODE](../../../server-management/variables-and-modes/sql-mode.md) is set, `NOT` has the same precedence as `!`.

The `||` operator's precedence, as well as its meaning, depends on the `PIPES_AS_CONCAT` [SQL\_MODE](../../../server-management/variables-and-modes/sql-mode.md) flag: if it is on, `||` can be used to concatenate strings (like the [CONCAT()](../sql-statements/built-in-functions/string-functions/concat.md) function) and has a higher precedence.

The `=` operator's precedence depends on the context - it is higher when `=` is used as a comparison operator.

[Parenthesis](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/parentheses.md) can be used to modify the operators precedence in an expression.

## Short-circuit evaluation

The `AND`, `OR`, `&&` and `||` operators support short-circuit evaluation. This means that, in some cases, the expression on the right of those operators is not evaluated, because its result cannot affect the result. In the following cases, short-circuit evaluation is used and `x()` is not evaluated:

* `FALSE AND x()`
* `FALSE && x()`
* `TRUE OR x()`
* `TRUE || x()`
* `NULL BETWEEN x() AND x()`

Note however that the short-circuit evaluation does _not_ apply to `NULL AND x()`. Also, `BETWEEN`'s right operands are not evaluated if the left operand is `NULL`, but in all other cases all the operands are evaluated.

This is a speed optimization. Also, since functions can have side-effects, this behavior can be used to choose whether execute them or not using a concise syntax:

```
SELECT some_function() OR log_error();
```

CC BY-SA / Gnu FDL
