# Galera Load Balancer (glb)

{% hint style="danger" %}
Not Recommended for New Deployments

This page is provided for historical and reference purposes only. The Galera Load Balancer (`glb`) is a simple TCP proxy that is no longer under active development and is not included in MariaDB packages. It lacks the advanced, database-aware features of modern proxies.

For new production deployments, we strongly recommend using a modern, fully supported solution like MariaDB MaxScale, ProxySQL, or HAProxy.
{% endhint %}

Galera Load Balancer (`glb`) is a simple, lightweight TCP load balancer specifically designed for Galera Cluster. It runs on Linux.

Inspired by Pen, `glb` is optimized for database workloads. A lightweight daemon called `glbd` receives connections from clients and redirects them to the backend MariaDB nodes. Several balancing policies are supported, and each node can be assigned a different weight to influence routing decisions.

Features

* Runtime-configurable list of backend servers.
* Supports server "draining" to allow existing connections to finish gracefully.
* Multi-threaded to utilize multiple CPU cores.
* Optional watchdog module to monitor backend node health.
* Includes `libglb`, a shared library to provide balancing to any application using the standard `connect()` call.

### Installation from Source

The `glb` utility is not typically available in standard package repositories and must be compiled from source.

1.  Install Prerequisite Packages: Ensure you have the necessary build tools on your system.

    ```bash
    # On Debian/Ubuntu
    sudo apt-get install git autoconf automake libtool gcc g++

    # On Red Hat/CentOS
    sudo yum install git autoconf automake libtool gcc-c++
    ```
2.  Clone the Repository: From a suitable directory (e.g., `/usr/local/src`), clone the source code from GitHub.

    ```bash
    git clone https://github.com/codership/glb
    ```
3.  Bootstrap and Configure: Navigate into the new `glb` directory and run the bootstrap and configure scripts.

    ```bash
    cd glb/
    ./bootstrap.sh
    ./configure
    ```
4.  Compile and Install: Build the application and install it. This will typically place the `glbd` binary in `/usr/local/sbin/`.

    ```bash
    make
    sudo make install
    ```

### Configuration

You can configure `glb` in two ways: through a configuration file when running it as a service, or directly with command-line options.

#### Using a Configuration File (for Service Management)

This method is used when you want to run `glbd` as a system service.

1.  Copy Service Files: From the `files` directory within the cloned source code, copy the `glbd.sh` script to `/etc/init.d/` and the `glbd.cfg` file to the appropriate location:

    * Red Hat/CentOS: `/etc/sysconfig/glbd`
    * Debian/Ubuntu: `/etc/default/glbd`

    ```bash
    sudo cp files/glbd.sh /etc/init.d/glb
    sudo cp files/glbd.cfg /etc/sysconfig/glbd  # For Red Hat systems
    ```
2.  Edit the Configuration File: Edit the configuration file (e.g., `/etc/sysconfig/glbd`) to define your cluster.

    | Parameter         | Description                                                         |
    | ----------------- | ------------------------------------------------------------------- |
    | `LISTEN_ADDR`     | The local IP address and/or port that `glb` will listen on.         |
    | `DEFAULT_TARGETS` | A space-separated list of backend MariaDB nodes (`IP:PORT:WEIGHT`). |
    | `OTHER_OPTIONS`   | Any additional command-line options (e.g., `--random`).             |

    Example `/etc/sysconfig/glbd`:

    ```toml
    # Address for clients to connect to
    LISTEN_ADDR="3307"

    # List of backend MariaDB nodes
    DEFAULT_TARGETS="192.168.1.10:3306 192.168.1.11:3306 192.168.1.12:3306"

    # Additional command-line options
    OTHER_OPTIONS="--leastconn"
    ```

#### Using Command-Line Options

You can also run `glbd` directly from the command line, passing all configuration as arguments. See the output of `glbd --help` for a full list of options.

Example:

```bash
/usr/local/sbin/glbd --address=10.0.1.10,10.0.1.11 \
                     --port=3307 \
                     --policy=leastconn \
                     --daemon
```

### 4. Balancing Policies

`glb` supports several balancing policies:

| Policy       | Description                                                                       |
| ------------ | --------------------------------------------------------------------------------- |
| `leastconn`  | New connections are sent to the server with the fewest active connections.        |
| `roundrobin` | Connections are distributed to each server in a circular order.                   |
| `single`     | All connections are sent to the single healthiest server with the highest weight. |
| `random`     | Connections are distributed randomly.                                             |
| `source`     | Connections from the same source IP are routed to the same backend server.        |

### 5. Service Management

If you have installed `glb` as a service, you can manage it using the `service` or `systemctl` command.

| Command                                 | Description                                                                                  |
| --------------------------------------- | -------------------------------------------------------------------------------------------- |
| `sudo service glb start`                | Starts the `glb` service.                                                                    |
| `sudo service glb stop`                 | Stops the `glb` service.                                                                     |
| `sudo service glb restart`              | Restarts the `glb` service.                                                                  |
| `sudo service glb status`               | Checks the current running status of the service.                                            |
| `sudo service glb getinfo`              | Displays the current routing table and connection statistics.                                |
| `sudo service glb add <IP:PORT:WEIGHT>` | Adds a new node to the routing table.                                                        |
| `sudo service glb drain <IP:PORT>`      | Drains a node, preventing new connections while allowing existing ones to finish gracefully. |
| `sudo service glb remove <IP:PORT>`     | Immediately removes a node from the routing table and closes all active connections to it.   |

