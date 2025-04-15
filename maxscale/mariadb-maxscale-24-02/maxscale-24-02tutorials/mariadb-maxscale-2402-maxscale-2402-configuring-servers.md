
# MaxScale 24.02 Configuring Servers

# Configuring Servers


The first step is to define the servers that make up the cluster. These servers
will be used by the services and are monitored by the monitor.



```
[dbserv1]
type=server
address=192.168.2.1
port=3306

[dbserv2]
type=server
address=192.168.2.2
port=3306

[dbserv3]
type=server
address=192.168.2.3
port=3306
```



The `<code>address</code>` and `<code>port</code>` parameters tell where the server is located.


## Enabling TLS


To enable encryption for the MaxScale-to-MariaDB communication, add `<code>ssl=true</code>`
to the server section. To enable server certificate verification, add
`<code>ssl_verify_peer_certificate=true</code>`.


The `<code>ssl</code>` and `<code>ssl_verify_peer_certificate</code>` parameters are similar to the
`<code>--ssl</code>` and `<code>--ssl-verify-server-cert</code>` options of the `<code>mysql</code>` command line
client.


For more information about TLS, refer to the
[Configuration Guide](../maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md).
