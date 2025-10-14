# Deployment

Created by Stefan Hinz · Last modified by Egor Ustinov on Oct 13, 2025

## Deployment

This section provides an overview of the deployment process for MariaDB Enterprise Manager, covering installation and upgrades for both the central server and the monitoring agents.

MariaDB Enterprise Manager is designed for a streamlined deployment experience. You can launch the main server with a single-line command for a quick start, and a UI-integrated helper tool simplifies the process of installing and registering agents on your monitored databases.

### Installing the Enterprise Manager Server

The Enterprise Manager Server is a Docker-based application installed on a dedicated host. The installation is handled by the installer script, which pulls the necessary container images and starts the application.

As a first step review the hardware, system, and network requirements:

* [Hardware and System Requirements](broken-reference)
* [Network and Firewall Requirements](broken-reference)

After confirming your hardware, system, and network are compliant, proceed with the installation instructions: [Installing MariaDB Enterprise Manager](broken-reference)

### Installing Enterprise Manager Agents

Agents are installed on each MariaDB Server and MaxScale host you wish to monitor. Use the Enterprise Manager UI to add database topology and to generate an agent setup command that will contain a proper set of labels for the metrics coming from monitored instances.

### Quick start

{% hint style="info" %}
You can quickly set up and launch MariaDB Enterprise Manager with a single-line command. This allows you to start exploring its capabilities without extensive configuration.

Enterprise Manager includes a helper tool, integrated in the UI, for adding agents. The helper prompts you to download a small (< 50M) binary and then provides command-line instructions to install and register agents, enabling quick and seamless addition of new MariaDB databases to Enterprise Manager.
{% endhint %}

### This section describes

* Installing MariaDB Enterprise Manager
* Installing agents
* Upgrading Enterprise Manager Server
* Upgrading agents
