
# Bitemporal Tables

Bitemporal tables are tables that use versioning both at the [system](system-versioned-tables.md) and [application-time period](application-time-periods.md) levels.



## Using Bitemporal Tables


To create a bitemporal table, use:


```
CREATE TABLE test.t3 (
   date_1 DATE,
   date_2 DATE,
   row_start TIMESTAMP(6) AS ROW START INVISIBLE,
   row_end TIMESTAMP(6) AS ROW END INVISIBLE,
   PERIOD FOR application_time(date_1, date_2),
   PERIOD FOR system_time(row_start, row_end))
WITH SYSTEM VERSIONING;
```

Note that, while `<code>system_time</code>` here is also a time period, it cannot be used in `<code>DELETE FOR PORTION</code>` or `<code>UPDATE FOR PORTION</code>` statements.


```
DELETE FROM test.t3 
FOR PORTION OF system_time 
    FROM '2000-01-01' TO '2018-01-01';
ERROR 42000: You have an error in your SQL syntax; check the manual that corresponds 
  to your MariaDB server version for the right syntax to use near
  'of system_time from '2000-01-01' to '2018-01-01'' at line 1
```

## See Also


* [System-versioned Tables](system-versioned-tables.md)
* [Application-time Periods](application-time-periods.md)

