
# MaxScale 25.01 Configuration Settings

# Configuration Settings




* [Configuration Settings](#configuration-settings)

  * [General](#general)

    * [MaxScale](#maxscale)

      * [Global Settings](#global-settings)

        * [admin_audit](#admin_audit)
        * [admin_audit_exclude_methods](#admin_audit_exclude_methods)
        * [admin_audit_file](#admin_audit_file)
        * [admin_auth](#admin_auth)
        * [admin_enabled](#admin_enabled)
        * [admin_gui](#admin_gui)
        * [admin_host](#admin_host)
        * [admin_jwt_algorithm](#admin_jwt_algorithm)
        * [admin_jwt_issuer](#admin_jwt_issuer)
        * [admin_jwt_key](#admin_jwt_key)
        * [admin_jwt_max_age](#admin_jwt_max_age)
        * [admin_log_auth_failures](#admin_log_auth_failures)
        * [admin_oidc_url](#admin_oidc_url)
        * [admin_pam_readonly_service](#admin_pam_readonly_service)
        * [admin_pam_readwrite_service](#admin_pam_readwrite_service)
        * [admin_port](#admin_port)
        * [admin_readwrite_hosts](#admin_readwrite_hosts)
        * [admin_secure_gui](#admin_secure_gui)
        * [admin_ssl_ca](#admin_ssl_ca)
        * [admin_ssl_cert](#admin_ssl_cert)
        * [admin_ssl_cipher](#admin_ssl_cipher)
        * [admin_ssl_key](#admin_ssl_key)
        * [admin_ssl_version](#admin_ssl_version)
        * [admin_verify_url](#admin_verify_url)
        * [auth_connect_timeout](#auth_connect_timeout)
        * [auto_tune](#auto_tune)
        * [cachedir](#cachedir)
        * [config_sync_cluster](#config_sync_cluster)
        * [config_sync_db](#config_sync_db)
        * [config_sync_interval](#config_sync_interval)
        * [config_sync_password](#config_sync_password)
        * [config_sync_timeout](#config_sync_timeout)
        * [config_sync_user](#config_sync_user)
        * [connector_plugindir](#connector_plugindir)
        * [core_file](#core_file)
        * [datadir](#datadir)
        * [debug](#debug)
        * [dump_last_statements](#dump_last_statements)
        * [execdir](#execdir)
        * [host_cache_size](#host_cache_size)
        * [key_manager](#key_manager)
        * [language](#language)
        * [libdir](#libdir)
        * [load_persisted_configs](#load_persisted_configs)
        * [local_address](#local_address)
        * [log_augmentation](#log_augmentation)
        * [log_debug](#log_debug)
        * [log_info](#log_info)
        * [log_notice](#log_notice)
        * [log_throttling](#log_throttling)
        * [log_warn_super_user](#log_warn_super_user)
        * [log_warning](#log_warning)
        * [logdir](#logdir)
        * [max_auth_errors_until_block](#max_auth_errors_until_block)
        * [maxlog](#maxlog)
        * [module_configdir](#module_configdir)
        * [ms_timestamp](#ms_timestamp)
        * [passive](#passive)
        * [persist_runtime_changes](#persist_runtime_changes)
        * [persistdir](#persistdir)
        * [piddir](#piddir)
        * [query_classifier_cache_size](#query_classifier_cache_size)
        * [query_retries](#query_retries)
        * [query_retry_timeout](#query_retry_timeout)
        * [rebalance_period](#rebalance_period)
        * [rebalance_threshold](#rebalance_threshold)
        * [rebalance_window](#rebalance_window)
        * [retain_last_statements](#retain_last_statements)
        * [secretsdir](#secretsdir)
        * [session_trace](#session_trace)
        * [session_trace_match](#session_trace_match)
        * [sharedir](#sharedir)
        * [skip_name_resolve](#skip_name_resolve)
        * [sql_mode](#sql_mode)
        * [substitute_variables](#substitute_variables)
        * [syslog](#syslog)
        * [threads](#threads)
        * [threads_max](#threads_max)
        * [trace_file_dir](#trace_file_dir)
        * [trace_file_size](#trace_file_size)
        * [users_refresh_interval](#users_refresh_interval)
        * [users_refresh_time](#users_refresh_time)
        * [writeq_high_water](#writeq_high_water)
        * [writeq_low_water](#writeq_low_water)
      * [Listener](#listener)

        * [address](#address)
        * [authenticator](#authenticator)
        * [authenticator_options](#authenticator_options)
        * [connection_init_sql_file](#connection_init_sql_file)
        * [connection_metadata](#connection_metadata)
        * [port](#port)
        * [protocol](#protocol)
        * [service](#service)
        * [socket](#socket)
        * [sql_mode](#sql_mode_1)
        * [user_mapping_file](#user_mapping_file)
      * [Server](#server)

        * [address](#address_1)
        * [disk_space_threshold](#disk_space_threshold)
        * [extra_port](#extra_port)
        * [max_routing_connections](#max_routing_connections)
        * [monitorpw](#monitorpw)
        * [monitoruser](#monitoruser)
        * [persistmaxtime](#persistmaxtime)
        * [persistpoolmax](#persistpoolmax)
        * [port](#port_1)
        * [priority](#priority)
        * [private_address](#private_address)
        * [proxy_protocol](#proxy_protocol)
        * [rank](#rank)
        * [replication_custom_options](#replication_custom_options)
        * [socket](#socket_1)
      * [Service](#service_1)

        * [auth_all_servers](#auth_all_servers)
        * [cluster](#cluster)
        * [connection_keepalive](#connection_keepalive)
        * [disable_sescmd_history](#disable_sescmd_history)
        * [enable_root_user](#enable_root_user)
        * [filters](#filters)
        * [force_connection_keepalive](#force_connection_keepalive)
        * [idle_session_pool_time](#idle_session_pool_time)
        * [log_auth_warnings](#log_auth_warnings)
        * [log_debug](#log_debug_1)
        * [log_info](#log_info_1)
        * [log_notice](#log_notice_1)
        * [log_warning](#log_warning_1)
        * [max_connections](#max_connections)
        * [max_sescmd_history](#max_sescmd_history)
        * [multiplex_timeout](#multiplex_timeout)
        * [net_write_timeout](#net_write_timeout)
        * [password](#password)
        * [prune_sescmd_history](#prune_sescmd_history)
        * [retain_last_statements](#retain_last_statements_1)
        * [router](#router)
        * [servers](#servers)
        * [session_track_trx_state](#session_track_trx_state)
        * [strip_db_esc](#strip_db_esc)
        * [targets](#targets)
        * [user](#user)
        * [user_accounts_file](#user_accounts_file)
        * [user_accounts_file_usage](#user_accounts_file_usage)
        * [version_string](#version_string)
        * [wait_timeout](#wait_timeout)
      * [Settings for File-based Key Manager](#settings-for-file-based-key-manager)

        * [file.keyfile](#filekeyfile)
      * [Settings for HashiCorp Vault Key Manager](#settings-for-hashicorp-vault-key-manager)

        * [vault.ca](#vaultca)
        * [vault.host](#vaulthost)
        * [vault.mount](#vaultmount)
        * [vault.port](#vaultport)
        * [vault.timeout](#vaulttimeout)
        * [vault.tls](#vaulttls)
        * [vault.token](#vaulttoken)
      * [Settings for KMIP Key Manager](#settings-for-kmip-key-manager)

        * [kmip.ca](#kmipca)
        * [kmip.cert](#kmipcert)
        * [kmip.host](#kmiphost)
        * [kmip.key](#kmipkey)
        * [kmip.port](#kmipport)
      * [Settings for TLS/SSL Encryption](#settings-for-tlsssl-encryption)

        * [ssl](#ssl)
        * [ssl_ca](#ssl_ca)
        * [ssl_cert](#ssl_cert)
        * [ssl_cert_verify_depth](#ssl_cert_verify_depth)
        * [ssl_cipher](#ssl_cipher)
        * [ssl_crl](#ssl_crl)
        * [ssl_key](#ssl_key)
        * [ssl_verify_peer_certificate](#ssl_verify_peer_certificate)
        * [ssl_verify_peer_host](#ssl_verify_peer_host)
        * [ssl_version](#ssl_version)
  * [Authenticators](#authenticators)

    * [Authentication-Modules](#authentication-modules)

      * [Settings](#settings)

        * [lower_case_table_names](#lower_case_table_names)
        * [match_host](#match_host)
        * [skip_authentication](#skip_authentication)
    * [GSSAPI-Authenticator](#gssapi-authenticator)

      * [Settings](#settings_1)

        * [gssapi_keytab_path](#gssapi_keytab_path)
        * [principal_name](#principal_name)
    * [MySQL-Authenticator](#mysql-authenticator)

      * [Settings](#settings_2)

        * [log_password_mismatch](#log_password_mismatch)
    * [PAM-Authenticator](#pam-authenticator)

      * [Settings](#settings_3)

        * [pam_backend_mapping](#pam_backend_mapping)
        * [pam_mapped_pw_file](#pam_mapped_pw_file)
        * [pam_mode](#pam_mode)
        * [pam_use_cleartext_plugin](#pam_use_cleartext_plugin)
  * [Filters](#filters_1)

    * [BinlogFilter](#binlogfilter)

      * [Settings](#settings_4)

        * [exclude](#exclude)
        * [match](#match)
        * [rewrite_dest](#rewrite_dest)
        * [rewrite_src](#rewrite_src)
    * [CCRFilter](#ccrfilter)

      * [Settings](#settings_5)

        * [count](#count)
        * [global](#global)
        * [ignore](#ignore)
        * [match](#match_1)
        * [options](#options)
        * [time](#time)
    * [Cache](#cache)

      * [Settings](#settings_6)

        * [cache_in_transactions](#cache_in_transactions)
        * [cached_data](#cached_data)
        * [clear_cache_on_parse_errors](#clear_cache_on_parse_errors)
        * [debug](#debug_1)
        * [enabled](#enabled)
        * [hard_ttl](#hard_ttl)
        * [invalidate](#invalidate)
        * [max_count](#max_count)
        * [max_resultset_rows](#max_resultset_rows)
        * [max_resultset_size](#max_resultset_size)
        * [max_size](#max_size)
        * [rules](#rules)
        * [selects](#selects)
        * [soft_ttl](#soft_ttl)
        * [storage](#storage)
        * [storage_options](#storage_options)
        * [timeout](#timeout)
        * [users](#users)
      * [storage_memcached](#storage_memcached)

        * [max_value_size](#max_value_size)
        * [server](#server_1)
      * [storage_redis](#storage_redis)

        * [password](#password_1)
        * [server](#server_2)
        * [ssl](#ssl_1)
        * [ssl_ca](#ssl_ca_1)
        * [ssl_cert](#ssl_cert_1)
        * [ssl_key](#ssl_key_1)
        * [username](#username)
    * [Comment](#comment)

      * [Settings](#settings_7)

        * [inject](#inject)
    * [LDIFilter](#ldifilter)

      * [Settings](#settings_8)

        * [host](#host)
        * [key](#key)
        * [no_verify](#no_verify)
        * [port](#port_2)
        * [protocol_version](#protocol_version)
        * [region](#region)
        * [secret](#secret)
        * [use_http](#use_http)
    * [Masking](#masking)

      * [Settings](#settings_9)

        * [check_subqueries](#check_subqueries)
        * [check_unions](#check_unions)
        * [check_user_variables](#check_user_variables)
        * [large_payload](#large_payload)
        * [prevent_function_usage](#prevent_function_usage)
        * [require_fully_parsed](#require_fully_parsed)
        * [rules](#rules_1)
        * [treat_string_arg_as_field](#treat_string_arg_as_field)
        * [warn_type_mismatch](#warn_type_mismatch)
    * [Maxrows](#maxrows)

      * [Settings](#settings_10)

        * [debug](#debug_2)
        * [max_resultset_return](#max_resultset_return)
        * [max_resultset_rows](#max_resultset_rows_1)
        * [max_resultset_size](#max_resultset_size_1)
    * [Named-Server-Filter](#named-server-filter)

      * [Settings](#settings_11)

        * [matchXY](#matchxy)
        * [options](#options_1)
        * [source](#source)
        * [targetXY](#targetxy)
        * [user](#user_1)
    * [Query-Log-All-Filter](#query-log-all-filter)

      * [Settings](#settings_12)

        * [append](#append)
        * [duration_unit](#duration_unit)
        * [exclude](#exclude_1)
        * [filebase](#filebase)
        * [flush](#flush)
        * [log_data](#log_data)
        * [log_type](#log_type)
        * [match](#match_2)
        * [newline_replacement](#newline_replacement)
        * [options](#options_2)
        * [separator](#separator)
        * [source](#source_1)
        * [source_exclude](#source_exclude)
        * [source_match](#source_match)
        * [use_canonical_form](#use_canonical_form)
        * [user](#user_2)
        * [user_exclude](#user_exclude)
        * [user_match](#user_match)
    * [Regex-Filter](#regex-filter)

      * [Settings](#settings_13)

        * [log_file](#log_file)
        * [log_trace](#log_trace)
        * [match](#match_3)
        * [options](#options_3)
        * [replace](#replace)
        * [source](#source_2)
        * [user](#user_3)
    * [RewriteFilter](#rewritefilter)

      * [Settings](#settings_14)

        * [case_sensitive](#case_sensitive)
        * [log_replacement](#log_replacement)
        * [regex_grammar](#regex_grammar)
        * [template_file](#template_file)
      * [Settings per template in the template file](#settings-per-template-in-the-template-file)

        * [case_sensitive](#case_sensitive_1)
        * [continue_if_matched](#continue_if_matched)
        * [ignore_whitespace](#ignore_whitespace)
        * [regex_grammar](#regex_grammar_1)
        * [what_if](#what_if)
    * [Tee-Filter](#tee-filter)

      * [Settings](#settings_15)

        * [exclude](#exclude_2)
        * [match](#match_4)
        * [options](#options_4)
        * [service](#service_2)
        * [source](#source_3)
        * [sync](#sync)
        * [target](#target)
        * [user](#user_4)
    * [Throttle](#throttle)

      * [Settings](#settings_16)

        * [continuous_duration](#continuous_duration)
        * [max_qps](#max_qps)
        * [sampling_duration](#sampling_duration)
        * [throttling_duration](#throttling_duration)
    * [Top-N-Filter](#top-n-filter)

      * [Settings](#settings_17)

        * [count](#count_1)
        * [exclude](#exclude_3)
        * [filebase](#filebase_1)
        * [match](#match_5)
        * [options](#options_5)
        * [source](#source_4)
        * [user](#user_5)
    * [Wcar](#wcar)

      * [Settings](#settings_18)

        * [capture_dir](#capture_dir)
        * [capture_duration](#capture_duration)
        * [capture_size](#capture_size)
        * [start_capture](#start_capture)
  * [Monitors](#monitors)

    * [Galera-Monitor](#galera-monitor)

      * [Settings](#settings_19)

        * [available_when_donor](#available_when_donor)
        * [disable_master_failback](#disable_master_failback)
        * [disable_master_role_setting](#disable_master_role_setting)
        * [root_node_as_master](#root_node_as_master)
        * [set_donor_nodes](#set_donor_nodes)
        * [use_priority](#use_priority)
    * [MariaDB-Monitor](#mariadb-monitor)

      * [Settings](#settings_20)

        * [assume_unique_hostnames](#assume_unique_hostnames)
        * [cooperative_monitoring_locks](#cooperative_monitoring_locks)
        * [enforce_read_only_servers](#enforce_read_only_servers)
        * [enforce_read_only_slaves](#enforce_read_only_slaves)
        * [enforce_writable_master](#enforce_writable_master)
        * [failcount](#failcount)
        * [maintenance_on_low_disk_space](#maintenance_on_low_disk_space)
        * [master_conditions](#master_conditions)
        * [script_max_replication_lag](#script_max_replication_lag)
        * [slave_conditions](#slave_conditions)
      * [Settings for Backup operations](#settings-for-backup-operations)

        * [backup_storage_address](#backup_storage_address)
        * [backup_storage_path](#backup_storage_path)
        * [rebuild_port](#rebuild_port)
        * [ssh_check_host_key](#ssh_check_host_key)
        * [ssh_keyfile](#ssh_keyfile)
        * [ssh_port](#ssh_port)
        * [ssh_timeout](#ssh_timeout)
        * [ssh_user](#ssh_user)
      * [Settings for Cluster manipulation operations](#settings-for-cluster-manipulation-operations)

        * [auto_failover](#auto_failover)
        * [auto_rejoin](#auto_rejoin)
        * [demotion_sql_file](#demotion_sql_file)
        * [enforce_simple_topology](#enforce_simple_topology)
        * [failover_timeout](#failover_timeout)
        * [handle_events](#handle_events)
        * [master_failure_timeout](#master_failure_timeout)
        * [promotion_sql_file](#promotion_sql_file)
        * [replication_master_ssl](#replication_master_ssl)
        * [replication_password](#replication_password)
        * [replication_user](#replication_user)
        * [servers_no_promotion](#servers_no_promotion)
        * [switchover_on_low_disk_space](#switchover_on_low_disk_space)
        * [switchover_timeout](#switchover_timeout)
        * [verify_master_failure](#verify_master_failure)
      * [Settings for Primary server write test](#settings-for-primary-server-write-test)

        * [write_test_fail_action](#write_test_fail_action)
        * [write_test_interval](#write_test_interval)
        * [write_test_table](#write_test_table)
    * [Monitor-Common](#monitor-common)

      * [Settings](#settings_21)

        * [backend_connect_attempts](#backend_connect_attempts)
        * [backend_connect_timeout](#backend_connect_timeout)
        * [backend_read_timeout](#backend_read_timeout)
        * [backend_write_timeout](#backend_write_timeout)
        * [disk_space_check_interval](#disk_space_check_interval)
        * [disk_space_threshold](#disk_space_threshold_1)
        * [events](#events)
        * [journal_max_age](#journal_max_age)
        * [module](#module)
        * [monitor_interval](#monitor_interval)
        * [password](#password_2)
        * [script](#script)
        * [script_timeout](#script_timeout)
        * [servers](#servers_1)
        * [user](#user_6)
  * [Protocols](#protocols)

    * [MariaDB](#mariadb)

      * [Settings](#settings_22)

        * [allow_replication](#allow_replication)
    * [NoSQL](#nosql)

      * [Settings](#settings_23)

        * [authentication_db](#authentication_db)
        * [authentication_key_id](#authentication_key_id)
        * [authentication_password](#authentication_password)
        * [authentication_required](#authentication_required)
        * [authentication_shared](#authentication_shared)
        * [authentication_user](#authentication_user)
        * [authorization_enabled](#authorization_enabled)
        * [auto_create_databases](#auto_create_databases)
        * [auto_create_tables](#auto_create_tables)
        * [cursor_timeout](#cursor_timeout)
        * [debug](#debug_3)
        * [host](#host_1)
        * [id_length](#id_length)
        * [internal_cache](#internal_cache)
        * [log_unknown_command](#log_unknown_command)
        * [on_unknown_command](#on_unknown_command)
        * [ordered_insert_behavior](#ordered_insert_behavior)
        * [password](#password_3)
        * [user](#user_7)
  * [Routers](#routers)

    * [Avrorouter](#avrorouter)

      * [Settings](#settings_24)

        * [avrodir](#avrodir)
        * [binlogdir](#binlogdir)
        * [codec](#codec)
        * [cooperative_replication](#cooperative_replication)
        * [exclude](#exclude_4)
        * [filestem](#filestem)
        * [gtid_start_pos](#gtid_start_pos)
        * [match](#match_6)
        * [server_id](#server_id)
        * [start_index](#start_index)
      * [Settings for Avro File](#settings-for-avro-file)

        * [block_size](#block_size)
        * [group_rows](#group_rows)
        * [group_trx](#group_trx)
        * [max_data_age](#max_data_age)
        * [max_file_size](#max_file_size)
    * [Binlogrouter](#binlogrouter)

      * [Settings](#settings_25)

        * [archivedir](#archivedir)
        * [compression_algorithm](#compression_algorithm)
        * [datadir](#datadir_1)
        * [ddl_only](#ddl_only)
        * [encryption_cipher](#encryption_cipher)
        * [encryption_key_id](#encryption_key_id)
        * [expiration_mode](#expiration_mode)
        * [expire_log_duration](#expire_log_duration)
        * [expire_log_minimum_files](#expire_log_minimum_files)
        * [net_timeout](#net_timeout)
        * [number_of_noncompressed_files](#number_of_noncompressed_files)
        * [rpl_semi_sync_slave_enabled](#rpl_semi_sync_slave_enabled)
        * [select_master](#select_master)
        * [server_id](#server_id_1)
    * [Diff](#diff)

      * [Settings](#settings_26)

        * [explain](#explain)
        * [explain_entries](#explain_entries)
        * [explain_period](#explain_period)
        * [main](#main)
        * [max_request_lag](#max_request_lag)
        * [on_error](#on_error)
        * [percentile](#percentile)
        * [qps_window](#qps_window)
        * [report](#report)
        * [reset_replication](#reset_replication)
        * [retain_faster_statements](#retain_faster_statements)
        * [retain_slower_statements](#retain_slower_statements)
        * [samples](#samples)
        * [service](#service_3)
    * [KafkaCDC](#kafkacdc)

      * [Settings](#settings_27)

        * [bootstrap_servers](#bootstrap_servers)
        * [cooperative_replication](#cooperative_replication_1)
        * [enable_idempotence](#enable_idempotence)
        * [exclude](#exclude_5)
        * [gtid](#gtid)
        * [kafka_sasl_mechanism](#kafka_sasl_mechanism)
        * [kafka_sasl_password](#kafka_sasl_password)
        * [kafka_sasl_user](#kafka_sasl_user)
        * [kafka_ssl](#kafka_ssl)
        * [kafka_ssl_ca](#kafka_ssl_ca)
        * [kafka_ssl_cert](#kafka_ssl_cert)
        * [kafka_ssl_key](#kafka_ssl_key)
        * [match](#match_7)
        * [read_gtid_from_kafka](#read_gtid_from_kafka)
        * [send_schema](#send_schema)
        * [server_id](#server_id_2)
        * [timeout](#timeout_1)
        * [topic](#topic)
    * [KafkaImporter](#kafkaimporter)

      * [Settings](#settings_28)

        * [batch_size](#batch_size)
        * [bootstrap_servers](#bootstrap_servers_1)
        * [engine](#engine)
        * [kafka_sasl_mechanism](#kafka_sasl_mechanism_1)
        * [kafka_sasl_password](#kafka_sasl_password_1)
        * [kafka_sasl_user](#kafka_sasl_user_1)
        * [kafka_ssl](#kafka_ssl_1)
        * [kafka_ssl_ca](#kafka_ssl_ca_1)
        * [kafka_ssl_cert](#kafka_ssl_cert_1)
        * [kafka_ssl_key](#kafka_ssl_key_1)
        * [table_name_in](#table_name_in)
        * [timeout](#timeout_2)
        * [topics](#topics)
    * [Mirror](#mirror)

      * [Settings](#settings_29)

        * [exporter](#exporter)
        * [file](#file)
        * [kafka_broker](#kafka_broker)
        * [kafka_topic](#kafka_topic)
        * [main](#main_1)
        * [on_error](#on_error_1)
        * [report](#report_1)
    * [ReadConnRoute](#readconnroute)

      * [Settings](#settings_30)

        * [master_accept_reads](#master_accept_reads)
        * [max_replication_lag](#max_replication_lag)
        * [router_options](#router_options)
    * [ReadWriteSplit](#readwritesplit)

      * [Settings](#settings_31)

        * [causal_reads](#causal_reads)
        * [causal_reads_timeout](#causal_reads_timeout)
        * [delayed_retry](#delayed_retry)
        * [delayed_retry_timeout](#delayed_retry_timeout)
        * [lazy_connect](#lazy_connect)
        * [master_accept_reads](#master_accept_reads_1)
        * [master_failure_mode](#master_failure_mode)
        * [master_reconnection](#master_reconnection)
        * [max_replication_lag](#max_replication_lag_1)
        * [max_slave_connections](#max_slave_connections)
        * [retry_failed_reads](#retry_failed_reads)
        * [slave_connections](#slave_connections)
        * [slave_selection_criteria](#slave_selection_criteria)
        * [strict_multi_stmt](#strict_multi_stmt)
        * [strict_sp_calls](#strict_sp_calls)
        * [strict_tmp_tables](#strict_tmp_tables)
        * [transaction_replay](#transaction_replay)
        * [transaction_replay_attempts](#transaction_replay_attempts)
        * [transaction_replay_checksum](#transaction_replay_checksum)
        * [transaction_replay_max_size](#transaction_replay_max_size)
        * [transaction_replay_retry_on_deadlock](#transaction_replay_retry_on_deadlock)
        * [transaction_replay_retry_on_mismatch](#transaction_replay_retry_on_mismatch)
        * [transaction_replay_safe_commit](#transaction_replay_safe_commit)
        * [transaction_replay_timeout](#transaction_replay_timeout)
        * [use_sql_variables_in](#use_sql_variables_in)
    * [SchemaRouter](#schemarouter)

      * [Settings](#settings_32)

        * [allow_duplicates](#allow_duplicates)
        * [ignore_tables](#ignore_tables)
        * [ignore_tables_regex](#ignore_tables_regex)
        * [max_staleness](#max_staleness)
        * [refresh_databases](#refresh_databases)
        * [refresh_interval](#refresh_interval)
    * [SmartRouter](#smartrouter)

      * [Settings](#settings_33)

        * [master](#master)




## General


### [MaxScale](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


#### Global Settings


##### [admin_audit](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


##### [admin_audit_exclude_methods](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>GET</code>`, `<code>PUT</code>`, `<code>POST</code>`, `<code>PATCH</code>`, `<code>DELETE</code>`, `<code>HEAD</code>`, `<code>OPTIONS</code>`, `<code>CONNECT</code>`, `<code>TRACE</code>`
* Default: No exclusions


##### [admin_audit_file](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `<code>/var/log/maxscale/admin_audit.csv</code>`


##### [admin_auth](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>true</code>`


##### [admin_enabled](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>true</code>`


##### [admin_gui](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>true</code>`


##### [admin_host](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>"127.0.0.1"</code>`


##### [admin_jwt_algorithm](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>auto</code>`, `<code>HS256</code>`, `<code>HS384</code>`, `<code>HS512</code>`, `<code>RS256</code>`, `<code>RS384</code>`, `<code>RS512</code>`, `<code>PS256</code>`, `<code>PS384</code>`, `<code>PS512</code>`, `<code>ES256</code>`, `<code>ES384</code>`, `<code>ES512</code>`, `<code>ED25519</code>`, `<code>ED448</code>`
* Default: `<code>auto</code>`


##### [admin_jwt_issuer](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>maxscale</code>`


##### [admin_jwt_key](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [admin_jwt_max_age](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>24h</code>`


##### [admin_log_auth_failures](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


##### [admin_oidc_url](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [admin_pam_readonly_service](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [admin_pam_readwrite_service](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [admin_port](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: No
* Default: `<code>8989</code>`


##### [admin_readwrite_hosts](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>%</code>`


##### [admin_secure_gui](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>true</code>`


##### [admin_ssl_ca](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [admin_ssl_cert](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [admin_ssl_cipher](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No


##### [admin_ssl_key](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [admin_ssl_version](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [enum_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>MAX</code>`, `<code>TLSv1.0</code>`, `<code>TLSv1.1</code>`, `<code>TLSv1.2</code>`, `<code>TLSv1.3</code>`, `<code>TLSv10</code>`, `<code>TLSv11</code>`, `<code>TLSv12</code>`, `<code>TLSv13</code>`
* Default: `<code>MAX</code>`


##### [admin_verify_url](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [auth_connect_timeout](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>10s</code>`


##### [auto_tune](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string list
* Values: `<code>all</code>` or list of auto tunable parameters, separated by `<code>,</code>`
* Default: No
* Mandatory: No
* Dynamic: No


##### [cachedir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>/var/cache/maxscale</code>`


##### [config_sync_cluster](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: monitor
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [config_sync_db](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>mysql</code>`


##### [config_sync_interval](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>5s</code>`


##### [config_sync_password](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: password
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [config_sync_timeout](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>10s</code>`


##### [config_sync_user](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [connector_plugindir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: OS Dependent


##### [core_file](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: true
* Dynamic: No


##### [datadir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>/var/lib/maxscale</code>`


##### [debug](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [dump_last_statements](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>on_close</code>`, `<code>on_error</code>`, `<code>never</code>`
* Default: `<code>never</code>`


##### [execdir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>/usr/bin</code>`


##### [host_cache_size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: integer
* Default: 128
* Dynamic: Yes


##### [key_manager](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Dynamic: Yes
* Values: `<code>none</code>`, `<code>file</code>`, `<code>kmip</code>`, `<code>vault</code>`
* Default: `<code>none</code>`


##### [language](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>/var/lib/maxscale/</code>`


##### [libdir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: OS Dependent


##### [load_persisted_configs](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>true</code>`


##### [local_address](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [log_augmentation](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>0</code>`


##### [log_debug](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [log_info](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [log_notice](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


##### [log_throttling](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number, [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md), [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>10, 1000ms, 10000ms</code>`


##### [log_warn_super_user](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>false</code>`


##### [log_warning](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


##### [logdir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>/var/log/maxscale</code>`


##### [max_auth_errors_until_block](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>10</code>`


##### [maxlog](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


##### [module_configdir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>/etc/maxscale.modules.d/</code>`


##### [ms_timestamp](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [passive](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [persist_runtime_changes](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: true
* Dynamic: No


##### [persistdir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>/var/lib/maxscale/maxscale.cnf.d/</code>`


##### [piddir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>/run/maxscale</code>`


##### [query_classifier_cache_size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: System Dependent


##### [query_retries](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: No
* Default: `<code>1</code>`


##### [query_retry_timeout](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>10s</code>`


##### [rebalance_period](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>0s</code>`


##### [rebalance_threshold](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>20</code>`


##### [rebalance_window](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>10</code>`


##### [retain_last_statements](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>0</code>`


##### [secretsdir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [session_trace](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>0</code>`


##### [session_trace_match](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [sharedir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>/usr/share/maxscale</code>`


##### [skip_name_resolve](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [sql_mode](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>default</code>`, `<code>oracle</code>`
* Default: `<code>default</code>`


##### [substitute_variables](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>false</code>`


##### [syslog](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [threads](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number or `<code>auto</code>`
* Mandatory: No
* Dynamic: No
* Default: `<code>auto</code>`


##### [threads_max](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: positive integer
* Default: 256
* Dynamic: No


##### [trace_file_dir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No


##### [trace_file_size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes


##### [users_refresh_interval](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>0s</code>`


##### [users_refresh_time](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>30s</code>`


##### [writeq_high_water](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>65536</code>`


##### [writeq_low_water](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>1024</code>`


#### Listener


##### [address](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>"::"</code>`


##### [authenticator](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [authenticator_options](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [connection_init_sql_file](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


##### [connection_metadata](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: stringlist
* Default: `<code>character_set_client=auto,character_set_connection=auto,character_set_results=auto,max_allowed_packet=auto,system_time_zone=auto,time_zone=auto,tx_isolation=auto,maxscale=auto</code>`
* Dynamic: Yes
* Mandatory: No


##### [port](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: Yes, if `<code>socket</code>` is not provided.
* Dynamic: No
* Default: `<code>0</code>`


##### [protocol](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: protocol
* Mandatory: No
* Dynamic: No
* Default: `<code>mariadb</code>`


##### [service](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: service
* Mandatory: Yes
* Dynamic: No


##### [socket](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: Yes, if `<code>port</code>` is not provided.
* Dynamic: No
* Default: `<code>""</code>`


##### [sql_mode](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>default</code>`, `<code>oracle</code>`
* Default: `<code>default</code>`


##### [user_mapping_file](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


#### Server


##### [address](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: Yes, if `<code>socket</code>` is not provided.
* Dynamic: Yes
* Default: `<code>""</code>`


##### [disk_space_threshold](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: Custom
* Mandatory: No
* Dynamic: No
* Default: None


##### [extra_port](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>0</code>`


##### [max_routing_connections](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>0</code>`


##### [monitorpw](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [monitoruser](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [persistmaxtime](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>0s</code>`


##### [persistpoolmax](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>0</code>`


##### [port](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>3306</code>`


##### [priority](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: 0


##### [private_address](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


##### [proxy_protocol](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [rank](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>primary</code>`, `<code>secondary</code>`
* Default: `<code>primary</code>`


##### [replication_custom_options](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Default: None
* Dynamic: Yes


##### [socket](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: Yes, if `<code>address</code>` is not provided.
* Dynamic: Yes
* Default: `<code>""</code>`


#### Service


##### [auth_all_servers](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [cluster](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: monitor
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [connection_keepalive](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>300s</code>`
* Auto tune: [Yes](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


##### [disable_sescmd_history](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [enable_root_user](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [filters](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: filter list
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [force_connection_keepalive](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: boolean
* Mandatory No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [idle_session_pool_time](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>-1s</code>`


##### [log_auth_warnings](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


##### [log_debug](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [log_info](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [log_notice](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [log_warning](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [max_connections](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>0</code>`


##### [max_sescmd_history](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>50</code>`


##### [multiplex_timeout](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>60s</code>`


##### [net_write_timeout](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [durations](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory No
* Dynamic: Yes
* Default: `<code>0s</code>`


##### [password](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: Yes
* Dynamic: Yes


##### [prune_sescmd_history](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


##### [retain_last_statements](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>-1</code>`


##### [router](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: router
* Mandatory: Yes
* Dynamic: No


##### [servers](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: server list
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [session_track_trx_state](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [strip_db_esc](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


##### [targets](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: target list
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [user](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: Yes
* Dynamic: Yes


##### [user_accounts_file](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [user_accounts_file_usage](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>add_when_load_ok</code>`, `<code>file_only_always</code>`
* Default: `<code>add_when_load_ok</code>`


##### [version_string](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: None


##### [wait_timeout](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>0s</code>`
* Auto tune: [Yes](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


#### Settings for File-based Key Manager


##### [file.keyfile](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: Yes
* Dynamic: Yes


#### Settings for HashiCorp Vault Key Manager


##### [vault.ca](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Default: `<code>""</code>`
* Dynamic: Yes


##### [vault.host](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Default: `<code>localhost</code>`
* Dynamic: Yes


##### [vault.mount](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Default: `<code>secret</code>`
* Dynamic: Yes


##### [vault.port](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: integer
* Default: `<code>8200</code>`
* Dynamic: Yes


##### [vault.timeout](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: 30s
* Dynamic: Yes


##### [vault.tls](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: true
* Dynamic: Yes


##### [vault.token](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: password
* Mandatory: Yes
* Dynamic: Yes


#### Settings for KMIP Key Manager


##### [kmip.ca](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Default: `<code>""</code>`
* Dynamic: Yes


##### [kmip.cert](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: Yes
* Dynamic: Yes


##### [kmip.host](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: Yes
* Dynamic: Yes


##### [kmip.key](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: Yes
* Dynamic: Yes


##### [kmip.port](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: integer
* Mandatory: Yes
* Dynamic: Yes


#### Settings for TLS/SSL Encryption


##### [ssl](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


##### [ssl_ca](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


##### [ssl_cert](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


##### [ssl_cert_verify_depth](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>9</code>`


##### [ssl_cipher](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


##### [ssl_crl](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


##### [ssl_key](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


##### [ssl_verify_peer_certificate](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [ssl_verify_peer_host](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [ssl_version](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [enum_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>MAX</code>`, `<code>TLSv1.0</code>`, `<code>TLSv1.1</code>`, `<code>TLSv1.2</code>`, `<code>TLSv1.3</code>`, `<code>TLSv10</code>`, `<code>TLSv11</code>`, `<code>TLSv12</code>`, `<code>TLSv13</code>`
* Default: `<code>MAX</code>`


## Authenticators


### [Authentication-Modules](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-authentication-modules.md)


#### Settings


##### [lower_case_table_names](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-authentication-modules.md)


* Type: number
* Mandatory: No
* Dynamic: No
* Default: `<code>0</code>`


##### [match_host](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-authentication-modules.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>true</code>`


##### [skip_authentication](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-authentication-modules.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>false</code>`


### [GSSAPI-Authenticator](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-gssapi-client-authenticator.md)


#### Settings


##### [gssapi_keytab_path](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-gssapi-client-authenticator.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: Kerberos Default


##### [principal_name](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-gssapi-client-authenticator.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>mariadb/localhost.localdomain</code>`


### [MySQL-Authenticator](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-mariadbmysql-authenticator.md)


#### Settings


##### [log_password_mismatch](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-mariadbmysql-authenticator.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>false</code>`


### [PAM-Authenticator](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)


#### Settings


##### [pam_backend_mapping](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)


* Type: [enumeration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>none</code>`, `<code>mariadb</code>`
* Default: `<code>none</code>`


##### [pam_mapped_pw_file](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: None


##### [pam_mode](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)


* Type: [enumeration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>password</code>`, `<code>password_2FA</code>`, `<code>suid</code>`
* Default: `<code>password</code>`


##### [pam_use_cleartext_plugin](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>false</code>`


## Filters


### [BinlogFilter](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-binlog-filter.md)


#### Settings


##### [exclude](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-binlog-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [match](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-binlog-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [rewrite_dest](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-binlog-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [rewrite_src](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-binlog-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


### [CCRFilter](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)


#### Settings


##### [count](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)


* Type: count
* Mandatory: No
* Dynamic: Yes
* Default: `<code>0</code>`


##### [global](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [ignore](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [match](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [options](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>ignorecase</code>`, `<code>case</code>`, `<code>extended</code>`
* Default: `<code>ignorecase</code>`


##### [time](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>60s</code>`


### [Cache](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


#### Settings


##### [cache_in_transactions](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>never</code>`, `<code>read_only_transactions</code>`, `<code>all_transactions</code>`
* Default: `<code>all_transactions</code>`


##### [cached_data](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>shared</code>`, `<code>thread_specific</code>`
* Default: `<code>thread_specific</code>`


##### [clear_cache_on_parse_errors](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>true</code>`


##### [debug](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>0</code>`


##### [enabled](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>true</code>`


##### [hard_ttl](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>0s</code>` (no limit)


##### [invalidate](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>never</code>`, `<code>current</code>`
* Default: `<code>never</code>`


##### [max_count](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: count
* Mandatory: No
* Dynamic: No
* Default: `<code>0</code>` (no limit)


##### [max_resultset_rows](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: count
* Mandatory: No
* Dynamic: No
* Default: `<code>0</code>` (no limit)


##### [max_resultset_size](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>0</code>` (no limit)


##### [max_size](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>0</code>` (no limit)


##### [rules](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>` (no rules)


##### [selects](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>assume_cacheable</code>`, `<code>verify_cacheable</code>`
* Default: `<code>assume_cacheable</code>`


##### [soft_ttl](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>0s</code>` (no limit)


##### [storage](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>storage_inmemory</code>`


##### [storage_options](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default:


##### [timeout](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>5s</code>`


##### [users](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>mixed</code>`, `<code>isolated</code>`
* Default: `<code>mixed</code>`


#### `<code>storage_memcached</code>`


##### [max_value_size](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: 1Mi


##### [server](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: The Memcached server address specified as `<code>host[:port]</code>`
* Mandatory: Yes
* Dynamic: No


#### `<code>storage_redis</code>`


##### [password](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [server](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: The Redis server address specified as `<code>host[:port]</code>`
* Mandatory: Yes
* Dynamic: No


##### [ssl](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>false</code>`


##### [ssl_ca](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [ssl_cert](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [ssl_key](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [username](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


### [Comment](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-comment-filter.md)


#### Settings


##### [inject](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-comment-filter.md)


* Type: string
* Mandatory: Yes
* Dynamic: Yes


### [LDIFilter](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)


#### Settings


##### [host](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `<code>s3.amazonaws.com</code>`


##### [key](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes


##### [no_verify](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


##### [port](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)


* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 0


##### [protocol_version](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)


* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 0
* Values: 0, 1, 2


##### [region](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `<code>us-east-1</code>`


##### [secret](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes


##### [use_http](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


### [Masking](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)


#### Settings


##### [check_subqueries](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)


* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


##### [check_unions](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)


* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


##### [check_user_variables](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)


* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


##### [large_payload](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>ignore</code>`, `<code>abort</code>`
* Default: `<code>abort</code>`


##### [prevent_function_usage](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)


* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


##### [require_fully_parsed](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)


* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


##### [rules](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)


* Type: path
* Mandatory: Yes
* Dynamic: Yes


##### [treat_string_arg_as_field](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)


* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


##### [warn_type_mismatch](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>never</code>`, `<code>always</code>`
* Default: `<code>never</code>`


### [Maxrows](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)


#### Settings


##### [debug](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>0</code>`


##### [max_resultset_return](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>empty</code>`, `<code>error</code>`, `<code>ok</code>`
* Default: `<code>empty</code>`


##### [max_resultset_rows](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: (no limit)


##### [max_resultset_size](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>64Ki</code>`


### [Named-Server-Filter](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-named-server-filter.md)


#### Settings


##### [matchXY](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-named-server-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [options](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-named-server-filter.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>ignorecase</code>`, `<code>case</code>`, `<code>extended</code>`
* Default: `<code>ignorecase</code>`


##### [source](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-named-server-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [targetXY](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-named-server-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [user](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-named-server-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


### [Query-Log-All-Filter](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


#### Settings


##### [append](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


##### [duration_unit](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `<code>milliseconds</code>`


##### [exclude](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [filebase](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: string
* Mandatory: Yes
* Dynamic: No


##### [flush](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [log_data](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: [enum_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>service</code>`, `<code>session</code>`, `<code>date</code>`, `<code>user</code>`, `<code>reply_time</code>`, `<code>total_reply_time</code>`, `<code>query</code>`, `<code>default_db</code>`, `<code>num_rows</code>`, `<code>reply_size</code>`, `<code>transaction</code>`, `<code>transaction_time</code>`, `<code>num_warnings</code>`, `<code>error_msg</code>`
* Default: `<code>date, user, query</code>`


##### [log_type](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: [enum_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>session</code>`, `<code>unified</code>`, `<code>stdout</code>`
* Default: `<code>session</code>`


##### [match](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [newline_replacement](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `<code>" "</code>`


##### [options](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: [enum_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>case</code>`, `<code>ignorecase</code>`, `<code>extended</code>`
* Default: `<code>case</code>`


##### [separator](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `<code>","</code>`


##### [source](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


##### [source_exclude](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes


##### [source_match](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes


##### [use_canonical_form](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [user](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


##### [user_exclude](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes


##### [user_match](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes


### [Regex-Filter](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)


#### Settings


##### [log_file](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [log_trace](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [match](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: Yes
* Dynamic: Yes


##### [options](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>ignorecase</code>`, `<code>case</code>`, `<code>extended</code>`
* Default: `<code>ignorecase</code>`


##### [replace](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)


* Type: string
* Mandatory: Yes
* Dynamic: Yes


##### [source](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [user](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


### [RewriteFilter](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)


#### Settings


##### [case_sensitive](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)


* Type: boolean
* Mandatory: No
* Dynamic: Yes
* Default: true


##### [log_replacement](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)


* Type: boolean
* Mandatory: No
* Dynamic: Yes
* Default: false


##### [regex_grammar](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: Native
* Values: `<code>Native</code>`, `<code>ECMAScript</code>`, `<code>Posix</code>`, `<code>EPosix</code>`, `<code>Awk</code>`, `<code>Grep</code>`, `<code>EGrep</code>`


##### [template_file](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)


* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Default: No default value


#### Settings per template in the template file


##### [case_sensitive](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)


* Type: boolean
* Default: From maxscale.cnf


##### [continue_if_matched](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)


* Type: boolean
* Default: false


##### [ignore_whitespace](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)


* Type: boolean
* Default: true


##### [regex_grammar](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)


* Type: string
* Values: `<code>Native</code>`, `<code>ECMAScript</code>`, `<code>Posix</code>`, `<code>EPosix</code>`, `<code>Awk</code>`, `<code>Grep</code>`, `<code>EGrep</code>`
* Default: From maxscale.cnf


##### [what_if](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)


* Type: boolean
* Default: false


### [Tee-Filter](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)


#### Settings


##### [exclude](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [match](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [options](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>ignorecase</code>`, `<code>case</code>`, `<code>extended</code>`
* Default: `<code>ignorecase</code>`


##### [service](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)


* Type: service
* Mandatory: No
* Dynamic: Yes
* Default: none


##### [source](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [sync](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [target](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)


* Type: target
* Mandatory: No
* Dynamic: Yes
* Default: none


##### [user](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


### [Throttle](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-throttle.md)


#### Settings


##### [continuous_duration](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-throttle.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 2s


##### [max_qps](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-throttle.md)


* Type: number
* Mandatory: Yes
* Dynamic: Yes


##### [sampling_duration](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-throttle.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 250ms


##### [throttling_duration](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-throttle.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: Yes
* Dynamic: Yes


### [Top-N-Filter](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)


#### Settings


##### [count](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>10</code>`


##### [exclude](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [filebase](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)


* Type: string
* Mandatory: Yes
* Dynamic: Yes


##### [match](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [options](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>ignorecase</code>`, `<code>case</code>`, `<code>extended</code>`
* Default: `<code>case</code>`


##### [source](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [user](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


### [Wcar](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-workload-capture-and-replay.md)


#### Settings


##### [capture_dir](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-workload-capture-and-replay.md)


* Type: path
* Default: /var/lib/maxscale/wcar/
* Mandatory: No
* Dynamic: No


##### [capture_duration](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-workload-capture-and-replay.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: 0s
* Mandatory: No
* Dynamic: No


##### [capture_size](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-workload-capture-and-replay.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: 0
* Mandatory: No
* Dynamic: No


##### [start_capture](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-workload-capture-and-replay.md)


* Type: boolean
* Default: false
* Mandatory: No
* Dynamic: No


## Monitors


### [Galera-Monitor](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)


#### Settings


##### [available_when_donor](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)


* Type: boolean
* Default: false
* Dynamic: Yes


##### [disable_master_failback](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)


* Type: boolean
* Default: false
* Dynamic: Yes


##### [disable_master_role_setting](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)


* Type: boolean
* Default: false
* Dynamic: Yes


##### [root_node_as_master](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)


* Type: boolean
* Default: false
* Dynamic: Yes


##### [set_donor_nodes](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)


* Type: boolean
* Default: false
* Dynamic: Yes


##### [use_priority](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)


* Type: boolean
* Default: false
* Dynamic: Yes


### [MariaDB-Monitor](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


#### Settings


##### [assume_unique_hostnames](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


##### [cooperative_monitoring_locks](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>none</code>`, `<code>majority_of_all</code>`, `<code>majority_of_running</code>`
* Default: `<code>none</code>`


##### [enforce_read_only_servers](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [enforce_read_only_slaves](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [enforce_writable_master](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [failcount](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>5</code>`


##### [maintenance_on_low_disk_space](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


##### [master_conditions](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [enum_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>none</code>`, `<code>connecting_slave</code>`, `<code>connected_slave</code>`, `<code>running_slave</code>`, `<code>primary_monitor_master</code>`, `<code>disk_space_ok</code>`
* Default: `<code>primary_monitor_master, disk_space_ok</code>`


##### [script_max_replication_lag](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>-1</code>`


##### [slave_conditions](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [enum_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>none</code>`, `<code>linked_master</code>`, `<code>running_master</code>`, `<code>writable_master</code>`, `<code>primary_monitor_master</code>`
* Default: `<code>none</code>`


#### Settings for Backup operations


##### [backup_storage_address](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [backup_storage_path](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [rebuild_port](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>4444</code>`


##### [ssh_check_host_key](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


##### [ssh_keyfile](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [ssh_port](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>22</code>`


##### [ssh_timeout](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>10s</code>`


##### [ssh_user](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


#### Settings for Cluster manipulation operations


##### [auto_failover](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>true</code>`, `<code>on</code>`, `<code>yes</code>`, `<code>1</code>`, `<code>false</code>`, `<code>off</code>`, `<code>no</code>`, `<code>0</code>`, `<code>safe</code>`
* Default: `<code>false</code>`


##### [auto_rejoin](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [demotion_sql_file](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [enforce_simple_topology](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [failover_timeout](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>90s</code>`


##### [handle_events](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


##### [master_failure_timeout](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>10s</code>`


##### [promotion_sql_file](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [replication_master_ssl](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [replication_password](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [replication_user](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [servers_no_promotion](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [switchover_on_low_disk_space](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [switchover_timeout](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>90s</code>`


##### [verify_master_failure](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


#### Settings for Primary server write test


##### [write_test_fail_action](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: `<code>log</code>`
* Values: `<code>log</code>`, `<code>failover</code>`
* Dynamic: Yes


##### [write_test_interval](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Dynamic: Yes
* Default: 0s


##### [write_test_table](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: string
* Dynamic: Yes
* Default: `<code>mxs.maxscale_write_test</code>`


### [Monitor-Common](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


#### Settings


##### [backend_connect_attempts](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>1</code>`


##### [backend_connect_timeout](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>3s</code>`


##### [backend_read_timeout](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>3s</code>`


##### [backend_write_timeout](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>3s</code>`


##### [disk_space_check_interval](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>0s</code>`


##### [disk_space_threshold](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [events](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: enum
* Mandatory: No
* Dynamic: Yes
* Values: `<code>master_down</code>`, `<code>master_up</code>`, `<code>slave_down</code>`, `<code>slave_up</code>`, `<code>server_down</code>`, `<code>server_up</code>`, `<code>lost_master</code>`, `<code>lost_slave</code>`, `<code>new_master</code>`, `<code>new_slave</code>`
* Default: All events


##### [journal_max_age](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>28800s</code>`


##### [module](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: string
* Mandatory: Yes
* Dynamic: No


##### [monitor_interval](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>2s</code>`


##### [password](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: string
* Mandatory: Yes
* Dynamic: Yes


##### [script](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [script_timeout](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>90s</code>`


##### [servers](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: string
* Mandatory: Yes
* Dynamic: Yes


##### [user](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: string
* Mandatory: Yes
* Dynamic: Yes


## Protocols


### [MariaDB](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-mariadb-protocol-module.md)


#### Settings


##### [allow_replication](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-mariadb-protocol-module.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true


### [NoSQL](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


#### Settings


##### [authentication_db](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: string
* Mandatory: No
* Default: `<code>"NoSQL"</code>`


##### [authentication_key_id](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: string
* Mandatory: No
* Default: `<code>""</code>`


##### [authentication_password](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: string
* Mandatory: No
* Default: `<code>""</code>`


##### [authentication_required](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `<code>false</code>`


##### [authentication_shared](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `<code>false</code>`


##### [authentication_user](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: string
* Mandatory: Yes, if `<code>authentication_shared</code>` is true.


##### [authorization_enabled](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `<code>false</code>`


##### [auto_create_databases](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `<code>true</code>`


##### [auto_create_tables](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `<code>true</code>`


##### [cursor_timeout](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `<code>60s</code>`


##### [debug](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [enum_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Values: `<code>none</code>`, `<code>in</code>`, `<code>out</code>`, `<code>back</code>`
* Default: `<code>none</code>`


##### [host](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: string
* Mandatory: No
* Default: `<code>"%"</code>`


##### [id_length](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: count
* Mandatory: No
* Range: `<code>[35, 2048]</code>`
* *Default: `<code>35</code>`


##### [internal_cache](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: string
* Mandatory: No
* Default: ''


##### [log_unknown_command](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `<code>false</code>`


##### [on_unknown_command](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Values: `<code>return_error</code>`, `<code>return_empty</code>`
* Default: `<code>return_error</code>`


##### [ordered_insert_behavior](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Values: `<code>atomic</code>`, `<code>default</code>`
* Default: `<code>default</code>`


##### [password](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: string
* Mandatory: No
* Default: `<code>""</code>`


##### [user](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: string
* Mandatory: No
* Default: `<code>""</code>`


## Routers


### [Avrorouter](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-avrorouter-tutorial.md)


#### Settings


##### [avrodir](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-avrorouter-tutorial.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>/var/lib/maxscale/</code>`


##### [binlogdir](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-avrorouter-tutorial.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>/var/lib/maxscale/</code>`


##### [codec](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-avrorouter-tutorial.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>null</code>`, `<code>deflate</code>`
* Default: `<code>null</code>`


##### [cooperative_replication](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-avrorouter-tutorial.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>false</code>`


##### [exclude](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-avrorouter-tutorial.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [filestem](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-avrorouter-tutorial.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>mysql-bin</code>`


##### [gtid_start_pos](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-avrorouter-tutorial.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [match](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-avrorouter-tutorial.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [server_id](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-avrorouter-tutorial.md)


* Type: number
* Mandatory: No
* Dynamic: No
* Default: `<code>1234</code>`


##### [start_index](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-avrorouter-tutorial.md)


* Type: number
* Mandatory: No
* Dynamic: No
* Default: `<code>1</code>`


#### Settings for Avro File


##### [block_size](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-avrorouter-tutorial.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>16KiB</code>`


##### [group_rows](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-avrorouter-tutorial.md)


* Type: number
* Mandatory: No
* Dynamic: No
* Default: `<code>1000</code>`


##### [group_trx](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-avrorouter-tutorial.md)


* Type: number
* Mandatory: No
* Dynamic: No
* Default: `<code>1</code>`


##### [max_data_age](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-avrorouter-tutorial.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: 0s


##### [max_file_size](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-avrorouter-tutorial.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: 0


### [Binlogrouter](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


#### Settings


##### [archivedir](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: string
* Mandatory: Yes
* Default: No
* Dynamic: No


##### [compression_algorithm](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>none</code>`, `<code>zstandard</code>`
* Default: `<code>none</code>`


##### [datadir](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>/var/lib/maxscale/binlogs</code>`


##### [ddl_only](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: boolean
* Mandatory: No
* Dynamic: No
* Default: false


##### [encryption_cipher](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>AES_CBC</code>`, `<code>AES_CTR</code>`, `<code>AES_GCM</code>`
* Default: `<code>AES_GCM</code>`


##### [encryption_key_id](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [expiration_mode](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Dynamic: No
* Values: `<code>purge</code>`, `<code>archive</code>`
* Default: `<code>purge</code>`


##### [expire_log_duration](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>0s</code>`


##### [expire_log_minimum_files](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: number
* Mandatory: No
* Dynamic: No
* Default: `<code>2</code>`


##### [net_timeout](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>10s</code>`


##### [number_of_noncompressed_files](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: count
* Mandatory: No
* Dynamic: No
* Default: `<code>2</code>`


##### [rpl_semi_sync_slave_enabled](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: false
* Dynamic: Yes


##### [select_master](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>false</code>`


##### [server_id](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: count
* Mandatory: No
* Dynamic: No
* Default: `<code>1234</code>`


### [Diff](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)


#### Settings


##### [explain](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>none</code>`, `<code>other</code>`, `both'
* Default: `<code>both</code>`


##### [explain_entries](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)


* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 2


##### [explain_period](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 15m


##### [main](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)


* Type: server
* Mandatory: Yes
* Dynamic: No


##### [max_request_lag](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)


* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 10


##### [on_error](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>close</code>`, `<code>ignore</code>`
* Default: `<code>ignore</code>`


##### [percentile](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)


* Type: count
* Mandatory: No
* Dynamic: Yes
* Min: 1
* Max: 100
* Default: 99


##### [qps_window](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: 15m


##### [report](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>always</code>`, `<code>on_discrepancy</code>`, `<code>never</code>`
* Default: `<code>on_discrepancy</code>`


##### [reset_replication](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


##### [retain_faster_statements](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)


* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 5


##### [retain_slower_statements](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)


* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 5


##### [samples](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)


* Type: count
* Mandatory: No
* Dynamic: Yes
* Min: 100
* Default: 1000


##### [service](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)


* Type: service
* Mandatory: Yes
* Dynamic: No


### [KafkaCDC](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


#### Settings


##### [bootstrap_servers](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: string
* Mandatory: Yes
* Dynamic: No


##### [cooperative_replication](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>false</code>`


##### [enable_idempotence](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>false</code>`


##### [exclude](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


##### [gtid](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [kafka_sasl_mechanism](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `<code>PLAIN</code>`, `<code>SCRAM-SHA-256</code>`, `<code>SCRAM-SHA-512</code>`
* Default: `<code>PLAIN</code>`


##### [kafka_sasl_password](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [kafka_sasl_user](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [kafka_ssl](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>false</code>`


##### [kafka_ssl_ca](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [kafka_ssl_cert](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [kafka_ssl_key](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [match](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


##### [read_gtid_from_kafka](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>true</code>`


##### [send_schema](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true


##### [server_id](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: number
* Mandatory: No
* Dynamic: No
* Default: `<code>1234</code>`


##### [timeout](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>10s</code>`


##### [topic](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: string
* Mandatory: Yes
* Dynamic: No


### [KafkaImporter](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


#### Settings


##### [batch_size](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: count
* Mandatory: No
* Dynamic: Yes
* Default: `<code>100</code>`


##### [bootstrap_servers](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: string
* Mandatory: Yes
* Dynamic: Yes


##### [engine](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: string
* Default: `<code>InnoDB</code>`
* Mandatory: No
* Dynamic: Yes


##### [kafka_sasl_mechanism](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>PLAIN</code>`, `<code>SCRAM-SHA-256</code>`, `<code>SCRAM-SHA-512</code>`
* Default: `<code>PLAIN</code>`


##### [kafka_sasl_password](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


##### [kafka_sasl_user](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


##### [kafka_ssl](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


##### [kafka_ssl_ca](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


##### [kafka_ssl_cert](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


##### [kafka_ssl_key](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


##### [table_name_in](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>topic</code>`, `<code>key</code>`
* Default: `<code>topic</code>`


##### [timeout](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>5000ms</code>`


##### [topics](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: stringlist
* Mandatory: Yes
* Dynamic: Yes


### [Mirror](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)


#### Settings


##### [exporter](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: Yes
* Dynamic: Yes
* Values: `<code>log</code>`, `<code>file</code>`, `<code>kafka</code>`


##### [file](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)


* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes


##### [kafka_broker](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)


* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes


##### [kafka_topic](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)


* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes


##### [main](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)


* Type: target
* Mandatory: Yes
* Dynamic: Yes


##### [on_error](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: `<code>ignore</code>`
* Mandatory: No
* Dynamic: Yes
* Values: `<code>ignore</code>`, `<code>close</code>`


##### [report](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: `<code>always</code>`
* Mandatory: No
* Dynamic: Yes
* Values: `<code>always</code>`, `<code>on_conflict</code>`


### [ReadConnRoute](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readconnroute.md)


#### Settings


##### [master_accept_reads](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readconnroute.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true


##### [max_replication_lag](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readconnroute.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 0s


##### [router_options](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readconnroute.md)


* Type: [enum_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>master</code>`, `<code>slave</code>`, `<code>synced</code>`, `<code>running</code>`
* Default: `<code>running</code>`


### [ReadWriteSplit](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


#### Settings


##### [causal_reads](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>none</code>`, `<code>local</code>`, `<code>global</code>`, `<code>fast</code>`, `<code>fast_global</code>`, `<code>universal</code>`, `<code>fast_universal</code>`
* Default: `<code>none</code>`


##### [causal_reads_timeout](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 10s


##### [delayed_retry](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


##### [delayed_retry_timeout](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 10s


##### [lazy_connect](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


##### [master_accept_reads](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


##### [master_failure_mode](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>fail_instantly</code>`, `<code>fail_on_write</code>`, `<code>error_on_write</code>`
* Default: `<code>fail_on_write</code>` (MaxScale 23.08: `<code>fail_instantly</code>`)


##### [master_reconnection](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true (>= MaxScale 24.02), false(<= MaxScale 23.08)


##### [max_replication_lag](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 0s


##### [max_slave_connections](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 255


##### [retry_failed_reads](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true


##### [slave_connections](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 255


##### [slave_selection_criteria](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>least_current_operations</code>`, `<code>adaptive_routing</code>`, `<code>least_behind_master</code>`, `<code>least_router_connections</code>`, `<code>least_global_connections</code>`
* Default: `<code>least_current_operations</code>`


##### [strict_multi_stmt](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


##### [strict_sp_calls](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


##### [strict_tmp_tables](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true (>= MaxScale 24.02), false (<= MaxScale 23.08)


##### [transaction_replay](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


##### [transaction_replay_attempts](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 5


##### [transaction_replay_checksum](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>full</code>`, `<code>result_only</code>`, `<code>no_insert_id</code>`
* Default: `<code>full</code>`


##### [transaction_replay_max_size](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 1 MiB


##### [transaction_replay_retry_on_deadlock](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


##### [transaction_replay_retry_on_mismatch](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


##### [transaction_replay_safe_commit](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true


##### [transaction_replay_timeout](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 30s (>= MaxScale 24.02), 0s (<= MaxScale 23.08)


##### [use_sql_variables_in](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>master</code>`, `<code>all</code>`
* Default: `<code>all</code>`


### [SchemaRouter](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-schemarouter-simple-sharding-with-two-servers.md)


#### Settings


##### [allow_duplicates](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-schemarouter-simple-sharding-with-two-servers.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


##### [ignore_tables](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-schemarouter-simple-sharding-with-two-servers.md)


* Type: stringlist
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


##### [ignore_tables_regex](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-schemarouter-simple-sharding-with-two-servers.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>""</code>`


##### [max_staleness](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-schemarouter-simple-sharding-with-two-servers.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 150s


##### [refresh_databases](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-schemarouter-simple-sharding-with-two-servers.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `<code>false</code>`


##### [refresh_interval](../mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-schemarouter-simple-sharding-with-two-servers.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>300s</code>`


### [SmartRouter](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-smartrouter.md)


#### Settings


##### [master](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-smartrouter.md)


* Type: target
* Mandatory: Yes
* Dynamic: No
