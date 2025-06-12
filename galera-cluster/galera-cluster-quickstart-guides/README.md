---
icon: rabbit-running
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
    visible: false
---

# Quickstart Guides

MariaDB's Galera Cluster Quickstart Guides provide essential steps for setting up a highly available, multi-master cluster with synchronous replication. These guides cover prerequisites, installation via package managers, configuration, bootstrapping a new cluster, adding nodes, and verifying replication for robust database operations. MariaDB's Galera Cluster Quickstart Guides simplify setting up highly available, multi-master synchronous replication. They cover installation via package managers, configuration, bootstrapping new clusters, adding nodes, and verifying replication.

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><p><strong>What is Galera Cluster?</strong></p><p><em>MariaDB Galera Cluster is a Linux-exclusive, multi-primary cluster designed for MariaDB, offering features such as active-active topology, read/write capabilities on any node, automatic membership and node joining, true parallel replication at the row level, and direct client connections, with an emphasis on the native MariaDB experience.</em></p></td><td><a href="https://mariadb.net/docs/galera-cluster/galera-cluster-quickstart-guides/mariadb-galera-cluster-guide">https://mariadb.net/docs/galera-cluster/galera-cluster-quickstart-guides/mariadb-galera-cluster-guide</a></td><td><a href="../.gitbook/assets/blue-1200x628.png">blue-1200x628.png</a></td></tr><tr><td><p><strong>What is Galera Replication?</strong></p><p><em>In Galera Cluster, transactions are replicated using the wsrep API, synchronously ensuring consistency across nodes. Synchronous replication offers high availability and consistency but is complex and potentially slower compared to asynchronous replication. Due to these challenges, asynchronous replication is often preferred for database performance and scalability, as seen in popular systems like MySQL and PostgreSQL, which typically favor asynchronous or semi-synchronous solutions.</em></p></td><td><a href="about-galera-replication.md">about-galera-replication.md</a></td><td><a href="../.gitbook/assets/blue-bright-1200x628.png">blue-bright-1200x628.png</a></td></tr><tr><td><p><strong>MariaDB Galera Cluster Quickstart</strong></p><p><em>MariaDB Galera Cluster is a solution designed to handle high workloads exceeding the capacity of a single server. It is based on Galera Cluster technology integrated with MariaDB Enterprise Server and includes features like data-at-rest encryption for added security. This multi-primary replication alternative is ideal for maintaining data consistency across multiple servers, providing enhanced reliability and scalability.</em></p></td><td><a href="mariadb-galera-cluster-usage-guide.md">mariadb-galera-cluster-usage-guide.md</a></td><td><a href="../.gitbook/assets/decorative-waves-orange-blue.jpg">decorative-waves-orange-blue.jpg</a></td></tr></tbody></table>
