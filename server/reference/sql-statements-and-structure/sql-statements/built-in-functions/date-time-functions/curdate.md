
# CURDATE

## Syntax


```
CURDATE()
CURRENT_DATE
CURRENT_DATE()
```

## Description


`<code>CURDATE</code>` returns the current date as a value in 'YYYY-MM-DD' or YYYYMMDD
format, depending on whether the function is used in a string or
numeric context.


`<code>CURRENT_DATE</code>` and `<code>CURRENT_DATE()</code>` are synonyms.


## Examples


```
SELECT CURDATE();
+------------+
| CURDATE()  |
+------------+
| 2019-03-05 |
+------------+
```

In a numeric context (note this is not performing date calculations):


```
SELECT CURDATE() +0;
+--------------+
| CURDATE() +0 |
+--------------+
|     20190305 |
+--------------+
```

Data calculation:


```
SELECT CURDATE() - INTERVAL 5 DAY;
+----------------------------+
| CURDATE() - INTERVAL 5 DAY |
+----------------------------+
| 2019-02-28                 |
+----------------------------+
```
