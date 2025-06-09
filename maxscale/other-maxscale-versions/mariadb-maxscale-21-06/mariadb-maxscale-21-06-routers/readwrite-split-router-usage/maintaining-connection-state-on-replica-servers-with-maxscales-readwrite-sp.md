
# Maintaining Connection State on Replica Servers with MaxScale's Read/Write Split Router


# Overview


The [Read/Write Split Router (readwritesplit)](../../../mariadb-maxscale-23-02/mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readwritesplit.md) load balances read-only queries between one or more replica servers. If a replica server fails, then the router may need to create new connections to a different replica server for any existing client connections. The router takes certain steps to ensure that those new replica server connections have the same state as the old replica server connections.


# Session Command History


The [Read/Write Split Router (readwritesplit)](../../../mariadb-maxscale-23-02/mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readwritesplit.md) maintains connection state on replica servers by keeping a session command history. If the router has to create a new connection, then it replays these session commands from the previous connection on the new connection.


# Minimizing Memory Usage of Session Command History


The session command history can require a lot of memory if connections are long-lived. In these cases, there are two options to limit memory usage:


* Configure a maximum size for the session command history
* Disable the session command history. This option is not recommended, because you would lose out on the benefits of the session command history.


## Configuring a Maximum Size of the Session Command History


1. Set the maximum size of the session command history by configuring some parameters for the Read/Write Split Router in `maxscale.cnf`.



| Parameter | Description |
| --- | --- |
| Parameter | Description |
| max_sescmd_history | • The maximum number of distinct session commands that will be stored for each connection. • The default value is 50. |
| prune_sescmd_history | • When this parameter is enabled, the session command history for a connection is pruned when the number of distinct session commands reaches max_sescmd_history. • When this parameter is disabled, the session command history for a connection is disabled when the number of distinct session commands reaches max_sescmd_history. • This parameter is disabled by default. |



For example:


```
[split-router]
type                     = service
router                   = readwritesplit
...
max_sescmd_history       = 1500
prune_sescmd_history     = true
```

2. Restart the MaxScale instance.


```
$ sudo systemctl restart maxscale
```

# Disabling the Session Command History


1. Disable the session command history by configuring the `disable_sescmd_history` parameter for the Read/Write Split Router in `maxscale.cnf`.


For example:


```
[split-router]
type                     = service
router                   = readwritesplit
...
disable_sescmd_history   = true
```

2. Restart the MaxScale instance.


```
$ sudo systemctl restart maxscale
```


Copyright © 2025 MariaDB


{% @marketo/form formId="4316" %}
