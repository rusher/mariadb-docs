---
description: >-
  MariaDB Exa deployment options and the production install order: configure
  MariaDB Server, install local storage Exasol, then connect MariaDB MaxScale
  with CDC.
icon: wrench
---

# Deployment

You can deploy MariaDB Exa in one of the following ways.

## Proof of Concept via Docker or Community Exasol

For testing or proof-of-concept environments, Exasol can be deployed (via Docker or Virtual Box with an OVA file).

This mode simplifies setup, but does not provide MPP[^1] benefits, high availability or real performance testing. These options are limited to using 2 VCPU[^2]s and 200G of data, and come with MariaDB's CDC[^3] solution and MaxScale integration.

## Clustered MPP Deployment

In production, MariaDB Exa is deployed as a cluster of nodes.

* Minimum 3 node deployments of 16 VCPUs, 256 GB RAM nodes.
* Optional standby nodes for High Availability.

Data is automatically distributed across nodes, using MariaDB Exa internal partitioning and replication for fault tolerance.

## Production Install

A complete MariaDB Exa deployment has three parts. Install and configure them in the following order.

1. [Install and configure MariaDB Server](#id-1.-install-and-configure-mariadb-server)
2. [Install and configure local storage Exasol](#id-2.-install-and-configure-local-storage-exasol)
3. [Install and configure MariaDB MaxScale with CDC](#id-3.-install-and-configure-mariadb-maxscale-with-cdc)

### 1. Install and configure MariaDB Server

MariaDB Server is the transactional front end for the deployment. Install it and apply your baseline configuration first.

* [Installing MariaDB Server Guide]({server}/mariadb-quickstart-guides/installing-mariadb-server-guide)
* [Configuring MariaDB with Option Files]({server}/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files)

### 2. Install and configure local storage Exasol

This section installs a single-node MariaDB Exa instance using local storage.

{% hint style="info" %}
MariaDB Exa is powered by [Exasol](https://www.exasol.com/), and the local-storage install follows Exasol's on-premise C4 deployment. For upstream reference, see Exasol's [on-premise installation guide](https://docs.exasol.com/db/latest/administration/on-premise/installation.htm) and [c4 parameter reference](https://docs.exasol.com/db/latest/administration/on-premise/c4/c4_parameters.htm).
{% endhint %}

**Prerequisites:**

* Ubuntu 22.04+ or RHEL 8+. Other Linux distributions might work, but are not tested or guaranteed.
* A static public IP address. Without one, the deployment will not work after a restart.
* Open ports: `8563` (default database port) and `8443` (admin UI).

#### Step 1: Prepare the jump host

SSH to the machine and update the existing packages. This can be the MaxScale machine.

```bash
ssh ubuntu@<JUMPHOST_IP>
```

Update and install the required packages:

```bash
sudo apt update -y
sudo apt full-upgrade -y
sudo apt install rsync ssh uuid-runtime wget curl git python3-pip byacc flex zip unzip jq -y
sudo apt full-upgrade -y
sudo reboot now
```

#### Step 2: Configure an SSH key for node access

On your jump host, create an SSH key pair and add the public key to the target instance where you will install Exasol.

```bash
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub
```

Add the public key to `authorized_keys`:

```bash
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

Check the permissions:

```bash
ls -la ~/.ssh/
# if needed: chmod 400 ~/.ssh/<key>.pem
```

Check that SSH works from the jump host to the Exasol node:

```bash
ssh ubuntu@<EXASOL_NODE_IP>
```

{% hint style="info" %}
Confirm that port `20002` is open. You may also need to add the SSH public key to the target's root `authorized_keys`.
{% endhint %}

#### Step 3: Download the Exasol C4 installer

{% hint style="warning" %}
MariaDB recommends running the C4 installer as a non-`root` user (as of February 2026). Exasol's default install is root-based, with an optional [rootless deployment](https://docs.exasol.com/db/latest/administration/on-premise/installation/install_rootless.htm) that requires extra per-host setup.
{% endhint %}

```bash
cd ~
wget https://x-up.s3.amazonaws.com/releases/c4/linux/x86_64/4.28.4/c4 -O c4
chmod +x c4
```

#### Step 4: Create the C4 configuration

```bash
mkdir ~/.ccc
vi ~/.ccc/config
```

Paste the following:

```ini
CCC_HOST_ADDRS=<HOST_PRIVATE_IP>
CCC_HOST_EXTERNAL_ADDRS=<HOST_PUBLIC_IP>
CCC_HOST_DATADISK=/dev/nvme1n1
CCC_HOST_IMAGE_USER=ubuntu
CCC_HOST_IMAGE_PASSWORD=
CCC_HOST_KEY_PAIR_FILE=id_rsa
CCC_PLAY_WORKING_COPY=@exasol-2025.1.8
CCC_PLAY_DATABASE_NAME=exa-analytics
CCC_PLAY_DB_PASSWORD="<DB_PASSWORD>"
CCC_PLAY_ADMIN_PASSWORD="<ADMIN_PASSWORD>"
CCC_ADMINUI_START_SERVER=true
CCC_HOST_CLEANUP=false
```

You must update the following values:

1. `CCC_HOST_ADDRS` — your private IP address (a static public address is required):

    ```bash
    hostname -i
    ```
2. `CCC_HOST_EXTERNAL_ADDRS` — your public IP address:

    ```bash
    ifconfig -a
    # or
    curl 'https://api.ipify.org?format=json'
    ```
3. `CCC_HOST_DATADISK` — find the data disk with:

    ```bash
    lsblk
    ```
4. `CCC_HOST_IMAGE_USER` — usually `ubuntu` or another default user that exists on both the jump host and the Exasol node:

    ```bash
    whoami
    ```

{% hint style="warning" %}
Set strong, unique values for `CCC_PLAY_DB_PASSWORD` and `CCC_PLAY_ADMIN_PASSWORD`, and keep them secret. Do not commit real credentials to source control or share them in documentation.
{% endhint %}

#### Step 5: Validate the environment

Run diagnostics:

```bash
./c4 ps
```

#### Step 6: Deploy the Exasol cluster

```bash
./c4 host play -i .ccc/config
```

View the logs on the target machine:

```bash
tail -f .ccc/play/local/*/main/11/data/logs/cored/exainit.log
```

#### Step 7: Check the deployment stages

On the jump host, view the status:

```bash
./c4 ps
```

| Stage | Meaning |
| --- | --- |
| a | Infrastructure resources are being allocated; nothing is reachable yet |
| b | The host is booting and running startup scripts |
| c | The cluster operating system (COS) service is running and reachable |
| d | The database is running and reachable |

Wait until the deployment is complete. If you encounter errors that you cannot triage yourself, contact support.

#### Step 8: Configure Exasol

On the target machine, use `CCC_PLAY_DB_PASSWORD` from `.ccc/config` (on the jump host) to check the connection to Exasol.

```bash
sudo apt install openjdk-21-jdk
```

```bash
sudo find / -name *exaplus*
```

```bash
exaplus -c 127.0.0.1/nocertcheck:8563 -u sys -p <DB_PASSWORD>
```

{% hint style="info" %}
To retrieve the password from the jump host: `cat .ccc/config | grep -i PLAY_DB`
{% endhint %}

Set `SQL_IDENTIFIER_COMPARISON` to be case insensitive:

```sql
ALTER SYSTEM SET SQL_IDENTIFIER_COMPARISON = 'IGNORE CASE';
```

Import the MariaDB helper functions / UDF from [mariadb-compat.sql](https://github.com/mariadb-corporation/exasol-mariadb-compat/blob/main/dist/mariadb-compat.sql):

```bash
exaplus -c 127.0.0.1/nocertcheck:8563 -u sys -p <DB_PASSWORD> -f mariadb-compat.sql
```

#### Step 9: Upload the Exasol license

Each on-prem customer has their own license file.

Copy the license file:

```bash
scp <license_id>.exasol_license ubuntu@<JUMPHOST_IP>:/home/ubuntu/
```

Get `CLUSTER_ID` from the `play_id` column of `./c4 ps`, then upload the license:

```bash
cat <license_id>.exasol_license | ./c4 connect -s cos -i <CLUSTER_ID> -- \
  confd_client license_upload license: '\""{< -}\""'
```

Verify:

```bash
./c4 connect -t1.11/cos
confd_client license_info
```

To stop and start the database (the name comes from `CCC_PLAY_DATABASE_NAME`):

```bash
./c4 connect -t 1/cos
confd_client db_stop db_name: exa-analytics
confd_client db_start db_name: exa-analytics
```

#### Step 10: Access the admin UI

Open the following in a browser:

```
https://<PUBLIC_IP>:8443/login
```

Use these credentials:

* **Username:** `admin`
* **Password:** the value you set for `CCC_PLAY_ADMIN_PASSWORD`

### 3. Install and configure MariaDB MaxScale with CDC

MariaDB MaxScale uses the ExasolRouter to stream changes from MariaDB Server into Exasol via Change Data Capture (CDC).

* [MariaDB MaxScale ExasolRouter Tutorial]({maxscale}/mariadb-maxscale-tutorials/mariadb-maxscale-exasolrouter)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}

[^1]: Massive Parallel Processing — analytical database designed for fast, large-scale SQL analytics

[^2]: Virtual CPU

[^3]: Change Data Capture — scenarios for integrating MariaDB Exa for analytical workloads and data pipelines
