
# SHOW CREATE FUNCTION

## Syntax


```
SHOW CREATE FUNCTION func_name
```

## Description


This statement is similar to [SHOW CREATE PROCEDURE](show-create-procedure.md) but for
[stored functions](../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md).


`<code>SHOW CREATE FUNCTION</code>` quotes identifiers according to the value of the [sql_quote_show_create](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) system variable. Prior to [MariaDB 10.6.5](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-1065-release-notes.md), [MariaDB 10.5.13](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10513-release-notes.md) and [MariaDB 10.4.22](../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10422-release-notes.md), the output of this statement was unreliably affected by the [sql_quote_show_create](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) system variable.


## Example


```
SHOW CREATE FUNCTION VatCents\G
*************************** 1. row ***************************
            Function: VatCents
            sql_mode: 
     Create Function: CREATE DEFINER=`root`@`localhost` FUNCTION `VatCents`(price DECIMAL(10,2)) RETURNS int(11)
    DETERMINISTIC
BEGIN
 DECLARE x INT;
 SET x = price * 114;
 RETURN x;
END
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
```

## See Also


* [Stored Functions](../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md)
* `<code class="highlight fixed" style="white-space:pre-wrap">[CREATE FUNCTION](../../data-definition/create/create-function.md)</code>`

