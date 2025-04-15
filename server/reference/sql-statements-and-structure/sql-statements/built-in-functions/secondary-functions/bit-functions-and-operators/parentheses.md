
# Parentheses

Parentheses are sometimes called precedence operators - this means that they can be used to change the other [operator's precedence](../../../../operators/operator-precedence.md) in an expression. The expressions that are written between parentheses are computed before the expressions that are written outside. Parentheses must always contain an expression (that is, they cannot be empty), and can be nested.


For example, the following expressions could return different results:


* `<code>NOT a OR b</code>`
* `<code>NOT (a OR b)</code>`


In the first case, `<code>NOT</code>` applies to `<code>a</code>`, so if `<code>a</code>` is `<code>FALSE</code>` or `<code>b</code>` is `<code>TRUE</code>`, the expression returns `<code>TRUE</code>`. In the second case, `<code>NOT</code>` applies to the result of `<code>a OR b</code>`, so if at least one of `<code>a</code>` or `<code>b</code>` is `<code>TRUE</code>`, the expression is `<code>TRUE</code>`.


When the precedence of operators is not intuitive, you can use parentheses to make it immediately clear for whoever reads the statement.


The precedence of the `<code>NOT</code>` operator can also be affected by the `<code>HIGH_NOT_PRECEDENCE</code>` [SQL_MODE](../../../../../../server-management/variables-and-modes/sql-mode.md) flag.


## Other uses


Parentheses must always be used to enclose [subqueries](../../../data-manipulation/selecting-data/joins-subqueries/subqueries/subqueries-and-all.md).


Parentheses can also be used in a `<code>[JOIN](../../../../../../../general-resources/learning-and-training/training-and-tutorials/basic-mariadb-articles/joining-tables-with-join-clauses.md)</code>` statement between multiple tables to determine which tables must be joined first.


Also, parentheses are used to enclose the list of parameters to be passed to built-in functions, user-defined functions and stored routines. However, when no parameter is passed to a stored procedure, parentheses are optional. For builtin functions and user-defined functions, spaces are not allowed between the function name and the open parenthesis, unless the `<code>IGNORE_SPACE</code>` [SQL_MODE](../../../../../../server-management/variables-and-modes/sql-mode.md) is set. For stored routines (and for functions if `<code>IGNORE_SPACE</code>` is set) spaces are allowed before the open parenthesis, including tab characters and new line characters.


## Syntax errors


If there are more open parentheses than closed parentheses, the error usually looks like this:


```
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that
corresponds to your MariaDB server version for the right syntax to use near '' a
t line 1
```

Note the empty string.


If there are more closed parentheses than open parentheses, the error usually looks like this:


```
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that
corresponds to your MariaDB server version for the right syntax to use near ')'
at line 1
```

Note the quoted closed parenthesis.

