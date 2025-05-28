---
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# MariaDB Enterprise Platform

### What is MariaDB Enterprise Platform? <a href="#what-is-mariadb-enterprise-platform" id="what-is-mariadb-enterprise-platform"></a>

MariaDB Enterprise Platform is designed to deliver best-in-class performance, data security, replication, clustering, and high availability for production workloads in any cloud environment, including private, public, hybrid, or multicloud setups. It empowers modern data strategies with an end-to-end database solution, ensuring consistent performance and unwavering stability for mission-critical applications in demanding environments. The platform simplifies the data landscape by running all workloads in a single, robust MariaDB environment, powered by open-source technology and fortified with enterprise-grade reliability, security, and support.

#### Components <a href="#components" id="components"></a>

MariaDB Enterprise Platform comprises a number of technology components, modules, tools, and services, notably these include:

* MariaDB Enterprise Server – a scalable database management system offering support for transactional, analytical, and hybrid workloads, working with relational, JSON, and hybrid data models
* MariaDB ColumnStore – a specialized storage engine for scalable, high-performance analytics without the need for complex schemas and indexes – distributed, columnar storage with parallel query processing
* MariaDB MaxScale – a database proxy which provides enterprise high availability, scalability, security and integration services, simplifying application development and database administration
* MariaDB Galera Cluster - a virtually synchronous multi-master cluster, providing read scalability and enhanced transaction security
* MariaDB Connectors – database drivers for practically every programming language

… and a number of services, including:

* Remote database administration
* Migration management
* Technical support

#### Security <a href="#security" id="security"></a>

MariaDB Enterprise Platform **includes advanced security features, such as transparent data encryption (TDE), query blocking, result limiting, and a database firewall**, which meet and exceed traditional enterprise security requirements. It also supports dynamic data masking and complete data obfuscation to protect personal data and meet GDPR requirements.

#### Innovation <a href="#innovation" id="innovation"></a>

The platform is **built for the enterprise and accelerated by open-source innovation, offering unmatched performance and compatibility with existing MySQL APIs and commands**. It supports a wide range of database workloads and data types, including transactional, analytical, semi-structured, and AI-ready vector data.

#### MariaDB Enterprise Platform 2025 <a href="#platform-2025-vs.-platform-2026" id="platform-2025-vs.-platform-2026"></a>

In January 2025, Platform 2025 was released. It includes Enterprise Server 11.4 and MaxScale 25.01. Subsequent platform launches will include all the latest new components, such as Enterprise Server 11.8.

## Product Overview <a href="#product-overview" id="product-overview"></a>

### Alternative 1 - fold descriptions into the Alternative 2 table, then remove this section

MariaDB Enterprise Platform comprises these products:

* **MariaDB Server**
  * **Transactional Workloads:** Optimized for OLTP (Online Transaction Processing), offering ACID compliance for critical applications.
  * **Web & Cloud Applications:** Scalable architecture making it ideal for modern web and cloud-based applications.
  * **Business Continuity:** Provides high availability and disaster recovery with replication and clustering features.
* **MaxScale**
  * **Load Balancing:** Distributes database queries across multiple servers to ensure efficient load handling.
  * **Database Security:** Acts as a proxy to protect the database from unauthorized access and threats.
  * **Data Routing:** Routes SQL queries and statements to the appropriate database nodes, improving performance.
* **ColumnStore**
  * **Analytical Workloads:** Designed for OLAP (Online Analytical Processing), suitable for complex queries and reporting.
  * **Big Data Solutions:** Handles large volumes of data with columnar storage, enhancing performance in data-intensive applications.
  * **Data Warehousing:** Efficiently aggregates and processes large datasets, making it suitable for business intelligence.
* **Galera Cluster**
  * **Synchronous Replication:** Guarantees that changes happening on one node in the cluster will happen on other cluster nodes at the same time.
  * **True parallel replication:** Replicates data on row level, reads and writes can be made to any cluster node
  * **Automatic:** Membership control, failed nodes drop from the cluster, automatic node joining

### Alternative 2

| Category                           | Product or Features                    | Description                                                                                                                        | Details                                                                                                     |
| ---------------------------------- | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Databases**                      | MariaDB Enterprise Server              | An enhanced, hardened, and secured version of the open-source database, designed for enterprise-grade reliability and scalability. | [Link](https://mariadb.com/products/enterprise/components/#mariadb-enterprise-server)                       |
| **Connectors**                     | MariaDB Connector/C                    | Enables C applications to connect to MariaDB and MySQL databases.                                                                  | [Link](https://mariadb.com/kb/en/mariadb-connector-c/)                                                      |
|                                    | MariaDB Connector/C++                  | Provides C++ applications with an object-oriented interface to MariaDB and MySQL databases.                                        | [Link](https://mariadb.com/docs/server/connect/programming-languages/)                                      |
|                                    | MariaDB Connector/J                    | Allows Java applications to connect using the standard JDBC API.                                                                   | [Link](https://mariadb.com/kb/en/mariadb-connector-j/)                                                      |
|                                    | MariaDB Connector/R2DBC                | Facilitates reactive programming in Java applications with non-blocking database access.                                           | [Link](https://mariadb.com/docs/server/connect/programming-languages/)                                      |
|                                    | MariaDB Connector/Node.js              | Enables Node.js applications to interact with MariaDB and MySQL databases.                                                         | [Link](https://mariadb.com/docs/server/connect/programming-languages/)                                      |
|                                    | MariaDB Connector/ODBC                 | Provides ODBC-compliant applications with access to MariaDB and MySQL databases.                                                   | [Link](https://mariadb.com/kb/en/mariadb-connector-odbc/)                                                   |
|                                    | MariaDB Connector/Python               | Allows Python applications to connect using a DB API 2.0-compliant interface.                                                      | [Link](https://mariadb-corporation.github.io/mariadb-connector-python/)                                     |
| **Tools & Automation**             | MariaDB MaxScale                       | A database proxy for scalability, high availability, and security; simplifies development and admin tasks.                         | [Link](https://mariadb.com/products/enterprise/components/#mariadb-maxscale)                                |
|                                    | MariaDB Enterprise Kubernetes Operator | Automates and simplifies deployment and management of MariaDB and MaxScale in Kubernetes environments.                             | [Link](https://mariadb.com/products/enterprise/components/#mariadb-enterprise-kubernetes-operator)          |
| **High Availability & Clustering** | MariaDB Enterprise Cluster             | An open-source, active-active, multi-master synchronous replication solution powered by Galera.                                    | [Link](https://mariadb.com/products/enterprise/components/#mariadb-enterprise-cluster)                      |
| **Analytics & AI**                 | MariaDB ColumnStore                    | Extends MariaDB with distributed columnar storage and massively parallel processing (MPP) for real-time analytics.                 | [Link](https://mariadb.com/products/enterprise/components/#mariadb-columnstore)                             |
|                                    | Vector Embedded Search                 | Native vector search for AI-powered applications, embedded directly into MariaDB.                                                  | [Link](https://mariadb.com/products/enterprise/capabilities/#vector-embedded-search)                        |
| **Security & Disaster Recovery**   | Security                               | Advanced features like encryption, masking, firewalls, and access control to protect your data.                                    | [Link](https://mariadb.com/database-topics/security/)                                                       |
|                                    | Disaster Recovery                      | Tools for backup, point-in-time recovery (PITR), delayed replicas, and failover strategies.                                        | [Link](https://mariadb.com/database-topics/disaster-recovery/)                                              |
| **Storage & Modeling**             | InnoDB                                 | Default transactional storage engine with ACID compliance and foreign key support.                                                 | [Link](https://mariadb.com/kb/en/innodb/)                                                                   |
|                                    | Aria                                   | Crash-safe alternative to MyISAM, used for internal temporary tables.                                                              | [Link](https://mariadb.com/kb/en/aria/)                                                                     |
|                                    | MyISAM                                 | Non-transactional engine, supports FULLTEXT indexing and spatial data types.                                                       | [Link](https://mariadb.com/kb/en/myisam/)                                                                   |
|                                    | MEMORY                                 | Stores all data in RAM for fast access in environments that require quick lookups.                                                 | [Link](https://mariadb.com/kb/en/memory-storage-engine/)                                                    |
|                                    | XtraDB                                 | Enhanced fork of InnoDB with improved performance and scalability.                                                                 | [Link](https://mariadb.com/kb/en/xtradb/)                                                                   |
|                                    | Storage Engines Overview               | Comprehensive guide to all available storage engines in MariaDB.                                                                   | [Link](https://mariadb.com/docs/server/reference/storage-engines/storage-engines-storage-engines-overview/) |
|                                    | Semi-Structured Data                   | Support for JSON and hybrid data models to enable flexible data modeling.                                                          | [Link](https://mariadb.com/database-topics/semi-structured-data/)                                           |
|                                    | Spider                                 |                                                                                                                                    |                                                                                                             |

These components collectively empower the MariaDB Platform to cater to diverse database management needs, from transactional operations to data analytics and enterprise-grade security.



<table data-view="cards"><thead><tr><th></th><th data-type="content-ref"></th></tr></thead><tbody><tr><td>MariaDB Server</td><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/">Server</a></td></tr><tr><td>MariaDB Connectors</td><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/CjGYMsT2MVP4nd3IyW2L/">Connectors</a></td></tr><tr><td>MariaDB ColumnStore</td><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/">ColumnStore</a></td></tr><tr><td>MariaDB MaxScale</td><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/">MaxScale</a></td></tr></tbody></table>

