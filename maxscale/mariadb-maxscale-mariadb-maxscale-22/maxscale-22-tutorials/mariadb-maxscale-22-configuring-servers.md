
# MaxScale 2.2 - Configuring Servers

# Configuring Servers


The first step is to define the servers that make up the cluster. These servers
will be used by the services and are monitored by the monitor.



```
[dbserv1]
type=server
address=192.168.2.1
port=3306
protocol=MariaDBBackend

[dbserv2]
type=server
address=192.168.2.2
port=3306
protocol=MariaDBBackend

[dbserv3]
type=server
address=192.168.2.3
port=3306
protocol=MariaDBBackend
```



The `<code>address</code>` and `<code>port</code>` parameters tell where the server is located. The
`<code>protocol</code>` should always be set to `<code>MariaDBBackend</code>`.
