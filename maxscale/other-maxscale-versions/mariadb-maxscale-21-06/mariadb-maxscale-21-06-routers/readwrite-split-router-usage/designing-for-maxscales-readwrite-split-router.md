
# Designing for MaxScale's Read/Write Split Router


# Overview


[MaxScale's Read/Write Split Router (readwritesplit)](../../../mariadb-maxscale-23-02/mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readwritesplit.md) performs query-based load balancing. For each client connected to MaxScale, it opens up connections to multiple back-end database servers. When the client sends a write query to MaxScale, it routes the query to the connection opened with the primary server. When the client sends a read query to MaxScale, it routes the query to a connection opened with one of the replicas.


This page contains topics that need to be considered when designing applications that use the Read/Write Split Router.


* How does the [Read/Write Split Router route queries?](routing-statements-with-maxscales-readwrite-split-router.md)


* How does the [Read/Write Split Router select replica servers to load balance queries?](selecting-replica-servers-with-maxscales-readwrite-split-router.md)


* How does the [ensuring-causal-consistency-with-maxscales-readwrite-split-routerRead/Write Split Router ensure that load-balanced read-only queries are causally consistent?](https://mariadb.com/kb/en/ensuring-causal-consistency-with-maxscales-readwrite-split-routerRead/Write_Split_Router_ensure_that_load-balanced_read-only_queries_are_causally_consistent%3F)


* How does the [Write Split Router reconnect client connections to the new primary server after automatic failover?](reconnecting-to-the-primary-server-with-maxscales-readwrite-split-router.md)


* How does the [Read/Write Split Router retry failed reads?](retrying-failed-reads-with-maxscales-readwrite-split-router.md)


* How does the [Read/Write Split Router retry failed queries during automatic failover?](delayed-retrying-of-failed-queries-with-maxscales-readwrite-split-router.md)


Additional information is available [here](../../../mariadb-maxscale-25/maxscale-25-routers/mariadb-maxscale-25-readwritesplit.md).


Copyright © 2025 MariaDB

