# Database fleet overview  T Copy

## Documentation : Database fleet overview--T Copy

Created by Tauseef Khan on Oct 10, 2025

The "fleet" dashboard is the central inventory for all your monitored database topologies. It provides a hierarchical, at-a-glance overview of the health, status, and configuration of your entire database environment.

#### Understanding the Dashboard Columns

**NAME Column**

This column displays the logical names of your databases and the individual server nodes within each topology. It also contains important status and quick-access icons.

Status Icons

| Icon     | Applies To                            | Meaning                                                                                          |
| -------- | ------------------------------------- | ------------------------------------------------------------------------------------------------ |
| 🟢 Green | Aggregated Topology, Server, MaxScale | The component and all its members are running correctly.                                         |
| 🔴 Red   | Aggregated Topology, Server, MaxScale | One or more members in the topology are down or not functioning properly.                        |
| ⚫ Gray   | Server                                | The server's status is unknown. This typically happens if the MaxScale node managing it is down. |

Quick-Access Icons

* View Monitoring Dashboard: This icon (🖥️) is a shortcut that takes you directly to the detailed Grafana monitoring dashboard for that specific node or topology.

**TYPE Column**

This column shows the role of each node as automatically detected by Enterprise Manager (e.g., `Primary`, `Replica`, `MaxScale`, `Galera Node`, `Standalone Server`).

{% hint style="warning" %}
If this column shows `-`, it indicates an issue. For instance, in a Primary/Replica topology, a server expected to be a `Replica` that shows `-` is likely not replicating correctly from the primary.
{% endhint %}

**LAST METRIC AGE Column**

This column shows the time elapsed since the agent on that node last reported metrics.

{% hint style="danger" %}
If the age is 5 minutes or greater, it indicates a problem. Verify that the `mema-agent` is installed, running, and can communicate with the Enterprise Manager server on that host.
{% endhint %}

#### Interacting with Your Databases

You can perform actions on your databases and nodes using the three-dot menu (⋮) on the far right of each row.

SSO to MaxScale (Single Sign-On)

For topologies managed by MaxScale, you can seamlessly access the MaxScale GUI directly from Enterprise Manager using Single Sign-On.

SSO to MaxScale requires MaxScale 25.10.0 or higher.

{% stepper %}
{% step %}
### Accessing the MaxScale GUI

* Click the three-dot menu (⋮) next to a MaxScale node.
* Select "Manage MaxScale".
{% endstep %}

{% step %}
### Configuring SSO in `maxscale.cnf`

To enable SSO, add the following parameters to your MaxScale configuration file (`maxscale.cnf`) on the MaxScale host:

{% code title="maxscale.cnf" %}
```
```
{% endcode %}

```
[maxscale]
# ... other settings ...
admin_host=0.0.0.0
admin_oidc_url=<Enterprise Manager Host Name>
admin_oidc_client_id=admin
admin_oidc_client_secret=mariadb
```

* `admin_oidc_url`: The hostname or IP address of your Enterprise Manager server.
* `admin_host`: Must be set to `0.0.0.0` to allow external connections from Enterprise Manager.
* `admin_oidc_client_id` & `admin_oidc_client_secret`: These are the default credentials used by Enterprise Manager to request the access token.
{% endstep %}
{% endstepper %}

Attachments

* &#x20;[FleetOverview-Manage-MaxScale.png](broken-reference) (image/png)
* &#x20;[5289c16b-2b40-4da7-91da-e697a21a10ad.png](broken-reference) (image/png)
* &#x20;[FleetOverview.png](broken-reference) (image/png)
* &#x20;[FleetOverview.png](broken-reference) (image/png)
* &#x20;[FleetOverview-Manage-MaxScale.png](broken-reference) (image/png)
