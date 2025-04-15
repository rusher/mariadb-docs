
# Performance Schema events_transactions_summary_by_account_by_event_name Table


##### MariaDB starting with [10.5.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md)
The events_transactions_summary_by_account_by_event_name table was introduced in [MariaDB 10.5.2](../../../../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md).


The `<code>events_transactions_summary_by_account_by_event_name</code>` table contains information on transaction events aggregated by account and event name.


The table contains the following columns:



| Column | Type | Description |
| --- | --- | --- |
| Column | Type | Description |
| USER | char(32) | User for which summary is generated. |
| HOST | char(60) | Host for which summary is generated. |
| EVENT_NAME | varchar(128) | Event name for which summary is generated. |
| COUNT_STAR | bigint(20) unsigned | The number of summarized events. This value includes all events, whether timed or nontimed. |
| SUM_TIMER_WAIT | bigint(20) unsigned | The total wait time of the summarized timed events. This value is calculated only for timed events because nontimed events have a wait time of NULL. The same is true for the other xxx_TIMER_WAIT values. |
| MIN_TIMER_WAIT | bigint(20) unsigned | The minimum wait time of the summarized timed events. |
| AVG_TIMER_WAIT | bigint(20) unsigned | The average wait time of the summarized timed events. |
| MAX_TIMER_WAIT | bigint(20) unsigned | The maximum wait time of the summarized timed events. |
| COUNT_READ_WRITE | bigint(20) unsigned | The total number of only READ/WRITE transaction events. |
| SUM_TIMER_READ_WRITE | bigint(20) unsigned | The total wait time of only READ/WRITE transaction events. |
| MIN_TIMER_READ_WRITE | bigint(20) unsigned | The minimum wait time of only READ/WRITE transaction events. |
| AVG_TIMER_READ_WRITE | bigint(20) unsigned | The average wait time of only READ/WRITE transaction events. |
| MAX_TIMER_READ_WRITE | bigint(20) unsigned | The maximum wait time of only READ/WRITE transaction events. |
| COUNT_READ_ONLY | bigint(20) unsigned | The total number of only READ ONLY transaction events. |
| SUM_TIMER_READ_ONLY | bigint(20) unsigned | The total wait time of only READ ONLY transaction events. |
| MIN_TIMER_READ_ONLY | bigint(20) unsigned | The minimum wait time of only READ ONLY transaction events. |
| AVG_TIMER_READ_ONLY | bigint(20) unsigned | The average wait time of only READ ONLY transaction events. |
| MAX_TIMER_READ_ONLY | bigint(20) unsigned | The maximum wait time of only READ ONLY transaction events. |


