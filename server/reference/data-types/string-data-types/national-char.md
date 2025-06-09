
# NATIONAL CHAR


# Overview


Fixed-length string of specific character set with limit up to 255 bytes.


EXAMPLES


```
CREATE TABLE national_char_example (
  example NATIONAL CHAR(32)
);
```

```
SHOW CREATE TABLE national_char_example\G
```

```
*************************** 1. row ***************************
       Table: national_char_example
Create Table: CREATE TABLE `national_char_example` (
  `example` char(32) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

# EXTERNAL REFERENCES


Additional information is available [here](varchar.md).


Copyright © 2025 MariaDB


{% @marketo/form formId="4316" %}
