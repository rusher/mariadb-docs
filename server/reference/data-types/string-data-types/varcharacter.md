
# VARCHARACTER


# Overview


See [VARCHAR](varchar.md).


# EXAMPLES


```
CREATE TABLE varcharacter_example (
  example VARCHARACTER(32)
);
```

```
SHOW CREATE TABLE varcharacter_example\G

*************************** 1. row ***************************
       Table: varcharacter_example
Create Table: CREATE TABLE `varcharacter_example` (
  `example` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```


Copyright © 2025 MariaDB

