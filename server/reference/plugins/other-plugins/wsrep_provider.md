# wsrep\_provider

This plugin implements `wsrep_provider` for MariaDB Galera Cluster.&#x20;

* It is available as of MariaDB 11.4.
* It is disabled by default.

Enabling it is done in two steps:

{% stepper %}
{% step %}
Add this to the my.cnf configuration file:

```ini
[mariadbd]
wsrep-on=ON
wsrep-cluster-address=gcomm://
wsrep-provider=@ENV.WSREP_PROVIDER
binlog-format=ROW
plugin-wsrep-provider=ON
```
{% endstep %}

{% step %}
Run this query:

```sql
SET GLOBAL wsrep_provider_repl_max_ws_size=1;
```

Alternatively, run this query:

```sql
SET GLOBAL wsrep_provider_options="repl.max_ws_size=1";
```
{% endstep %}
{% endstepper %}

See the [wsrep\_provider\_options](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_provider_options) page for what you can configure.

For plugin version and maturity level, see [this page](../information-on-plugins/list-of-plugins.md).

