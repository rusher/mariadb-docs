# Coordinated Universal Time

UTC stands for Coordinated Universal Time, and is the world standard for regulating time.

MariaDB stores values internally in UTC, converting them to the required time zone as required.

In general terms it is equivalent to Greenwich Mean Time (GMT), but UTC is used in technical contexts as it is precisely defined at the subsecond level.

[Time zones](time-zones.md) are offset relative to UTC. For example, time in Tonga is UTC + 13, so 03h00 UTC will be 16h00 in Tonga.

## See Also

* [UTC\_DATE](../../../../sql-functions/date-time-functions/utc_date.md)
* [UTC\_TIME](../../../../sql-functions/date-time-functions/utc_time.md)
* [UTC\_TIMESTAMP](../../../../sql-functions/date-time-functions/utc_timestamp.md)

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
