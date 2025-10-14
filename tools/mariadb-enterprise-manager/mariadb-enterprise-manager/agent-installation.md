# Agent installation

Created by Egor Ustinov, last modified by Esa Korhonen on Oct 06, 2025

## Agent Installation and Setup With Package Manager

* Instructions to install and register agent on MariaDB and MaxScale servers with package manager from repositories.
* Documentation of parameters (Metrics collection frequency, Open Telemetry destination endpoint configuration to export metrics to 3rd party monitoring, SSL certificate, etc.)

Install the MariaDB Enterprise Manager Agent from the MariaDB Enterprise repository. First, if the MariaDB enterprise repository is not yet installed, install it with the repository setup script as described here: https://mariadb.com/docs/server/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage. Follow the instructions for `mariadb_es_repo_setup`.

{% stepper %}
{% step %}
### Repository setup

If the MariaDB Enterprise repository is not installed yet, run the repository setup script as described in the link above and follow the steps for `mariadb_es_repo_setup`.
{% endstep %}

{% step %}
### Install the mema-agent package

Install the mema-agent package using your distribution's package manager.

{% tabs %}
{% tab title="Ubuntu / Debian" %}
Run:

{% code title="Install on Debian/Ubuntu" %}
```bash
apt-get install mema-agent
```
{% endcode %}
{% endtab %}

{% tab title="RHEL / Rocky" %}
Run:

{% code title="Install on RHEL/Rocky" %}
```bash
yum install mema-agent
```
{% endcode %}
{% endtab %}
{% endtabs %}

Note: the original documentation lists other package manager options with "and …?" — follow your distribution-specific instructions if different.
{% endstep %}

{% step %}
### Register and configure the agent

After installation, register and configure the agent according to your environment and the MariaDB Enterprise Manager instructions. Configure parameters such as:

* Metrics collection frequency
* Open Telemetry destination endpoint for exporting metrics to third-party monitoring
* SSL certificate settings
* Any other agent-specific parameters required by your deployment

Refer to the MariaDB Enterprise Manager documentation for exact configuration file locations and available options.
{% endstep %}
{% endstepper %}

## Agent Installation With Binary

Prerequisite for setting up agent for MariaDB Server

{% hint style="info" %}
A MariaDB user must be created with the required permissions for the agent to collect metrics.
{% endhint %}

Create the user and grant permissions:

{% code title="MariaDB SQL" %}
```sql
CREATE USER 'monitor'@'localhost' IDENTIFIED BY '<password>';
GRANT SELECT, PROCESS, REPLICATION CLIENT, RELOAD, REPLICA MONITOR, REPLICATION MASTER ADMIN ON *.* TO 'monitor'@'localhost';
```
{% endcode %}

## Attachments

&#x20;(image/png)
