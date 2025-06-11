# Retrying Failed Reads with MaxScale's Read/Write Split Router

The [Read/Write Split Router (readwritesplit)](../../../mariadb-maxscale-23-02/mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readwritesplit.md) routes write queries to the primary server and load balances read-only queries between one or more replica servers. If a read-only query fails, then the router can retry the query on a different server.

## Configuring Retries for Failed Reads

1. Configure retries for failed reads by configuring the `retry_failed_reads` parameter for the Read/Write Split Router in `maxscale.cnf`.

For example:

```
[split-router]
type                     = service
router                   = readwritesplit
...
retry_failed_reads       = true
```

2. Restart the MaxScale instance.

```
$ sudo systemctl restart maxscale
```

Copyright © 2025 MariaDB

{% @marketo/form formId="4316" %}
