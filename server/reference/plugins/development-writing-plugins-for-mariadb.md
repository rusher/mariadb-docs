# Writing Plugins for MariaDB

## About

Generally speaking, writing plugins for MariaDB is very similar to writing plugins for MySQL.

## Authentication Plugins

See [Pluggable Authentication](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/plugins/authentication-plugins/pluggable-authentication-overview.md).

## Storage Engine Plugins

Storage engines can extend `CREATE TABLE` syntax with optional\
index, field, and table attribute clauses. See [Extending CREATE TABLE](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/storage-engines/storage-engines-storage-engine-development/engine-defined-new-tablefieldindex-attributes.md) for more information.

See [Storage Engine Development](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/storage-engines/storage-engines-storage-engine-development/README.md).

## Information Schema Plugins

Information Schema plugins can have their own [FLUSH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) and [SHOW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show) statements. See [FLUSH and SHOW for Information Schema plugins](information-schema-plugins-show-and-flush-statements.md).

## Encryption Plugins

[Encryption plugins](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/mariadb-enterprise-server-differences/mariadb-enterprise-server-data-at-rest-encryption/encryption-plugins) in MariaDB are used for the [data at rest encryption](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) feature. They are responsible for both key management and for the actual encryption and decryption of data.

## Function Plugins

Function plugins add new SQL functions to MariaDB. Unlike the old [UDF](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/server-usage/user-defined-functions/README.md) API, function plugins can do almost anything that a built-function can.

## Plugin Declaration Structure

The MariaDB plugin declaration differs from\
the MySQL plugin declaration in the following ways:

1. it has no useless 'reserved' field (the very last field in the MySQL plugin declaration)
2. it has a 'maturity' declaration
3. it has a field for a text representation of the version field

MariaDB can load plugins that only have the MySQL plugin declaration but both `PLUGIN_MATURITY` and `PLUGIN_AUTH_VERSION` will show up as 'Unknown' in the [INFORMATION\_SCHEMA.PLUGINS table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/plugins-table-information-schema).

For compiled-in (not dynamically loaded) plugins, the presence of the MariaDB plugin declaration is mandatory.

### Example Plugin Declaration

The MariaDB plugin declaration looks like this:

```
/* MariaDB plugin declaration */
maria_declare_plugin(example)
{
   MYSQL_STORAGE_ENGINE_PLUGIN, /* the plugin type (see include/mysql/plugin.h) */
   &example_storage_engine_info, /* pointer to type-specific plugin descriptor   */
   "EXAMPLEDB", /* plugin name */
   "John Smith",  /* plugin author */
   "Example of plugin interface", /* the plugin description */
   PLUGIN_LICENSE_GPL, /* the plugin license (see include/mysql/plugin.h) */
   example_init_func,   /* Pointer to plugin initialization function */
   example_deinit_func,  /* Pointer to plugin deinitialization function */
   0x0001 /* Numeric version 0xAABB means AA.BB version */,
   example_status_variables,  /* Status variables */
   example_system_variables,  /* System variables */
   "0.1 example",  /* String version representation */
   MariaDB_PLUGIN_MATURITY_EXPERIMENTAL /* Maturity (see include/mysql/plugin.h)*/
}
maria_declare_plugin_end;
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
