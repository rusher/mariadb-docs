
# Embedded MariaDB Interface

The embedded MariaDB server, `<code class="highlight fixed" style="white-space:pre-wrap">libmysqld</code>` has the identical interface as the [C client library](../../../../../connectors/mariadb-connector-cpp/mariadb-connector-cpp-sample-application.md)`<code class="highlight fixed" style="white-space:pre-wrap">libmysqclient</code>`.


The normal usage of the embedded server is to use the normal `<code class="highlight fixed" style="white-space:pre-wrap">mysql.h</code>` include file in your application and link with `<code class="highlight fixed" style="white-space:pre-wrap">libmysqld</code>` instead of `<code class="highlight fixed" style="white-space:pre-wrap">libmysqlclient</code>`.


The intention is that one should be able to move from a server/client version of MariaDB to a single server version of MariaDB by just changing which library you link with.


This means that the embedded C client API only changes when the normal C API changes, usually only between major releases.


The only major change required in your application if you are going to use the embedded server is that you have to call the following functions from your application:


```
int mysql_library_init(int argc, char **argv, char **groups)
void mysql_library_end(void);
```

This is also safe to do when using the standard C library.


## Notes


* libmysqld.so has many more exported symbols than the C library to allow one to expose and use more parts of MariaDB. In normal applications one should not use them, as they may change between every release.
* Before [MariaDB 5.5.60](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5560-release-notes.md) ([MariaDB 10.0.35](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10035-release-notes.md), [MariaDB 10.1.33](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10133-release-notes.md), [MariaDB 10.2.15](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10215-release-notes.md), [MariaDB 10.3.7](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1037-release-notes.md)), the embedded server library did not support SSL when it was used to connect to remote servers.
* Starting with [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md) the embedded server library and related test binaries are no longer part of binary tarball release archives.


## See Also


* [mysql_library_init](../../../../../connectors/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_library_init.md)
* [mariadb client with MariaDB embedded](../../../../clients-and-utilities/mariadb-embedded.md)

