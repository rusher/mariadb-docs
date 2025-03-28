# ps_is_account_enabled

#

# Syntax

```
sys.ps_is_account_enabled(host,user)
```

#

# Description

`ps_is_account_enabled` is a [stored function](/en/stored-functions/) available with the [Sys Schema](../sys-schema-sys_config-table.md).

It takes *host* and *user* arguments, and returns an ENUM('YES','NO') depending on whether Performance Schema instrumentation for the given account is enabled.

#

# Examples

```
SELECT sys.ps_is_account_enabled('localhost', 'root');
+------------------------------------------------+
| sys.ps_is_account_enabled('localhost', 'root') |
+------------------------------------------------+
| YES |
+------------------------------------------------+
```