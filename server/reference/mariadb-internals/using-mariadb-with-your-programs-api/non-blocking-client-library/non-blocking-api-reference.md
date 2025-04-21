
# Non-blocking API Reference

Here is a list of all functions in the non-blocking client API and their
parameters. Apart from operating in a non-blocking way, they all work exactly
the same as their blocking counterparts, so their exact semantics can be
obtained from the documentation of the normal client API.


The API also contains the following three functions which are used to get the
socket `fd` and `timeout` values when waiting for events to occur:


```
my_socket mysql_get_socket(const MYSQL *mysql)
```

 Return the descriptor of the socket used for the connection.



```
unsigned int STDCALL mysql_get_timeout_value(const MYSQL *mysql)
```

 This should only be called when a `_start()` or `_cont()` function
 returns a value with the `MYSQL_WAIT_TIMEOUT` flag set. In this case, it
 returns the value, in seconds, after which a timeout has occured and the
 application should call the appropriate `_cont()` function passing
 `MYSQL_WAIT_TIMEOUT` as the event that occured.



 This is used to handle connection and read timeouts.



```
unsigned int STDCALL mysql_get_timeout_value_ms(const MYSQL *mysql)
```

 This function is available starting from [MariaDB 5.5.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5528-release-notes) and [MariaDB 10.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1000-release-notes).



 Like mysql_get_timeout_value(), this should only be called when a _start() or
 _cont() function returns a value with the MYSQL_WAIT_TIMEOUT flag set. In this
 case, it returns the value, in millisecondsseconds, after which a timeout has
 occured and the application should call the appropriate _cont() function
 passing MYSQL_WAIT_TIMEOUT as the event that occured.



 The difference to mysql_get_timeout_value() is that this provides millisecond
 resolution for timeouts, rather than just whole seconds. In [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0),
 internal timeouts can now be in milliseconds, while in 5.5 and below it was
 only whole seconds.



 This milliseconds version is provided also in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) (from 5.5.28
 onwards) to make it easier for applications to work with either library
 version. However, in 5.5 it always returns a multiple of 1000 milliseconds.



[At the end](#client-api-functions-which-never-block) is a list of all
functions from the normal API which can be used safely in a non-blocking
program, since they never need to block.


```
int mysql_real_connect_start(MYSQL **ret, MYSQL *mysql, const char *host,
                         const char *user, const char *passwd, const char *db,
                         unsigned int port, const char *unix_socket,
                         unsigned long client_flags)
```

```
int mysql_real_connect_cont(MYSQL **ret, MYSQL *mysql, int ready_status)
```

 `mysql_real_connect_start()` initiates a non-blocking connection request to
 a server.



 When `mysql_real_connect_start()` or `mysql_real_connect_cont()` returns
 zero, a copy of the passed '`mysql`' argument is stored in `*ret`.



```
int mysql_real_query_start(int *ret, MYSQL *mysql, const char *stmt_str,
unsigned long length)
int mysql_real_query_cont(int *ret, MYSQL *mysql, int ready_status)
```

```
int mysql_fetch_row_start(MYSQL_ROW *ret, MYSQL_RES *result)
int mysql_fetch_row_cont(MYSQL_ROW *ret, MYSQL_RES *result, int ready_status)
```

 Initiate fetch of another row from a `SELECT` query.



 If the `MYSQL_RES` was obtained from `mysql_use_result()`, then this
 function allows stream processing, where initial rows are returned to the
 application while the server is still sending subsequent rows. When no more
 data is available on the socket, `mysql_fetch_row_start()` or
 `mysql_fetch_row_cont()` will return `MYSQL_WAIT_READ` (or possibly
 `MYSQL_WAIT_WRITE` if using TLS and TLS re-negotiation is needed; also
 `MYSQL_WAIT_TIMEOUT` may be set if read timeout is enabled). When data
 becomes available, more rows can be fetched with `mysql_fetch_row_cont()`.



 If the `MYSQL_RES` was obtained from `mysql_store_result()` /
 `mysql_store_result_start()` / `mysql_store_result_cont()`, then this
 function cannot block — `mysql_fetch_row_start()`
 will always return 0 (and if desired, `plain mysql_fetch_row()` may be used
 instead with equivalent effect).



```
int mysql_set_character_set_start(int *ret, MYSQL *mysql, const char *csname)
int mysql_set_character_set_cont(int *ret, MYSQL *mysql, int ready_status)
```

```
mysql_select_db_start(int *ret, MYSQL *mysql, const char *db)
int mysql_select_db_cont(int *ret, MYSQL *mysql, int ready_status)
```

```
int mysql_send_query_start(int *ret, MYSQL *mysql, const char *q, unsigned long length)
int mysql_send_query_cont(int *ret, MYSQL *mysql, int ready_status)
```

```
int mysql_store_result_start(MYSQL_RES **ret, MYSQL *mysql)
int mysql_store_result_cont(MYSQL_RES **ret, MYSQL *mysql, int ready_status)
```

```
int mysql_free_result_start(MYSQL_RES *result)
int mysql_free_result_cont(MYSQL_RES *result, int ready_status)
```

 This function can need to wait if not all rows were fetched before it was
 called (then it needs to consume any pending rows sent from the server so
 they do not interfere with any subsequent queries sent).



 If all rows were already fetched, then this function will not need to wait.
 `mysql_free_result_start()` will return zero (or if so desired, plain
 `mysql_free_result()` may be used instead).



 Note that `mysql_free_result()` returns no value, so there is no extra
 '`ret`' parameter for `mysql_free_result_start()` or
 `mysql_free_result_cont()`.



```
int mysql_close_start(MYSQL *sock)
int mysql_close_cont(MYSQL *sock, int ready_status)
```

 `mysql_close()` sends a `COM_QUIT` request to the server, though it does
 not wait for any reply.



 Thus teoretically it can block (if the socket buffer is full), though in
 practise it is probably unlikely to occur frequently.



 The non-blocking version of `mysql_close()` is provided for completeness;
 for many applications using the normal `mysql_close()` is probably
 sufficient (and may be simpler).



 Note that `mysql_close()` returns no value, so there is no extra '`ret`'
 parameter for `mysql_close_start()` or `mysql_close_cont()`.



```
int mysql_change_user_start(my_bool *ret, MYSQL *mysql, const char *user, const
                            char *passwd, const char *db)
int mysql_change_user_cont(my_bool *ret, MYSQL *mysql, int ready_status)
```

```
int mysql_query_start(int *ret, MYSQL *mysql, const char *q)
int mysql_query_cont(int *ret, MYSQL *mysql, int ready_status)
```

```
int mysql_shutdown_start(int *ret, MYSQL *mysql, enum mysql_enum_shutdown_level
                        shutdown_level)
int mysql_shutdown_cont(int *ret, MYSQL *mysql, int ready_status)
```

```
int mysql_dump_debug_info_start(int *ret, MYSQL *mysql)
int mysql_dump_debug_info_cont(int *ret, MYSQL *mysql, int ready_status)
```

```
int mysql_refresh_start(int *ret, MYSQL *mysql, unsigned int refresh_options)
int mysql_refresh_cont(int *ret, MYSQL *mysql, int ready_status)
```

```
int mysql_kill_start(int *ret, MYSQL *mysql, unsigned long pid)
int mysql_kill_cont(int *ret, MYSQL *mysql, int ready_status)
```

```
int mysql_set_server_option_start(int *ret, MYSQL *mysql,
                              enum enum_mysql_set_option option)
int mysql_set_server_option_cont(int *ret, MYSQL *mysql, int ready_status)
```

```
int mysql_ping_start(int *ret, MYSQL *mysql)
int mysql_ping_cont(int *ret, MYSQL *mysql, int ready_status)
```

```
int mysql_stat_start(const char **ret, MYSQL *mysql)
int mysql_stat_cont(const char **ret, MYSQL *mysql, int ready_status)
```

```
int mysql_list_dbs_start(MYSQL_RES **ret, MYSQL *mysql, const char *wild)
int mysql_list_dbs_cont(MYSQL_RES **ret, MYSQL *mysql, int ready_status)
```

```
int mysql_list_tables_start(MYSQL_RES **ret, MYSQL *mysql, const char *wild)
int mysql_list_tables_cont(MYSQL_RES **ret, MYSQL *mysql, int ready_status)
```

```
int mysql_list_processes_start(MYSQL_RES **ret, MYSQL *mysql)
int mysql_list_processes_cont(MYSQL_RES **ret, MYSQL *mysql, int ready_status)
```

```
int mysql_list_fields_start(MYSQL_RES **ret, MYSQL *mysql, const char *table,
                        const char *wild)
int mysql_list_fields_cont(MYSQL_RES **ret, MYSQL *mysql, int ready_status)
```

```
int mysql_read_query_result_start(my_bool *ret, MYSQL *mysql)
int mysql_read_query_result_cont(my_bool *ret, MYSQL *mysql, int ready_status)
```

```
int mysql_stmt_prepare_start(int *ret, MYSQL_STMT *stmt, const char *query,
                         unsigned long length)
int mysql_stmt_prepare_cont(int *ret, MYSQL_STMT *stmt, int ready_status)
```

```
int mysql_stmt_execute_start(int *ret, MYSQL_STMT *stmt)
int mysql_stmt_execute_cont(int *ret, MYSQL_STMT *stmt, int ready_status)
```

```
int mysql_stmt_fetch_start(int *ret, MYSQL_STMT *stmt)
int mysql_stmt_fetch_cont(int *ret, MYSQL_STMT *stmt, int ready_status)
```

```
int mysql_stmt_store_result_start(int *ret, MYSQL_STMT *stmt)
int mysql_stmt_store_result_cont(int *ret, MYSQL_STMT *stmt, int ready_status)
```

```
int mysql_stmt_close_start(my_bool *ret, MYSQL_STMT *stmt)
int mysql_stmt_close_cont(my_bool *ret, MYSQL_STMT *stmt, int ready_status)
```

```
int mysql_stmt_reset_start(my_bool *ret, MYSQL_STMT *stmt)
int mysql_stmt_reset_cont(my_bool *ret, MYSQL_STMT *stmt, int ready_status)
```

```
int mysql_stmt_free_result_start(my_bool *ret, MYSQL_STMT *stmt)
int mysql_stmt_free_result_cont(my_bool *ret, MYSQL_STMT *stmt, int ready_status)
```

```
int mysql_stmt_send_long_data_start(my_bool *ret, MYSQL_STMT *stmt,
                                unsigned int param_number,
                                const char *data, unsigned long length)
int mysql_stmt_send_long_data_cont(my_bool *ret, MYSQL_STMT *stmt, int ready_status)
```

```
int mysql_commit_start(my_bool *ret, MYSQL *mysql)
int mysql_commit_cont(my_bool *ret, MYSQL *mysql, int ready_status)
```

```
int mysql_rollback_start(my_bool *ret, MYSQL *mysql)
int mysql_rollback_cont(my_bool *ret, MYSQL *mysql, int ready_status)
```

```
int mysql_autocommit_start(my_bool *ret, MYSQL *mysql, my_bool auto_mode)
int mysql_autocommit_cont(my_bool *ret, MYSQL *mysql, int ready_status)
```

```
int mysql_next_result_start(int *ret, MYSQL *mysql)
int mysql_next_result_cont(int *ret, MYSQL *mysql, int ready_status)
```

```
int mysql_stmt_next_result_start(int *ret, MYSQL_STMT *stmt)
int mysql_stmt_next_result_cont(int *ret, MYSQL_STMT *stmt, int ready_status)
```

## Client API functions which never block


The following client API functions never need to do I/O and thus can never
block. Therefore, they can be used as normal in programs using non-blocking
operations; no need to call any special `_start()` variant. (Even if a
`_start()` variant was available, it would always return zero, so no
`_cont()` call would ever be needed).


* [mysql_num_rows()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_num_rows)
* [mysql_num_fields()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_num_fields)
* mysql_eof()``
* [mysql_fetch_field_direct()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_fetch_field_direct)
* [mysql_fetch_fields()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_fetch_fields)
* [mysql_row_tell](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_row_tell)
* [mysql_field_tell()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_field_tell)
* [mysql_field_count()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_field_count)
* [mysql_affected_rows()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_affected_rows)
* [mysql_insert_id()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_insert_id)
* [mysql_errno()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_errno)
* [mysql_error()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_error)
* [mysql_sqlstate()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_sqlstate)
* [mysql_warning_count()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_warning_count)
* [mysql_info()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_info)
* [mysql_thread_id()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_thread_id)
* [mysql_character_set_name()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_character_set_name)
* [mysql_init()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_init)
* [mysql_ssl_set()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_ssl_set)
* [mysql_get_ssl_cipher()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_get_ssl_cipher)
* [mysql_use_result()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_use_result)
* [mysql_get_character_set_info()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_get_character_set_info)
* mysql_set_local_infile_handler()
* mysql_set_local_infile_default()
* [mysql_get_server_info()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_get_server_info)
* mysql_get_server_name()
* [mysql_get_client_info()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_get_client_info)
* [mysql_get_client_version()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_get_client_version)
* [mysql_get_host_info()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_get_host_info)
* [mysql_get_server_version()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_get_server_version)
* [mysql_get_proto_info()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_get_proto_info)
* [mysql_options()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_options)
* [mysql_data_seek()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_data_seek)
* [mysql_row_seek()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_row_seek)
* [mysql_field_seek()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_field_seek)
* [mysql_fetch_lengths()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_fetch_lengths)
* [mysql_fetch_field()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_fetch_field)
* [mysql_escape_string()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_escape_string)
* [mysql_hex_string()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_hex_string)
* [mysql_real_escape_string()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_real_escape_string)
* [mysql_debug()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_debug)
* myodbc_remove_escape()
* mysql_thread_safe()
* mysql_embedded()
* mariadb_connection()
* [mysql_stmt_init()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_init)
* [mysql_stmt_fetch_column()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_fetch_column)
* [mysql_stmt_param_count()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_param_count)
* [mysql_stmt_attr_set()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_attr_set)
* [mysql_stmt_attr_get()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_attr_get)
* [mysql_stmt_bind_param()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_bind_param)
* [mysql_stmt_bind_result()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_bind_result)
* [mysql_stmt_result_metadata()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_result_metadata)
* [mysql_stmt_param_metadata()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_param_metadata)
* [mysql_stmt_errno()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_errno)
* [mysql_stmt_error()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_error)
* [mysql_stmt_sqlstate()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_sqlstate)
* [mysql_stmt_row_seek()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_row_seek)
* [mysql_stmt_row_tell()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_row_tell)
* [mysql_stmt_data_seek()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_data_seek)
* [mysql_stmt_num_rows()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_num_rows)
* [mysql_stmt_affected_rows()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_affected_rows)
* [mysql_stmt_insert_id()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_insert_id)
* [mysql_stmt_field_count()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_field_count)
* [mysql_more_results()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_more_results)
* mysql_get_socket()
* mysql_get_timeout_value
* mysql_get_timeout_value_ms

