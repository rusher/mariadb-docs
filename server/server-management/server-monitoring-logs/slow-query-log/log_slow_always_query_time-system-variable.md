
# log_slow_always_query_time System Variable

* Description: Queries slower than log_slow_always_query_time are not affected by [log_slow_rate_limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_rate_limit) or [log_slow_min_examined_row_limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_min_examined_row_limit). Query will be logged to the [slow query log](slow-query-log-overview.md) if the execution time of the query is longer than [log_slow_query_time](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query_time) and log_slow_always_query_time. The argument will be treated as a decimal value with microsecond precision.
* Commandline: `--log-slow-always-query-time=num`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric (double)`
* Default Value: `31536000.000000`
* Range: `0` to `31536000`
* Introduced: [MariaDB 11.7](../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md)

