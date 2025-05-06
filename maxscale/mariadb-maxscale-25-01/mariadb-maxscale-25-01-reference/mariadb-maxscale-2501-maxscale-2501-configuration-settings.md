
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
* Values: `GET`, `PUT`, `POST`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`, `CONNECT`, `TRACE`
* Default: No exclusions


##### [admin_audit_file](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `/var/log/maxscale/admin_audit.csv`


##### [admin_auth](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`


##### [admin_enabled](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`


##### [admin_gui](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`


##### [admin_host](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `"127.0.0.1"`


##### [admin_jwt_algorithm](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `auto`, `HS256`, `HS384`, `HS512`, `RS256`, `RS384`, `RS512`, `PS256`, `PS384`, `PS512`, `ES256`, `ES384`, `ES512`, `ED25519`, `ED448`
* Default: `auto`


##### [admin_jwt_issuer](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `maxscale`


##### [admin_jwt_key](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [admin_jwt_max_age](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `24h`


##### [admin_log_auth_failures](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`


##### [admin_oidc_url](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [admin_pam_readonly_service](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [admin_pam_readwrite_service](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [admin_port](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: No
* Default: `8989`


##### [admin_readwrite_hosts](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `%`


##### [admin_secure_gui](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`


##### [admin_ssl_ca](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [admin_ssl_cert](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [admin_ssl_cipher](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No


##### [admin_ssl_key](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [admin_ssl_version](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [enum_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `MAX`, `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`, `TLSv10`, `TLSv11`, `TLSv12`, `TLSv13`
* Default: `MAX`


##### [admin_verify_url](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [auth_connect_timeout](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`


##### [auto_tune](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string list
* Values: `all` or list of auto tunable parameters, separated by `,`
* Default: No
* Mandatory: No
* Dynamic: No


##### [cachedir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/cache/maxscale`


##### [config_sync_cluster](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: monitor
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [config_sync_db](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `mysql`


##### [config_sync_interval](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `5s`


##### [config_sync_password](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: password
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [config_sync_timeout](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`


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
* Default: `/var/lib/maxscale`


##### [debug](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [dump_last_statements](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `on_close`, `on_error`, `never`
* Default: `never`


##### [execdir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/usr/bin`


##### [host_cache_size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: integer
* Default: 128
* Dynamic: Yes


##### [key_manager](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Dynamic: Yes
* Values: `none`, `file`, `kmip`, `vault`
* Default: `none`


##### [language](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/`


##### [libdir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: OS Dependent


##### [load_persisted_configs](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`


##### [local_address](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [log_augmentation](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`


##### [log_debug](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [log_info](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [log_notice](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`


##### [log_throttling](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number, [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md), [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10, 1000ms, 10000ms`


##### [log_warn_super_user](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`


##### [log_warning](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`


##### [logdir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/log/maxscale`


##### [max_auth_errors_until_block](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`


##### [maxlog](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`


##### [module_configdir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/etc/maxscale.modules.d/`


##### [ms_timestamp](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [passive](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [persist_runtime_changes](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: true
* Dynamic: No


##### [persistdir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/maxscale.cnf.d/`


##### [piddir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/run/maxscale`


##### [query_classifier_cache_size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: System Dependent


##### [query_retries](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1`


##### [query_retry_timeout](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`


##### [rebalance_period](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`


##### [rebalance_threshold](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `20`


##### [rebalance_window](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`


##### [retain_last_statements](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`


##### [secretsdir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [session_trace](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`


##### [session_trace_match](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [sharedir](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/usr/share/maxscale`


##### [skip_name_resolve](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [sql_mode](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `default`, `oracle`
* Default: `default`


##### [substitute_variables](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`


##### [syslog](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [threads](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number or `auto`
* Mandatory: No
* Dynamic: No
* Default: `auto`


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
* Default: `0s`


##### [users_refresh_time](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `30s`


##### [writeq_high_water](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `65536`


##### [writeq_low_water](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `1024`


#### Listener


##### [address](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `"::"`


##### [authenticator](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [authenticator_options](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [connection_init_sql_file](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`


##### [connection_metadata](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: stringlist
* Default: `character_set_client=auto,character_set_connection=auto,character_set_results=auto,max_allowed_packet=auto,system_time_zone=auto,time_zone=auto,tx_isolation=auto,maxscale=auto`
* Dynamic: Yes
* Mandatory: No


##### [port](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: Yes, if `socket` is not provided.
* Dynamic: No
* Default: `0`


##### [protocol](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: protocol
* Mandatory: No
* Dynamic: No
* Default: `mariadb`


##### [service](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: service
* Mandatory: Yes
* Dynamic: No


##### [socket](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: Yes, if `port` is not provided.
* Dynamic: No
* Default: `""`


##### [sql_mode](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `default`, `oracle`
* Default: `default`


##### [user_mapping_file](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`


#### Server


##### [address](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: Yes, if `socket` is not provided.
* Dynamic: Yes
* Default: `""`


##### [disk_space_threshold](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: Custom
* Mandatory: No
* Dynamic: No
* Default: None


##### [extra_port](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`


##### [max_routing_connections](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`


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
* Default: `0s`


##### [persistpoolmax](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`


##### [port](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `3306`


##### [priority](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: 0


##### [private_address](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`


##### [proxy_protocol](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [rank](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `primary`, `secondary`
* Default: `primary`


##### [replication_custom_options](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Default: None
* Dynamic: Yes


##### [socket](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: Yes, if `address` is not provided.
* Dynamic: Yes
* Default: `""`


#### Service


##### [auth_all_servers](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [cluster](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: monitor
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [connection_keepalive](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `300s`
* Auto tune: [Yes](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


##### [disable_sescmd_history](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [enable_root_user](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [filters](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: filter list
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [force_connection_keepalive](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: boolean
* Mandatory No
* Dynamic: Yes
* Default: `false`


##### [idle_session_pool_time](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `-1s`


##### [log_auth_warnings](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`


##### [log_debug](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [log_info](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [log_notice](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [log_warning](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [max_connections](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`


##### [max_sescmd_history](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `50`


##### [multiplex_timeout](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `60s`


##### [net_write_timeout](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [durations](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory No
* Dynamic: Yes
* Default: `0s`


##### [password](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: Yes
* Dynamic: Yes


##### [prune_sescmd_history](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`


##### [retain_last_statements](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `-1`


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
* Default: `false`


##### [strip_db_esc](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`


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
* Default: `""`


##### [user_accounts_file_usage](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `add_when_load_ok`, `file_only_always`
* Default: `add_when_load_ok`


##### [version_string](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: None


##### [wait_timeout](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`
* Auto tune: [Yes](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


#### Settings for File-based Key Manager


##### [file.keyfile](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: Yes
* Dynamic: Yes


#### Settings for HashiCorp Vault Key Manager


##### [vault.ca](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Default: `""`
* Dynamic: Yes


##### [vault.host](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Default: `localhost`
* Dynamic: Yes


##### [vault.mount](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Default: `secret`
* Dynamic: Yes


##### [vault.port](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: integer
* Default: `8200`
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
* Default: `""`
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
* Default: `""`


##### [ssl_cert](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`


##### [ssl_cert_verify_depth](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `9`


##### [ssl_cipher](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`


##### [ssl_crl](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`


##### [ssl_key](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`


##### [ssl_verify_peer_certificate](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [ssl_verify_peer_host](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory No
* Dynamic: Yes
* Default: `false`


##### [ssl_version](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)


* Type: [enum_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `MAX`, `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`, `TLSv10`, `TLSv11`, `TLSv12`, `TLSv13`
* Default: `MAX`


## Authenticators


### [Authentication-Modules](/en/maxscale-25-01-authentication-modules/)


#### Settings


##### [lower_case_table_names](https://mariadb.com/kb/en/maxscale-25-01-authentication-modules/#lower_case_table_names)


* Type: number
* Mandatory: No
* Dynamic: No
* Default: `0`


##### [match_host](https://mariadb.com/kb/en/maxscale-25-01-authentication-modules/#match_host)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`


##### [skip_authentication](https://mariadb.com/kb/en/maxscale-25-01-authentication-modules/#skip_authentication)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`


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
* Default: `mariadb/localhost.localdomain`


### [MySQL-Authenticator](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-mariadbmysql-authenticator.md)


#### Settings


##### [log_password_mismatch](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-mariadbmysql-authenticator.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`


### [PAM-Authenticator](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)


#### Settings


##### [pam_backend_mapping](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)


* Type: [enumeration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `none`, `mariadb`
* Default: `none`


##### [pam_mapped_pw_file](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: None


##### [pam_mode](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)


* Type: [enumeration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `password`, `password_2FA`, `suid`
* Default: `password`


##### [pam_use_cleartext_plugin](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`


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
* Default: `0`


##### [global](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [ignore](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [match](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [options](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`


##### [time](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `60s`


### [Cache](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


#### Settings


##### [cache_in_transactions](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `never`, `read_only_transactions`, `all_transactions`
* Default: `all_transactions`


##### [cached_data](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `shared`, `thread_specific`
* Default: `thread_specific`


##### [clear_cache_on_parse_errors](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`


##### [debug](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`


##### [enabled](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`


##### [hard_ttl](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `0s` (no limit)


##### [invalidate](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `never`, `current`
* Default: `never`


##### [max_count](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: count
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)


##### [max_resultset_rows](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: count
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)


##### [max_resultset_size](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)


##### [max_size](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)


##### [rules](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""` (no rules)


##### [selects](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `assume_cacheable`, `verify_cacheable`
* Default: `assume_cacheable`


##### [soft_ttl](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `0s` (no limit)


##### [storage](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `storage_inmemory`


##### [storage_options](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default:


##### [timeout](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `5s`


##### [users](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `mixed`, `isolated`
* Default: `mixed`


#### `storage_memcached`


##### [max_value_size](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: 1Mi


##### [server](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: The Memcached server address specified as `host[:port]`
* Mandatory: Yes
* Dynamic: No


#### `storage_redis`


##### [password](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [server](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: The Redis server address specified as `host[:port]`
* Mandatory: Yes
* Dynamic: No


##### [ssl](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`


##### [ssl_ca](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [ssl_cert](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [ssl_key](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [username](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`


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
* Default: `s3.amazonaws.com`


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
* Default: `us-east-1`


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
* Default: `true`


##### [check_unions](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)


* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`


##### [check_user_variables](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)


* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`


##### [large_payload](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `ignore`, `abort`
* Default: `abort`


##### [prevent_function_usage](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)


* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`


##### [require_fully_parsed](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)


* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`


##### [rules](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)


* Type: path
* Mandatory: Yes
* Dynamic: Yes


##### [treat_string_arg_as_field](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)


* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`


##### [warn_type_mismatch](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `never`, `always`
* Default: `never`


### [Maxrows](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)


#### Settings


##### [debug](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`


##### [max_resultset_return](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `empty`, `error`, `ok`
* Default: `empty`


##### [max_resultset_rows](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: (no limit)


##### [max_resultset_size](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `64Ki`


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
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`


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
* Default: `true`


##### [duration_unit](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `milliseconds`


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
* Default: `false`


##### [log_data](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: [enum_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `service`, `session`, `date`, `user`, `reply_time`, `total_reply_time`, `query`, `default_db`, `num_rows`, `reply_size`, `transaction`, `transaction_time`, `num_warnings`, `error_msg`
* Default: `date, user, query`


##### [log_type](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: [enum_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `session`, `unified`, `stdout`
* Default: `session`


##### [match](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [newline_replacement](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `" "`


##### [options](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: [enum_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `case`, `ignorecase`, `extended`
* Default: `case`


##### [separator](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `","`


##### [source](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`


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
* Default: `false`


##### [user](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`


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
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`


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
* Values: `Native`, `ECMAScript`, `Posix`, `EPosix`, `Awk`, `Grep`, `EGrep`


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
* Values: `Native`, `ECMAScript`, `Posix`, `EPosix`, `Awk`, `Grep`, `EGrep`
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
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`


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
* Default: `false`


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
* Default: `10`


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
* Values: `ignorecase`, `case`, `extended`
* Default: `case`


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
* Default: `true`


##### [cooperative_monitoring_locks](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `majority_of_all`, `majority_of_running`
* Default: `none`


##### [enforce_read_only_servers](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [enforce_read_only_slaves](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [enforce_writable_master](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [failcount](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `5`


##### [maintenance_on_low_disk_space](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`


##### [master_conditions](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [enum_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `connecting_slave`, `connected_slave`, `running_slave`, `primary_monitor_master`, `disk_space_ok`
* Default: `primary_monitor_master, disk_space_ok`


##### [script_max_replication_lag](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `-1`


##### [slave_conditions](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [enum_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `linked_master`, `running_master`, `writable_master`, `primary_monitor_master`
* Default: `none`


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
* Default: `4444`


##### [ssh_check_host_key](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`


##### [ssh_keyfile](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [ssh_port](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `22`


##### [ssh_timeout](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`


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
* Values: `true`, `on`, `yes`, `1`, `false`, `off`, `no`, `0`, `safe`
* Default: `false`


##### [auto_rejoin](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [demotion_sql_file](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [enforce_simple_topology](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [failover_timeout](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`


##### [handle_events](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`


##### [master_failure_timeout](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`


##### [promotion_sql_file](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [replication_master_ssl](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


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
* Default: `false`


##### [switchover_timeout](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`


##### [verify_master_failure](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`


#### Settings for Primary server write test


##### [write_test_fail_action](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: `log`
* Values: `log`, `failover`
* Dynamic: Yes


##### [write_test_interval](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Dynamic: Yes
* Default: 0s


##### [write_test_table](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)


* Type: string
* Dynamic: Yes
* Default: `mxs.maxscale_write_test`


### [Monitor-Common](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


#### Settings


##### [backend_connect_attempts](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `1`


##### [backend_connect_timeout](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`


##### [backend_read_timeout](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`


##### [backend_write_timeout](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`


##### [disk_space_check_interval](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`


##### [disk_space_threshold](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None


##### [events](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: enum
* Mandatory: No
* Dynamic: Yes
* Values: `master_down`, `master_up`, `slave_down`, `slave_up`, `server_down`, `server_up`, `lost_master`, `lost_slave`, `new_master`, `new_slave`
* Default: All events


##### [journal_max_age](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `28800s`


##### [module](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: string
* Mandatory: Yes
* Dynamic: No


##### [monitor_interval](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `2s`


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
* Default: `90s`


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
* Default: `"NoSQL"`


##### [authentication_key_id](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: string
* Mandatory: No
* Default: `""`


##### [authentication_password](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: string
* Mandatory: No
* Default: `""`


##### [authentication_required](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `false`


##### [authentication_shared](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `false`


##### [authentication_user](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: string
* Mandatory: Yes, if `authentication_shared` is true.


##### [authorization_enabled](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `false`


##### [auto_create_databases](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `true`


##### [auto_create_tables](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `true`


##### [cursor_timeout](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `60s`


##### [debug](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [enum_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Values: `none`, `in`, `out`, `back`
* Default: `none`


##### [host](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: string
* Mandatory: No
* Default: `"%"`


##### [id_length](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: count
* Mandatory: No
* Range: `[35, 2048]`
* *Default: `35`


##### [internal_cache](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: string
* Mandatory: No
* Default: ''


##### [log_unknown_command](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `false`


##### [on_unknown_command](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Values: `return_error`, `return_empty`
* Default: `return_error`


##### [ordered_insert_behavior](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Values: `atomic`, `default`
* Default: `default`


##### [password](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: string
* Mandatory: No
* Default: `""`


##### [user](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)


* Type: string
* Mandatory: No
* Default: `""`


## Routers


### [Avrorouter](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)


#### Settings


##### [avrodir](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/`


##### [binlogdir](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/`


##### [codec](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `null`, `deflate`
* Default: `null`


##### [cooperative_replication](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`


##### [exclude](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [filestem](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `mysql-bin`


##### [gtid_start_pos](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [match](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [server_id](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)


* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1234`


##### [start_index](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)


* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1`


#### Settings for Avro File


##### [block_size](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)


* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `16KiB`


##### [group_rows](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)


* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1000`


##### [group_trx](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)


* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1`


##### [max_data_age](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: 0s


##### [max_file_size](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)


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
* Values: `none`, `zstandard`
* Default: `none`


##### [datadir](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/binlogs`


##### [ddl_only](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: boolean
* Mandatory: No
* Dynamic: No
* Default: false


##### [encryption_cipher](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `AES_CBC`, `AES_CTR`, `AES_GCM`
* Default: `AES_GCM`


##### [encryption_key_id](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [expiration_mode](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Dynamic: No
* Values: `purge`, `archive`
* Default: `purge`


##### [expire_log_duration](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `0s`


##### [expire_log_minimum_files](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: number
* Mandatory: No
* Dynamic: No
* Default: `2`


##### [net_timeout](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `10s`


##### [number_of_noncompressed_files](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: count
* Mandatory: No
* Dynamic: No
* Default: `2`


##### [rpl_semi_sync_slave_enabled](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: false
* Dynamic: Yes


##### [select_master](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`


##### [server_id](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)


* Type: count
* Mandatory: No
* Dynamic: No
* Default: `1234`


### [Diff](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)


#### Settings


##### [explain](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `other`, `both'
* Default: `both`


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
* Values: `close`, `ignore`
* Default: `ignore`


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
* Values: `always`, `on_discrepancy`, `never`
* Default: `on_discrepancy`


##### [reset_replication](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`


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
* Default: `false`


##### [enable_idempotence](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`


##### [exclude](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `""`


##### [gtid](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [kafka_sasl_mechanism](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `PLAIN`, `SCRAM-SHA-256`, `SCRAM-SHA-512`
* Default: `PLAIN`


##### [kafka_sasl_password](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [kafka_sasl_user](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [kafka_ssl](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`


##### [kafka_ssl_ca](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [kafka_ssl_cert](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [kafka_ssl_key](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [match](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `""`


##### [read_gtid_from_kafka](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`


##### [send_schema](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true


##### [server_id](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1234`


##### [timeout](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`


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
* Default: `100`


##### [bootstrap_servers](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: string
* Mandatory: Yes
* Dynamic: Yes


##### [engine](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: string
* Default: `InnoDB`
* Mandatory: No
* Dynamic: Yes


##### [kafka_sasl_mechanism](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `PLAIN`, `SCRAM-SHA-256`, `SCRAM-SHA-512`
* Default: `PLAIN`


##### [kafka_sasl_password](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`


##### [kafka_sasl_user](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`


##### [kafka_ssl](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`


##### [kafka_ssl_ca](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`


##### [kafka_ssl_cert](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`


##### [kafka_ssl_key](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`


##### [table_name_in](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `topic`, `key`
* Default: `topic`


##### [timeout](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `5000ms`


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
* Values: `log`, `file`, `kafka`


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
* Default: `ignore`
* Mandatory: No
* Dynamic: Yes
* Values: `ignore`, `close`


##### [report](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: `always`
* Mandatory: No
* Dynamic: Yes
* Values: `always`, `on_conflict`


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
* Values: `master`, `slave`, `synced`, `running`
* Default: `running`


### [ReadWriteSplit](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


#### Settings


##### [causal_reads](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)


* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `local`, `global`, `fast`, `fast_global`, `universal`, `fast_universal`
* Default: `none`


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
* Values: `fail_instantly`, `fail_on_write`, `error_on_write`
* Default: `fail_on_write` (MaxScale 23.08: `fail_instantly`)


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
* Values: `least_current_operations`, `adaptive_routing`, `least_behind_master`, `least_router_connections`, `least_global_connections`
* Default: `least_current_operations`


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
* Values: `full`, `result_only`, `no_insert_id`
* Default: `full`


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
* Values: `master`, `all`
* Default: `all`


### [SchemaRouter](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)


#### Settings


##### [allow_duplicates](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false


##### [ignore_tables](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)


* Type: stringlist
* Mandatory: No
* Dynamic: Yes
* Default: `""`


##### [ignore_tables_regex](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)


* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `""`


##### [max_staleness](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 150s


##### [refresh_databases](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)


* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`


##### [refresh_interval](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)


* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `300s`


### [SmartRouter](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-smartrouter.md)


#### Settings


##### [master](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-smartrouter.md)


* Type: target
* Mandatory: Yes
* Dynamic: No
