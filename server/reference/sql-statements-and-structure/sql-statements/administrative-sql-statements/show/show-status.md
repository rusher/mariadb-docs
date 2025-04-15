
# SHOW STATUS

## Syntax


```
SHOW [GLOBAL | SESSION] STATUS
    [LIKE 'pattern' | WHERE expr]
```

## Description


`<code class="highlight fixed" style="white-space:pre-wrap">SHOW STATUS</code>` provides server status information. This
information also can be obtained using the [mariadb-admin extended-status](../../../../../clients-and-utilities/mariadb-admin.md) command, or by querying the [Information Schema GLOBAL_STATUS and SESSION_STATUS](../system-tables/information-schema/information-schema-tables/information-schema-global_status-and-session_status-tables.md) tables.
The `<code class="highlight fixed" style="white-space:pre-wrap">LIKE</code>` clause, if present, indicates which variable names
to match. The `<code class="highlight fixed" style="white-space:pre-wrap">WHERE</code>` clause can be given to select rows using
more general conditions.


With the `<code class="highlight fixed" style="white-space:pre-wrap">GLOBAL</code>` modifier, `<code class="highlight fixed" style="white-space:pre-wrap">SHOW STATUS</code>`
displays the status values for all connections to MariaDB. With
`<code class="highlight fixed" style="white-space:pre-wrap">SESSION</code>`, it displays the status values
for the current connection. If no modifier is present, the default is
 `<code class="highlight fixed" style="white-space:pre-wrap">SESSION</code>`. `<code class="highlight fixed" style="white-space:pre-wrap">LOCAL</code>` is a synonym for
 `<code class="highlight fixed" style="white-space:pre-wrap">SESSION</code>`. If you see a lot of 0 values, the reason is probably that you have used `<code class="highlight fixed" style="white-space:pre-wrap">SHOW STATUS</code>` with a new connection instead of `<code class="highlight fixed" style="white-space:pre-wrap">SHOW GLOBAL STATUS</code>`.


Some status variables have only a global value. For these, you get the
same value for both `<code class="highlight fixed" style="white-space:pre-wrap">GLOBAL</code>` and `<code class="highlight fixed" style="white-space:pre-wrap">SESSION</code>`.


See [Server Status Variables](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md) for a full list, scope and description of the variables that can be viewed with `<code>SHOW STATUS</code>`.


The `<code class="highlight fixed" style="white-space:pre-wrap">LIKE</code>` clause, if present on its own, indicates which variable name to match.


The `<code class="highlight fixed" style="white-space:pre-wrap">WHERE</code>` and `<code class="highlight fixed" style="white-space:pre-wrap">LIKE</code>` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md).


## Examples


```
SHOW GLOBAL STATUS;
+--------------------------------------------------------------+----------------------------------------+
| Variable_name                                                | Value                                  |
+--------------------------------------------------------------+----------------------------------------+
| Aborted_clients                                              | 0                                      |
| Aborted_connects                                             | 0                                      |
| Access_denied_errors                                         | 0                                      |
| Acl_column_grants                                            | 0                                      |
| Acl_database_grants                                          | 2                                      |
| Acl_function_grants                                          | 0                                      |
| Acl_procedure_grants                                         | 0                                      |
| Acl_proxy_users                                              | 2                                      |
| Acl_role_grants                                              | 0                                      |
| Acl_roles                                                    | 0                                      |
| Acl_table_grants                                             | 0                                      |
| Acl_users                                                    | 6                                      |
| Aria_pagecache_blocks_not_flushed                            | 0                                      |
| Aria_pagecache_blocks_unused                                 | 15706                                  |
...
| wsrep_local_index                                            | 18446744073709551615                   |
| wsrep_provider_name                                          |                                        |
| wsrep_provider_vendor                                        |                                        |
| wsrep_provider_version                                       |                                        |
| wsrep_ready                                                  | OFF                                    |
| wsrep_thread_count                                           | 0                                      |
+--------------------------------------------------------------+----------------------------------------+
516 rows in set (0.00 sec)
```

Example of filtered output:


```
SHOW STATUS LIKE 'Key%';
+------------------------+--------+
| Variable_name          | Value  |
+------------------------+--------+
| Key_blocks_not_flushed | 0      |
| Key_blocks_unused      | 107163 |
| Key_blocks_used        | 0      |
| Key_blocks_warm        | 0      |
| Key_read_requests      | 0      |
| Key_reads              | 0      |
| Key_write_requests     | 0      |
| Key_writes             | 0      |
+------------------------+--------+
8 rows in set (0.00 sec)
```
