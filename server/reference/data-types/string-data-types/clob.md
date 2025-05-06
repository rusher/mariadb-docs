
# CLOB


# Overview


See [LONGTEXT](longtext.md).


# EXAMPLES


```
SET sql_mode='oracle';

CREATE TABLE clob_example (
  example CLOB
);
```

```
SHOW CREATE TABLE clob_example\G
```

```
*************************** 1. row ***************************
       Table: clob_example
Create Table: CREATE TABLE "clob_example" (
  "example" longtext DEFAULT NULL
)
```


Copyright © 2025 MariaDB

