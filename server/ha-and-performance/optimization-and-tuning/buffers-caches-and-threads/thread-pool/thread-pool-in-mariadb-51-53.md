# Thread Pool in MariaDB 5.1 - 5.3

This article describes the old thread pool in [MariaDB 5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1) - 5.3. MariaDB 5.5 and later use an improved thread pool - see [Thread pool in MariaDB](thread-pool-in-mariadb.md).

## About pool of threads

This is an extended version of the pool-of-threads code from MySQL 6.0. This\
allows you to use a limited set of threads to handle all queries, instead of\
the old 'one-thread-per-connection' style. In recent times, its also been referred to as "thread pool" or "thread pooling" as this feature (in a different implementation) is available in Enterprise editions of MySQL (not in the Community edition).

This can be a very big win if most of your queries are short running queries\
and there are few table/row locks in your system.

## Instructions

To enable pool-of-threads you must first run configure with the`--with-libevent` option. (This is automatically done if you\
use any 'max' scripts in the BUILD directory):

```
./configure --with-libevent
```

When starting mysqld with the pool of threads code you should use

```
mysqld --thread-handling=pool-of-threads --thread-pool-size=20
```

Default values are:

```
thread-handling=  one-thread-per-connection
thread-pool-size= 20
```

One issue with pool-of-threads is that if all worker threads are doing\
work (like running long queries) or are locked by a row/table lock no\
new connections can be established and you can't login and find out\
what's wrong or login and kill queries.

To help this, we have introduced two new options for mysqld; [extra\_port](thread-pool-system-status-variables.md) and [extra\_max\_connections](thread-pool-system-status-variables.md):

```
--extra-port=#             (Default 0)
--extra-max-connections=#  (Default 1)
```

If [extra-port](thread-pool-system-status-variables.md) is <> 0 then you can connect max\_connections number of\
normal threads + 1 extra SUPER user through the 'extra-port' TCP/IP\
port. These connections use the old one-thread-per-connection method.

To connect with through the extra port, use:

```
mysql --port='number-of-extra-port' --protocol=tcp
```

This allows you to freely use, on connection bases, the optimal\
connection/thread model.

## See also

* [Thread-handling and thread-pool-size variables](thread-pool-system-status-variables.md)
* [How MySQL Uses Threads for Client Connections](https://dev.mysql.com/doc/refman/5.6/en/connection-threads.html)

CC BY-SA / Gnu FDL
