
# INTEGER

## Syntax


```
INTEGER[(M)] [SIGNED | UNSIGNED | ZEROFILL]
```

## Description


This type is a synonym for [INT](../../../../general-resources/learning-and-training/video-presentations-and-screencasts/interviews-related-to-mariadb.md).


## EXAMPLES


```
CREATE TABLE integer_example (
  example INTEGER
);
```

```
SHOW CREATE TABLE integer_example\G

*************************** 1. row ***************************
       Table: integer_example
Create Table: CREATE TABLE `integer_example` (
  `example` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```
