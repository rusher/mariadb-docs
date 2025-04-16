
# Connection Redirection Mechanism in the MariaDB Client/Server Protocol


##### MariaDB starting with [11.3](../../../release-notes/mariadb-community-server/what-is-mariadb-113.md)
A connection redirection mechanism was added in [MariaDB 11.3.0](../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md) ([MDEV-15935](https://jira.mariadb.org/browse/MDEV-15935))


Redirection mechanisms are widely used in proxy-based scenarios.


Previously, when multiple servers shared one proxy, the proxy forwarded all packets between servers and clients. Thus, the proxy added latency, consuming computing resources and impacting overall performance. For scenarios with many short connections, such as WordPress, latency can be a critical issue.


With a redirection mechanism, much like HTTP redirects or Oracle redirected connections, clients get the servers’ address from proxies and connect to servers transparently, without latency and without wasting resources.


## Usage


Redirection is handled through a new system variable, [redirect_url](optimization-and-tuning/system-variables/server-system-variables.md#redirect_url). The value defaults to an empty string, but can also contain a connection string in the conventional format (in the style of a Connector/C etc. connection url), that is:


```
{mysql,mariadb}://host[:port]
```

where *host* is an arbitrary string not containing colons, and *port* is a number between 0 and 65535 inclusive.


This variable is appended to the default value of the [session_track_system_variables](optimization-and-tuning/system-variables/server-system-variables.md#session_track_system_variables) system variable. If not empty, clients will be redirected to the specified server.


## Possible Use Cases


* Always redirect all clients to a new location: 

  * set @@global.redirect_url, start the server with --redirect-url=, or put it in my.cnf
* redirect to a group of servers randomly

  * create a table with connection urls, one per row.
  * use an sql script that selects a random row from it and sets @@redirect_url to this value
  * specify this script in the --init-connect server parameter
* dynamically redirect from the primary to one of the replicas

  * same as above, but use [INFORMATION_SCHEMA.PROCESSLIST](../../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) to get the list of active replicas.


## Example


```
set global redirect_url="mysql://mariadb.org:12345";
```

Invalid formats are not permitted:


```
set global redirect_url="mysql://mariadb.org:"; 
ERROR 1231 (42000): Variable 'redirect_url' can't be set to the value of 'mysql://mariadb.org:'
```
