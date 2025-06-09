
# ROW TYPE OF


# Overview


This is special declaration only available inside a stored procedure.


# EXAMPLES


```
CREATE TABLE rowtypeof_table(
  descr VARCHAR(20),
  val INT
);
```

```
INSERT INTO rowtypeof_table VALUES ('Life', 42);
```

```
DELIMITER $$
CREATE PROCEDURE rowtypeof_proc()
BEGIN
  DECLARE rec1 ROW TYPE OF rowtypeof_table;
  SELECT * INTO rec1 FROM rowtypeof_table;
  SELECT rec1.descr, rec1.val;
END;
$$
DELIMITER ;
```

```
CALL rowtypeof_proc();

+------------+----------+
| rec1.descr | rec1.val |
+------------+----------+
| Life       |       42 |
+------------+----------+
```


Copyright © 2025 MariaDB


{% @marketo/form formId="4316" %}
