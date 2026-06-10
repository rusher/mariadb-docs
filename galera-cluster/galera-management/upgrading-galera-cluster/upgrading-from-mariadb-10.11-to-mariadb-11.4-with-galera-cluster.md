---
hidden: true
---

# Upgrading from MariaDB 10.11 to MariaDB 11.4 with Galera Cluster

ships with the MariaDB Server\[cite: 5, 6, 7, 8]. Upgrading a Galera Cluster node is very similar to upgrading a server from MariaDB 10.11 to MariaDB 11.4\[cite: 5, 6, 7]. For more information on that process as well as incompatibilities between versions, see the Upgrade Guide\[cite: 5, 6, 7, 8]. Performing a Rolling Upgrade The following steps can be used to perform a rolling upgrade from MariaDB 10.11 to MariaDB 11.4 when using Galera Cluster\[cite: 5, 6, 7, 8]. In a rolling upgrade, each node is upgraded individually, so the cluster is always operational\[cite: 5, 6, 7, 8]. There is no downtime from the application's perspective\[cite: 5, 6, 7, 8]. First, before you get started: First, take a look at Upgrading from MariaDB 10.11 to MariaDB 11.4 to see what has changed between the major versions\[cite: 5, 6, 7, 8]. Check whether any system variables or options have been changed or removed\[cite: 5, 6, 7, 8]. For example, the old\_alter\_table variable has been completely removed in MariaDB 11.x\[cite: 10]. Make sure that your server's configuration is compatible with the new MariaDB version before upgrading\[cite: 5, 6, 7, 8]. Check whether replication has changed in the new MariaDB version in any way that could cause issues while the cluster contains upgraded and non-upgraded nodes\[cite: 5, 6, 7, 8]. Check whether any new features have been added to the new MariaDB version\[cite: 5, 6, 7, 8]. If a new feature in the new MariaDB version cannot be replicated to the old MariaDB version, then do not use that feature until all cluster nodes have been upgraded to the new MariaDB version\[cite: 5, 6, 7, 8]. Next, make sure that the Galera version numbers are compatible\[cite: 5, 6, 7, 8]. If you are upgrading from standard releases of MariaDB 10.11 to MariaDB 11.4, note your specific maintenance version numbers. Both MariaDB 10.11 and 11.4 initially shipped with Galera 3\[cite: 5, 6, 7, 8]. However, Galera 4 (wsrep API 26) was introduced in maintenance releases starting with MariaDB 10.11.11 and MariaDB 11.4.5\[cite: 9, 10]. For the purposes of a rolling upgrade, ensure your versions align across these ecosystem baselines. See What is MariaDB Galera Cluster?: Galera wsrep provider Versions for information on which MariaDB releases use which Galera wsrep provider versions\[cite: 5, 6, 7, 8]. You want to have a large enough gcache to avoid a State Snapshot Transfer (SST) during the rolling upgrade\[cite: 5, 6, 7, 8]. The gcache size can be configured by setting gcache.size\[cite: 5, 6, 7, 8]. For example: wsrep\_provider\_options="gcache.size=2G"\[cite: 5, 6, 7, 8]. Before you upgrade, it would be best to take a backup of your database\[cite: 5, 6, 7, 8]. This is always a good idea to do before an upgrade\[cite: 5, 6, 7, 8]. We would recommend mariadb-backup\[cite: 5, 6, 7, 8]. Then, for each node, perform the following steps:

{% stepper %}
{% step %}
Modify the repository configuration, so the system's package manager installs MariaDB 11.4\[cite: 5, 6, 7, 8].

{% tabs %}
{% tab title="Debian, Ubuntu, ..." %}
see Updating the MariaDB APT repository to a New Major Release for more information\[cite: 5, 6, 7].
{% endtab %}

{% tab title="RHEL, CentOS, Fedora, ..." %}
see Updating the MariaDB YUM repository to a New Major Release for more information\[cite: 5, 6, 7, 8].
{% endtab %}

{% tab title="SLES, OpenSUSE, ..." %}
see Updating the MariaDB ZYpp repository to a New Major Release for more information\[cite: 5, 6, 7, 8].
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
If you use a load balancing proxy such as MaxScale or HAProxy, make sure to drain the server from the pool so it does not receive any new connections\[cite: 5, 6, 7, 8].
{% endstep %}

{% step %}
Stop MariaDB\[cite: 5, 6, 7, 8].
{% endstep %}

{% step %}
Uninstall the old version of MariaDB and the Galera wsrep provider\[cite: 5, 6, 7, 8].

{% tabs %}
{% tab title="Debian, Ubuntu, ..." %}
Bash sudo apt-get remove mariadb-server galera
{% endtab %}

{% tab title="RHEL, CentOS, Fedora, ..." %}
Bash sudo yum remove MariaDB-server galera
{% endtab %}

{% tab title="SLES, OpenSUSE, ..." %}
Bash sudo zypper remove MariaDB-server galera
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
Install the new version of MariaDB and the Galera wsrep provider\[cite: 5, 6, 7, 8].

{% tabs %}
{% tab title="Debian, Ubuntu, ..." %}
see Installing MariaDB Packages with APT for more information\[cite: 5, 6, 8].
{% endtab %}

{% tab title="RHEL, CentOS, Fedora, ..." %}
see Installing MariaDB Packages with YUM for more information\[cite: 5, 6, 7, 8].
{% endtab %}

{% tab title="SLES, OpenSUSE, ..." %}
see Installing MariaDB Packages with ZYpp for more information\[cite: 5, 6, 7, 8].
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
Make any desired changes to configuration options in option files, such as my.cnf\[cite: 5, 6, 7, 8]. This includes removing any system variables or options that are no longer supported\[cite: 5, 6, 7, 8].
{% endstep %}

{% step %}
On Linux distributions that use systemd you may need to increase the service startup timeout as the default timeout of 90 seconds may not be sufficient\[cite: 5, 6, 7, 8]. See Systemd: Configuring the Systemd Service Timeout for more information\[cite: 5, 6, 7, 8].
{% endstep %}

{% step %}
Start MariaDB\[cite: 5, 6, 7, 8].
{% endstep %}

{% step %}
Run mysql\_upgrade (or mariadb-upgrade) with the --skip-write-binlog option\[cite: 5, 6, 7, 8]. mysql\_upgrade does two things: Ensures that the system tables in the mysql database are fully compatible with the new version\[cite: 5, 6, 7, 8]. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB\[cite: 5, 6, 7, 8].
{% endstep %}
{% endstepper %}

When this process is done for one node, move onto the next node\[cite: 5, 6, 7, 8].

{% hint style="warning" %}
When upgrading the Galera wsrep provider, sometimes the Galera protocol version can change\[cite: 5, 6, 7, 8]. The Galera wsrep provider should not start using the new protocol version until all cluster nodes have been upgraded to the new version, so this is not generally an issue during a rolling upgrade\[cite: 5, 6, 7, 8]. However, this can cause issues if you restart a non-upgraded node in a cluster where the rest of the nodes have been upgraded\[cite: 5, 6, 7, 8].
{% endhint %}

This page is licensed: CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
