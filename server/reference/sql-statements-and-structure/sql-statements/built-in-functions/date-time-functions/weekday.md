
# WEEKDAY

## Syntax


```
WEEKDAY(date)
```

## Description


Returns the weekday index for `<code>date</code>` 
(`<code>0</code>` = Monday, `<code>1</code>` = Tuesday, ... `<code>6</code>` = Sunday).


This contrasts with `<code>[DAYOFWEEK()](dayofweek.md)</code>` which follows the ODBC standard
(`<code>1</code>` = Sunday, `<code>2</code>` = Monday, ..., `<code>7</code>` = Saturday).


## Examples


```
SELECT WEEKDAY('2008-02-03 22:23:00');
+--------------------------------+
| WEEKDAY('2008-02-03 22:23:00') |
+--------------------------------+
|                              6 |
+--------------------------------+

SELECT WEEKDAY('2007-11-06');
+-----------------------+
| WEEKDAY('2007-11-06') |
+-----------------------+
|                     1 |
+-----------------------+
```

```
CREATE TABLE t1 (d DATETIME);
INSERT INTO t1 VALUES
    ("2007-01-30 21:31:07"),
    ("1983-10-15 06:42:51"),
    ("2011-04-21 12:34:56"),
    ("2011-10-30 06:31:41"),
    ("2011-01-30 14:03:25"),
    ("2004-10-07 11:19:34");
```

```
SELECT d FROM t1 where WEEKDAY(d) = 6;
+---------------------+
| d                   |
+---------------------+
| 2011-10-30 06:31:41 |
| 2011-01-30 14:03:25 |
+---------------------+
```
