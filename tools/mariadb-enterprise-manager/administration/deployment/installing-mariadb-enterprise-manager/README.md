# Installing MariaDB Enterprise Manager

{% hint style="info" %}
Prerequisites

* Prepare a machine for Enterprise Manager installation that complies with [Hardware and System Requirements](../hardware-and-system-requirements.md)
* Make sure that you have required network ports opened: [Network and Firewall Requirements](../hardware-and-system-requirements.md)
* Obtain MariaDB Customer Download Token
  * Navigate to the [Customer Download Token at the MariaDB Customer Portal](https://customers.mariadb.com/downloads/token/)
  * Log in using your [MariaDB ID](https://id.mariadb.com/)
  * Copy the Customer Download Token to use as the password when logging in to the MariaDB Enterprise Docker Registry
* Setup MariaDB Enterprise Repository - `MariaDB Tools` for each monitored MariaDB Server and MaxScale
  * https://mariadb.com/docs/server/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage
{% endhint %}

{% stepper %}
{% step %}
### Login to Docker registry

Login to the MariaDB Enterprise Docker Registry providing your [MariaDB ID](https://id.mariadb.com/) as a username and Customer Download Token as a password:

{% code title="# Login" %}
```bash
docker login docker.mariadb.com
```
{% endcode %}
{% endstep %}

{% step %}
### Download the installation script

Insert your Customer Download Token into the download URL and download the installation script:

{% code title="# Download installer" %}
```bash
wget https://dlm.mariadb.com/<Customer_Download_Token>/enterprise-release-helpers/install-enterprise-manager.sh
```
{% endcode %}
{% endstep %}

{% step %}
### Make the installer executable

{% code title="# Make executable" %}
```bash
chmod +x install-enterprise-manager.sh
```
{% endcode %}
{% endstep %}

{% step %}
### Run the installer

Install Enterprise Manager by running the script:

{% code title="# Run installer" %}
```bash
./install-enterprise-manager.sh
```
{% endcode %}

The script will ask for the IP address/hostname and port on which Enterprise Manager should listen for incoming connections. Input the correct address if the auto-detected value is incorrect. The address and port combination should be reachable from all monitored MariaDB Servers and MaxScales. The script will also launch Enterprise Manager.
{% endstep %}

{% step %}
### Verify containers

Run `docker compose ps` in the `enterprise-manager` directory to check that all of the constituent Docker containers are running. The containers are:

* `enterprise-manager-grafana`
* `enterprise-manager-nginx`
* `enterprise-manager-otelcol`
* `enterprise-manager-prometheus`
* `enterprise-manager-supermax`

{% code title="# Check containers" %}
```bash
cd enterprise-manager
docker compose ps
```
{% endcode %}
{% endstep %}

{% step %}
### Access the UI

Access Enterprise Manager UI at:

https://`<Enterprise_Manager_IP>`:8090

At the login screen, use default username `admin` and password `mariadb`.
{% endstep %}
{% endstepper %}

The installer generates a self-signed TLS certificate for Enterprise Manager. To change the certificate, follow instructions at [Security in Enterprise Manager](../../security-in-enterprise-manager.md).

To modify metrics retention time, see [Metrics retention configuration](metrics-retention-configuration.md).

## Enterprise Manager Server Air-Gapped Installation

Installing Enterprise Manager to a machine without an Internet connection is possible by manually copying the Docker images and related settings from an Internet-connected machine to the final target machine.

Follow these steps:

{% stepper %}
{% step %}
### Install on an Internet-connected machine

First, install Enterprise Manager on an Internet-connected machine as explained in the normal installation section. When the installation script asks for the address and port that Enterprise Manager should listen at for incoming connections, enter the values for the final target machine.
{% endstep %}

{% step %}
### Save images and settings

Once installation is complete, save all related Docker images and settings by running the following commands from the directory that contains the `enterprise-manager` folder:

{% code title="# Save images and archive" %}
```bash
cd enterprise-manager
docker image save -o grafana.tar docker.io/grafana/grafana:12.1
docker image save -o prometheus.tar docker.io/prom/prometheus:v3.5.0
docker image save -o otelcol.tar docker.io/otel/opentelemetry-collector-contrib:0.135.0
docker image save -o supermax.tar docker.mariadb.com/supermax:<version>  # (NEED FINAL TAG)
docker image save -o nginx.tar docker.io/nginx:1.29
cd ..
tar -czvf enterprise-manager.tar.gz enterprise-manager
```
{% endcode %}

The resulting archive `enterprise-manager.tar.gz` contains all components of Enterprise Manager.
{% endstep %}

{% step %}
### Transfer archive to target machine

Copy `enterprise-manager.tar.gz` to the target (air-gapped) machine into the directory under which you want to install Enterprise Manager.
{% endstep %}

{% step %}
### Extract and load images on target machine

On the target machine, extract the archive and load the Docker images:

{% code title="# Extract and load images" %}
```bash
tar -xzvf enterprise-manager.tar.gz
cd enterprise-manager
docker image load -i grafana.tar
docker image load -i prometheus.tar
docker image load -i otelcol.tar
docker image load -i supermax.tar
docker image load -i nginx.tar
```
{% endcode %}
{% endstep %}

{% step %}
### Start Enterprise Manager

Start Enterprise Manager with:

{% code title="# Start containers" %}
```bash
docker compose up -d
```
{% endcode %}
{% endstep %}
{% endstepper %}
