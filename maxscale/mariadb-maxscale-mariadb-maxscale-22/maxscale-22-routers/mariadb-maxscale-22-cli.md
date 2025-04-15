
# MaxScale 2.2 CLI

# CLI


The command line interface as used by `<code>maxadmin</code>`. The *CLI* router requires the
use of the `<code>maxscaled</code>` protocol.


## Configuration


Two components are required to run the command line interface for *maxadmin*; a
service and a listener. The listener may either use a Unix domain socket or an
internet socket.


The default entries required are shown below.



```
[CLI]
type=service
router=cli

# Unix Domain Socket
[CLI Unix Listener]
type=listener
service=CLI
protocol=maxscaled
socket=default

# Internet Socket
[CLI Inet Listener]
type=listener
service=CLI
protocol=maxscaled
address=localhost
port=6603
```



In the example above, two listeners have been specified; one that listens on the
default Unix domain socket and one that listens on the default port. In the
latter case, if the `<code>address=</code>` entry is removed, connections are allowed from
any machine on your network.


In the former case, if the value of `<code>socket</code>` is changed and in the latter case,
if the value of `<code>port</code>` is changed, *maxadmin* must be invoked with the `<code>-S</code>` and
`<code>-P</code>` options, respectively.


If Unix domain sockets are used, the connection is secure, but *maxadmin* can
only be used on the same host where MariaDB MaxScale runs. If internet sockets
are used, the connection is *inherently insecure* but *maxadmin* can be used
from another host than the one where MariaDB MaxScale runs.


Note that the latter approach is **deprecated** and will be removed in a future
version of MariaDB MaxScale.
