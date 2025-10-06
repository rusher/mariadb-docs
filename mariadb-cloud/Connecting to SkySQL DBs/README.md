---
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
---

# Connecting to MariaDB Cloud Databases

This page describes how to connect to a MariaDB Cloud database using a MariaDB-compatible client.

{% hint style="info" %}
**Whitelist IP Address**\
Access to all services is by default protected by a firewall. You need to IP whitelist your client’s (your desktop, laptop or server) IP. Select ‘Manage —> Security Access’ and then click ‘Add my current IP’ to add the IP of your current workstation (laptop, desktop).
{% endhint %}

{% hint style="danger" %}
**Warning**: Using `0.0.0.0/0` will disable the firewall. Never do this for production databases.\
For more details, go to the [Firewall](<../Security/Configuring Firewall.md>) settings page.
{% endhint %}

## Connecting Using the MariaDB Client

Once your DB service is launched, click on the ‘Connect’ option for your service on the dashboard. This pops up all the required attributes to connect from any SQL client.

Connection parameters include:

* Default username
* Default password
* Hostname (Fully Qualified Domain Name)
* TCP port (3306 or 3307)
* ssl-verify-server-cert (if SSL is ON)

{% hint style="info" %}
Unlike previous MariaDB Cloud versions, the current version no longer requires clients to supply the Server SSL Certificate for SSL connections. Customers who migrated from MariaDB corporation to MariaDB Cloud Inc can continue to use provided certificates (when using the previous MariaDB Cloud method for connecting). But, we strongly recommend moving to the connection properties as shown in the Connect window for your service.
{% endhint %}

{% hint style="warning" %}
There is a default config change in the 11.4.2 MariaDB client that requires SSL. This needs to be disabled by setting `--ssl-verify-server-cert=0`.
{% endhint %}

<figure><img src="connect_window.png" alt=""><figcaption></figcaption></figure>

### Install and Connect Using the MariaDB Client

After [installing the MariaDB client](<Connect using MariaDB CLI.md>) according to your operating system, copy and paste the MariaDB  command as displayed in the Connect window.

## Connecting From Your Application

Applications can connect to MariaDB Cloud using any of the below MariaDB supported connectors. There are several other connectors from the community too.

* [C](<Connect from ‘C’ App.md>)
* [C++](<Connect from ‘C++’ App.md>)
* [Java](<Connect from Java App.md>)
* [Java R2DBC](<Connect using Connector R2DBC.md>)
* [Node.js (JavaScript)](<Connect from Node js App.md>)
* [ODBC API](<Connect using ODBC.md>)
* [Python](<Connect from Python App.md>)
* [MongoDB Client](<Connect from MongoDB clients.md>)

{% hint style="info" %}
For Server With Replicas, you can also use any MongoDB client and use the [NoSQL Interface](<Connect from MongoDB clients.md>).
{% endhint %}

## Connecting From SQL Tools

Clients listed here have been tested to properly connect with MariaDB Cloud and execute queries.

Most of the SQL clients and editors natively support MariaDB. Most often you can also just select 'MySQL' and connect to your MariaDB Cloud DB service.

* [Connecting using Java clients like Squirrel SQL](https://squirrel-sql.sourceforge.io/)
  * All you need to do is to make sure the "useSsl" property is set to 'true' if SSL is ON.
* MariaDB CLI
* [Sequel Ace](https://sequel-ace.com/) - Connect to MariaDB from MacOS
  * In the connection window, you should select 'Require SSL' if your MariaDB Cloud database has SSL turned ON (the default).

### Graphical User Interfaces (GUIs)

The following GUI clients have been tested to properly connect with MariaDB Cloud and execute queries. Most SQL clients and editors natively support MariaDB. You can often select 'MySQL' as the connection type to connect to your MariaDB Cloud DB service.

* [Connect using DBeaver](../Integrations/DBeaver.md) (CloudDBA recommended)
* [Connect using DBGate](../Integrations/DBGate.md)
* [Connect using HeidiSQL](../Integrations/HeidiSQL.md)
* [Connect using TablePlus](../Integrations/TablePlus.md)
