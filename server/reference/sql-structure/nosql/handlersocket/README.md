# HandlerSocket

HandlerSocket gives you direct access to [InnoDB](../../../../server-usage/storage-engines/innodb/) and [SPIDER](../../../../server-usage/storage-engines/spider/). It is included in MariaDB as a ready-to use plugin.

HandlerSocket is a NoSQL plugin for MariaDB. It works as a daemon inside the mariadbd process, accepting TCP connections, and executing requests from clients. HandlerSocket does not support SQL queries. Instead, it supports simple CRUD operations on tables.

HandlerSocket can be much faster than mysqld/libmysql in some cases because it has lower CPU, disk, and network overhead:

1. To lower CPU usage it does not parse SQL.
2. Next, it batch-processes requests where possible, which further reduces CPU usage and lowers disk usage.
3. Lastly, the client/server protocol is very compact compared to mysql/libmysql, which reduces network usage.
