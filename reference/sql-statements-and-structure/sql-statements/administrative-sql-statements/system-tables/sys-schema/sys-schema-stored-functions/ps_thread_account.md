# ps_thread_account

#

# Syntax

```
sys.ps_thread_account(thread_id)
```

#

# Description

`ps_thread_account` is a [stored function](/en/stored-functions/) available with the [Sys Schema](../sys-schema-sys_config-table.md) that returns the account (username@hostname) associated with the given *thread_id*.

Returns `NULL` if the thread_id is not found.

#

# Examples

```
SELECT sys.ps_thread_account(sys.ps_thread_id(CONNECTION_ID()));
+----------------------------------------------------------+
| sys.ps_thread_account(sys.ps_thread_id(CONNECTION_ID())) |
+----------------------------------------------------------+
| msandbox@localhost |
+----------------------------------------------------------+

SELECT sys.ps_thread_account(sys.ps_thread_id(2042));
+-----------------------------------------------+
| sys.ps_thread_account(sys.ps_thread_id(2042)) |
+-----------------------------------------------+
| NULL |
+-----------------------------------------------+

SELECT sys.ps_thread_account(sys.ps_thread_id(NULL));
+-----------------------------------------------+
| sys.ps_thread_account(sys.ps_thread_id(NULL)) |
+-----------------------------------------------+
| msandbox@localhost |
+-----------------------------------------------+
```