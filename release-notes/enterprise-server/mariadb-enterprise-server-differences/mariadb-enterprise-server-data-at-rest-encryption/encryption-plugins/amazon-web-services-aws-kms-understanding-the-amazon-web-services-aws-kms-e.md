# Understanding the Amazon Web Services (AWS) KMS Encryption Plugin

##

## Overview

The AWS KMS Encryption Plugin (aws\_key\_management) integrates with Amazon Web Services (AWS) KMS.

## When to Use the AWS KMS Encryption Plugin?

The AWS KMS Encryption Plugin (aws\_key\_management) allows you to:

* Use [AWS KMS](https://aws.amazon.com/kms/) to manage MariaDB's encryption keys.
* Encrypt MariaDB data using those keys, including:
  * [InnoDB Data](https://mariadb.com/kb/en/encrypting-innodb-data)
  * [Aria Data](https://mariadb.com/kb/en/encrypting-aria-data)
  * [Binary Logs](https://mariadb.com/kb/en/mariadb-enterprise-server-data-at-rest-encryption-encrypting-binary-logs)
  * [Galera Cluster's GCache](../encrypting-galera-clusters-gcache.md)
* Rotate encryption keys.

Additional information is available [here](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin).

Copyright © 2025 MariaDB
