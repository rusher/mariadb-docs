# MIN

#

# Syntax

```
MIN([DISTINCT] expr)
```

#

# Description

Returns the minimum value of *`expr`*. `MIN()` may take a string
argument, in which case it returns the minimum string value. The `DISTINCT`
keyword can be used to find the minimum of the distinct values of *`expr`*,
however, this produces the same result as omitting `DISTINCT`.

Note that [SET](../../../../../server-usage/replication-cluster-multi-master/standard-replication/setting-up-replication.md) and [ENUM](../../../../data-types/string-data-types/enum.md) fields are currently compared by their string value rather than their relative position in the set, so MIN() may produce a different lowest result than ORDER BY ASC.

It is an [aggregate function](../special-functions/window-functions/aggregate-functions-as-window-functions.md), and so can be used with the [GROUP BY](../../data-manipulation/selecting-data/group-by.md) clause.

`MIN()` can be used as a [window function](../special-functions/window-functions/window-functions-overview.md).

`MIN()` returns `NULL` if there were no matching rows.

From [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-114), not only ascending but also [descending indexes](../../data-definition/create/create-tablespace.md#index-types) can be used to optimize MIN.

#

# Examples

```
CREATE TABLE student (name CHAR(10), test CHAR(10), score TINYINT); 

INSERT INTO student VALUES 
 ('Chun', 'SQL', 75), ('Chun', 'Tuning', 73), 
 ('Esben', 'SQL', 43), ('Esben', 'Tuning', 31), 
 ('Kaolin', 'SQL', 56), ('Kaolin', 'Tuning', 88), 
 ('Tatiana', 'SQL', 87), ('Tatiana', 'Tuning', 83);

SELECT name, MIN(score) FROM student GROUP BY name;
+---------+------------+
| name | MIN(score) |
+---------+------------+
| Chun | 73 |
| Esben | 31 |
| Kaolin | 56 |
| Tatiana | 83 |
+---------+------------+
```

MIN() with a string:

```
SELECT MIN(name) FROM student;
+-----------+
| MIN(name) |
+-----------+
| Chun |
+-----------+
```

Be careful to avoid this common mistake, not grouping correctly and returning mismatched data:

```
SELECT name,test,MIN(score) FROM student;
+------+------+------------+
| name | test | MIN(score) |
+------+------+------------+
| Chun | SQL | 31 |
+------+------+------------+
```

Difference between ORDER BY ASC and MIN():

```
CREATE TABLE student2(name CHAR(10),grade ENUM('b','c','a'));

INSERT INTO student2 VALUES('Chun','b'),('Esben','c'),('Kaolin','a');

SELECT MIN(grade) FROM student2;
+------------+
| MIN(grade) |
+------------+
| a |
+------------+

SELECT grade FROM student2 ORDER BY grade ASC LIMIT 1;
+-------+
| grade |
+-------+
| b |
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

SELECT name, test, score, MIN(score) 
 OVER (PARTITION BY name) AS lowest_score FROM student_test;
+---------+--------+-------+--------------+
| name | test | score | lowest_score |
+---------+--------+-------+--------------+
| Chun | SQL | 75 | 73 |
| Chun | Tuning | 73 | 73 |
| Esben | SQL | 43 | 31 |
| Esben | Tuning | 31 | 31 |
| Kaolin | SQL | 56 | 56 |
| Kaolin | Tuning | 88 | 56 |
| Tatiana | SQL | 87 | 87 |
+---------+--------+-------+--------------+
```

#

# See Also

* [AVG](avg.md) (average)
* [MAX](../../../../../security/user-account-management/limiting-size-of-created-disk-temporary-files-and-tables/max_tmp_total_space_usage-system-variable.md) (maximum)
* [SUM](sum.md) (sum total)
* [MIN/MAX optimization](https://app.gitbook.com/s/iJPrPCGi329TSR8WIXJW/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/mariadb-internals-documentation/mariadb-internals-documentation-query-optimizer/minmax-optimization) used by the optimizer
* [LEAST()](../../../operators/comparison-operators/least.md) returns the smallest value from a list.