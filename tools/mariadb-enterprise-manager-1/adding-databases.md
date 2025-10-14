# Adding Databases

Created by Stefan Hinz, last modified by Egor Ustinov on Oct 13, 2025

This is the final draft.

## Adding Databases to MariaDB Enterprise Manager

This guide outlines the two primary methods for registering and monitoring your database topologies in MariaDB Enterprise Manager: adding a standalone server directly or adding a full cluster via its MaxScale instance.

***

## Option 1: Adding a Server or Cluster (Without MaxScale)

Use this method for a single MariaDB Server or to manually define a Primary/Replica or Galera cluster.

{% stepper %}
{% step %}
### Prepare Your Server(s)

First, perform these actions on each MariaDB Server you plan to add.

* Install the Agent package.

{% code title="RHEL / CentOS / Rocky" %}
```bash
# For Red Hat/CentOS/Rocky
sudo dnf install -y mema-agent
```
{% endcode %}

{% code title="Debian / Ubuntu" %}
```bash
# For Debian/Ubuntu
sudo apt install -y mema-agent
```
{% endcode %}

* Create the Enterprise Manager user (allows the Enterprise Manager server to connect remotely):

```sql
CREATE USER 'monitor'@'<Enterprise_Manager_IP>' IDENTIFIED BY '<password>';
GRANT REPLICA MONITOR ON *.* TO 'monitor'@'<Enterprise_Manager_IP>';
```

Replace `<Enterprise_Manager_IP>` with the IP of your Enterprise Manager server and `<password>` with a secure password.

* Create the Local Agent user (required for the agent to collect detailed metrics from the local database instance):

```sql
CREATE USER 'monitor'@'localhost' IDENTIFIED BY '<password>';
GRANT PROCESS, BINLOG MONITOR, REPLICA MONITOR, REPLICATION MASTER ADMIN ON *.* TO 'monitor'@'localhost';
```

Replace `<password>` with a secure password.
{% endstep %}

{% step %}
### Register in the UI

1. Go to your MariaDB Enterprise Manager web interface (for example `https://<Enterprise_Manager_IP>:8090`).
2. Log in (default credentials: `admin` / `mariadb`).
3. Begin the Add Database process:
   * If this is your first time and no databases are present, you'll be on the "Add Database" screen automatically.
   * If you already have other databases, click the **+ Add Database** button.
4. Ensure the **Database without MaxScale** option is selected.
5. Fill in the connection details for your first server using the Enterprise Manager User (`'monitor'@'<Enterprise_Manager_IP>'`).

At this point you have a choice:

* To add a Standalone Server: Click **Add** and proceed to the next step.
* To create a Cluster:
  * Click the Plus icon (+) to add another server node.
  * Fill in the connection details for the second server in your cluster and click **Confirm**. Repeat for all nodes in your cluster.
  * Once all nodes are added, select the Topology Type (e.g., Primary/Replica — default — or Galera Cluster) and click **Confirm**.

To convert an existing standalone server into a cluster: click the three-dot menu (⋮) next to the server, choose **Edit**, and click the Plus icon (+). Then follow the same steps to add nodes.
{% endstep %}

{% step %}
### Link the Agent(s) 🔗

For each server added, link its agent:

1. Find the server in the inventory list, click the three-dot menu (⋮), and select **Install Agent**.
2. Enter the credentials for the Local Agent User (`'monitor'@'localhost'`) to generate a setup command.
3. Copy the command and run it on that server's terminal to link the agent.
{% endstep %}
{% endstepper %}

***

## Option 2: Adding a Cluster (With MaxScale)

Use this method to add a complete primary/replica or Galera cluster that is managed by one or more MaxScale instances.

{% stepper %}
{% step %}
### Prepare All Servers in the Topology

Perform these actions on every server in the topology: the MaxScale instance(s) and each backend MariaDB Server attached.

* Install the Agent package on all servers.

{% code title="RHEL / CentOS / Rocky" %}
```bash
# For Red Hat/CentOS/Rocky
sudo dnf install -y mema-agent
```
{% endcode %}

{% code title="Debian / Ubuntu" %}
```bash
# For Debian/Ubuntu
sudo apt install -y mema-agent
```
{% endcode %}

* Create a Local Agent user on each backend MariaDB Server:

```sql
CREATE USER 'monitor'@'localhost' IDENTIFIED BY '<password>';
GRANT PROCESS, BINLOG MONITOR, REPLICA MONITOR, REPLICATION MASTER ADMIN ON *.* TO 'monitor'@'localhost';
```

Replace `<password>` with a secure password.
{% endstep %}

{% step %}
### Register the MaxScale Instance in the UI 🖥️

1. Begin the Add Database process:
   * If this is your first time and no databases are present, you'll be on the "Add Database" screen automatically.
   * If you already have other databases, click the **+ Add Database** button.
2. Select the **Database with MaxScale** option.
3. Provide the connection details for your MaxScale instance (IP address, API port `8989`, and its admin credentials).
4. Click **Add**. Enterprise Manager will connect to MaxScale and automatically discover all backend MariaDB servers it manages.
{% endstep %}

{% step %}
### Link All Agents 🔗

You must link the agent on every server in the topology to Enterprise Manager. The UI will show the MaxScale instance and discovered backend servers marked as "Not Registered."

For each server in the list (start with the MaxScale instance, then each MariaDB server):

1. Click the three-dot menu (⋮) and select **Install Agent**.
2. The UI will generate a unique setup command for that specific server with the username and password you provide. Copy the command.
3. On that specific server, paste and run the command in the terminal.

Repeat this process for every server in the topology. Once all agents are linked, the dashboard will begin showing the health and performance of the entire cluster.
{% endstep %}
{% endstepper %}

***

## Images / Attachments

(The images referenced above are attached in the original document and are kept with their original filenames and paths.)

* image-20251007-171506.png
* image-20251007-171533.png
* image-20251007-171712.png
* image-20251007-171917.png
* image-20251007-173016.png
* image-20251007-180005.png
* image-20251007-180227.png
* image-20251007-180519.png
* image-20251007-181434.png
* image-20251007-181531.png
* image-20251007-185513.png
* image-20251007-185616.png
* image-20251007-192342.png
* image-20251007-192407.png
* image-20251009-133647.png
* image-20251009-133727.png
* image-20251009-133819.png
* image-20251009-134324.png
* image-20251009-134517.png
* image-20251009-145512.png
* image-20251009-145641.png

Document generated by Confluence on Oct 13, 2025 16:28

Atlassian: http://www.atlassian.com/
