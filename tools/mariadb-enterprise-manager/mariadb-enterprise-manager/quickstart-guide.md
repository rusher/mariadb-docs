# Quickstart Guide

Created by Stefan Hinz, last modified by Egor Ustinov on Oct 13, 2025

MariaDB Enterprise Manager is a database management and observability solution that provides advanced topology-aware monitoring coupled with visual schema management, query editing, and ERD design across multiple database connections.

This guide describes steps to install MariaDB Enterprise Manager for evaluation purposes.

Prerequisites

* Prepare a machine for Enterprise Manager installation that complies with the following requirements:
  * Minimal hardware resources (for evaluation setup):
    * CPU: 2 cores (or 2 vCPUs) with x86-64 architecture
    * RAM: 4 GB
    * Storage: 100 GB
  * 64-bit Linux OS with installed Docker engine and Docker compose: https://docs.docker.com/engine/install/
  * Network ports 8090 and 4318 are opened for inbound traffic
* Obtain MariaDB Customer Download Token:
  * Navigate to the Customer Download Token at the MariaDB Customer Portal: https://customers.mariadb.com/downloads/token/
  * Log in using your MariaDB ID: https://id.mariadb.com/
  * Copy the Customer Download Token to use as the password when logging in to the MariaDB Enterprise Docker Registry
* Setup MariaDB Enterprise Repository - `MariaDB Tools` for each monitored MariaDB Server and MaxScale:
  * https://mariadb.com/docs/server/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage

{% stepper %}
{% step %}
### Install Enterprise Manager

* Login to the MariaDB Enterprise Docker Registry providing your MariaDB ID as a username and Customer Download Token as a password:

{% code title="Login to Docker registry" %}
```bash
docker login docker.mariadb.com
```
{% endcode %}

* Insert your Customer Download Token into the download URL and download the installation script (replace \<Customer\_Download\_Token> with your token):

```

</div>

- Install Enterprise Manager following default options:

<div data-gb-custom-block data-tag="code">
./install-enterprise-manager.sh
```

* Setup agent on every MaxScale and MariaDB server with the command generated individually per MaxScale and MariaDB Server in Enterprise Manager UI:
  * Click the three dots beside the server or MaxScale instance you want to install the Agent on and click Install Agent.
  * The UI will generate a unique setup command for that specific server/MaxScale instance with the username and password you provide. Copy the command.
  * On that specific server, paste and run the command in your terminal.
  * Repeat the steps for all the MaxScale and MariaDB servers.
* Wait 1–2 minutes until metrics start populating in Enterprise Manager from agents (default collection interval is 1 minute).
{% endstep %}
{% endstepper %}

Attachments

* &#x20;[image-20250930-112426.png](broken-reference) (image/png)
* &#x20;[image-20250930-113014.png](broken-reference) (image/png)
* &#x20;[image-20250930-113158.png](broken-reference) (image/png)
* &#x20;[image-20250930-115151.png](broken-reference) (image/png)
* &#x20;[image-20250930-115309.png](broken-reference) (image/png)
* &#x20;[image-20250930-115500.png](broken-reference) (image/png)
* &#x20;[image-20250930-121005.png](broken-reference) (image/png)
* &#x20;[image-20250930-121629.png](broken-reference) (image/png)
* &#x20;[image-20250930-121750.png](broken-reference) (image/png)
