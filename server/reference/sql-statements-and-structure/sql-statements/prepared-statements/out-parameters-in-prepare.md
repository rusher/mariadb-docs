
# Out Parameters in PREPARE

Out parameters in PREPARE were only available for an earlier version of MariaDB.


One can use question mark placeholders for out-parameters in the [PREPARE](prepare-statement.md) statement. Only [SELECT … INTO](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmark-results/select-random-ranges-and-select-random-point.md#into) can be used this way:


```
prepare test from "select id into ? from t1 where val=?";
execute test using @out, @in;
```

This is particularly convenient when used with [compound statements](../../../../server-usage/programming-customizing-mariadb/programmatic-compound-statements/using-compound-statements-outside-of-stored-programs.md):


```
PREPARE stmt FROM "BEGIN NOT ATOMIC
  DECLARE v_res INT;
  SELECT COUNT(*) INTO v_res FROM t1;
  SELECT 'Hello World', v_res INTO ?,?;
END"|
```
