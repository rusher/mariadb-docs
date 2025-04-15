# mysql.plugin Table

**System tables should not normally be edited directly. Use the related SQL statements instead.**

The `mysql.plugin` table can be queried to get information about installed [plugins](../information-schema/information-schema-tables/plugins-table-information-schema.md).

This table only contains information about [plugins](../information-schema/information-schema-tables/plugins-table-information-schema.md) that have been installed via the following methods:

* The [INSTALL SONAME](../../plugin-sql-statements/install-soname.md) statement.
* The [INSTALL PLUGIN](../../plugin-sql-statements/install-plugin.md) statement.
* The [mariadb-plugin](../../../../../../clients-and-utilities/mariadb-plugin.md) utility.

This table does not contain information about:

* Built-in plugins.
* Plugins loaded with the [--plugin-load-add](/en/mysqld-options/#-plugin-load-add) option.
* Plugins loaded with the [--plugin-load](/en/mysqld-options/#-plugin-load) option.

This table only contains enough information to reload the plugin when the server is restarted, which means it only contains the plugin name and the plugin library.

This table uses the [Aria](../../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/aria-encryption/aria-enabling-encryption.md) storage engine.

The `mysql.plugin` table contains the following fields:

| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| name | varchar(64) | NO | PRI | | Plugin name. |
| dl | varchar(128) | NO | | | Name of the plugin library. |

#

# Example

```
SELECT * FROM mysql.plugin;
+---------------------------+------------------------+
| name | dl |
+---------------------------+------------------------+
| spider | ha_spider.so |
| spider_alloc_mem | ha_spider.so |
| METADATA_LOCK_INFO | metadata_lock_info.so |
| OQGRAPH | ha_oqgraph.so |
| cassandra | ha_cassandra.so |
| QUERY_RESPONSE_TIME | query_response_time.so |
| QUERY_RESPONSE_TIME_AUDIT | query_response_time.so |
| LOCALES | locales.so |
| sequence | ha_sequence.so |
+---------------------------+------------------------+
```