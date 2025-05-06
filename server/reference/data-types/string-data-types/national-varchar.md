
# NATIONAL VARCHAR


# Overview


Variable-length string of specific character set with limit up to 65,535 bytes.


# EXAMPLES


```
CREATE TABLE national_varchar_example (
  example NATIONAL VARCHAR(32)
);
```

```
SHOW CREATE TABLE national_varchar_example\G
```

```
*************************** 1. row ***************************
       Table: national_varchar_example
Create Table: CREATE TABLE `national_varchar_example` (
  `example` varchar(32) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```


Copyright © 2025 MariaDB

