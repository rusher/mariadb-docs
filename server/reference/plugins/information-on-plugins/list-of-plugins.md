
# List of Plugins


## MariaDB Plugin Maturity


The following table lists the various plugins included in MariaDB ordered by their maturity. Note that maturity will differ across MariaDB versions - see below for an easy way to get a complete list of plugins and their maturity in your version of MariaDB:



| Plugin | Version | Maturity | Version | Plugin | Version | Maturity | From | Plugin | Version | Maturity | From | Plugin | Version | Maturity | From | Plugin | Version | Maturity | Version |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Plugin | Version | Maturity | Version |
| [Archive](../../storage-engines/archive/README.md) | 3.0 | Stable |  |
| [Aria](../../storage-engines/aria/README.md) | 1.5 | Stable |  |
| [Audit Plugin](../mariadb-audit-plugin/mariadb-audit-plugin-log-settings.md) | 1.4 | Stable |  |
| [aws_key_management](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin.md) | 1.0 | Stable |  |
| [binlog](../../../server-management/server-monitoring-logs/binary-log/README.md) | 1.0 | Stable |  |
| [Blackhole](../../storage-engines/blackhole.md) | 1.0 | Stable |  |
| [Connect](../../storage-engines/connect/README.md) | 1.7 | Stable | [MariaDB 10.4.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10412-release-notes), [MariaDB 10.3.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10322-release-notes) |
| [CLIENT_STATISTICS](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) | 2.0 | Stable |  |
| [cracklib_password_check](../password-validation-plugins/cracklib-password-check-plugin.md) | 1.0 | Stable |  |
| [CSV](../../storage-engines/csv/README.md) | 1.0 | Stable |  |
| [DISKS](../other-plugins/disks-plugin.md) | 1.1 | Stable | [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1047-release-notes), [MariaDB 10.3.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10317-release-notes) |
| [ed25519](../authentication-plugins/authentication-plugin-ed25519.md) | 1.1 | Stable | [MariaDB 10.4.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1040-release-notes) |
| [FederatedX](../../storage-engines/federatedx-storage-engine/README.md)[[1](#_note-0)] | 2.1 | Stable |  |
| [Feedback](../other-plugins/feedback-plugin.md) | 1.1 | Stable |  |
| [file_key_management](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md) | 1.0 | Stable |
| [gssapi](../authentication-plugins/authentication-plugin-gssapi.md) | 1.0 | Stable |  |
| [INDEX_STATISTICS](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) | 2.0 | Stable |  |
| [INET6](../../data-types/string-data-types/inet6.md) | 1.0 | Stable | [MariaDB 10.5.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-10512-release-notes) |
| [InnoDB](../../storage-engines/innodb/README.md) | 10.* | Stable |  |
| [LOCALES](../../data-types/string-data-types/character-sets/internationalization-and-localization/locales-plugin.md) | 1.0 | Stable |  |
| [Memory](../../storage-engines/memory-storage-engine.md) | 1.0 | Stable |  |
| [METADATA_LOCK_INFO](../other-plugins/metadata-lock-info-plugin.md) | 0.1 | Stable |  |
| [MRG_MyISAM](../../storage-engines/merge.md) | 1.0 | Stable |  |
| [Mroonga](../../storage-engines/mroonga/README.md) | 7.7 | Stable |  |
| [MyISAM](../../storage-engines/myisam-storage-engine/README.md) | 1.0 | Stable |  |
| [MyRocks](../../storage-engines/myrocks/README.md) | 1.0 | Stable | [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes) |
| [mysql_json](../other-plugins/mysql_json.md) | 0.1 | Stable | [MariaDB 10.5.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-10517-release-notes) |
| [mysql_native_password](../authentication-plugins/authentication-plugin-mysql_native_password.md) | 1.0 | Stable |  |
| [mysql_old_password](../authentication-plugins/authentication-plugin-mysql_old_password.md) | 1.0 | Stable |  |
| [named_pipe](../authentication-plugins/authentication-plugin-named-pipe.md) | 1.0 | Stable |  |
| [pam](../authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md) | 1.0 | Stable |  |
| [password_reuse_check](../password-validation-plugins/password-reuse-check-plugin.md) | 2.0 | Stable | [MariaDB 10.8.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-10-8-7-release-notes), [MariaDB 10.9.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-10-9-5-release-notes), [MariaDB 10.10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/mariadb-10-10-2-release-notes) |
| partition | 1.0 | Stable |  |
| [Performance_Schema](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/README.md) | 0.1 | Stable |  |
| [QUERY_CACHE_INFO](../other-plugins/query-cache-information-plugin.md) | 1.1 | Stable |  |
| [query_response_time](../other-plugins/query-response-time-plugin.md) | 1.0 | Stable |  |
| [S3](../../storage-engines/s3-storage-engine/README.md) | 1.0 | Stable | [MariaDB 10.5.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-10512-release-notes) |
| [semisync](../../../server-usage/replication-cluster-multi-master/standard-replication/semisynchronous-replication.md) | 1.0 | Stable | Built-in, no longer a plugin from [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes) |
| [Sequence](../../storage-engines/sequence-storage-engine.md) | 1.0 | Stable |  |
| [SERVER_AUDIT](../mariadb-audit-plugin/README.md) | 1.4 | Stable |  |
| [simple_password_check](../password-validation-plugins/simple-password-check-plugin.md) | 1.0 | Stable |  |
| [Spider](../../storage-engines/spider/README.md) | 3.3 | Stable | <= [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104), [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1057-release-notes) |
| [SQL_ERROR_LOG](../../../server-management/server-monitoring-logs/sql-error-log-plugin.md) | 1.0 | Stable |  |
| [TABLE_STATISTICS](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) | 2.0 | Stable |  |
| [USER_STATISTICS](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) | 2.0 | Stable |  |
| [user_variables](../other-plugins/user-variables-plugin.md) | 1.0 | Stable | [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes) |
| [TokuDB](../../storage-engines/tokudb/README.md) | 4.0 | Stable | Disabled in [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/what-is-mariadb-105) and removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106) |
| [unix_socket](../authentication-plugins/authentication-plugin-unix-socket.md) | 1.0 | Stable |  |
| [UUID](../../data-types/string-data-types/uuid-data-type.md) | 1.0 | Stable | [MariaDB 10.9.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-1091-release-notes) |
| [wsrep](../../../server-usage/replication-cluster-multi-master/galera-cluster/README.md) | 1.0 | Stable |  |
| [WSREP_INFO](../mariadb-replication-cluster-plugins/wsrep_info-plugin.md) | 1.0 | Stable |  |
| Plugin | Version | Maturity | From |
| [Federated](../../storage-engines/legacy-storage-engines/federated-storage-engine.md)[[2](#_note-1)] | 1.0 | Gamma |  |
| [OQGraph](../../storage-engines/oqgraph-storage-engine/README.md) | 3.0 | Gamma |  |
| [Sphinx](../../storage-engines/sphinx-storage-engine/README.md) | 2.0 | Gamma |  |
| Plugin | Version | Maturity | From |
| [Columnstore](/en/mariadb-columnstore/) | 1.0 | Beta | [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1054-release-notes) |
| [handlersocket](../../sql-statements-and-structure/nosql/handlersocket/README.md) | 1.0 | Beta |  |
| Plugin | Version | Maturity | From |
| [Cassandra](../../storage-engines/legacy-storage-engines/cassandra/README.md) | 0.1 | Experimental | Removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-6-series/what-is-mariadb-106) |
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
* [SHOW PLUGINS](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-plugins.md)
* [INSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md)
* [UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)
* [UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)




