
# LONG CHARACTER VARYING


# Overview


See [MEDIUMTEXT](data-types-mediumtext).


# EXAMPLES


```
CREATE TABLE long_character_varying_example (
  example LONG CHARACTER VARYING
);
```

```
SHOW CREATE TABLE long_character_varying_example\G
```

```
*************************** 1. row ***************************
       Table: long_character_varying_example
Create Table: CREATE TABLE `long_character_varying_example` (
  `example` mediumtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```


Copyright © 2025 MariaDB

