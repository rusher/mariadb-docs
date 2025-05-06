
# Date and Time Units

The `INTERVAL` keyword can be used to add or subtract a time interval of time to a `[DATETIME](../../../../data-types/date-and-time-data-types/datetime.md)`, `[DATE](../../../../data-types/date-and-time-data-types/date.md)` or `[TIME](../../../../data-types/date-and-time-data-types/time.md)` value.


The syntax is:


```
INTERVAL time_quantity time_unit
```

For example, the `SECOND` unit is used below by the `[DATE_ADD()](date_add.md)` function:


```
SELECT '2008-12-31 23:59:59' + INTERVAL 1 SECOND;
+-------------------------------------------+
| '2008-12-31 23:59:59' + INTERVAL 1 SECOND |
+-------------------------------------------+
| 2009-01-01 00:00:00                       |
+-------------------------------------------+
```

The following units are valid:



| Unit | Description |
| --- | --- |
| Unit | Description |
| MICROSECOND | Microseconds |
| SECOND | Seconds |
| MINUTE | Minutes |
| HOUR | Hours |
| DAY | Days |
| WEEK | Weeks |
| MONTH | Months |
| QUARTER | Quarters |
| YEAR | Years |
| SECOND_MICROSECOND | Seconds.Microseconds |
| MINUTE_MICROSECOND | Minutes.Seconds.Microseconds |
| MINUTE_SECOND | Minutes.Seconds |
| HOUR_MICROSECOND | Hours.Minutes.Seconds.Microseconds |
| HOUR_SECOND | Hours.Minutes.Seconds |
| HOUR_MINUTE | Hours.Minutes |
| DAY_MICROSECOND | Days Hours.Minutes.Seconds.Microseconds |
| DAY_SECOND | Days Hours.Minutes.Seconds |
| DAY_MINUTE | Days Hours.Minutes |
| DAY_HOUR | Days Hours |
| YEAR_MONTH | Years-Months |



The time units containing an underscore are composite; that is, they consist of multiple base time units. For base time units, `time_quantity` is an integer number. For composite units, the quantity must be expressed as a string with multiple integer numbers separated by any punctuation character.


Example of composite units:


```
INTERVAL '2:2' YEAR_MONTH
INTERVAL '1:30:30' HOUR_SECOND
INTERVAL '1!30!30' HOUR_SECOND -- same as above
```

Time units can be used in the following contexts:


* after a `[+](../numeric-functions/addition-operator.md)` or a `[-](../../../operators/arithmetic-operators/subtraction-operator-.md)` operator;
* with the following `DATE` or `TIME` functions: `[ADDDATE()](adddate.md)`, `[SUBDATE()](subdate.md)`, `[DATE_ADD()](date_add.md)`, `[DATE_SUB()](date_sub.md)`, `[TIMESTAMPADD()](timestampadd.md)`, `[TIMESTAMPDIFF()](timestampdiff.md)`, `[EXTRACT()](extract.md)`;
* in the `ON SCHEDULE` clause of `[CREATE EVENT](../../data-definition/create/create-event.md)` and `[ALTER EVENT](../../../../../server-usage/programming-customizing-mariadb/triggers-events/event-scheduler/alter-event.md)`.
* when defining a [partitioning](../../data-definition/create/create-table.md#partitions) `BY SYSTEM_TIME`


## See Also


* [Date and time literals](../../../sql-language-structure/date-and-time-literals.md)
* [Operator Precedence](../../../operators/operator-precedence.md)


CC BY-SA / Gnu FDL

