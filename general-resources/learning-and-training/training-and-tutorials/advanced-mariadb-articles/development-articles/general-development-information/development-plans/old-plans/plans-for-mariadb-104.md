
# Plans for MariaDB 10.4


"[What is MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)" shows all features already implemented for 10.4.


[MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104) is stable, so no new features will be added to 10.4. See [Plans for MariaDB 10.5](plans-for-mariadb-105.md) instead.


Planning for 10.4 began at the 2017 MariaDB Developer's Unconference in Shenzhen, and further discussions were held at the 2018 Developers Unconference in New York. The features below were considered for inclusion in [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104).


## Very Likely


### Better Security


* Automatic DOS attacks detection - MariaDB Corporation
* Automatic password crack detection - MariaDB Corporation
* Encryption on client side - MariaDB Corporation
* Password expiration - MariaDB Foundation
* Multiple authentication plugins per user - MariaDB Foundation
* Socket authentication by default ([MDEV-12484](https://jira.mariadb.org/browse/MDEV-12484)) - MariaDB Foundation
* Encryption plugin (Tencent Cloud)
* Column encryption (Tencent Cloud)


### Compatibility


* Oracle stage 2 ([MDEV-10872](https://jira.mariadb.org/browse/MDEV-10872))
* CONNECT BY - Alibaba Cloud, MariaDB Corporation & MariaDB Foundation
* MSSQL (?)


### Spider


* Spider (10.4 patches) - Kentoku & MariaDB Corporation
* Tencent Spider patches (10 patches)
* Vertical partitioning - Kentoku


### Distributed Storage Engine (stage 1 of 4)


* Write scaling
* Planning to be done in November-December


### InnoDB


* Instant drop column etc. ([MDEV-15562](https://jira.mariadb.org/browse/MDEV-15562)) - MariaDB Corporation
* Better redo log ([MDEV-14425](https://jira.mariadb.org/browse/MDEV-14425)) - MariaDB Corporation & Tencent Cloud


### Performance


* Micro optimization ([MDEV-7941](https://jira.mariadb.org/browse/MDEV-7941)) - MariaDB Foundation (Svoj)
* Scalability issues - MariaDB Foundation (Svoj) & IBM
* Moving blocks without using any L? cache (Svoj and Monty)
* [MDEV-7487](https://jira.mariadb.org/browse/MDEV-7487) - semi-join optimisations - (MariaDB Corporation)
* Aggregation on the server (Tencent Cloud)
* GROUP INSERT (Alibaba Cloud)


### Re-Entrant Items


* Building block for parallel query and be able to share stored procedures between threads (Stored procedure cache)
* Reading and updating my.cnf from server - MariaDB Corporation


### Other


* Galera 4 - Codership
* MySQL syntax for multi source (CHANNEL) - Alibaba Cloud
* Updates to MyRocks - MariaDB Corporation & Facebook
* Reverse privileges - MariaDB Foundation
* BLOB & optimized VARCHAR for memory tables - MariaDB Corporation (Greatly reduces memory for internal temporary tables)


## Rolling Features


### Backup


* Backup from the server through storage engine API, patch for mariabackup (MariaDB Corporation and Alibaba)


### Columnstore


* Columnstore integration (MariaDB Corporation)


### Replication


* GTID in OK Packet ([MDEV-11956](https://jira.mariadb.org/browse/MDEV-11956)) - MariaDB Corporation


### Optimizer


* Better ORDER BY LIMIT Optimization ([MDEV-8306](https://jira.mariadb.org/browse/MDEV-8306)) - MariaDB Corporation
* Optimizer trace ([MDEV-6111](https://jira.mariadb.org/browse/MDEV-6111)) - MariaDB Corporation
* Better histograms ([MDEV-12313](https://jira.mariadb.org/browse/MDEV-12313)) - [Google Summer of Code project](../../../../../../../company-and-community/contributing-participating/google-summers-of-code/google-summer-of-code-2018.md)
* Prefiltering - MariaDB Corporation (Igor)
* Better telemetry ???
* Improve single-thread CPU performance ???


### Other


* Virtual host in protocol - Microsoft(?)
* Index on expression - MariaDB Corporation
* Pattern matching for keys
* Downscaling memory on demand/request - MariaDB Corporation (?)

  * Closing not used connections
  * Reducing buffer-pool and key caches
  * Flush all internal caches
* Parallel replication of one table - Tencent Cloud

  * Depending on benchmark results
* TIMESTAMP with timezone support ([MDEV-7928](https://jira.mariadb.org/browse/MDEV-7928)) - Seth(?)
* Implement all window function features - [MDEV-12987](https://jira.mariadb.org/browse/MDEV-12987), [MDEV-6115](https://jira.mariadb.org/browse/MDEV-6115)
* Remove the need to use comments for configuration (MariaDB Corporation)
* Remotely provision slaves (?)


## Other Activities Overlapping with 10.4 Release


* Allow community builds - MariaDB Foundation (Vicentiu)
* Docker - MariaDB Foundation (Vicentiu)
* Staging trees - MariaDB Foundation (Vicentiu)
* Python Connector - MariaDB Foundation (Vicentiu)
* Query characteristics being returned to Connector (MariaDB Corporation)
* Reduce the number of open MDEVs (?)


## JIRA


We manage our development plans in JIRA, so the definitive list will be there. [This search](https://jira.mariadb.org/issues/?jql=project+%3D+MDEV+AND+issuetype+%3D+Task+AND+fixVersion+in+%2810.4%29+ORDER+BY+priority+DESC) shows what we **currently** plan for 10.4. It shows all tasks with the **Fix-Version** being 10.4. Not all these tasks will really end up in 10.4, but tasks with the "red" priorities have a much higher chance of being done in time for 10.4. Practically, you can think of these tasks as "features that **will** be in 10.4". Tasks with the "green" priorities probably won't be in 10.4. Think of them as "bonus features that would be **nice to have** in 10.4".


## See Also


* [Current tasks for 10.4](https://jira.mariadb.org/issues/?jql=project%20%3D%20MDEV%20AND%20issuetype%20%3D%20Task%20AND%20fixVersion%20in%20(10.4)%20ORDER%20BY%20priority%20DESC)
* [10.4 Features/fixes by vote](https://jira.mariadb.org/issues/?jql=project%20%3D%20MDEV%20AND%20issuetype%20%3D%20Task%20AND%20fixVersion%20in%20(10.4)%20ORDER%20BY%20votes%20DESC%2C%20priority%20DESC)
* [What is MariaDB 10.4?](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)
* [What is MariaDB 10.3?](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)
* [What is MariaDB 10.2?](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102)

