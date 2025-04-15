
# About XtraDB

Percona XtraDB was an enhanced version of the InnoDB storage engine [used in MariaDB before MariaDB 10.2](/kb/en/why-does-mariadb-102-use-innodb-instead-of-xtradb/), designed to better scale on modern hardware, and it includes a variety of other features
useful in high performance environments.


It is fully backwards compatible, and it identifies itself to MariaDB as
"`<code>ENGINE=InnoDB</code>`" (just like InnoDB), and so can be used as a drop-in replacement
for standard InnoDB.


Percona XtraDB includes all of InnoDB's robust, reliable [ACID](../../../../../general-resources/learning-and-training/training-and-tutorials/intermediate-mariadb-articles/database-theory/acid-concurrency-control-with-transactions.md)-compliant design
and advanced MVCC architecture, and builds on that solid foundation with more
features, more tunability, more metrics, and more scalability. In particular,
it is designed to scale better on many cores, to use memory more efficiently,
and to be more convenient and useful. The new features are especially designed
to alleviate some of InnoDB's limitations. We choose features and fixes based
on customer requests and on our best judgment of real-world needs as a
high-performance consulting company.


XtraDB was also available in MariaDB for Windows.


## Percona XtraDB versions in MariaDB


### [MariaDB 10.1](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md)


* XtraDB from [Percona Server 5.6.49-89.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.49-89.0.html) in [MariaDB 10.1.46](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10146-release-notes.md)
* XtraDB from [Percona Server 5.6.46-86.2](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.46-86.2.html) in [MariaDB 10.1.44](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10144-release-notes.md)
* XtraDB from [Percona Server 5.6.43-84.3](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.43-84.3.html) in [MariaDB 10.1.39](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10139-release-notes.md)
* XtraDB from [Percona Server 5.6.41-84.1](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.41-84.1.html) in [MariaDB 10.1.36](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10136-release-notes.md)
* XtraDB from [Percona Server 5.6.38-83.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.38-83.0.html)[[1](#_note-0)] in [MariaDB 10.1.31](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10131-release-notes.md)
* XtraDB from [Percona Server 5.6.37-82.2](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.37-82.2.html)[[2](#_note-1)]in [MariaDB 10.1.27](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10127-release-notes.md)
* XtraDB from [Percona Server 5.6.36-82.1](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.36-82.1.html) in [MariaDB 10.1.26](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10126-release-notes.md)
* XtraDB from [Percona Server 5.6.36-82.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.36-82.0.html) in [MariaDB 10.1.24](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10124-release-notes.md)
* XtraDB from [Percona Server 5.6.35-80.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.35-80.0.html) in [MariaDB 10.1.22](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10122-release-notes.md)
* XtraDB from [Percona Server 5.6.34-79.1](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.34-79.1.html) in [MariaDB 10.1.20](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10120-release-notes.md)
* XtraDB from [Percona Server 5.6.33-79.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.33-79.0.html)[[3](#_note-2)] in [MariaDB 10.1.19](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10119-release-notes.md)
* XtraDB from [Percona Server 5.6.32-78.1](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.32-78.1.html) in [MariaDB 10.1.18](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10118-release-notes.md)
* XtraDB from [Percona Server 5.6.31-77.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.31-77.0.html) in [MariaDB 10.1.17](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10117-release-notes.md)
* XtraDB from [Percona Server 5.6.30-76.3](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.30-76.3.html) in [MariaDB 10.1.15](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10115-release-notes.md)
* XtraDB from [Percona Server 5.6.29-76.2](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.29-76.2.html) in [MariaDB 10.1.14](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10114-release-notes.md)
* XtraDB from [Percona Server 5.6.28-76.1](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.28-76.1.html) in [MariaDB 10.1.12](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10112-release-notes.md)
* XtraDB from [Percona Server 5.6.26-76.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.26-76.0.html) in [MariaDB 10.1.10](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10110-release-notes.md)
* XtraDB from [Percona Server 5.6.26-74.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.26-74.0.html) in [MariaDB 10.1.8](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-8-release-notes.md)
* XtraDB from [Percona Server 5.6.25-73.1](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.25-73.1.html) in [MariaDB 10.1.7](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-7-release-notes.md)
* XtraDB from [Percona Server 5.6.24-72.2](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.24-72.2.html) in [MariaDB 10.1.6](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-6-release-notes.md)
* XtraDB from [Percona Server 5.6.23-72.1](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.23-72.1.html) in [MariaDB 10.1.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-5-release-notes.md)
* XtraDB from [Percona Server 5.6.22-72.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.22-72.0.html) in [MariaDB 10.1.4](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-4-release-notes.md)
* XtraDB from [Percona Server 5.6.21-70.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.21-70.0.html) in [MariaDB 10.1.2](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-2-release-notes.md)
* XtraDB from [Percona Server 5.6.17-65.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.17-65.0.html) in [MariaDB 10.1.1](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes.md)


### [MariaDB 10.0](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)


* XtraDB from [Percona Server 5.6.42-84.2](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.42-84.2.html) in [MariaDB 10.0.38](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10038-release-notes.md)
* XtraDB from [Percona Server 5.6.41-84.1](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.41-84.1.html) in [MariaDB 10.0.37](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10037-release-notes.md)
* XtraDB from [Percona Server 5.6.39-83.1](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.39-83.1.html) in [MariaDB 10.0.35](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10035-release-notes.md)
* XtraDB from [Percona Server 5.6.38-83.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.38-83.0.html)[[4](#_note-3)]in [MariaDB 10.0.34](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10034-release-notes.md)
* XtraDB from [Percona Server 5.6.37-82.2](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.37-82.2.html)[[5](#_note-4)]in [MariaDB 10.0.33](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10033-release-notes.md)
* XtraDB from [Percona Server 5.6.36-82.1](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.36-82.1.html) in [MariaDB 10.0.32](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10032-release-notes.md)
* XtraDB from [Percona Server 5.6.36-82.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.36-82.0.html) in [MariaDB 10.0.31](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10031-release-notes.md)
* XtraDB from [Percona Server 5.6.35-80.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.35-80.0.html) in [MariaDB 10.0.30](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10030-release-notes.md)
* XtraDB from [Percona Server 5.6.34-79.1](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.34-79.1.html) in [MariaDB 10.0.29](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10029-release-notes.md)
* XtraDB from [Percona Server 5.6.33-79.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.33-79.0.html)[[6](#_note-5)] in [MariaDB 10.0.28](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10028-release-notes.md)
* XtraDB from [Percona Server 5.6.31-77.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.31-77.0.html) in [MariaDB 10.0.27](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10027-release-notes.md)
* XtraDB from [Percona Server 5.6.30-76.3](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.30-76.3.html) in [MariaDB 10.0.26](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10026-release-notes.md)
* XtraDB from [Percona Server 5.6.29-76.2](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.29-76.2.html) in [MariaDB 10.0.25](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10025-release-notes.md)
* XtraDB from [Percona Server 5.6.28-76.1](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.28-76.1.html) in [MariaDB 10.0.24](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10024-release-notes.md)
* XtraDB from [Percona Server 5.6.27-76.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.27-76.0.html) in [MariaDB 10.0.23](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10023-release-notes.md)
* XtraDB from [Percona Server 5.6.26-74.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.26-74.0.html) in [MariaDB 10.0.22](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10022-release-notes.md)
* XtraDB from [Percona Server 5.6.25-73.1](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.25-73.1.html) in [MariaDB 10.0.21](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10021-release-notes.md)
* XtraDB from [Percona Server 5.6.24-72.2](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.24-72.2.html) in [MariaDB 10.0.20](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10020-release-notes.md)
* XtraDB from [Percona Server 5.6.23-72.1](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.23-72.1.html) in [MariaDB 10.0.18](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10018-release-notes.md)
* XtraDB from [Percona Server 5.6.22-72.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.22-72.0.html) in [MariaDB 10.0.17](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10017-release-notes.md)
* XtraDB from [Percona Server 5.6.22-71.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.22-71.0.html) in [MariaDB 10.0.16](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10016-release-notes.md)
* XtraDB from [Percona Server 5.6.21-70.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.21-70.0.html) in [MariaDB 10.0.15](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10015-release-notes.md)
* XtraDB from [Percona Server 5.6.20-68.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.20-68.0.html) in [MariaDB 10.0.14](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10014-release-notes.md)
* XtraDB from [Percona Server 5.6.19-67.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.19-67.0.html) in [MariaDB 10.0.13](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10013-release-notes.md)
* XtraDB from [Percona Server 5.6.17-65.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.17-65.0.html) in [MariaDB 10.0.11](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10011-release-notes.md)
* XtraDB from [Percona Server 5.6.14-rel62.0](https://www.percona.com/doc/percona-server/5.6/release-notes/Percona-Server-5.6.14-62.0.html) in [MariaDB 10.0.7](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1007-release-notes.md)


### [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)


* XtraDB from [Percona Server 5.5.61-38.13](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.61-38.13.html) in [MariaDB 5.5.62](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5562-release-notes.md)
* XtraDB from [Percona Server 5.5.59-38.11](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.59-38.11.html) in [MariaDB 5.5.60](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5560-release-notes.md)
* XtraDB from [Percona Server 5.5.58-38.10](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.58-38.10.html) in [MariaDB 5.5.59](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5559-release-notes.md)
* XtraDB from [Percona Server 5.5.55-38.9](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.55-38.9.html) in [MariaDB 5.5.58](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5558-release-notes.md)
* XtraDB from [Percona Server 5.5.55-38.8](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.55-38.8.html) in [MariaDB 5.5.57](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5557-release-notes.md)
* XtraDB from [Percona Server 5.5.52-38.3](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.52-38.3.html) in [MariaDB 5.5.53](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5553-release-notes.md)
* XtraDB from [Percona Server 5.5.50-38.0](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.50-38.0.html) in [MariaDB 5.5.51](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5551-release-notes.md)
* XtraDB from [Percona Server 5.5.49-37.9](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.49-37.9.html) in [MariaDB 5.5.50](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5550-release-notes.md)
* XtraDB from [Percona Server 5.5.48-37.8](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.48-37.8.html) in [MariaDB 5.5.49](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5549-release-notes.md)
* XtraDB from [Percona Server 5.5.46-37.7](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.46-37.7.html) in [MariaDB 5.5.48](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5548-release-notes.md)
* XtraDB from [Percona Server 5.5.46-37.6](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.46-37.6.html) in [MariaDB 5.5.47](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5547-release-notes.md)
* XtraDB from [Percona Server 5.5.45-37.4](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.45-37.4.html) in [MariaDB 5.5.46](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5546-release-notes.md)
* XtraDB from [Percona Server 5.5.44-37.3](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.44-37.3.html) in [MariaDB 5.5.45](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5545-release-notes.md)
* XtraDB from [Percona Server 5.5.42-37.2](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.42-37.2.html) in [MariaDB 5.5.44](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5544-release-notes.md)
* XtraDB from [Percona Server 5.5.42-37.1](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.42-37.1.html) in [MariaDB 5.5.43](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5543-release-notes.md)
* XtraDB from [Percona Server 5.5.40-36.1](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.40-36.1.html) in [MariaDB 5.5.40](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5540-release-notes.md)
* XtraDB from [Percona Server 5.5.38-35.2](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.38-35.2.html) in [MariaDB 5.5.39](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5539-release-notes.md)
* XtraDB from [Percona Server 5.5.37-35.0](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.37-35.0.html) in [MariaDB 5.5.38](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5538-release-notes.md)
* XtraDB from [Percona Server 5.5.36-34.0](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.36-34.0.html) in [MariaDB 5.5.37](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5537-release-notes.md)
* XtraDB from [Percona Server 5.5.35-33.0](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.35-33.0.html) in [MariaDB 5.5.35](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5535-release-notes.md)
* XtraDB from [Percona Server 5.5.34-32.0](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.34-32.0.html) in [MariaDB 5.5.34](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5534-release-notes.md)
* XtraDB from [Percona Server 5.5.33-31.1](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.33-31.1.html) in [MariaDB 5.5.33](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5533-release-notes.md)
* XtraDB from [Percona Server-5.5.32-31.0](https://www.percona.com/doc/percona-server/5.5/release-notes/Percona-Server-5.5.32-31.0.html) in [MariaDB 5.5.32](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5532-release-notes.md)


### [MariaDB 5.2](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md) and [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md)


* [MariaDB 5.2](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md) and 5.3 include the latest XtraDB version from [MariaDB 5.1](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md) at the time they were released.


### [MariaDB 5.1](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md)


* version [5.1.59-13](https://www.percona.com/doc/percona-server/5.1/release-notes/Percona-Server-5.1.59-13.0.html) in [MariaDB 5.1.60](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/mariadb-5160-release-notes.md)
* version 5.1.54-12.5 in
 [MariaDB 5.1.55](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/mariadb-5155-release-notes.md)
* version 5.1.52-11.6 in
 [MariaDB 5.2.4](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-2-series/mariadb-524-release-notes.md) and
 [5.1.53](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/mariadb-5153-release-notes.md)
* version 5.1.49-12 in
 [MariaDB 5.1.50](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/mariadb-5150-release-notes.md)
* version
 [5.1.47-11.2](https://www.percona.com/docs/wiki/percona-server:release_notes_51#release_5147-112) in
 [MariaDB 5.1.49](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/mariadb-5149-release-notes.md)
* version 1.0.6-10 in
 [MariaDB 5.1.47](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/mariadb-5147-release-notes.md)
* version 1.0.6-9 in
 [MariaDB 5.1.42](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/mariadb-5142-release-notes.md),
 [5.1.44](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/mariadb-5144-release-notes.md), and
 [5.1.44b](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/mariadb-5144b-release-notes.md).
* version 1.0.4-8 in
 [MariaDB 5.1.41 RC](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/mariadb-5141-release-notes.md)
* version 1.0.3-8 in
 [MariaDB 5.1.39 Beta](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/mariadb-5139-release-notes.md)
* version 1.0.3-6 in
 [MariaDB 5.1.38 Beta](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/mariadb-5138-release-notes.md)


## Notes


1. [↑](#_ref-0) Misidentifies itself as 5.6.36-83.0 in [MariaDB 10.1.31](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10131-release-notes.md)
1. [↑](#_ref-1) Misidentifies itself as 5.6.36-82.2 from [MariaDB 10.1.27](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10127-release-notes.md) to [MariaDB 10.1.30](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10130-release-notes.md)
1. [↑](#_ref-2) Misidentifies itself as 5.6.32-79.0 in [MariaDB 10.1.19](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10119-release-notes.md)
1. [↑](#_ref-3) Misidentifies itself as 5.6.36-83.0 in [MariaDB 10.0.34](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10034-release-notes.md)
1. [↑](#_ref-4) Misidentifies itself as 5.6.36-82.2 in [MariaDB 10.0.33](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10033-release-notes.md)
1. [↑](#_ref-5) Misidentifies itself as 5.6.32-79.0 in [MariaDB 10.0.28](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10028-release-notes.md)


## See Also


More information can be found in the
[Percona documentation](https://www.percona.com/doc/percona-server/5.5/percona_xtradb.html?id=percona-xtradb:start).

