
# HandlerSocket Configuration Options

The [HandlerSocket](handlersocket-external-resources.md) plugin has the following options.


See also the [Full list of MariaDB options, system and status variables](../../../../server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables.md).


Add the options to the [mysqld] section of your my.cnf file.



### `<code>handlersocket_accept_balance</code>`


* Description: When set to a value other than zero ('`<code>0</code>`'), handlersocket will try to balance accepted connections among threads. Default is `<code>0</code>` but if you use persistent connections (for example if you use client-side connection pooling) then a non-zero value is recommended.
* Commandline: `<code>--handlersocket-accept-balance="value"</code>`
* Scope: Global
* Dynamic: No
* Type: number
* Range: `<code>0</code>` to `<code>10000</code>`
* Default Value: `<code>0</code>`



### `<code>handlersocket_address</code>`


* Description: Specify the IP address to bind to.
* Commandline: `<code>--handlersocket-address="value"</code>`
* Scope: Global
* Dynamic: No
* Type: IP Address
* Default Value: Empty, previously `<code>0.0.0.0</code>`



### `<code>handlersocket_backlog</code>`


* Description: Specify the listen backlog length.
* Commandline: `<code>--handlersocket-backlog="value"</code>`
* Scope: Global
* Dynamic: No
* Type: number
* Range: `<code>5</code>` to `<code>1000000</code>`
* Default Value: `<code>32768</code>`



### `<code>handlersocket_epoll</code>`


* Description: Specify whether to use epoll for I/O multiplexing.
* Commandline: `<code>--handlersocket-epoll="value"</code>`
* Scope: Global
* Dynamic: No
* Type: number
* Valid values:

  * Min: `<code>0</code>`
  * Max: `<code>1</code>`
* Default Value: `<code>1</code>`



### `<code>handlersocket_plain_secret</code>`


* Description: When set, enables plain-text authentication for the listener for read requests, with the value of the option specifying the secret authentication key.
* Commandline: `<code>--handlersocket-plain-secret="value"</code>`
* Dynamic: No
* Type: string
* Default Value: Empty



### `<code>handlersocket_plain_secret_wr</code>`


* Description: When set, enables plain-text authentication for the listener for write requests, with the value of the option specifying the secret authentication key.
* Commandline: `<code>--handlersocket-plain-secret-wr="value"</code>`
* Dynamic: No
* Type: string
* Default Value: Empty



### `<code>handlersocket_port</code>`


* Description: Specify the port to bind to for reads. An empty value disables the listener.
* Commandline: `<code>--handlersocket-port="value"</code>`
* Scope: Global
* Dynamic: No
* Type: number
* Default Value: Empty, previously `<code>9998</code>`



### `<code>handlersocket_port_wr</code>`


* Description: Specify the port to bind to for writes. An empty value disables the listener.
* Commandline: `<code>--handlersocket-port-wr="value"</code>`
* Scope: Global
* Dynamic: No
* Type: number
* Default Value: Empty, previously `<code>9999</code>`



### `<code>handlersocket_rcvbuf</code>`


* Description: Specify the maximum socket receive buffer (in bytes). If '0' then the system default is used.
* Commandline: `<code>--handlersocket-rcvbuf="value"</code>`
* Scope: Global
* Dynamic: No
* Type: number
* Range: `<code>0</code>` to `<code>1677216</code>`
* Default Value: `<code>0</code>`



### `<code>handlersocket_readsize</code>`


* Description: Specify the minimum length of the request buffer. Larger values consume available memory but can make handlersocket faster for large requests.
* Commandline: `<code>--handlersocket-readsize="value"</code>`
* Scope: Global
* Dynamic: No
* Type: number
* Range: `<code>0</code>` to `<code>1677216</code>`
* Default Value: `<code>0</code>` (possibly `<code>4096</code>`)



### `<code>handlersocket_sndbuf</code>`


* Description: Specify the maximum socket send buffer (in bytes). If '0' then the system default is used.
* Commandline: `<code>--handlersocket-sndbuf="value"</code>`
* Scope: Global
* Dynamic: No
* Type: number
* Range: `<code>0</code>` to `<code>1677216</code>`
* Default Value: `<code>0</code>`



### `<code>handlersocket_threads</code>`


* Description: Specify the number of worker threads for reads. Recommended value = ((

# CPU cores) * 2).
* Commandline: `<code>--handlersocket-threads="value"</code>`
* Scope: Global
* Dynamic: No
* Type: number
* Range: `<code>1</code>` to `<code>3000</code>`
* Default Value: `<code>16</code>`



### `<code>handlersocket_threads_wr</code>`


* Description: Specify the number of worker threads for writes. Recommended value = 1.
* Commandline: `<code>--handlersocket-threads-wr="value"</code>`
* Scope: Global
* Dynamic: No
* Type: number
* Range: `<code>1</code>` to `<code>3000</code>`
* Default Value: `<code>1</code>`



### `<code>handlersocket_timeout</code>`


* Description: Specify the socket timeout in seconds.
* Commandline: `<code>--handlersocket-timeout="value"</code>`
* Scope: Global
* Dynamic: No
* Type: number
* Range: `<code>30</code>` to `<code>3600</code>`
* Default Value: `<code>300</code>`



### `<code>handlersocket_verbose</code>`


* Description: Specify the logging verbosity.
* Commandline: `<code>--handlersocket-verbose="value"</code>`
* Scope: Global
* Dynamic: No
* Type: number
* Valid values:

  * Min: `<code>0</code>`
  * Max: `<code>10000</code>`
* Default Value: `<code>10</code>`



### `<code>handlersocket_wrlock_timeout</code>`


* Description: The write lock timeout in seconds. When acting on write requests, handlersocket locks an advisory lock named 'handlersocket_wr' and this option sets the timeout for it.
* Commandline: `<code>--handlersocket-wrlock-timeout="value"</code>`
* Scope: Global
* Dynamic: No
* Type: number
* Range: `<code>0</code>` to `<code>3600</code>``<code>
</code>`


