# RANK

#

# Syntax

```
RANK() OVER (
 [ PARTITION BY partition_expression ]
 [ ORDER BY order_list ]
)
```

#

# Description

RANK() is a [window function](window-functions-overview.md) that displays the number of a given row, starting at one and following the [ORDER BY](../../../data-manipulation/selecting-data/order-by.md) sequence of the window function, with identical values receiving the same result. It is similar to the [ROW_NUMBER()](row_number.md) function except that in that function, identical values will receive a different row number for each result.

#

# Examples

The distinction between [DENSE_RANK()](dense_rank.md), RANK() and [ROW_NUMBER()](row_number.md):

```
CREATE TABLE student(course VARCHAR(10), mark int, name varchar(10));

INSERT INTO student VALUES 
 ('Maths', 60, 'Thulile'),
 ('Maths', 60, 'Pritha'),
 ('Maths', 70, 'Voitto'),
 ('Maths', 55, 'Chun'),
 ('Biology', 60, 'Bilal'),
 ('Biology', 70, 'Roger');

SELECT 
 RANK() OVER (PARTITION BY course ORDER BY mark DESC) AS rank, 
 DENSE_RANK() OVER (PARTITION BY course ORDER BY mark DESC) AS dense_rank, 
 ROW_NUMBER() OVER (PARTITION BY course ORDER BY mark DESC) AS row_num, 
 course, mark, name 
FROM student ORDER BY course, mark DESC;
+------+------------+---------+---------+------+---------+
| rank | dense_rank | row_num | course | mark | name |
+------+------------+---------+---------+------+---------+
| 1 | 1 | 1 | Biology | 70 | Roger |
| 2 | 2 | 2 | Biology | 60 | Bilal |
| 1 | 1 | 1 | Maths | 70 | Voitto |
| 2 | 2 | 2 | Maths | 60 | Thulile |
| 2 | 2 | 3 | Maths | 60 | Pritha |
| 4 | 3 | 4 | Maths | 55 | Chun |
+------+------------+---------+---------+------+---------+
```

#

# See Also

* [DENSE_RANK()](dense_rank.md)
* [ROW_NUMBER()](row_number.md)
* [ORDER BY](../../../data-manipulation/selecting-data/order-by.md)