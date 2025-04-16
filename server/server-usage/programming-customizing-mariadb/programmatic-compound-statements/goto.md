
# GOTO

## Syntax


```
GOTO label
```


## Description


The `GOTO` statement causes the code to jump to the specified label, and continue operating from there. It is only accepted when in [Oracle mode](../../../../release-notes/mariadb-community-server/compatibility-and-differences/sql_modeoracle.md).


## Example


```
SET sql_mode=ORACLE;

DELIMITER //

CREATE OR REPLACE PROCEDURE p1 AS

BEGIN

  SELECT 1;
  GOTO label;
  SELECT 2;
  <<label>>
  SELECT 3;

END;

//

DELIMITER 

call p1();
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.000 sec)

+---+
| 3 |
+---+
| 3 |
+---+
1 row in set (0.000 sec)
```
