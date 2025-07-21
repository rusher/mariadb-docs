---
description: Data-at-rest encryption secures data on the file system.
---

# MariaDB Enterprise Server - Data-at-Rest Encryption

## Overview

[MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) and MariaDB Community Server support data-at-rest encryption, which secures data on the file system. The server and storage engines encrypt data before writing and decrypt it during reads, ensuring that the data is only unencrypted when accessed directly through the server.

## Encryption Plugins

| Topic                         | Resources                                                                                                                                                                                                                                                                                                                                |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Encryption Plugins            | [Choosing an Encryption Plugin](encryption-plugins/choosing-an-encryption-plugin.md)                                                                                                                                                                                                                                                     |
| HashiCorp Vault               | [Understanding the HashiCorp Vault Encryption Plugin](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-differences/mariadb-enterprise-server-data-at-rest-encryption/hashicorp-vault-understanding-the-hashicorp-vault-encryption-plugin/README.md) |
| Amazon Web Services (AWS) KMS | [Understanding the AWS KMS Encryption Plugin](encryption-plugins/amazon-web-services-aws-kms-understanding-the-amazon-web-services-aws-kms-e.md)                                                                                                                                                                                         |
| File Key Management           | [Understanding the File Key Management Encryption Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin)                                                           |

## Storage Engine Encryption

| Topic                                                                                        | Resources                                                                                                                                                                           |
| -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) | [Encrypting InnoDB Data](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption) |
| [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria)     | [Encrypting Aria Data](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/aria-encryption)     |

## Replication Cache Encryption

| Topic                                                                                                                    | Resources                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Binary Logs                                                                                                              | [Encrypting Binary Logs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/encrypting-binary-logs) |
| [Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) Gcache | [Encrypting Galera Cluster's Gcache](encrypting-galera-clusters-gcache.md)                                                                                                               |

Additional information is available on the [MariaDB documentation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption).
