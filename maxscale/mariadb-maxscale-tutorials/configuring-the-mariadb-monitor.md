# Configuring the MariaDB Monitor

This document describes how to configure a MariaDB primary-replica cluster monitor to be used with MaxScale.

## Configuring the Monitor

Define the monitor that monitors the servers.

```ini
[Replication-Monitor]
type=monitor
module=mariadbmon
servers=dbserv1, dbserv2, dbserv3
user=monitor_user
password=my_password
monitor_interval=2000ms
```

The mandatory parameters are the object type, the monitor module to use, the list of servers to monitor, and the username and password to use when connecting to the servers. The `monitor_interval` parameter controls how long the monitor waits between each monitoring loop.

## Monitor User

The monitor user requires the `REPLICATION CLIENT` privilege to do basic monitoring. To create a user with the proper grants, run:

```sql
CREATE USER 'monitor_user'@'%' IDENTIFIED BY 'my_password';
GRANT REPLICATION CLIENT ON *.* TO 'monitor_user'@'%';
```

**Note:** If the automatic failover of MariaDB Monitor is used, the user needs additional grants:

```sql
GRANT SUPER, RELOAD ON *.* TO 'monitor_user'@'%';
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
