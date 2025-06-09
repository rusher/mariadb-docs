# Choosing an Encryption Plugin

##

## Overview

[MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) and MariaDB Community Server support data-at-rest encryption, which secures data on the file system. The server and storage engines encrypt data before writing and decrypt during reads, ensuring that the data is only unencrypted when accessed directly through the server.

They support multiple encryption plugins, which are suited for different use cases.

| Encryption Plugin                                                                                                                                                                                                                                                                                                                   | Description                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Encryption Plugin                                                                                                                                                                                                                                                                                                                   | Description                                                                                                                              |
| [HashiCorp Vault](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-differences/mariadb-enterprise-server-data-at-rest-encryption/encryption-plugins/hashicorp-vault-understanding-the-hashicorp-vault-encryption-plugin/README.md)             | • It integrates with HashiCorp Vault • It supports key rotation • It securely communicates with the remote KMS using TLS.                |
| [Amazon Web Services (AWS) KMS](amazon-web-services-aws-kms-understanding-the-amazon-web-services-aws-kms-e.md)                                                                                                                                                                                                                     | • It integrates with AWS KMS. • It supports key rotation. • It must be compiled from source.                                             |
| [File Key Management](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-differences/mariadb-enterprise-server-data-at-rest-encryption/encryption-plugins/file-key-management-understanding-the-file-key-management-encryption-plugin/README.md) | • stores encryption keys in a local plain-text key file. • The plain-text key file can be encrypted. • It does not support key rotation. |

| Feature                                | HashiCorp Vault | Amazon Web Services (AWS) KMS | File Key Management\\ |
| -------------------------------------- | --------------- | ----------------------------- | --------------------- |
| Feature                                | HashiCorp Vault | Amazon Web Services (AWS) KMS | File Key Management\\ |
| Supported by MariaDB Enterprise Server | Yes             | Yes                           | Yes                   |
| Supported by MariaDB Community Server  | No              | Yes                           | Yes                   |
| Supports key rotation                  | Yes             | Yes                           | No                    |

Copyright © 2025 MariaDB

{% @marketo/form formid="4316" formId="4316" %}
