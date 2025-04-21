
# Embedded MariaDB Interface

The embedded MariaDB server, `libmysqld` has the identical interface as the [C client library](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/)`libmysqclient`.


The normal usage of the embedded server is to use the normal `mysql.h` include file in your application and link with `libmysqld` instead of `libmysqlclient`.


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
* Before [MariaDB 5.5.60](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5560-release-notes) ([MariaDB 10.0.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10035-release-notes), [MariaDB 10.1.33](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10133-release-notes), [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10215-release-notes), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes)), the embedded server library did not support SSL when it was used to connect to remote servers.
* Starting with [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-10-5-series/what-is-mariadb-105) the embedded server library and related test binaries are no longer part of binary tarball release archives.


## See Also


* [mysql_library_init](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_library_init)
* [mariadb client with MariaDB embedded](../../../../clients-and-utilities/mariadb-embedded.md)

