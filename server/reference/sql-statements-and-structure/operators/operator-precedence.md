
# Operator Precedence

The precedence is the order in which the SQL operators are evaluated.


The following list shows the SQL operator precedence. Operators that appear first in the list have a higher precedence. Operators which are listed together have the same precedence.


* `<code>[INTERVAL](../sql-statements/built-in-functions/date-time-functions/date-and-time-units.md)</code>`
* `<code>[BINARY](../sql-statements/built-in-functions/string-functions/binary-operator.md)</code>`, `<code>[COLLATE](../../data-types/string-data-types/character-sets/setting-character-sets-and-collations.md#literals)</code>`
* `<code>[!](../../mariadb-internals/mariadb-internals-documentation-query-optimizer/notes-when-an-index-cannot-be-used.md)</code>`
* `<code>[-](arithmetic-operators/subtraction-operator-.md)</code>` (unary minus), [bitwise not](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/bitwise-not.md) () (unary bit inversion)
* `<code>||</code>` (string concatenation)
* `<code>[^](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/bitwise-xor.md)</code>`
* `<code>[*](../sql-statements/built-in-functions/numeric-functions/multiplication-operator.md)</code>`, `<code>[/](../sql-statements/built-in-functions/numeric-functions/division-operator.md)</code>`, `<code>[DIV](../sql-statements/built-in-functions/numeric-functions/div.md)</code>`, `<code>[%](arithmetic-operators/modulo-operator.md)</code>`, `<code>[MOD](../sql-statements/built-in-functions/numeric-functions/mod.md)</code>`
* `<code>[-](arithmetic-operators/subtraction-operator-.md)</code>`, `<code>[+](../sql-statements/built-in-functions/numeric-functions/addition-operator.md)</code>`
* `<code>[<<](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/shift-left.md)</code>`, `<code>[>>](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/shift-right.md)</code>`
* `<code>[&](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/bitwise_and.md)</code>`
* `<code>[|](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/bitwise-or.md)</code>`
* `<code>[LIKE](../sql-statements/built-in-functions/string-functions/like.md)</code>`, `<code>[REGEXP](../sql-statements/built-in-functions/string-functions/regular-expressions-functions/regexp.md)</code>`, `<code>[IN](../../../../columnstore/columnstore-getting-started/preparing-and-installing-mariadb-columnstore-11x/installing-and-configuring-a-multi-server-columnstore-system-11x.md)</code>`
* `<code>[BETWEEN](comparison-operators/between-and.md)</code>`
* `<code>[=](../geographic-geometric-features/geometry-relations/equals.md)</code>` (comparison), `<code>[<=>](comparison-operators/null-safe-equal.md)</code>`, `<code>[>=](comparison-operators/greater-than-or-equal.md)</code>`, `<code>[>](comparison-operators/greater-than-or-equal.md)</code>`, `<code>[<=](comparison-operators/less-than-or-equal.md)</code>`, `<code>[<](comparison-operators/less-than.md)</code>`, `<code>[<>](comparison-operators/not-equal.md)</code>`, `<code>[!=](comparison-operators/not-equal.md)</code>`, `<code>[IS](../geographic-geometric-features/geometry-properties/isclosed.md)</code>`
* `<code>[NOT](../../mariadb-internals/mariadb-internals-documentation-query-optimizer/notes-when-an-index-cannot-be-used.md)</code>`
* `<code>[&&](logical-operators/and.md)</code>`, `<code>[AND](logical-operators/and.md)</code>`
* `<code>[XOR](logical-operators/xor.md)</code>`
* `<code>[||](../sql-statements/built-in-functions/string-functions/ord.md)</code>` (logical or), `<code>[OR](../sql-statements/built-in-functions/string-functions/ord.md)</code>`
* `<code>[=](assignment-operators/assignment-operators-assignment-operator.md)</code>` (assignment), `<code>[:=](assignment-operators/assignment-operators-assignment-operator.md)</code>`


Functions precedence is always higher than operators precedence.


In this page `<code>CASE</code>` refers to the [CASE operator](../sql-statements/built-in-functions/control-flow-functions/case-operator.md), not to the [CASE statement](../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/case-statement.md)`<code>.</code>`


If the `<code>HIGH_NOT_PRECEDENCE</code>` [SQL_MODE](../../../server-management/variables-and-modes/sql-mode.md) is set, `<code>NOT</code>` has the same precedence as `<code>!</code>`.


The `<code>||</code>` operator's precedence, as well as its meaning, depends on the `<code>PIPES_AS_CONCAT</code>` [SQL_MODE](../../../server-management/variables-and-modes/sql-mode.md) flag: if it is on, `<code>||</code>` can be used to concatenate strings (like the [CONCAT()](../sql-statements/built-in-functions/string-functions/concat_ws.md) function) and has a higher precedence.


The `<code>=</code>` operator's precedence depends on the context - it is higher when `<code>=</code>` is used as a comparison operator.


[Parenthesis](../sql-statements/built-in-functions/secondary-functions/bit-functions-and-operators/parentheses.md) can be used to modify the operators precedence in an expression.


## Short-circuit evaluation


The `<code>AND</code>`, `<code>OR</code>`, `<code>&&</code>` and `<code>||</code>` operators support short-circuit evaluation. This means that, in some cases, the expression on the right of those operators is not evaluated, because its result cannot affect the result. In the following cases, short-circuit evaluation is used and `<code>x()</code>` is not evaluated:


* `<code>FALSE AND x()</code>`
* `<code>FALSE && x()</code>`
* `<code>TRUE OR x()</code>`
* `<code>TRUE || x()</code>`
* `<code>NULL BETWEEN x() AND x()</code>`


Note however that the short-circuit evaluation does *not* apply to `<code>NULL AND x()</code>`. Also, `<code>BETWEEN</code>`'s right operands are not evaluated if the left operand is `<code>NULL</code>`, but in all other cases all the operands are evaluated.


This is a speed optimization. Also, since functions can have side-effects, this behavior can be used to choose whether execute them or not using a concise syntax:


```
SELECT some_function() OR log_error();
```
