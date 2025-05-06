
# NCHAR VARCHAR


# Overview


See [NATIONAL VARCHAR](national-varchar.md).


# EXAMPLES


```
CREATE TABLE nchar_varchar_example (
  example NCHAR VARCHAR(32)
);
```

```
SHOW CREATE TABLE nchar_varchar_example\G
```

```
*************************** 1. row ***************************
       Table: nchar_varchar_example
Create Table: CREATE TABLE `nchar_varchar_example` (
  `example` varchar(32) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```


Copyright © 2025 MariaDB

