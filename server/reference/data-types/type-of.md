
# TYPE OF


# Overview


This is special declaration only available inside a stored procedure.


# EXAMPLES


```
CREATE TABLE typeof_table(
  descr VARCHAR(20),
  val INT
);
```

```
INSERT INTO typeof_table VALUES ('Life', 42);
```

```
DELIMITER $$
CREATE PROCEDURE typeof_proc()
BEGIN
  DECLARE descr TYPE OF typeof_table.descr;
  DECLARE val TYPE OF typeof_table.val;
  SELECT * INTO descr, val FROM typeof_table;
  SELECT descr, val;
END;
$$
DELIMITER ;
```

```
CALL typeof_proc();

+-------+------+
| descr | val  |
+-------+------+
| Life  |   42 |
+-------+------+
```


Copyright © 2025 MariaDB


{% @marketo/form formId="4316" %}
