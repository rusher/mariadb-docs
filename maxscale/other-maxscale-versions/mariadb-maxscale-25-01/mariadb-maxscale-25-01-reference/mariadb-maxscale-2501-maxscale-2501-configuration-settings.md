# MaxScale 25.01 Configuration Settings

## Configuration Settings

* [Configuration Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#configuration-settings)
  * [General](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#general)
    * [MaxScale](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#maxscale)
      * [Global Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#global-settings)
        * [admin\_audit](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_audit)
        * [admin\_audit\_exclude\_methods](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_audit_exclude_methods)
        * [admin\_audit\_file](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_audit_file)
        * [admin\_auth](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_auth)
        * [admin\_enabled](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_enabled)
        * [admin\_gui](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_gui)
        * [admin\_host](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_host)
        * [admin\_jwt\_algorithm](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_jwt_algorithm)
        * [admin\_jwt\_issuer](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_jwt_issuer)
        * [admin\_jwt\_key](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_jwt_key)
        * [admin\_jwt\_max\_age](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_jwt_max_age)
        * [admin\_log\_auth\_failures](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_log_auth_failures)
        * [admin\_oidc\_url](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_oidc_url)
        * [admin\_pam\_readonly\_service](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_pam_readonly_service)
        * [admin\_pam\_readwrite\_service](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_pam_readwrite_service)
        * [admin\_port](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_port)
        * [admin\_readwrite\_hosts](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_readwrite_hosts)
        * [admin\_secure\_gui](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_secure_gui)
        * [admin\_ssl\_ca](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_ssl_ca)
        * [admin\_ssl\_cert](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_ssl_cert)
        * [admin\_ssl\_cipher](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_ssl_cipher)
        * [admin\_ssl\_key](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_ssl_key)
        * [admin\_ssl\_version](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_ssl_version)
        * [admin\_verify\_url](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#admin_verify_url)
        * [auth\_connect\_timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#auth_connect_timeout)
        * [auto\_tune](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#auto_tune)
        * [cachedir](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#cachedir)
        * [config\_sync\_cluster](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#config_sync_cluster)
        * [config\_sync\_db](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#config_sync_db)
        * [config\_sync\_interval](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#config_sync_interval)
        * [config\_sync\_password](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#config_sync_password)
        * [config\_sync\_timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#config_sync_timeout)
        * [config\_sync\_user](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#config_sync_user)
        * [connector\_plugindir](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#connector_plugindir)
        * [core\_file](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#core_file)
        * [datadir](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#datadir)
        * [debug](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#debug)
        * [dump\_last\_statements](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#dump_last_statements)
        * [execdir](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#execdir)
        * [host\_cache\_size](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#host_cache_size)
        * [key\_manager](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#key_manager)
        * [language](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#language)
        * [libdir](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#libdir)
        * [load\_persisted\_configs](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#load_persisted_configs)
        * [local\_address](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#local_address)
        * [log\_augmentation](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#log_augmentation)
        * [log\_debug](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#log_debug)
        * [log\_info](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#log_info)
        * [log\_notice](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#log_notice)
        * [log\_throttling](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#log_throttling)
        * [log\_warn\_super\_user](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#log_warn_super_user)
        * [log\_warning](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#log_warning)
        * [logdir](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#logdir)
        * [max\_auth\_errors\_until\_block](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_auth_errors_until_block)
        * [maxlog](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#maxlog)
        * [module\_configdir](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#module_configdir)
        * [ms\_timestamp](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ms_timestamp)
        * [passive](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#passive)
        * [persist\_runtime\_changes](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#persist_runtime_changes)
        * [persistdir](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#persistdir)
        * [piddir](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#piddir)
        * [query\_classifier\_cache\_size](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#query_classifier_cache_size)
        * [query\_retries](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#query_retries)
        * [query\_retry\_timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#query_retry_timeout)
        * [rebalance\_period](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#rebalance_period)
        * [rebalance\_threshold](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#rebalance_threshold)
        * [rebalance\_window](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#rebalance_window)
        * [retain\_last\_statements](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#retain_last_statements)
        * [secretsdir](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#secretsdir)
        * [session\_trace](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#session_trace)
        * [session\_trace\_match](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#session_trace_match)
        * [sharedir](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#sharedir)
        * [skip\_name\_resolve](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#skip_name_resolve)
        * [sql\_mode](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#sql_mode)
        * [substitute\_variables](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#substitute_variables)
        * [syslog](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#syslog)
        * [threads](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#threads)
        * [threads\_max](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#threads_max)
        * [trace\_file\_dir](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#trace_file_dir)
        * [trace\_file\_size](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#trace_file_size)
        * [users\_refresh\_interval](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#users_refresh_interval)
        * [users\_refresh\_time](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#users_refresh_time)
        * [writeq\_high\_water](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#writeq_high_water)
        * [writeq\_low\_water](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#writeq_low_water)
      * [Listener](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#listener)
        * [address](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#address)
        * [authenticator](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#authenticator)
        * [authenticator\_options](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#authenticator_options)
        * [connection\_init\_sql\_file](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#connection_init_sql_file)
        * [connection\_metadata](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#connection_metadata)
        * [port](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#port)
        * [protocol](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#protocol)
        * [service](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#service)
        * [socket](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#socket)
        * [sql\_mode](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#sql_mode_1)
        * [user\_mapping\_file](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#user_mapping_file)
      * [Server](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#server)
        * [address](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#address_1)
        * [disk\_space\_threshold](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#disk_space_threshold)
        * [extra\_port](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#extra_port)
        * [max\_routing\_connections](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_routing_connections)
        * [monitorpw](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#monitorpw)
        * [monitoruser](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#monitoruser)
        * [persistmaxtime](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#persistmaxtime)
        * [persistpoolmax](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#persistpoolmax)
        * [port](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#port_1)
        * [priority](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#priority)
        * [private\_address](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#private_address)
        * [proxy\_protocol](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#proxy_protocol)
        * [rank](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#rank)
        * [replication\_custom\_options](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#replication_custom_options)
        * [socket](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#socket_1)
      * [Service](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#service_1)
        * [auth\_all\_servers](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#auth_all_servers)
        * [cluster](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#cluster)
        * [connection\_keepalive](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#connection_keepalive)
        * [disable\_sescmd\_history](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#disable_sescmd_history)
        * [enable\_root\_user](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#enable_root_user)
        * [filters](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#filters)
        * [force\_connection\_keepalive](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#force_connection_keepalive)
        * [idle\_session\_pool\_time](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#idle_session_pool_time)
        * [log\_auth\_warnings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#log_auth_warnings)
        * [log\_debug](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#log_debug_1)
        * [log\_info](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#log_info_1)
        * [log\_notice](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#log_notice_1)
        * [log\_warning](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#log_warning_1)
        * [max\_connections](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_connections)
        * [max\_sescmd\_history](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_sescmd_history)
        * [multiplex\_timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#multiplex_timeout)
        * [net\_write\_timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#net_write_timeout)
        * [password](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#password)
        * [prune\_sescmd\_history](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#prune_sescmd_history)
        * [retain\_last\_statements](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#retain_last_statements_1)
        * [router](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#router)
        * [servers](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#servers)
        * [session\_track\_trx\_state](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#session_track_trx_state)
        * [strip\_db\_esc](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#strip_db_esc)
        * [targets](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#targets)
        * [user](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#user)
        * [user\_accounts\_file](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#user_accounts_file)
        * [user\_accounts\_file\_usage](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#user_accounts_file_usage)
        * [version\_string](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#version_string)
        * [wait\_timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#wait_timeout)
      * [Settings for File-based Key Manager](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings-for-file-based-key-manager)
        * [file.keyfile](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#filekeyfile)
      * [Settings for HashiCorp Vault Key Manager](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings-for-hashicorp-vault-key-manager)
        * [vault.ca](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#vaultca)
        * [vault.host](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#vaulthost)
        * [vault.mount](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#vaultmount)
        * [vault.port](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#vaultport)
        * [vault.timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#vaulttimeout)
        * [vault.tls](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#vaulttls)
        * [vault.token](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#vaulttoken)
      * [Settings for KMIP Key Manager](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings-for-kmip-key-manager)
        * [kmip.ca](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kmipca)
        * [kmip.cert](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kmipcert)
        * [kmip.host](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kmiphost)
        * [kmip.key](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kmipkey)
        * [kmip.port](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kmipport)
      * [Settings for TLS/SSL Encryption](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings-for-tlsssl-encryption)
        * [ssl](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ssl)
        * [ssl\_ca](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ssl_ca)
        * [ssl\_cert](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ssl_cert)
        * [ssl\_cert\_verify\_depth](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ssl_cert_verify_depth)
        * [ssl\_cipher](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ssl_cipher)
        * [ssl\_crl](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ssl_crl)
        * [ssl\_key](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ssl_key)
        * [ssl\_verify\_peer\_certificate](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ssl_verify_peer_certificate)
        * [ssl\_verify\_peer\_host](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ssl_verify_peer_host)
        * [ssl\_version](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ssl_version)
  * [Authenticators](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#authenticators)
    * [Authentication-Modules](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#authentication-modules)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings)
        * [lower\_case\_table\_names](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#lower_case_table_names)
        * [match\_host](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#match_host)
        * [skip\_authentication](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#skip_authentication)
    * [GSSAPI-Authenticator](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#gssapi-authenticator)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_1)
        * [gssapi\_keytab\_path](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#gssapi_keytab_path)
        * [principal\_name](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#principal_name)
    * [MySQL-Authenticator](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#mysql-authenticator)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_2)
        * [log\_password\_mismatch](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#log_password_mismatch)
    * [PAM-Authenticator](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#pam-authenticator)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_3)
        * [pam\_backend\_mapping](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#pam_backend_mapping)
        * [pam\_mapped\_pw\_file](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#pam_mapped_pw_file)
        * [pam\_mode](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#pam_mode)
        * [pam\_use\_cleartext\_plugin](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#pam_use_cleartext_plugin)
  * [Filters](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#filters_1)
    * [BinlogFilter](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#binlogfilter)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_4)
        * [exclude](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#exclude)
        * [match](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#match)
        * [rewrite\_dest](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#rewrite_dest)
        * [rewrite\_src](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#rewrite_src)
    * [CCRFilter](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ccrfilter)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_5)
        * [count](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#count)
        * [global](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#global)
        * [ignore](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ignore)
        * [match](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#match_1)
        * [options](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#options)
        * [time](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#time)
    * [Cache](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#cache)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_6)
        * [cache\_in\_transactions](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#cache_in_transactions)
        * [cached\_data](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#cached_data)
        * [clear\_cache\_on\_parse\_errors](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#clear_cache_on_parse_errors)
        * [debug](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#debug_1)
        * [enabled](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#enabled)
        * [hard\_ttl](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#hard_ttl)
        * [invalidate](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#invalidate)
        * [max\_count](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_count)
        * [max\_resultset\_rows](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_resultset_rows)
        * [max\_resultset\_size](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_resultset_size)
        * [max\_size](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_size)
        * [rules](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#rules)
        * [selects](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#selects)
        * [soft\_ttl](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#soft_ttl)
        * [storage](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#storage)
        * [storage\_options](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#storage_options)
        * [timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#timeout)
        * [users](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#users)
      * [storage\_memcached](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#storage_memcached)
        * [max\_value\_size](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_value_size)
        * [server](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#server_1)
      * [storage\_redis](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#storage_redis)
        * [password](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#password_1)
        * [server](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#server_2)
        * [ssl](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ssl_1)
        * [ssl\_ca](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ssl_ca_1)
        * [ssl\_cert](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ssl_cert_1)
        * [ssl\_key](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ssl_key_1)
        * [username](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#username)
    * [Comment](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#comment)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_7)
        * [inject](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#inject)
    * [LDIFilter](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ldifilter)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_8)
        * [host](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#host)
        * [key](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#key)
        * [no\_verify](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#no_verify)
        * [port](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#port_2)
        * [protocol\_version](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#protocol_version)
        * [region](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#region)
        * [secret](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#secret)
        * [use\_http](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#use_http)
    * [Masking](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#masking)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_9)
        * [check\_subqueries](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#check_subqueries)
        * [check\_unions](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#check_unions)
        * [check\_user\_variables](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#check_user_variables)
        * [large\_payload](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#large_payload)
        * [prevent\_function\_usage](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#prevent_function_usage)
        * [require\_fully\_parsed](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#require_fully_parsed)
        * [rules](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#rules_1)
        * [treat\_string\_arg\_as\_field](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#treat_string_arg_as_field)
        * [warn\_type\_mismatch](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#warn_type_mismatch)
    * [Maxrows](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#maxrows)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_10)
        * [debug](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#debug_2)
        * [max\_resultset\_return](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_resultset_return)
        * [max\_resultset\_rows](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_resultset_rows_1)
        * [max\_resultset\_size](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_resultset_size_1)
    * [Named-Server-Filter](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#named-server-filter)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_11)
        * [matchXY](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#matchxy)
        * [options](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#options_1)
        * [source](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#source)
        * [targetXY](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#targetxy)
        * [user](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#user_1)
    * [Query-Log-All-Filter](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#query-log-all-filter)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_12)
        * [append](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#append)
        * [duration\_unit](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#duration_unit)
        * [exclude](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#exclude_1)
        * [filebase](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#filebase)
        * [flush](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#flush)
        * [log\_data](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#log_data)
        * [log\_type](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#log_type)
        * [match](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#match_2)
        * [newline\_replacement](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#newline_replacement)
        * [options](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#options_2)
        * [separator](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#separator)
        * [source](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#source_1)
        * [source\_exclude](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#source_exclude)
        * [source\_match](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#source_match)
        * [use\_canonical\_form](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#use_canonical_form)
        * [user](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#user_2)
        * [user\_exclude](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#user_exclude)
        * [user\_match](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#user_match)
    * [Regex-Filter](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#regex-filter)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_13)
        * [log\_file](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#log_file)
        * [log\_trace](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#log_trace)
        * [match](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#match_3)
        * [options](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#options_3)
        * [replace](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#replace)
        * [source](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#source_2)
        * [user](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#user_3)
    * [RewriteFilter](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#rewritefilter)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_14)
        * [case\_sensitive](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#case_sensitive)
        * [log\_replacement](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#log_replacement)
        * [regex\_grammar](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#regex_grammar)
        * [template\_file](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#template_file)
      * [Settings per template in the template file](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings-per-template-in-the-template-file)
        * [case\_sensitive](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#case_sensitive_1)
        * [continue\_if\_matched](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#continue_if_matched)
        * [ignore\_whitespace](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ignore_whitespace)
        * [regex\_grammar](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#regex_grammar_1)
        * [what\_if](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#what_if)
    * [Tee-Filter](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#tee-filter)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_15)
        * [exclude](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#exclude_2)
        * [match](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#match_4)
        * [options](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#options_4)
        * [service](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#service_2)
        * [source](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#source_3)
        * [sync](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#sync)
        * [target](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#target)
        * [user](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#user_4)
    * [Throttle](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#throttle)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_16)
        * [continuous\_duration](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#continuous_duration)
        * [max\_qps](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_qps)
        * [sampling\_duration](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#sampling_duration)
        * [throttling\_duration](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#throttling_duration)
    * [Top-N-Filter](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#top-n-filter)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_17)
        * [count](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#count_1)
        * [exclude](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#exclude_3)
        * [filebase](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#filebase_1)
        * [match](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#match_5)
        * [options](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#options_5)
        * [source](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#source_4)
        * [user](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#user_5)
    * [Wcar](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#wcar)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_18)
        * [capture\_dir](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#capture_dir)
        * [capture\_duration](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#capture_duration)
        * [capture\_size](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#capture_size)
        * [start\_capture](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#start_capture)
  * [Monitors](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#monitors)
    * [Galera-Monitor](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#galera-monitor)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_19)
        * [available\_when\_donor](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#available_when_donor)
        * [disable\_master\_failback](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#disable_master_failback)
        * [disable\_master\_role\_setting](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#disable_master_role_setting)
        * [root\_node\_as\_master](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#root_node_as_master)
        * [set\_donor\_nodes](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#set_donor_nodes)
        * [use\_priority](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#use_priority)
    * [MariaDB-Monitor](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#mariadb-monitor)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_20)
        * [assume\_unique\_hostnames](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#assume_unique_hostnames)
        * [cooperative\_monitoring\_locks](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#cooperative_monitoring_locks)
        * [enforce\_read\_only\_servers](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#enforce_read_only_servers)
        * [enforce\_read\_only\_slaves](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#enforce_read_only_slaves)
        * [enforce\_writable\_master](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#enforce_writable_master)
        * [failcount](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#failcount)
        * [maintenance\_on\_low\_disk\_space](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#maintenance_on_low_disk_space)
        * [master\_conditions](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#master_conditions)
        * [script\_max\_replication\_lag](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#script_max_replication_lag)
        * [slave\_conditions](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#slave_conditions)
      * [Settings for Backup operations](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings-for-backup-operations)
        * [backup\_storage\_address](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#backup_storage_address)
        * [backup\_storage\_path](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#backup_storage_path)
        * [rebuild\_port](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#rebuild_port)
        * [ssh\_check\_host\_key](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ssh_check_host_key)
        * [ssh\_keyfile](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ssh_keyfile)
        * [ssh\_port](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ssh_port)
        * [ssh\_timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ssh_timeout)
        * [ssh\_user](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ssh_user)
      * [Settings for Cluster manipulation operations](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings-for-cluster-manipulation-operations)
        * [auto\_failover](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#auto_failover)
        * [auto\_rejoin](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#auto_rejoin)
        * [demotion\_sql\_file](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#demotion_sql_file)
        * [enforce\_simple\_topology](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#enforce_simple_topology)
        * [failover\_timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#failover_timeout)
        * [handle\_events](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#handle_events)
        * [master\_failure\_timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#master_failure_timeout)
        * [promotion\_sql\_file](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#promotion_sql_file)
        * [replication\_master\_ssl](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#replication_master_ssl)
        * [replication\_password](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#replication_password)
        * [replication\_user](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#replication_user)
        * [servers\_no\_promotion](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#servers_no_promotion)
        * [switchover\_on\_low\_disk\_space](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#switchover_on_low_disk_space)
        * [switchover\_timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#switchover_timeout)
        * [verify\_master\_failure](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#verify_master_failure)
      * [Settings for Primary server write test](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings-for-primary-server-write-test)
        * [write\_test\_fail\_action](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#write_test_fail_action)
        * [write\_test\_interval](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#write_test_interval)
        * [write\_test\_table](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#write_test_table)
    * [Monitor-Common](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#monitor-common)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_21)
        * [backend\_connect\_attempts](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#backend_connect_attempts)
        * [backend\_connect\_timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#backend_connect_timeout)
        * [backend\_read\_timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#backend_read_timeout)
        * [backend\_write\_timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#backend_write_timeout)
        * [disk\_space\_check\_interval](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#disk_space_check_interval)
        * [disk\_space\_threshold](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#disk_space_threshold_1)
        * [events](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#events)
        * [journal\_max\_age](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#journal_max_age)
        * [module](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#module)
        * [monitor\_interval](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#monitor_interval)
        * [password](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#password_2)
        * [script](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#script)
        * [script\_timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#script_timeout)
        * [servers](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#servers_1)
        * [user](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#user_6)
  * [Protocols](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#protocols)
    * [MariaDB](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#mariadb)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_22)
        * [allow\_replication](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#allow_replication)
    * [NoSQL](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#nosql)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_23)
        * [authentication\_db](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#authentication_db)
        * [authentication\_key\_id](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#authentication_key_id)
        * [authentication\_password](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#authentication_password)
        * [authentication\_required](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#authentication_required)
        * [authentication\_shared](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#authentication_shared)
        * [authentication\_user](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#authentication_user)
        * [authorization\_enabled](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#authorization_enabled)
        * [auto\_create\_databases](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#auto_create_databases)
        * [auto\_create\_tables](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#auto_create_tables)
        * [cursor\_timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#cursor_timeout)
        * [debug](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#debug_3)
        * [host](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#host_1)
        * [id\_length](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#id_length)
        * [internal\_cache](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#internal_cache)
        * [log\_unknown\_command](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#log_unknown_command)
        * [on\_unknown\_command](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#on_unknown_command)
        * [ordered\_insert\_behavior](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ordered_insert_behavior)
        * [password](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#password_3)
        * [user](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#user_7)
  * [Routers](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#routers)
    * [Avrorouter](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#avrorouter)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_24)
        * [avrodir](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#avrodir)
        * [binlogdir](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#binlogdir)
        * [codec](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#codec)
        * [cooperative\_replication](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#cooperative_replication)
        * [exclude](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#exclude_4)
        * [filestem](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#filestem)
        * [gtid\_start\_pos](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#gtid_start_pos)
        * [match](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#match_6)
        * [server\_id](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#server_id)
        * [start\_index](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#start_index)
      * [Settings for Avro File](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings-for-avro-file)
        * [block\_size](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#block_size)
        * [group\_rows](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#group_rows)
        * [group\_trx](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#group_trx)
        * [max\_data\_age](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_data_age)
        * [max\_file\_size](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_file_size)
    * [Binlogrouter](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#binlogrouter)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_25)
        * [archivedir](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#archivedir)
        * [compression\_algorithm](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#compression_algorithm)
        * [datadir](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#datadir_1)
        * [ddl\_only](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ddl_only)
        * [encryption\_cipher](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#encryption_cipher)
        * [encryption\_key\_id](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#encryption_key_id)
        * [expiration\_mode](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#expiration_mode)
        * [expire\_log\_duration](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#expire_log_duration)
        * [expire\_log\_minimum\_files](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#expire_log_minimum_files)
        * [net\_timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#net_timeout)
        * [number\_of\_noncompressed\_files](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#number_of_noncompressed_files)
        * [rpl\_semi\_sync\_slave\_enabled](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#rpl_semi_sync_slave_enabled)
        * [select\_master](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#select_master)
        * [server\_id](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#server_id_1)
    * [Diff](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#diff)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_26)
        * [explain](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#explain)
        * [explain\_entries](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#explain_entries)
        * [explain\_period](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#explain_period)
        * [main](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#main)
        * [max\_request\_lag](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_request_lag)
        * [on\_error](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#on_error)
        * [percentile](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#percentile)
        * [qps\_window](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#qps_window)
        * [report](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#report)
        * [reset\_replication](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#reset_replication)
        * [retain\_faster\_statements](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#retain_faster_statements)
        * [retain\_slower\_statements](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#retain_slower_statements)
        * [samples](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#samples)
        * [service](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#service_3)
    * [KafkaCDC](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kafkacdc)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_27)
        * [bootstrap\_servers](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#bootstrap_servers)
        * [cooperative\_replication](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#cooperative_replication_1)
        * [enable\_idempotence](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#enable_idempotence)
        * [exclude](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#exclude_5)
        * [gtid](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#gtid)
        * [kafka\_sasl\_mechanism](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kafka_sasl_mechanism)
        * [kafka\_sasl\_password](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kafka_sasl_password)
        * [kafka\_sasl\_user](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kafka_sasl_user)
        * [kafka\_ssl](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kafka_ssl)
        * [kafka\_ssl\_ca](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kafka_ssl_ca)
        * [kafka\_ssl\_cert](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kafka_ssl_cert)
        * [kafka\_ssl\_key](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kafka_ssl_key)
        * [match](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#match_7)
        * [read\_gtid\_from\_kafka](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#read_gtid_from_kafka)
        * [send\_schema](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#send_schema)
        * [server\_id](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#server_id_2)
        * [timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#timeout_1)
        * [topic](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#topic)
    * [KafkaImporter](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kafkaimporter)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_28)
        * [batch\_size](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#batch_size)
        * [bootstrap\_servers](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#bootstrap_servers_1)
        * [engine](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#engine)
        * [kafka\_sasl\_mechanism](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kafka_sasl_mechanism_1)
        * [kafka\_sasl\_password](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kafka_sasl_password_1)
        * [kafka\_sasl\_user](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kafka_sasl_user_1)
        * [kafka\_ssl](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kafka_ssl_1)
        * [kafka\_ssl\_ca](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kafka_ssl_ca_1)
        * [kafka\_ssl\_cert](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kafka_ssl_cert_1)
        * [kafka\_ssl\_key](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kafka_ssl_key_1)
        * [table\_name\_in](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#table_name_in)
        * [timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#timeout_2)
        * [topics](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#topics)
    * [Mirror](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#mirror)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_29)
        * [exporter](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#exporter)
        * [file](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#file)
        * [kafka\_broker](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kafka_broker)
        * [kafka\_topic](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#kafka_topic)
        * [main](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#main_1)
        * [on\_error](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#on_error_1)
        * [report](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#report_1)
    * [ReadConnRoute](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#readconnroute)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_30)
        * [master\_accept\_reads](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#master_accept_reads)
        * [max\_replication\_lag](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_replication_lag)
        * [router\_options](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#router_options)
    * [ReadWriteSplit](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#readwritesplit)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_31)
        * [causal\_reads](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#causal_reads)
        * [causal\_reads\_timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#causal_reads_timeout)
        * [delayed\_retry](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#delayed_retry)
        * [delayed\_retry\_timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#delayed_retry_timeout)
        * [lazy\_connect](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#lazy_connect)
        * [master\_accept\_reads](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#master_accept_reads_1)
        * [master\_failure\_mode](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#master_failure_mode)
        * [master\_reconnection](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#master_reconnection)
        * [max\_replication\_lag](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_replication_lag_1)
        * [max\_slave\_connections](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_slave_connections)
        * [retry\_failed\_reads](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#retry_failed_reads)
        * [slave\_connections](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#slave_connections)
        * [slave\_selection\_criteria](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#slave_selection_criteria)
        * [strict\_multi\_stmt](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#strict_multi_stmt)
        * [strict\_sp\_calls](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#strict_sp_calls)
        * [strict\_tmp\_tables](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#strict_tmp_tables)
        * [transaction\_replay](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#transaction_replay)
        * [transaction\_replay\_attempts](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#transaction_replay_attempts)
        * [transaction\_replay\_checksum](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#transaction_replay_checksum)
        * [transaction\_replay\_max\_size](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#transaction_replay_max_size)
        * [transaction\_replay\_retry\_on\_deadlock](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#transaction_replay_retry_on_deadlock)
        * [transaction\_replay\_retry\_on\_mismatch](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#transaction_replay_retry_on_mismatch)
        * [transaction\_replay\_safe\_commit](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#transaction_replay_safe_commit)
        * [transaction\_replay\_timeout](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#transaction_replay_timeout)
        * [use\_sql\_variables\_in](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#use_sql_variables_in)
    * [SchemaRouter](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#schemarouter)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_32)
        * [allow\_duplicates](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#allow_duplicates)
        * [ignore\_tables](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ignore_tables)
        * [ignore\_tables\_regex](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#ignore_tables_regex)
        * [max\_staleness](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#max_staleness)
        * [refresh\_databases](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#refresh_databases)
        * [refresh\_interval](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#refresh_interval)
    * [SmartRouter](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#smartrouter)
      * [Settings](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#settings_33)
        * [master](mariadb-maxscale-2501-maxscale-2501-configuration-settings.md#master)

### General

#### [MaxScale](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

**Global Settings**

[**admin\_audit**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**admin\_audit\_exclude\_methods**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `GET`, `PUT`, `POST`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`, `CONNECT`, `TRACE`
* Default: No exclusions

[**admin\_audit\_file**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `/var/log/maxscale/admin_audit.csv`

[**admin\_auth**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**admin\_enabled**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**admin\_gui**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**admin\_host**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `"127.0.0.1"`

[**admin\_jwt\_algorithm**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `auto`, `HS256`, `HS384`, `HS512`, `RS256`, `RS384`, `RS512`, `PS256`, `PS384`, `PS512`, `ES256`, `ES384`, `ES512`, `ED25519`, `ED448`
* Default: `auto`

[**admin\_jwt\_issuer**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `maxscale`

[**admin\_jwt\_key**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_jwt\_max\_age**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `24h`

[**admin\_log\_auth\_failures**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**admin\_oidc\_url**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_pam\_readonly\_service**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_pam\_readwrite\_service**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_port**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `8989`

[**admin\_readwrite\_hosts**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `%`

[**admin\_secure\_gui**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**admin\_ssl\_ca**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_ssl\_cert**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_ssl\_cipher**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No

[**admin\_ssl\_key**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_ssl\_version**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum\_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `MAX`, `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`, `TLSv10`, `TLSv11`, `TLSv12`, `TLSv13`
* Default: `MAX`

[**admin\_verify\_url**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**auth\_connect\_timeout**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**auto\_tune**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string list
* Values: `all` or list of auto tunable parameters, separated by `,`
* Default: No
* Mandatory: No
* Dynamic: No

[**cachedir**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/cache/maxscale`

[**config\_sync\_cluster**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: monitor
* Mandatory: No
* Dynamic: Yes
* Default: None

[**config\_sync\_db**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `mysql`

[**config\_sync\_interval**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `5s`

[**config\_sync\_password**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: password
* Mandatory: No
* Dynamic: Yes
* Default: None

[**config\_sync\_timeout**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**config\_sync\_user**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**connector\_plugindir**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: OS Dependent

[**core\_file**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: true
* Dynamic: No

[**datadir**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale`

[**debug**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**dump\_last\_statements**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `on_close`, `on_error`, `never`
* Default: `never`

[**execdir**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/usr/bin`

[**host\_cache\_size**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: integer
* Default: 128
* Dynamic: Yes

[**key\_manager**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Dynamic: Yes
* Values: `none`, `file`, `kmip`, `vault`
* Default: `none`

[**language**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/`

[**libdir**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: OS Dependent

[**load\_persisted\_configs**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**local\_address**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**log\_augmentation**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**log\_debug**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_info**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_notice**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**log\_throttling**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number, [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md), [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10, 1000ms, 10000ms`

[**log\_warn\_super\_user**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**log\_warning**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**logdir**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/log/maxscale`

[**max\_auth\_errors\_until\_block**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`

[**maxlog**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**module\_configdir**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/etc/maxscale.modules.d/`

[**ms\_timestamp**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**passive**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**persist\_runtime\_changes**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: true
* Dynamic: No

[**persistdir**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/maxscale.cnf.d/`

[**piddir**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/run/maxscale`

[**query\_classifier\_cache\_size**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: System Dependent

[**query\_retries**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1`

[**query\_retry\_timeout**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**rebalance\_period**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

[**rebalance\_threshold**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `20`

[**rebalance\_window**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`

[**retain\_last\_statements**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**secretsdir**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**session\_trace**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**session\_trace\_match**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**sharedir**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/usr/share/maxscale`

[**skip\_name\_resolve**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**sql\_mode**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `default`, `oracle`
* Default: `default`

[**substitute\_variables**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**syslog**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**threads**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number or `auto`
* Mandatory: No
* Dynamic: No
* Default: `auto`

[**threads\_max**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: positive integer
* Default: 256
* Dynamic: No

[**trace\_file\_dir**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No

[**trace\_file\_size**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes

[**users\_refresh\_interval**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

[**users\_refresh\_time**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `30s`

[**writeq\_high\_water**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `65536`

[**writeq\_low\_water**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `1024`

**Listener**

[**address**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `"::"`

[**authenticator**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**authenticator\_options**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**connection\_init\_sql\_file**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**connection\_metadata**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: stringlist
* Default: `character_set_client=auto,character_set_connection=auto,character_set_results=auto,max_allowed_packet=auto,system_time_zone=auto,time_zone=auto,tx_isolation=auto,maxscale=auto`
* Dynamic: Yes
* Mandatory: No

[**port**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: Yes, if `socket` is not provided.
* Dynamic: No
* Default: `0`

[**protocol**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: protocol
* Mandatory: No
* Dynamic: No
* Default: `mariadb`

[**service**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: service
* Mandatory: Yes
* Dynamic: No

[**socket**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: Yes, if `port` is not provided.
* Dynamic: No
* Default: `""`

[**sql\_mode**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `default`, `oracle`
* Default: `default`

[**user\_mapping\_file**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

**Server**

[**address**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: Yes, if `socket` is not provided.
* Dynamic: Yes
* Default: `""`

[**disk\_space\_threshold**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: Custom
* Mandatory: No
* Dynamic: No
* Default: None

[**extra\_port**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**max\_routing\_connections**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**monitorpw**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**monitoruser**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**persistmaxtime**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

[**persistpoolmax**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**port**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `3306`

[**priority**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: 0

[**private\_address**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**proxy\_protocol**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**rank**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `primary`, `secondary`
* Default: `primary`

[**replication\_custom\_options**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Default: None
* Dynamic: Yes

[**socket**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: Yes, if `address` is not provided.
* Dynamic: Yes
* Default: `""`

**Service**

[**auth\_all\_servers**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**cluster**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: monitor
* Mandatory: No
* Dynamic: Yes
* Default: None

[**connection\_keepalive**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `300s`
* Auto tune: [Yes](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

[**disable\_sescmd\_history**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**enable\_root\_user**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**filters**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: filter list
* Mandatory: No
* Dynamic: Yes
* Default: None

[**force\_connection\_keepalive**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: boolean
* Mandatory No
* Dynamic: Yes
* Default: `false`

[**idle\_session\_pool\_time**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `-1s`

[**log\_auth\_warnings**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**log\_debug**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_info**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_notice**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_warning**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**max\_connections**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**max\_sescmd\_history**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `50`

[**multiplex\_timeout**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `60s`

[**net\_write\_timeout**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [durations](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory No
* Dynamic: Yes
* Default: `0s`

[**password**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**prune\_sescmd\_history**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**retain\_last\_statements**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `-1`

[**router**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: router
* Mandatory: Yes
* Dynamic: No

[**servers**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: server list
* Mandatory: No
* Dynamic: Yes
* Default: None

[**session\_track\_trx\_state**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**strip\_db\_esc**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**targets**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: target list
* Mandatory: No
* Dynamic: Yes
* Default: None

[**user**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**user\_accounts\_file**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**user\_accounts\_file\_usage**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `add_when_load_ok`, `file_only_always`
* Default: `add_when_load_ok`

[**version\_string**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: None

[**wait\_timeout**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`
* Auto tune: [Yes](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

**Settings for File-based Key Manager**

[**file.keyfile**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: Yes
* Dynamic: Yes

**Settings for HashiCorp Vault Key Manager**

[**vault.ca**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Default: `""`
* Dynamic: Yes

[**vault.host**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Default: `localhost`
* Dynamic: Yes

[**vault.mount**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Default: `secret`
* Dynamic: Yes

[**vault.port**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: integer
* Default: `8200`
* Dynamic: Yes

[**vault.timeout**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: 30s
* Dynamic: Yes

[**vault.tls**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: true
* Dynamic: Yes

[**vault.token**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: password
* Mandatory: Yes
* Dynamic: Yes

**Settings for KMIP Key Manager**

[**kmip.ca**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Default: `""`
* Dynamic: Yes

[**kmip.cert**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: Yes
* Dynamic: Yes

[**kmip.host**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**kmip.key**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: Yes
* Dynamic: Yes

[**kmip.port**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: integer
* Mandatory: Yes
* Dynamic: Yes

**Settings for TLS/SSL Encryption**

[**ssl**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**ssl\_ca**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_cert**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_cert\_verify\_depth**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `9`

[**ssl\_cipher**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_crl**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_key**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_verify\_peer\_certificate**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**ssl\_verify\_peer\_host**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory No
* Dynamic: Yes
* Default: `false`

[**ssl\_version**](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)

* Type: [enum\_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `MAX`, `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`, `TLSv10`, `TLSv11`, `TLSv12`, `TLSv13`
* Default: `MAX`

### Authenticators

#### [Authentication-Modules](../../../../en/maxscale-25-01-authentication-modules/)

**Settings**

[**lower\_case\_table\_names**](https://mariadb.com/kb/en/maxscale-25-01-authentication-modules/#lower_case_table_names)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `0`

[**match\_host**](https://mariadb.com/kb/en/maxscale-25-01-authentication-modules/#match_host)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**skip\_authentication**](https://mariadb.com/kb/en/maxscale-25-01-authentication-modules/#skip_authentication)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

#### [GSSAPI-Authenticator](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-gssapi-client-authenticator.md)

**Settings**

[**gssapi\_keytab\_path**](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-gssapi-client-authenticator.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: Kerberos Default

[**principal\_name**](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-gssapi-client-authenticator.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `mariadb/localhost.localdomain`

#### [MySQL-Authenticator](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-mariadbmysql-authenticator.md)

**Settings**

[**log\_password\_mismatch**](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-mariadbmysql-authenticator.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

#### [PAM-Authenticator](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)

**Settings**

[**pam\_backend\_mapping**](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)

* Type: [enumeration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `none`, `mariadb`
* Default: `none`

[**pam\_mapped\_pw\_file**](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: None

[**pam\_mode**](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)

* Type: [enumeration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `password`, `password_2FA`, `suid`
* Default: `password`

[**pam\_use\_cleartext\_plugin**](../mariadb-maxscale-25-01-authenticators/mariadb-maxscale-2501-maxscale-2501-pam-authenticator.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

### Filters

#### [BinlogFilter](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-binlog-filter.md)

**Settings**

[**exclude**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-binlog-filter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**match**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-binlog-filter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**rewrite\_dest**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-binlog-filter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**rewrite\_src**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-binlog-filter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [CCRFilter](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)

**Settings**

[**count**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**global**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**ignore**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `""`

[**match**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `""`

[**options**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

[**time**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-consistent-critical-read-filter.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `60s`

#### [Cache](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

**Settings**

[**cache\_in\_transactions**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `never`, `read_only_transactions`, `all_transactions`
* Default: `all_transactions`

[**cached\_data**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `shared`, `thread_specific`
* Default: `thread_specific`

[**clear\_cache\_on\_parse\_errors**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**debug**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**enabled**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**hard\_ttl**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `0s` (no limit)

[**invalidate**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `never`, `current`
* Default: `never`

[**max\_count**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

[**max\_resultset\_rows**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

[**max\_resultset\_size**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

[**max\_size**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

[**rules**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""` (no rules)

[**selects**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `assume_cacheable`, `verify_cacheable`
* Default: `assume_cacheable`

[**soft\_ttl**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `0s` (no limit)

[**storage**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `storage_inmemory`

[**storage\_options**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default:

[**timeout**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `5s`

[**users**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `mixed`, `isolated`
* Default: `mixed`

**`storage_memcached`**

[**max\_value\_size**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: 1Mi

[**server**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: The Memcached server address specified as `host[:port]`
* Mandatory: Yes
* Dynamic: No

**`storage_redis`**

[**password**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**server**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: The Redis server address specified as `host[:port]`
* Mandatory: Yes
* Dynamic: No

[**ssl**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**ssl\_ca**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`

[**ssl\_cert**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`

[**ssl\_key**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`

[**username**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-cache.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

#### [Comment](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-comment-filter.md)

**Settings**

[**inject**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-comment-filter.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

#### [LDIFilter](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)

**Settings**

[**host**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `s3.amazonaws.com`

[**key**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes

[**no\_verify**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**port**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 0

[**protocol\_version**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 0
* Values: 0, 1, 2

[**region**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `us-east-1`

[**secret**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes

[**use\_http**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-ldi-filter.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

#### [Masking](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

**Settings**

[**check\_subqueries**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**check\_unions**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**check\_user\_variables**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**large\_payload**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `ignore`, `abort`
* Default: `abort`

[**prevent\_function\_usage**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**require\_fully\_parsed**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**rules**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

* Type: path
* Mandatory: Yes
* Dynamic: Yes

[**treat\_string\_arg\_as\_field**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**warn\_type\_mismatch**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-masking.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `never`, `always`
* Default: `never`

#### [Maxrows](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)

**Settings**

[**debug**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**max\_resultset\_return**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `empty`, `error`, `ok`
* Default: `empty`

[**max\_resultset\_rows**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: (no limit)

[**max\_resultset\_size**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-maxrows.md)

* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `64Ki`

#### [Named-Server-Filter](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-named-server-filter.md)

**Settings**

[**matchXY**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-named-server-filter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**options**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-named-server-filter.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

[**source**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-named-server-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**targetXY**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-named-server-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**user**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-named-server-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [Query-Log-All-Filter](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

**Settings**

[**append**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**duration\_unit**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `milliseconds`

[**exclude**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**filebase**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: string
* Mandatory: Yes
* Dynamic: No

[**flush**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_data**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [enum\_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `service`, `session`, `date`, `user`, `reply_time`, `total_reply_time`, `query`, `default_db`, `num_rows`, `reply_size`, `transaction`, `transaction_time`, `num_warnings`, `error_msg`
* Default: `date, user, query`

[**log\_type**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [enum\_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `session`, `unified`, `stdout`
* Default: `session`

[**match**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**newline\_replacement**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `" "`

[**options**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [enum\_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `case`, `ignorecase`, `extended`
* Default: `case`

[**separator**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `","`

[**source**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**source\_exclude**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes

[**source\_match**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes

[**use\_canonical\_form**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [bool](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**user**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**user\_exclude**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes

[**user\_match**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-query-log-all-filter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes

#### [Regex-Filter](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)

**Settings**

[**log\_file**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**log\_trace**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**match**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: Yes
* Dynamic: Yes

[**options**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

[**replace**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**source**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**user**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-regex-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [RewriteFilter](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

**Settings**

[**case\_sensitive**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

* Type: boolean
* Mandatory: No
* Dynamic: Yes
* Default: true

[**log\_replacement**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

* Type: boolean
* Mandatory: No
* Dynamic: Yes
* Default: false

[**regex\_grammar**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: Native
* Values: `Native`, `ECMAScript`, `Posix`, `EPosix`, `Awk`, `Grep`, `EGrep`

[**template\_file**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Default: No default value

**Settings per template in the template file**

[**case\_sensitive**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

* Type: boolean
* Default: From maxscale.cnf

[**continue\_if\_matched**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

* Type: boolean
* Default: false

[**ignore\_whitespace**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

* Type: boolean
* Default: true

[**regex\_grammar**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

* Type: string
* Values: `Native`, `ECMAScript`, `Posix`, `EPosix`, `Awk`, `Grep`, `EGrep`
* Default: From maxscale.cnf

[**what\_if**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-rewrite-filter.md)

* Type: boolean
* Default: false

#### [Tee-Filter](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)

**Settings**

[**exclude**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**match**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**options**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

[**service**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)

* Type: service
* Mandatory: No
* Dynamic: Yes
* Default: none

[**source**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**sync**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**target**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)

* Type: target
* Mandatory: No
* Dynamic: Yes
* Default: none

[**user**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-tee-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [Throttle](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-throttle.md)

**Settings**

[**continuous\_duration**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-throttle.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 2s

[**max\_qps**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-throttle.md)

* Type: number
* Mandatory: Yes
* Dynamic: Yes

[**sampling\_duration**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-throttle.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 250ms

[**throttling\_duration**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-throttle.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: Yes
* Dynamic: Yes

#### [Top-N-Filter](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)

**Settings**

[**count**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`

[**exclude**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**filebase**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**match**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**options**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `ignorecase`, `case`, `extended`
* Default: `case`

[**source**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**user**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-top-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [Wcar](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-workload-capture-and-replay.md)

**Settings**

[**capture\_dir**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-workload-capture-and-replay.md)

* Type: path
* Default: /var/lib/maxscale/wcar/
* Mandatory: No
* Dynamic: No

[**capture\_duration**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-workload-capture-and-replay.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: 0s
* Mandatory: No
* Dynamic: No

[**capture\_size**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-workload-capture-and-replay.md)

* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: 0
* Mandatory: No
* Dynamic: No

[**start\_capture**](../mariadb-maxscale-25-01-filters/mariadb-maxscale-2501-maxscale-2501-workload-capture-and-replay.md)

* Type: boolean
* Default: false
* Mandatory: No
* Dynamic: No

### Monitors

#### [Galera-Monitor](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)

**Settings**

[**available\_when\_donor**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)

* Type: boolean
* Default: false
* Dynamic: Yes

[**disable\_master\_failback**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)

* Type: boolean
* Default: false
* Dynamic: Yes

[**disable\_master\_role\_setting**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)

* Type: boolean
* Default: false
* Dynamic: Yes

[**root\_node\_as\_master**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)

* Type: boolean
* Default: false
* Dynamic: Yes

[**set\_donor\_nodes**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)

* Type: boolean
* Default: false
* Dynamic: Yes

[**use\_priority**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-galera-monitor.md)

* Type: boolean
* Default: false
* Dynamic: Yes

#### [MariaDB-Monitor](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

**Settings**

[**assume\_unique\_hostnames**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**cooperative\_monitoring\_locks**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `majority_of_all`, `majority_of_running`
* Default: `none`

[**enforce\_read\_only\_servers**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**enforce\_read\_only\_slaves**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**enforce\_writable\_master**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**failcount**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `5`

[**maintenance\_on\_low\_disk\_space**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**master\_conditions**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [enum\_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `connecting_slave`, `connected_slave`, `running_slave`, `primary_monitor_master`, `disk_space_ok`
* Default: `primary_monitor_master, disk_space_ok`

[**script\_max\_replication\_lag**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `-1`

[**slave\_conditions**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [enum\_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `linked_master`, `running_master`, `writable_master`, `primary_monitor_master`
* Default: `none`

**Settings for Backup operations**

[**backup\_storage\_address**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**backup\_storage\_path**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: None

[**rebuild\_port**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `4444`

[**ssh\_check\_host\_key**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**ssh\_keyfile**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: None

[**ssh\_port**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `22`

[**ssh\_timeout**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**ssh\_user**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

**Settings for Cluster manipulation operations**

[**auto\_failover**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `true`, `on`, `yes`, `1`, `false`, `off`, `no`, `0`, `safe`
* Default: `false`

[**auto\_rejoin**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**demotion\_sql\_file**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**enforce\_simple\_topology**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**failover\_timeout**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`

[**handle\_events**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**master\_failure\_timeout**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**promotion\_sql\_file**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**replication\_master\_ssl**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**replication\_password**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**replication\_user**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**servers\_no\_promotion**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**switchover\_on\_low\_disk\_space**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**switchover\_timeout**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`

[**verify\_master\_failure**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

**Settings for Primary server write test**

[**write\_test\_fail\_action**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: `log`
* Values: `log`, `failover`
* Dynamic: Yes

[**write\_test\_interval**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Dynamic: Yes
* Default: 0s

[**write\_test\_table**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-mariadb-monitor.md)

* Type: string
* Dynamic: Yes
* Default: `mxs.maxscale_write_test`

#### [Monitor-Common](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

**Settings**

[**backend\_connect\_attempts**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `1`

[**backend\_connect\_timeout**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`

[**backend\_read\_timeout**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`

[**backend\_write\_timeout**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`

[**disk\_space\_check\_interval**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

[**disk\_space\_threshold**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**events**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: enum
* Mandatory: No
* Dynamic: Yes
* Values: `master_down`, `master_up`, `slave_down`, `slave_up`, `server_down`, `server_up`, `lost_master`, `lost_slave`, `new_master`, `new_slave`
* Default: All events

[**journal\_max\_age**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `28800s`

[**module**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: string
* Mandatory: Yes
* Dynamic: No

[**monitor\_interval**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `2s`

[**password**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**script**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**script\_timeout**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`

[**servers**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**user**](../mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

### Protocols

#### [MariaDB](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-mariadb-protocol-module.md)

**Settings**

[**allow\_replication**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-mariadb-protocol-module.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true

#### [NoSQL](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

**Settings**

[**authentication\_db**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: `"NoSQL"`

[**authentication\_key\_id**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: `""`

[**authentication\_password**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: `""`

[**authentication\_required**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `false`

[**authentication\_shared**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `false`

[**authentication\_user**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: string
* Mandatory: Yes, if `authentication_shared` is true.

[**authorization\_enabled**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `false`

[**auto\_create\_databases**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `true`

[**auto\_create\_tables**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `true`

[**cursor\_timeout**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `60s`

[**debug**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [enum\_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Values: `none`, `in`, `out`, `back`
* Default: `none`

[**host**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: `"%"`

[**id\_length**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: count
* Mandatory: No
* Range: `[35, 2048]`
* \*Default: `35`

[**internal\_cache**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: ''

[**log\_unknown\_command**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: `false`

[**on\_unknown\_command**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Values: `return_error`, `return_empty`
* Default: `return_error`

[**ordered\_insert\_behavior**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Values: `atomic`, `default`
* Default: `default`

[**password**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: `""`

[**user**](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: `""`

### Routers

#### [Avrorouter](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

**Settings**

[**avrodir**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/`

[**binlogdir**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/`

[**codec**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `null`, `deflate`
* Default: `null`

[**cooperative\_replication**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**exclude**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `""`

[**filestem**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `mysql-bin`

[**gtid\_start\_pos**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**match**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `""`

[**server\_id**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1234`

[**start\_index**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1`

**Settings for Avro File**

[**block\_size**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `16KiB`

[**group\_rows**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1000`

[**group\_trx**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1`

[**max\_data\_age**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: 0s

[**max\_file\_size**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-avrorouter.md)

* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: 0

#### [Binlogrouter](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

**Settings**

[**archivedir**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: string
* Mandatory: Yes
* Default: No
* Dynamic: No

[**compression\_algorithm**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `none`, `zstandard`
* Default: `none`

[**datadir**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/binlogs`

[**ddl\_only**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: boolean
* Mandatory: No
* Dynamic: No
* Default: false

[**encryption\_cipher**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `AES_CBC`, `AES_CTR`, `AES_GCM`
* Default: `AES_GCM`

[**encryption\_key\_id**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**expiration\_mode**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Dynamic: No
* Values: `purge`, `archive`
* Default: `purge`

[**expire\_log\_duration**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `0s`

[**expire\_log\_minimum\_files**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `2`

[**net\_timeout**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `10s`

[**number\_of\_noncompressed\_files**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `2`

[**rpl\_semi\_sync\_slave\_enabled**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Default: false
* Dynamic: Yes

[**select\_master**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**server\_id**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-binlogrouter.md)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `1234`

#### [Diff](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

**Settings**

[**explain**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `other`, \`both'
* Default: `both`

[**explain\_entries**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 2

[**explain\_period**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 15m

[**main**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: server
* Mandatory: Yes
* Dynamic: No

[**max\_request\_lag**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 10

[**on\_error**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `close`, `ignore`
* Default: `ignore`

[**percentile**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Min: 1
* Max: 100
* Default: 99

[**qps\_window**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: 15m

[**report**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `always`, `on_discrepancy`, `never`
* Default: `on_discrepancy`

[**reset\_replication**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**retain\_faster\_statements**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 5

[**retain\_slower\_statements**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 5

[**samples**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Min: 100
* Default: 1000

[**service**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-diff-router-for-comparing-servers.md)

* Type: service
* Mandatory: Yes
* Dynamic: No

#### [KafkaCDC](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

**Settings**

[**bootstrap\_servers**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: string
* Mandatory: Yes
* Dynamic: No

[**cooperative\_replication**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**enable\_idempotence**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**exclude**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**gtid**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_sasl\_mechanism**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Values: `PLAIN`, `SCRAM-SHA-256`, `SCRAM-SHA-512`
* Default: `PLAIN`

[**kafka\_sasl\_password**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_sasl\_user**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_ssl**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**kafka\_ssl\_ca**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_ssl\_cert**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_ssl\_key**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**match**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**read\_gtid\_from\_kafka**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**send\_schema**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true

[**server\_id**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1234`

[**timeout**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**topic**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md)

* Type: string
* Mandatory: Yes
* Dynamic: No

#### [KafkaImporter](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

**Settings**

[**batch\_size**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Default: `100`

[**bootstrap\_servers**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**engine**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: string
* Default: `InnoDB`
* Mandatory: No
* Dynamic: Yes

[**kafka\_sasl\_mechanism**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `PLAIN`, `SCRAM-SHA-256`, `SCRAM-SHA-512`
* Default: `PLAIN`

[**kafka\_sasl\_password**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**kafka\_sasl\_user**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**kafka\_ssl**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**kafka\_ssl\_ca**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**kafka\_ssl\_cert**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**kafka\_ssl\_key**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**table\_name\_in**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `topic`, `key`
* Default: `topic`

[**timeout**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `5000ms`

[**topics**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkaimporter.md)

* Type: stringlist
* Mandatory: Yes
* Dynamic: Yes

#### [Mirror](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)

**Settings**

[**exporter**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: Yes
* Dynamic: Yes
* Values: `log`, `file`, `kafka`

[**file**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)

* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes

[**kafka\_broker**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)

* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes

[**kafka\_topic**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)

* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes

[**main**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)

* Type: target
* Mandatory: Yes
* Dynamic: Yes

[**on\_error**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: `ignore`
* Mandatory: No
* Dynamic: Yes
* Values: `ignore`, `close`

[**report**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-mirror.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Default: `always`
* Mandatory: No
* Dynamic: Yes
* Values: `always`, `on_conflict`

#### [ReadConnRoute](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readconnroute.md)

**Settings**

[**master\_accept\_reads**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readconnroute.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true

[**max\_replication\_lag**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readconnroute.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 0s

[**router\_options**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readconnroute.md)

* Type: [enum\_mask](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `master`, `slave`, `synced`, `running`
* Default: `running`

#### [ReadWriteSplit](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

**Settings**

[**causal\_reads**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `local`, `global`, `fast`, `fast_global`, `universal`, `fast_universal`
* Default: `none`

[**causal\_reads\_timeout**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 10s

[**delayed\_retry**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**delayed\_retry\_timeout**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 10s

[**lazy\_connect**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**master\_accept\_reads**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**master\_failure\_mode**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `fail_instantly`, `fail_on_write`, `error_on_write`
* Default: `fail_on_write` (MaxScale 23.08: `fail_instantly`)

[**master\_reconnection**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true (>= MaxScale 24.02), false(<= MaxScale 23.08)

[**max\_replication\_lag**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 0s

[**max\_slave\_connections**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 255

[**retry\_failed\_reads**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true

[**slave\_connections**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 255

[**slave\_selection\_criteria**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `least_current_operations`, `adaptive_routing`, `least_behind_master`, `least_router_connections`, `least_global_connections`
* Default: `least_current_operations`

[**strict\_multi\_stmt**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**strict\_sp\_calls**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**strict\_tmp\_tables**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true (>= MaxScale 24.02), false (<= MaxScale 23.08)

[**transaction\_replay**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**transaction\_replay\_attempts**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 5

[**transaction\_replay\_checksum**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `full`, `result_only`, `no_insert_id`
* Default: `full`

[**transaction\_replay\_max\_size**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [size](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 1 MiB

[**transaction\_replay\_retry\_on\_deadlock**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**transaction\_replay\_retry\_on\_mismatch**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**transaction\_replay\_safe\_commit**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true

[**transaction\_replay\_timeout**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 30s (>= MaxScale 24.02), 0s (<= MaxScale 23.08)

[**use\_sql\_variables\_in**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md)

* Type: [enum](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `master`, `all`
* Default: `all`

#### [SchemaRouter](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)

**Settings**

[**allow\_duplicates**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**ignore\_tables**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)

* Type: stringlist
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ignore\_tables\_regex**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)

* Type: [regex](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `""`

[**max\_staleness**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: 150s

[**refresh\_databases**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)

* Type: [boolean](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**refresh\_interval**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter.md)

* Type: [duration](../mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `300s`

#### [SmartRouter](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-smartrouter.md)

**Settings**

[**master**](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-smartrouter.md)

* Type: target
* Mandatory: Yes
* Dynamic: No

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
