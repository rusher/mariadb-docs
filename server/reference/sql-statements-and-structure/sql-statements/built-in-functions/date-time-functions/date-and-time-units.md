
# Date and Time Units

The `<code>INTERVAL</code>` keyword can be used to add or subtract a time interval of time to a `<code>[DATETIME](../../../../data-types/date-and-time-data-types/datetime.md)</code>`, `<code>[DATE](../../../sql-language-structure/date-and-time-literals.md)</code>` or `<code>[TIME](../../administrative-sql-statements/system-tables/information-schema/time_ms-column-in-information_schemaprocesslist.md)</code>` value.


The syntax is:


```
INTERVAL time_quantity time_unit
```

For example, the `<code>SECOND</code>` unit is used below by the `<code>[DATE_ADD()](date_add.md)</code>` function:


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



The time units containing an underscore are composite; that is, they consist of multiple base time units. For base time units, `<code>time_quantity</code>` is an integer number. For composite units, the quantity must be expressed as a string with multiple integer numbers separated by any punctuation character.


Example of composite units:


```
INTERVAL '2:2' YEAR_MONTH
INTERVAL '1:30:30' HOUR_SECOND
INTERVAL '1!30!30' HOUR_SECOND -- same as above
```

Time units can be used in the following contexts:


* after a `<code>[+](../numeric-functions/addition-operator.md)</code>` or a `<code>[-](../../../operators/arithmetic-operators/subtraction-operator-.md)</code>` operator;
* with the following `<code>DATE</code>` or `<code>TIME</code>` functions: `<code>[ADDDATE()](adddate.md)</code>`, `<code>[SUBDATE()](subdate.md)</code>`, `<code>[DATE_ADD()](date_add.md)</code>`, `<code>[DATE_SUB()](date_sub.md)</code>`, `<code>[TIMESTAMPADD()](timestampadd.md)</code>`, `<code>[TIMESTAMPDIFF()](timestampdiff.md)</code>`, `<code>[EXTRACT()](../../administrative-sql-statements/system-tables/sys-schema/sys-schema-stored-functions/extract_schema_from_file_name.md)</code>`;
* in the `<code>ON SCHEDULE</code>` clause of `<code>[CREATE EVENT](../../data-definition/create/create-event.md)</code>` and `<code>[ALTER EVENT](../../../../../server-usage/programming-customizing-mariadb/triggers-events/event-scheduler/alter-event.md)</code>`.
* when defining a [partitioning](../../../vectors/create-table-with-vectors.md#partitions) `<code>BY SYSTEM_TIME</code>`


## See Also


* [Date and time literals](../../../sql-language-structure/date-and-time-literals.md)
* [Operator Precedence](../../../operators/operator-precedence.md)

