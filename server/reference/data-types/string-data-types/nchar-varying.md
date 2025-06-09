
# NCHAR VARYING


# Overview


See [NATIONAL VARCHAR](national-char.md).


# EXAMPLES


```
CREATE TABLE nchar_varying_example (
  example NCHAR VARYING(32)
);
```

```
SHOW CREATE TABLE nchar_varying_example\G
```

```
*************************** 1. row ***************************
       Table: nchar_varying_example
Create Table: CREATE TABLE `nchar_varying_example` (
  `example` varchar(32) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```


Copyright © 2025 MariaDB


{% @marketo/form formId="4316" %}
