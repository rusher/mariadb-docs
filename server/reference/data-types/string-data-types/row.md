
# ROW


## Syntax


```
ROW (<field name> <data type> [{, <field name> <data type>}... ])
```

## Description


`<code>ROW</code>` is a data type for [stored procedure](../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md) variables.


## Features


### ROW fields as normal variables


`<code>ROW</code>` fields (members) act as normal variables, and are able to appear in all
query parts where a stored procedure variable is allowed:


* Assignment is using the `<code>:=</code>` operator and the [SET](../../../../connectors/mariadb-connector-cpp/setup-for-connector-cpp-examples.md) command:


```
a.x:= 10;
a.x:= b.x;
SET a.x= 10, a.y=20, a.z= b.z;
```

* Passing to functions and operators:


```
SELECT f1(rec.a), rec.a<10;
```

* Clauses (select list, WHERE, HAVING, LIMIT, etc...,):


```
SELECT var.a, t1.b FROM t1 WHERE t1.b=var.b LIMIT var.c;
```

* `<code>INSERT</code>` values:


```
INSERT INTO t1 VALUES (rec.a, rec.b, rec.c);
```

* `<code>SELECT .. INTO</code>` targets


```
SELECT a,b INTO rec.a, rec.b FROM t1 WHERE t1.id=10;
```

* Dynamic SQL out parameters ([EXECUTE](../../sql-statements-and-structure/sql-statements/prepared-statements/execute-statement.md) and [EXECUTE IMMEDIATE](../../sql-statements-and-structure/sql-statements/prepared-statements/execute-immediate.md))


```
EXECUTE IMMEDIATE 'CALL proc_with_out_param(?)' USING rec.a;
```

### ROW type variables as FETCH targets


`<code>ROW</code>` type variables are allowed as [FETCH](../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/programmatic-compound-statements-cursors/fetch.md) targets:


```
FETCH cur INTO rec;
```

where `<code>cur</code>` is a `<code>CURSOR</code>` and `<code>rec</code>` is a `<code>ROW</code>` type stored procedure variable.


Note, currently an attempt to use `<code>FETCH</code>` for a `<code>ROW</code>` type variable returns this error:

```
ERROR 1328 (HY000): Incorrect number of FETCH variables
```



`<code>FETCH</code>` from a cursor `<code>cur</code>` into a `<code>ROW</code>` variable `<code>rec</code>` works as follows:


* The number of fields in `<code>cur</code>` must match the number of fields in `<code>rec</code>`.
 Otherwise, an error is reported.


* Assignment is done from left to right. The first cursor field is assigned to
 the first variable field, the second cursor field is assigned to the second
 variable field, etc.


* Field names in `<code>rec</code>` are not important and can differ from field names
 in `<code>cur</code>`.


See [FETCH Examples](#fetch-examples) (below) for examples of using this with
`<code>sql_mode=ORACLE</code>` and `<code>sql_mode=DEFAULT</code>`.


### ROW type variables as `<code>SELECT...INTO</code>` targets


`<code>ROW</code>` type variables are allowed as `<code>SELECT..INTO</code>` targets with some
differences depending on which `<code>sql_mode</code>` is in use.


* When using `<code>sql_mode=ORACLE</code>`, `<code>table%ROWTYPE</code>` and `<code>cursor%ROWTYPE</code>`
 variables can be used as `<code>SELECT...INTO</code>` targets.


* Using multiple `<code>ROW</code>` variables in the `<code>SELECT..INTO</code>` list will report an
 error.


* Using `<code>ROW</code>` variables with a different column count than in
 the `<code>SELECT..INTO</code>` list will report an error.


See [SELECT...INTO Examples](#selectinto-examples) (below) for examples of
using this with `<code>sql_mode=ORACLE</code>` and `<code>sql_mode=DEFAULT</code>`.


## Features not implemented


The following features are planned, but not implemented yet:


* Returning a ROW type expression from a stored function (see [MDEV-12252](https://jira.mariadb.org/browse/MDEV-12252)). This will need some grammar change to support field names after parentheses:


```
SELECT f1().x FROM DUAL;
```

* Returning a ROW type expression from a built-in hybrid type function, such as `<code>CASE</code>`, `<code>IF</code>`, etc.
* ROW of ROWs


## Examples


### Declaring a ROW in a stored procedure


```
DELIMITER $$
CREATE PROCEDURE p1()
BEGIN
  DECLARE r ROW (c1 INT, c2 VARCHAR(10));
  SET r.c1= 10;
  SET r.c2= 'test';
  INSERT INTO t1 VALUES (r.c1, r.c2);
END;
$$
DELIMITER ;
CALL p1();
```

### FETCH Examples


A complete `<code>FETCH</code>` example for `<code>sql_mode=ORACLE</code>`:


```
DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (a INT, b VARCHAR(32));
INSERT INTO t1 VALUES (10,'b10');
INSERT INTO t1 VALUES (20,'b20');
INSERT INTO t1 VALUES (30,'b30');

SET sql_mode=oracle;
DROP PROCEDURE IF EXISTS p1;
DELIMITER $$
CREATE PROCEDURE p1 AS
  rec ROW(a INT, b VARCHAR(32));
  CURSOR c IS SELECT a,b FROM t1;
BEGIN
  OPEN c;
  LOOP
    FETCH c INTO rec;
    EXIT WHEN c%NOTFOUND;
    SELECT ('rec=(' || rec.a ||','|| rec.b||')');
  END LOOP;
  CLOSE c;
END;
$$
DELIMITER ;
CALL p1();
```

A complete `<code>FETCH</code>` example for `<code>sql_mode=DEFAULT</code>`:


```
DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (a INT, b VARCHAR(32));
INSERT INTO t1 VALUES (10,'b10');
INSERT INTO t1 VALUES (20,'b20');
INSERT INTO t1 VALUES (30,'b30');

SET sql_mode=DEFAULT;
DROP PROCEDURE IF EXISTS p1;
DELIMITER $$
CREATE PROCEDURE p1()
BEGIN
  DECLARE done INT DEFAULT FALSE;
  DECLARE rec ROW(a INT, b VARCHAR(32));
  DECLARE c CURSOR FOR SELECT a,b FROM t1;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  OPEN c;
read_loop:
  LOOP
    FETCH c INTO rec;
    IF done THEN
      LEAVE read_loop;
    END IF;
    SELECT CONCAT('rec=(',rec.a,',',rec.b,')');
  END LOOP;
  CLOSE c;
END;
$$
DELIMITER ;
CALL p1();
```

### SELECT...INTO Examples


A `<code>SELECT...INTO</code>` example for `<code>sql_mode=DEFAULT</code>`:


```
SET sql_mode=DEFAULT;
DROP TABLE IF EXISTS t1;
DROP PROCEDURE IF EXISTS p1;
CREATE TABLE t1 (a INT, b VARCHAR(32));
INSERT INTO t1 VALUES (10,'b10');
DELIMITER $$
CREATE PROCEDURE p1()
BEGIN
  DECLARE rec1 ROW(a INT, b VARCHAR(32));
  SELECT * FROM t1 INTO rec1;
  SELECT rec1.a, rec1.b;
END;
$$
DELIMITER ;
CALL p1();
```

The above example returns:


```
+--------+--------+
| rec1.a | rec1.b |
+--------+--------+
|     10 | b10    |
+--------+--------+
```

A `<code>SELECT...INTO</code>` example for `<code>sql_mode=ORACLE</code>`:


```
SET sql_mode=ORACLE;
DROP TABLE IF EXISTS t1;
DROP PROCEDURE IF EXISTS p1;
CREATE TABLE t1 (a INT, b VARCHAR(32));
INSERT INTO t1 VALUES (10,'b10');
DELIMITER $$
CREATE PROCEDURE p1 AS
  rec1 ROW(a INT, b VARCHAR(32));
BEGIN
  SELECT * FROM t1 INTO rec1;
  SELECT rec1.a, rec1.b;
END;
$$
DELIMITER ;
CALL p1();
```

The above example returns:


```
+--------+--------+
| rec1.a | rec1.b |
+--------+--------+
|     10 | b10    |
+--------+--------+
```

An example for `<code>sql_mode=ORACLE</code>` using `<code>table%ROWTYPE</code>` variables as `<code>SELECT..INTO</code>` targets:


```
SET sql_mode=ORACLE;
DROP TABLE IF EXISTS t1;
DROP PROCEDURE IF EXISTS p1;
CREATE TABLE t1 (a INT, b VARCHAR(32));
INSERT INTO t1 VALUES (10,'b10');
DELIMITER $$
CREATE PROCEDURE p1 AS
  rec1 t1%ROWTYPE;
BEGIN
  SELECT * FROM t1 INTO rec1;
  SELECT rec1.a, rec1.b;
END;
$$
DELIMITER ;
CALL p1();
```

The above example returns:


```
+--------+--------+
| rec1.a | rec1.b |
+--------+--------+
|     10 | b10    |
+--------+--------+
```

An example for `<code>sql_mode=ORACLE</code>` using `<code>cursor%ROWTYPE</code>` variables as `<code>SELECT..INTO</code>` targets:


```
SET sql_mode=ORACLE;
DROP TABLE IF EXISTS t1;
DROP PROCEDURE IF EXISTS p1;
CREATE TABLE t1 (a INT, b VARCHAR(32));
INSERT INTO t1 VALUES (10,'b10');
DELIMITER $$
CREATE PROCEDURE p1 AS
  CURSOR cur1 IS SELECT * FROM t1;
  rec1 cur1%ROWTYPE;
BEGIN
  SELECT * FROM t1 INTO rec1;
  SELECT rec1.a, rec1.b;
END;
$$
DELIMITER ;
CALL p1();
```

The above example returns:


```
+--------+--------+
| rec1.a | rec1.b |
+--------+--------+
|     10 | b10    |
+--------+--------+
```

Row_Table Example:


```
CREATE TABLE row_table(
  descr VARCHAR(20),
  val INT
);
```

```
INSERT INTO row_table VALUES ('Life', 42);
```

```
DELIMITER $$
CREATE PROCEDURE row_proc()
BEGIN
  DECLARE rec1 ROW(descr VARCHAR(20), val INT);
  SELECT * INTO rec1 FROM row_table;
  SELECT rec1.descr, rec1.val;
END;
$$
DELIMITER ;
```

```
CALL row_proc();

+------------+----------+
| rec1.descr | rec1.val |
+------------+----------+
| Life       |       42 |
+------------+----------+
```

## See Also


* [STORED PROCEDURES](../../../server-usage/programming-customizing-mariadb/stored-routines/stored-procedures/README.md)
* [DECLARE Variable](../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/declare-variable.md)

