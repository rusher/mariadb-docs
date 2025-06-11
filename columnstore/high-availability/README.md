---
icon: bolt
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

# High Availability

MariaDB ColumnStore offers high availability through multi-node deployments. It utilizes shared storage (like NFS or S3) so remaining nodes can access data upon failure. MariaDB MaxScale enhances this with monitoring and automatic failover for continuous analytical processing.

