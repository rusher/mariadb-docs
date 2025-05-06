
# Reconnecting to the Primary Server with MaxScale's Read/Write Split Router


# Overview


The Read/Write Split Router (readwritesplit) routes write queries to the primary server and load balances read-only queries between one or more replica servers. If the primary server fails, then the router can automatically reconnect existing client connections to the new primary server.


# Configuring Automatic Primary Server Re-connection


1. Configure automatic primary server re-connection by configuring several parameters for the Read/Write Split Router in maxscale.cnf.



| Parameter | Description |
| --- | --- |
| Parameter | Description |
| master_reconnection | • When this parameter is enabled, if the primary server fails and if master_failure_mode is not set to fail_instantly, then existing client connections will be automatically reconnected to the new primary server. • This parameter is disabled by default. |
| master_failure_mode | • This parameter defines how client connections are handled when the primary server fails. • This parameter must be set to either fail_on_write or error_on_write to allow automatic primary server reconnection. • When this parameter is set to fail_on_write, the client connection is closed if a write query is received when no primary is available. • When this parameter is set to error_on_write, if no primary server is available and a write query is received, an error is returned stating that the connection is in read-only mode. |



For example:


```
[split-router]
type                     = service
router                   = readwritesplit
...
master_reconnection            = true
master_failure_mode            = fail_on_write
```

2. Restart the MaxScale instance.


```
$ sudo systemctl restart maxscale
```


Copyright © 2025 MariaDB

