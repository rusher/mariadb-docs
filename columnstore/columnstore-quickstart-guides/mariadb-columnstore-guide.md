# About MariaDB ColumnStore

MariaDB ColumnStore is a columnar storage engine that utilizes a massively parallel distributed data architecture. It's a columnar storage system built by porting InfiniDB 4.6.7 to MariaDB, and released under the GPL license.

From [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-10-5-series/mariadb-1054-release-notes), it is available as a storage engine for MariaDB Server. Before then, it is only available as a separate download.

Release notes and other documentation for ColumnStore is also available in the Enterprise docs section of the MariaDB website. For example:

* [ColumnStore 23.10 Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/columnstore/mariadb-columnstore-23-10-release-notes)
* [ColumnStore 23.02 Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/columnstore/mariadb-columnstore-23-02-release-notes)
* [ColumnStore 22.08 Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/columnstore/mariadb-columnstore-22-08-release-notes)
* [ColumnStore 6 Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/columnstore/mariadb-columnstore-6-release-notes)
* [ColumnStore 5.6 Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/columnstore/mariadb-columnstore-5-6-release-notes)
* [Deployment Instructions](../../kb/en/mariadb-columnstore/)

It is designed for big data scaling to process petabytes of data, linear scalability and exceptional performance with real-time response to analytical queries. It leverages the I/O benefits of columnar storage, compression, just-in-time projection, and horizontal and vertical partitioning to deliver tremendous performance when analyzing large data sets.

Links:

* [MariaDB Columnstore Blogs](https://mariadb.com/resources/blog/tag/columnstore/).
* A Google Group exists for MariaDB ColumnStore that can be used to discuss ideas, issues and communicate with the community: Send email to mariadb-columnstore@googlegroups.com or use the [forum interface](https://groups.google.com/forum/#!forum/mariadb-columnstore)
* Bugs can be reported in MariaDB Jira: [jira.mariadb.org](https://jira.mariadb.org) (see [Reporting Bugs](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/company-and-community/bug-tracking/reporting-bugs)). Please file bugs under the MCOL project and include the output from the [support utility](../management/system-troubleshooting-mariadb-columnstore.md) if possible.

MariaDB ColumnStore is released under the GPL license.

CC BY-SA / Gnu FDL
