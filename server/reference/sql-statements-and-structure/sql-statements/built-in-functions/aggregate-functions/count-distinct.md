
# COUNT DISTINCT

## Syntax


```
COUNT(DISTINCT expr,[expr...])
```


## Description


Returns a count of the number of different non-NULL values.


COUNT(DISTINCT) returns 0 if there were no matching rows.


Although, from [MariaDB 10.2.0](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1020-release-notes.md), [COUNT](count.md) can be used as a [window function](../special-functions/window-functions/window-functions-overview.md), COUNT DISTINCT cannot be.


## Examples


```
CREATE TABLE student (name CHAR(10), test CHAR(10), score TINYINT); 

INSERT INTO student VALUES 
  ('Chun', 'SQL', 75), ('Chun', 'Tuning', 73), 
  ('Esben', 'SQL', 43), ('Esben', 'Tuning', 31), 
  ('Kaolin', 'SQL', 56), ('Kaolin', 'Tuning', 88), 
  ('Tatiana', 'SQL', 87), ('Tatiana', 'Tuning', 83);

SELECT COUNT(*) FROM student;
+----------+
| COUNT(*) |
+----------+
|        8 |
+----------+

SELECT COUNT(DISTINCT (name)) FROM student;
+------------------------+
| COUNT(DISTINCT (name)) |
+------------------------+
|                      4 |
+------------------------+
```

## See Also


* [SELECT](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md)
* [COUNT](count.md)

