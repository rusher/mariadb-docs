# ps\_is\_account\_enabled

## Syntax

```
sys.ps_is_account_enabled(host,user)
```

## Description

`ps_is_account_enabled` is a [stored function](../../../../../../server-usage/stored-routines/stored-functions/) available with the [Sys Schema](../).

It takes _host_ and _user_ arguments, and returns an ENUM('YES','NO') depending on whether Performance Schema instrumentation for the given account is enabled.

## Examples

```
SELECT sys.ps_is_account_enabled('localhost', 'root');
+------------------------------------------------+
| sys.ps_is_account_enabled('localhost', 'root') |
+------------------------------------------------+
| YES                                            |
+------------------------------------------------+
```

CC BY-SA / Gnu FDL
