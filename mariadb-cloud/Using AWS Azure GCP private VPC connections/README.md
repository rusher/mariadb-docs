---
layout:
  width: default
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
  metadata:
    visible: true
---

# Using AWS/AZURE/GCP Private VPC Connections

By default, connections to MariaDB Cloud cloud databases occur with TLS/SSL encryption and can be initiated only from allowlisted IP addresses.

Some customers have regulatory requirements or information security policies that prohibit database connections over the public internet, and result in a requirement for private connections.

MariaDB Cloud cloud databases can optionally be configured for private connections between your VPC (virtual private clouds) and MariaDB Cloud cloud databases:

* [AWS PrivateLink](<Setting up AWS Private Link.md>) is supported for MariaDB Cloud cloud databases on AWS
* [Azure PrivateLink](<Setting up Azure Private Link.md>) is supported for MariaDB Cloud cloud databases on Azure
* [Private Service Connect](<Setting up GCP Private Service Connect.md>) is supported for MariaDB Cloud cloud databases on GCP
