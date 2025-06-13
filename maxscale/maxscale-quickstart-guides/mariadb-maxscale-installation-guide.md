---
description: MariaDB MaxScale installation quickstart guide
---

# MariaDB MaxScale Installation Guide

### Quickstart Guide: MariaDB MaxScale

MariaDB MaxScale is an advanced, open-source database proxy that provides intelligent routing, load balancing, high availability, and security features for your MariaDB and MySQL deployments. It acts as an intermediary, forwarding database statements to one or more backend database servers based on configured rules and server roles, all transparently to your applications.

#### 1. Key Concepts

To understand MaxScale, familiarize yourself with these core components:

* **Servers:** These are your backend MariaDB or MySQL instances that MaxScale will manage traffic to.
* **Monitors:** Plugins that observe the health and state of your backend servers (e.g., primary, replica, down).
* **Routers:** Plugins that determine how client queries are directed to backend servers (e.g., `readwritesplit` router for directing writes to a primary and reads to replicas).
* **Services:** Define a combination of a router and a set of servers, along with any filters.
* **Listeners:** Define how clients connect to MaxScale (port, protocol) and which service they connect to.
* **Filters:** Optional components that can inspect, modify, or log queries as they pass through MaxScale (e.g., `qlafilter` for auditing).

#### 2. Installation

MariaDB MaxScale is typically installed from the official MariaDB repositories.

**a. Add MariaDB Repository:**

Use the MariaDB Repository Configuration Tool (search "MariaDB Repository Generator") to get specific instructions for your OS and MaxScale version.

**Example for Debian/Ubuntu (MaxScale 23.08):**

```bash
sudo apt update
sudo apt install dirmngr software-properties-common apt-transport-https ca-certificates curl -y
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash
sudo apt update
```

**b. Install MaxScale:**

```bash
sudo apt install maxscale -y # For Debian/Ubuntu
# sudo yum install maxscale -y # For RHEL/CentOS
```

#### 3. Basic Configuration (`maxscale.cnf`)

MaxScale's configuration is primarily done in its main configuration file, typically `/etc/maxscale.cnf`.

**a. Define Servers:**

Add a section for each of your backend MariaDB servers.

```ini
[server1]
type=server
address=192.168.1.101 # IP address or hostname of your first MariaDB server
port=3306
protocol=MariaDBBackend

[server2]
type=server
address=192.168.1.102 # IP address or hostname of your second MariaDB server
port=3306
protocol=MariaDBBackend
```

**b. Define a Monitor:**

This section tells MaxScale how to monitor your backend servers' health and roles.

```ini
[MariaDB-Monitor]
type=monitor
module=mariadbmon # Standard MariaDB monitoring module
servers=server1,server2 # List of servers to monitor
user=maxscale_monitor # A MariaDB user with REPLICATION SLAVE privilege
password=monitor_password
monitor_interval=5000 # Check every 5 seconds
```

**Important:** Create the `maxscale_monitor` user on your _backend MariaDB servers_ with appropriate privileges (e.g., `GRANT REPLICATION SLAVE ON *.* TO 'maxscale_monitor'@'%' IDENTIFIED BY 'monitor_password';`).

**c. Define a Service (e.g., Read-Write Split):**

This configures how MaxScale routes queries. The readwritesplit router is very common for replication setups.

```ini
[Read-Write-Service]
type=service
router=readwritesplit # Use the read-write split router
servers=server1,server2 # Servers available for this service
user=maxscale_user # A MariaDB user your applications will use to connect THROUGH MaxScale
password=application_password
# router_options= ... (optional router-specific settings)
```

**Important:** Create the `maxscale_user` on your _backend MariaDB servers_ with the privileges your application needs.

**d. Define a Listener:**

This specifies the port and protocol MaxScale will listen on for incoming client connections and which service to direct them to.

```ini
[Read-Write-Listener]
type=listener
service=Read-Write-Service # Link to the service defined above
protocol=MariaDBClient # MaxScale listens as a MariaDB client
port=3307 # MaxScale will listen on port 3307 for applications
```

**e. Basic MaxScale Configuration (at the top of `maxscale.cnf`):**

```ini
[maxscale]
threads=4 # Number of worker threads
# Other global settings
```

#### 4. Start and Enable MaxScale

After configuring `maxscale.cnf`, start and enable the MaxScale service.

```bash
sudo systemctl start maxscale
sudo systemctl enable maxscale
sudo systemctl status maxscale # Check status
```

#### 5. Basic Usage and Verification

Once MaxScale is running, configure your applications to connect to MaxScale's listener port (e.g., `localhost:3307`) instead of directly to a MariaDB server.

**Example (Connect with `mariadb` client):**

```bash
mariadb -h 127.0.0.1 -P 3307 -u maxscale_user -p
```

* `maxscale_user` should be the user defined in your MaxScale `[Read-Write-Service]` section.

**Verify Read-Write Split (if configured):**

1. Connect to MaxScale (`127.0.0.1:3307`).
2. Execute a `WRITE` query (e.g., `INSERT INTO your_table ...`). This should be routed to the primary server.
3. Execute a `READ` query (e.g., `SELECT * FROM your_table`). This should be load-balanced across your replica servers.
4. You can use `maxctrl show sessions` or `maxctrl show servers` to observe routing in action.

#### Further Resources:

* [MariaDB MaxScale Installation Guide](https://www.google.com/search?q=https://mariadb.com/docs/maxscale/latest/install/\&authuser=1)
* [MariaDB MaxScale Configuration Guide](https://www.google.com/search?q=https://mariadb.com/docs/maxscale/latest/config/\&authuser=1)
* [MariaDB MaxScale GitHub Repository](https://github.com/mariadb-corporation/MaxScale)
* [DigitalOcean: How To Install and Configure MariaDB MaxScale (Tutorial)](https://www.google.com/search?q=https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-mariadb-maxscale-on-ubuntu-22-04\&authuser=1)
