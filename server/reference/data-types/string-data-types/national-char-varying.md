
# NATIONAL CHAR VARYING


# Overview


See [NATIONAL VARCHAR](national-char.md).


# EXAMPLES


```
CREATE TABLE national_char_varying_example (
  example NATIONAL CHAR VARYING(32)
);
```

```
SHOW CREATE TABLE national_char_varying_example\G
```

```
*************************** 1. row ***************************
       Table: national_char_varying_example
Create Table: CREATE TABLE `national_char_varying_example` (
  `example` varchar(32) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```


Copyright © 2025 MariaDB


{% @marketo/form formId="4316" %}
