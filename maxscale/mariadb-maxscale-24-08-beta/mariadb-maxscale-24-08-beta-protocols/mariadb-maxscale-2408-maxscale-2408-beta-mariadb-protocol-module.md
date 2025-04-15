
# MaxScale 24.08 Beta MariaDB Protocol Module

# MariaDB Protocol Module


The `<code>mariadbprotocol</code>` module implements the MariaDB client-server protocol.


The legacy protocol names `<code>mysqlclient</code>`, `<code>mariadb</code>` and `<code>mariadbclient</code>` are all
aliases to `<code>mariadbprotocol</code>`.




* [MariaDB Protocol Module](#mariadb-protocol-module)

  * [Configuration](#configuration)

    * [allow_replication](#allow_replication)




## Configuration


Protocol level parameters are defined in the listeners. They must be defined
using the scoped parameter syntax where the protocol name is used as the prefix.



```
[MyListener]
type=listener
service=MyService
protocol=mariadbprotocol
mariadbprotocol.allow_replication=false
port=3306
```



For the MariaDB protocol module, the prefix is always `<code>mariadbprotocol</code>`.


### `<code>allow_replication</code>`


* Type: [boolean](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: true


Whether the use of the replication protocol is allowed through this listener. If
disabled with `<code>mariadbprotocol.allow_replication=false</code>`, all attempts to start
replication will be rejected with a ER_FEATURE_DISABLED error (error number
1289).
