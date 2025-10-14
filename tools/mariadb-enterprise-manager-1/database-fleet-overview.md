# Database fleet overview

## Documentation: Database fleet overview

Created by Egor Ustinov, last modified by Thien Ly on Oct 09, 2025

### Database fleet NAME column

#### Status icon

**Database Aggregated Status**

* Green icon — All members in the database topology are running.
* Red icon — One or more members in the database topology are down.

**MaxScale Status**

* Green icon — MaxScale is running.
* Red icon — MaxScale is not running.

**Server Status**

* Green icon — The server is running.
* Red icon — The server is not running.
* Gray icon — The server status is unknown. This typically occurs in a database topology where all MaxScale nodes are down.

#### View Monitoring Dashboard icon

This is a quick-access icon button to the Grafana dashboard. Alternatively, click the three-dot menu on the right and select "View Monitoring Dashboard."

### TYPE column

The **Type** column displays the role of each node in the database topology.

* Automatic Detection: Enterprise Manager automatically detects the server role.
* Indicator of Issues:
  * `-` — The server is not functioning properly.
  * Example: In a Primary/Replica topology, if a server is expected to be a "Replica" but appears as `-`, it indicates that the server is not replicating from the primary.

### LAST METRIC AGE column

The Last Metric Age column indicates the time elapsed since each service last reported metrics.

* Scope: Applies to MariaDB and MaxScale services over the past 30 days.
* Warning Threshold: ≥ 5 minutes — No recent metric updates; verify that the monitoring agent is installed and running.

## SSO to MaxScale

SSO functionality requires MaxScale 25.10.0 or higher.

The application allows SSO access to MaxScale for supported versions.

#### Accessing MaxScale via SSO

* Click the three-dot menu on the right.
* Select "Manage MaxScale."

#### Configuring SSO

To enable SSO, add the following parameters to `maxscale.cnf`:

{% code title="maxscale.cnf" %}
```ini
admin_oidc_url=<Enterprise Manager Host Name>
admin_host=0.0.0.0
# Enterprise Manager credentials for requesting the access token
admin_oidc_client_id=admin
admin_oidc_client_secret=mariadb
```
{% endcode %}

### Attachments

* [FleetOverview.png](broken-reference) (image/png)
* [5289c16b-2b40-4da7-91da-e697a21a10ad.png](broken-reference) (image/png)
* [FleetOverview-Manage-MaxScale.png](broken-reference) (image/png)
* [FleetOverview-Manage-MaxScale.png](broken-reference) (image/png)

For more information, see the original source links in this document.
