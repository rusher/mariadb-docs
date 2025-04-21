
# Performance Schema host_cache Table

The `host_cache` table contains host and IP information from the host_cache, used for avoiding DNS lookups for new client connections.


The host_cache table contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| IP | Client IP address. |
| HOST | IP's resolved DNS host name, or NULL if unknown. |
| HOST_VALIDATED | YES if the IP-to-host DNS lookup was successful, and the HOST column can be used to avoid DNS calls, or NO if unsuccessful, in which case DNS lookup is performed for each connect until either successful or a permanent error. |
| SUM_CONNECT_ERRORS | Number of connection errors. Counts only protocol handshake errors for hosts that passed validation. These errors count towards [max_connect_errors](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_connect_errors). |
| COUNT_HOST_BLOCKED_ERRORS | Number of blocked connections because SUM_CONNECT_ERRORS exceeded the [max_connect_errors](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_connect_errors) system variable. |
| COUNT_NAMEINFO_TRANSIENT_ERRORS | Number of transient errors during IP-to-host DNS lookups. |
| COUNT_NAMEINFO_PERMANENT_ERRORS | Number of permanent errors during IP-to-host DNS lookups. |
| COUNT_FORMAT_ERRORS | Number of host name format errors, for example a numeric host column. |
| COUNT_ADDRINFO_TRANSIENT_ERRORS | Number of transient errors during host-to-IP reverse DNS lookups. |
| COUNT_ADDRINFO_PERMANENT_ERRORS | Number of permanent errors during host-to-IP reverse DNS lookups. |
| COUNT_FCRDNS_ERRORS | Number of forward-confirmed reverse DNS errors, which occur when IP-to-host DNS lookup does not match the originating IP address. |
| COUNT_HOST_ACL_ERRORS | Number of errors occurring because no user from the host is permitted to log in. These attempts return [error code](../../../../../../mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-code-reference.md) 1130 ER_HOST_NOT_PRIVILEGED and do not proceed to username and password authentication. |
| COUNT_NO_AUTH_PLUGIN_ERRORS | Number of errors due to requesting an authentication plugin that was not available. This can be due to the plugin never having been loaded, or the load attempt failing. |
| COUNT_AUTH_PLUGIN_ERRORS | Number of errors reported by an authentication plugin. Plugins can increment COUNT_AUTHENTICATION_ERRORS or COUNT_HANDSHAKE_ERRORS instead, but, if specified or the error is unknown, this column is incremented. |
| COUNT_HANDSHAKE_ERRORS | Number of errors detected at the wire protocol level. |
| COUNT_PROXY_USER_ERRORS | Number of errors detected when a proxy user is proxied to a user that does not exist. |
| COUNT_PROXY_USER_ACL_ERRORS | Number of errors detected when a proxy user is proxied to a user that exists, but the proxy user doesn't have the PROXY privilege. |
| COUNT_AUTHENTICATION_ERRORS | Number of errors where authentication failed. |
| COUNT_SSL_ERRORS | Number of errors due to TLS problems. |
| COUNT_MAX_USER_CONNECTIONS_ERRORS | Number of errors due to the per-user quota being exceeded. |
| COUNT_MAX_USER_CONNECTIONS_PER_HOUR_ERRORS | Number of errors due to the per-hour quota being exceeded. |
| COUNT_DEFAULT_DATABASE_ERRORS | Number of errors due to the user not having permission to access the specified default database, or it not existing. |
| COUNT_INIT_CONNECT_ERRORS | Number of errors due to statements in the [init_connect](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#init_connect) system variable. |
| COUNT_LOCAL_ERRORS | Number of local server errors, such as out-of-memory errors, unrelated to network, authentication, or authorization. |
| COUNT_UNKNOWN_ERRORS | Number of unknown errors that cannot be allocated to another column. |
| FIRST_SEEN | Timestamp of the first connection attempt by the IP. |
| LAST_SEEN | Timestamp of the most recent connection attempt by the IP. |
| FIRST_ERROR_SEEN | Timestamp of the first error seen from the IP. |
| LAST_ERROR_SEEN | Timestamp of the most recent error seen from the IP. |



The `host_cache` table, along with the `host_cache`, is cleared with [FLUSH HOSTS](../../../flush-commands/flush.md), [TRUNCATE TABLE](../../../../table-statements/truncate-table.md) `host_cache` or by setting the [host_cache_size](../../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#host_cache_size) system variable at runtime.

