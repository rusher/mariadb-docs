
# RAW


# Overview


See [VARBINARY](varbinary.md).


# EXAMPLES


```
SET sql_mode='oracle';
```

```
CREATE TABLE raw_example (
  example RAW(32)
);
```

```
SHOW CREATE TABLE raw_example\G
```

```
*************************** 1. row ***************************
       Table: raw_example
Create Table: CREATE TABLE "raw_example" (
  "example" varbinary(32) DEFAULT NULL
)
```


Copyright © 2025 MariaDB


{% @marketo/form formId="4316" %}
