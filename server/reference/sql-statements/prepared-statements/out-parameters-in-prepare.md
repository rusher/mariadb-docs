# Out Parameters in PREPARE

Out parameters in PREPARE were only available for an earlier version of MariaDB.

One can use question mark placeholders for out-parameters in the [PREPARE](prepare-statement.md) statement. Only [SELECT … INTO](../data-manipulation/selecting-data/select.md#into) can be used this way:

```
prepare test from "select id into ? from t1 where val=?";
execute test using @out, @in;
```

This is particularly convenient when used with [compound statements](../../../server-usage/programmatic-compound-statements/using-compound-statements-outside-of-stored-programs.md):

```
PREPARE stmt FROM "BEGIN NOT ATOMIC
  DECLARE v_res INT;
  SELECT COUNT(*) INTO v_res FROM t1;
  SELECT 'Hello World', v_res INTO ?,?;
END"|
```

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
