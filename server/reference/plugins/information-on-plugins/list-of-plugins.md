
# List of Plugins


## MariaDB Plugin Maturity


The following table lists the various plugins included in MariaDB ordered by their maturity. Note that maturity will differ across MariaDB versions - see below for an easy way to get a complete list of plugins and their maturity in your version of MariaDB:



| Plugin | Version | Maturity | Version | Plugin | Version | Maturity | From | Plugin | Version | Maturity | From | Plugin | Version | Maturity | From | Plugin | Version | Maturity | Version |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Plugin | Version | Maturity | Version |
| [Archive](../../storage-engines/archive/README.md) | 3.0 | Stable |  |
| [Aria](../../storage-engines/s3-storage-engine/aria_s3_copy.md) | 1.5 | Stable |  |
| [Audit Plugin](../mariadb-audit-plugin/mariadb-audit-plugin-log-settings.md) | 1.4 | Stable |  |
| [aws_key_management](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin-setup-guide.md) | 1.0 | Stable |  |
| [binlog](../../storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) | 1.0 | Stable |  |
| [Blackhole](../../storage-engines/blackhole.md) | 1.0 | Stable |  |
| [Connect](../../../../connectors/mariadb-connector-nodejs/connector-nodejs-pipelining.md) | 1.7 | Stable | [MariaDB 10.4.12](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10412-release-notes.md), [MariaDB 10.3.22](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10322-release-notes.md) |
| [CLIENT_STATISTICS](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) | 2.0 | Stable |  |
| [cracklib_password_check](../password-validation-plugins/cracklib-password-check-plugin.md) | 1.0 | Stable |  |
| [CSV](../../storage-engines/csv/csv-overview.md) | 1.0 | Stable |  |
| [DISKS](../other-plugins/disks-plugin.md) | 1.1 | Stable | [MariaDB 10.4.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1047-release-notes.md), [MariaDB 10.3.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10317-release-notes.md) |
| [ed25519](../authentication-plugins/authentication-plugin-ed25519.md) | 1.1 | Stable | [MariaDB 10.4.0](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1040-release-notes.md) |
| [FederatedX](../../storage-engines/federatedx-storage-engine/README.md)[[1](#_note-0)] | 2.1 | Stable |  |
| [Feedback](../other-plugins/feedback-plugin.md) | 1.1 | Stable |  |
| [file_key_management](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md) | 1.0 | Stable |
| [gssapi](../authentication-plugins/authentication-plugin-gssapi.md) | 1.0 | Stable |  |
| [INDEX_STATISTICS](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) | 2.0 | Stable |  |
| [INET6](../../sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/miscellaneous-functions/inet6_aton.md) | 1.0 | Stable | [MariaDB 10.5.12](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10512-release-notes.md) |
| [InnoDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) | 10.* | Stable |  |
| [LOCALES](../../data-types/string-data-types/character-sets/internationalization-and-localization/locales-plugin.md) | 1.0 | Stable |  |
| [Memory](../../storage-engines/memory-storage-engine.md) | 1.0 | Stable |  |
| [METADATA_LOCK_INFO](../other-plugins/metadata-lock-info-plugin.md) | 0.1 | Stable |  |
| [MRG_MyISAM](../../storage-engines/merge.md) | 1.0 | Stable |  |
| [Mroonga](../../storage-engines/mroonga/mroonga-user-defined-functions/mroonga_snippet_html.md) | 7.7 | Stable |  |
| [MyISAM](../../storage-engines/myisam-storage-engine/README.md) | 1.0 | Stable |  |
| [MyRocks](../../storage-engines/myrocks/myrocks-in-mariadb-102-vs-mariadb-103.md) | 1.0 | Stable | [MariaDB 10.3.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md) |
| [mysql_json](../other-plugins/mysql_json.md) | 0.1 | Stable | [MariaDB 10.5.17](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10517-release-notes.md) |
| [mysql_native_password](../authentication-plugins/authentication-plugin-mysql_native_password.md) | 1.0 | Stable |  |
| [mysql_old_password](../authentication-plugins/authentication-plugin-mysql_old_password.md) | 1.0 | Stable |  |
| [named_pipe](../authentication-plugins/authentication-plugin-named-pipe.md) | 1.0 | Stable |  |
| [pam](../authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md) | 1.0 | Stable |  |
| [password_reuse_check](../password-validation-plugins/password-reuse-check-plugin.md) | 2.0 | Stable | [MariaDB 10.8.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-8-series/mariadb-10-8-7-release-notes.md), [MariaDB 10.9.5](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-9-series/mariadb-10-9-5-release-notes.md), [MariaDB 10.10.2](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-10-series/mariadb-10-10-2-release-notes.md) |
| partition | 1.0 | Stable |  |
| [Performance_Schema](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-table_handles-table.md) | 0.1 | Stable |  |
| [QUERY_CACHE_INFO](../other-plugins/query-cache-information-plugin.md) | 1.1 | Stable |  |
| [query_response_time](../other-plugins/query-response-time-plugin.md) | 1.0 | Stable |  |
| [S3](../../storage-engines/s3-storage-engine/s3-storage-engine-status-variables.md) | 1.0 | Stable | [MariaDB 10.5.12](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10512-release-notes.md) |
| [semisync](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md) | 1.0 | Stable | Built-in, no longer a plugin from [MariaDB 10.3.3](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md) |
| [Sequence](../../storage-engines/sequence-storage-engine.md) | 1.0 | Stable |  |
| [SERVER_AUDIT](../mariadb-audit-plugin/release-notes-mariadb-audit-plugin/mariadb-audit-plugin-113-release-notes.md) | 1.4 | Stable |  |
| [simple_password_check](../password-validation-plugins/simple-password-check-plugin.md) | 1.0 | Stable |  |
| [Spider](../../storage-engines/spider/spider-functions/spider_copy_tables.md) | 3.3 | Stable | <= [MariaDB 10.4](../../../../release-notes/mariadb-community-server/what-is-mariadb-104.md), [MariaDB 10.5.7](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1057-release-notes.md) |
| [SQL_ERROR_LOG](../../../server-management/server-monitoring-logs/sql-error-log-plugin.md) | 1.0 | Stable |  |
| [TABLE_STATISTICS](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) | 2.0 | Stable |  |
| [USER_STATISTICS](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) | 2.0 | Stable |  |
| [user_variables](../other-plugins/user-variables-plugin.md) | 1.0 | Stable | [MariaDB 10.3.13](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10313-release-notes.md) |
| [TokuDB](../../storage-engines/tokudb/tokudb-resources.md) | 4.0 | Stable | Disabled in [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md) and removed in [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md) |
| [unix_socket](../authentication-plugins/authentication-plugin-unix-socket.md) | 1.0 | Stable |  |
| [UUID](../../data-types/string-data-types/uuid-data-type.md) | 1.0 | Stable | [MariaDB 10.9.1](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-9-series/mariadb-1091-release-notes.md) |
| [wsrep](../../sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md) | 1.0 | Stable |  |
| [WSREP_INFO](../mariadb-replication-cluster-plugins/wsrep_info-plugin.md) | 1.0 | Stable |  |
| Plugin | Version | Maturity | From |
| [Federated](../../storage-engines/legacy-storage-engines/federated-storage-engine.md)[[2](#_note-1)] | 1.0 | Gamma |  |
| [OQGraph](../../storage-engines/oqgraph-storage-engine/README.md) | 3.0 | Gamma |  |
| [Sphinx](../../storage-engines/sphinx-storage-engine/README.md) | 2.0 | Gamma |  |
| Plugin | Version | Maturity | From |
| [Columnstore](../../../../columnstore/using-mariadb-columnstore/mariadb-columnstore-with-spark.md) | 1.0 | Beta | [MariaDB 10.5.4](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1054-release-notes.md) |
| [handlersocket](../../sql-statements-and-structure/nosql/handlersocket/handlersocket-external-resources.md) | 1.0 | Beta |  |
| Plugin | Version | Maturity | From |
| [Cassandra](../../storage-engines/legacy-storage-engines/cassandra/cassandra-storage-engine-issues.md) | 0.1 | Experimental | Removed in [MariaDB 10.6](../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md) |
| [debug_key_management](../../mariadb-internals/encryption-plugin-api.md) | 1.0 | Experimental |  |
| [example_key_management](../../mariadb-internals/encryption-plugin-api.md) | 1.0 | Experimental |  |
| Plugin | Version | Maturity | Version |



Execute the following on your MariaDB server to get a complete list of plugins and their maturity for your version of MariaDB:


```
SELECT plugin_name, plugin_version, plugin_maturity
FROM information_schema.plugins
ORDER BY plugin_name;
```

## See Also


* [Plugin Overview](../plugin-overview.md)
* [INSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md)
* [INFORMATION_SCHEMA.PLUGINS Table](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md)
* [mysql_plugin](../../../clients-and-utilities/legacy-clients-and-utilities/mysql_plugin.md)
* [SHOW PLUGINS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-plugins-soname.md)
* [INSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md)
* [UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)
* [UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)




