
# Connect Memory Usage

When creating a connection, a THD object is created for that connection. This contains
all connection information and also caches to speed up queries and avoid frequent malloc() calls.


When creating a new connection, the following malloc() calls are done for the THD:


The following information is the state in [MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/mariadb-1061-release-notes) when compiled without debugging.


## Local Thread Memory


This is part of `select memory_used from information_schema.processlist`.



| Amount allocated | Where allocated | Description |
| --- | --- | --- |
| Amount allocated | Where allocated | Description |
| 26646 | THD::THD | Allocation of THD object |
| 256 | Statement_map::Statement_map(), my_hash_init(key_memory_prepared_statement_map, &st_hash | Prepared statements |
| 256 | my_hash_init(key_memory_prepared_statement_map, &names_hash | Names of used prepared statements |
| 128 | wsrep_wfc(), Opt_trace_context(), dynamic_array() |  |
| 1024 | Diagnostics_area::init(),init_sql_alloc(PSI_INSTRUMENT_ME, &m_warn_root |  |
| 120 | Session_sysvars_tracker, global_system_variables.session_track_system_variables | Tracking of changed session variables |
| 280 | THD::THD,my_hash_init(key_memory_user_var_entry,&user_vars |  |
| 280 | THD::THD,my_hash_init(PSI_INSTRUMENT_ME, &sequences | Cache of used sequences |
| 1048 | THD::THD, m_token_array= my_malloc(PSI_INSTRUMENT_ME, max_digest_length |  |
| 16416 | CONNECT::create_thd(), my_net_init(), net_allocate_new_packet() | This is for reading data from the connected user |
| 16416 | check_connection(), thd->packet.alloc() | This is for sending data to connected user |



## Objects Stored in THD->memroot During Connect



| Amount allocated | Where allocated | Description |
| --- | --- | --- |
| Amount allocated | Where allocated | Description |
| 72 | send_server_handshake_packet, mpvio->cached_server_packet.pkt= |  |
| 64 | parse_client_handshake_packet, thd->copy_with_error(...db,db_len) |  |
| 32 | parse_client_handshake_packet, sctx->user= |  |
| 368 | ACL_USER::copy(), root= | Allocation of ACL_USER object |
| 56 | ACL_USER::copy(), dst->user= safe_lexcstrdup_root(root, user) |  |
| 56 | ACL_USER::copy() | Allocation of other connect attributes |
| 56 | ACL_USER::copy() |  |
| 64 | ACL_USER::copy() |  |
| 64 | ACL_USER::copy() |  |
| 32 | mysql_change_db() | Store current db in THD |
| 48 | dbname_cache->insert(db_name) | Store db name in db name cache |
| 40 | mysql_change_db(), my_register_filename(db.opt) | Store filename db.opt |
| 8216 | load_db_opt(), init_io_cache() | Disk cache for reading db.opt |
| 1112 | load_db_opts(), put_dbopts() | Cache default database parameters |



## State at First Call to mysql_execute_command


```
(gdb) p thd->status_var.local_memory_used
$24 = 75496
(gdb) p thd->status_var.global_memory_used
$25 = 17544
(gdb) p thd->variables.query_prealloc_size
$30 = 24576
(gdb) p thd->variables.trans_prealloc_size
$37 = 4096
```


CC BY-SA / Gnu FDL

