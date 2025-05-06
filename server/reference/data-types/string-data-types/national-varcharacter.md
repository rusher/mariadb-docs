
# NATIONAL VARCHARACTER


# Overview


See [NATIONAL VARCHAR](national-char.md).


# EXAMPLES


```
CREATE TABLE national_varcharacter_example (
  example NATIONAL VARCHARACTER(32)
);
```

```
SHOW CREATE TABLE national_varcharacter_example\G
```

```
*************************** 1. row ***************************
       Table: national_varcharacter_example
Create Table: CREATE TABLE `national_varcharacter_example` (
  `example` varchar(32) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```


Copyright © 2025 MariaDB

