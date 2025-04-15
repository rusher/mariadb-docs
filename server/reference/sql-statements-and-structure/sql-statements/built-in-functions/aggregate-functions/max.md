
# MAX

## Syntax


```
MAX([DISTINCT] expr)
```


## Description


Returns the largest, or maximum, value of *`<code>expr</code>`*. `<code>MAX()</code>` can also take a string
argument in which case it returns the maximum string value. The `<code>DISTINCT</code>`
keyword can be used to find the maximum of the distinct values of *`<code>expr</code>`*,
however, this produces the same result as omitting `<code>DISTINCT</code>`.


Note that [SET](../../../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md) and [ENUM](../../../../data-types/string-data-types/enum.md) fields are currently compared by their string value rather than their relative position in the set, so MAX() may produce a different highest result than ORDER BY DESC.


It is an [aggregate function](../special-functions/window-functions/aggregate-functions-as-window-functions.md), and so can be used with the [GROUP BY](../../data-manipulation/selecting-data/group-by.md) clause.


MAX() can be used as a [window function](../special-functions/window-functions/window-functions-overview.md).


`<code>MAX()</code>` returns `<code>NULL</code>` if there were no matching rows.


From [MariaDB 11.4](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-114.md), not only ascending but also [descending indexes](../../../vectors/create-table-with-vectors.md#index-types) can be used to optimize MAX.


## Examples


```
CREATE TABLE student (name CHAR(10), test CHAR(10), score TINYINT); 

INSERT INTO student VALUES 
  ('Chun', 'SQL', 75), ('Chun', 'Tuning', 73), 
  ('Esben', 'SQL', 43), ('Esben', 'Tuning', 31), 
  ('Kaolin', 'SQL', 56), ('Kaolin', 'Tuning', 88), 
  ('Tatiana', 'SQL', 87), ('Tatiana', 'Tuning', 83);

SELECT name, MAX(score) FROM student GROUP BY name;
+---------+------------+
| name    | MAX(score) |
+---------+------------+
| Chun    |         75 |
| Esben   |         43 |
| Kaolin  |         88 |
| Tatiana |         87 |
+---------+------------+
```

MAX string:


```
SELECT MAX(name) FROM student;
+-----------+
| MAX(name) |
+-----------+
| Tatiana   |
+-----------+
```

Be careful to avoid this common mistake, not grouping correctly and returning mismatched data:


```
SELECT name,test,MAX(SCORE) FROM student;
+------+------+------------+
| name | test | MAX(SCORE) |
+------+------+------------+
| Chun | SQL  |         88 |
+------+------+------------+
```

Difference between ORDER BY DESC and MAX():


```
CREATE TABLE student2(name CHAR(10),grade ENUM('b','c','a'));

INSERT INTO student2 VALUES('Chun','b'),('Esben','c'),('Kaolin','a');

SELECT MAX(grade) FROM student2;
+------------+
| MAX(grade) |
+------------+
| c          |
+------------+

SELECT grade FROM student2 ORDER BY grade DESC LIMIT 1;
+-------+
| grade |
+-------+
| a     |
+-------+
```

As a [window function](../special-functions/window-functions/window-functions-overview.md):


```
CREATE OR REPLACE TABLE student_test (name CHAR(10), test CHAR(10), score TINYINT);
INSERT INTO student_test VALUES 
    ('Chun', 'SQL', 75), ('Chun', 'Tuning', 73), 
    ('Esben', 'SQL', 43), ('Esben', 'Tuning', 31), 
    ('Kaolin', 'SQL', 56), ('Kaolin', 'Tuning', 88), 
    ('Tatiana', 'SQL', 87);

SELECT name, test, score, MAX(score) 
  OVER (PARTITION BY name) AS highest_score FROM student_test;
+---------+--------+-------+---------------+
| name    | test   | score | highest_score |
+---------+--------+-------+---------------+
| Chun    | SQL    |    75 |            75 |
| Chun    | Tuning |    73 |            75 |
| Esben   | SQL    |    43 |            43 |
| Esben   | Tuning |    31 |            43 |
| Kaolin  | SQL    |    56 |            88 |
| Kaolin  | Tuning |    88 |            88 |
| Tatiana | SQL    |    87 |            87 |
+---------+--------+-------+---------------+
```

## See Also


* [AVG](avg.md) (average)
* [MIN](../../../../mariadb-internals/mariadb-internals-documentation-query-optimizer/minmax-optimization.md) (minimum)
* [SUM](sum.md) (sum total)
* [MIN/MAX optimization](../../../../mariadb-internals/mariadb-internals-documentation-query-optimizer/minmax-optimization.md) used by the optimizer
* [GREATEST()](../../../operators/comparison-operators/greatest.md) returns the largest value from a list

