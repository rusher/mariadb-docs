
# Data-at-Rest Encryption Overview


## Overview


Having tables encrypted makes it almost impossible for someone to access or
steal a hard disk and get access to the original data. MariaDB got Data-at-Rest Encryption with [MariaDB 10.1](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md). This functionality is also known as "Transparent Data Encryption (TDE)".


This assumes that encryption keys are stored on another system.


Using encryption has an overhead of roughly *3-5%*.


## Which Storage Engines Does MariaDB Encryption Support?


MariaDB encryption is fully supported for the [InnoDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md) storage engines. Encryption is also supported for the Aria storage engine, but only for tables created with `ROW_FORMAT=PAGE` (the default), and for the binary log (replication log).


MariaDB allows the user to configure flexibly what to encrypt. In or InnoDB, one can choose to encrypt:


* everything — all tablespaces (with all tables) (with [innodb_encrypt_tables=1](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables))
* individual tables
* everything, excluding individual tables


Additionally, one can choose to encrypt InnoDB log files (recommended, with [innodb_encrypt_log=1](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_log)) and InnoDB Temporary Tables (with [innodb_encrypt_temporary_tables=1](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_temporary_tables)).


When [innodb_encrypt_log=1](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_log) or [innodb_encrypt_temporary_tables=1](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_temporary_tables) an encryption key of 1 must be defined. See [Enabling InnoDB Encryption](innodb-encryption/innodb-enabling-encryption.md).


## Limitations


These limitations exist in the data-at-rest encryption implementation:


* Only data and only at rest is encrypted. Metadata (for example `.frm` files) and data sent to the client are not encrypted (but see [Secure Connections](../data-in-transit-encryption/secure-connections-overview.md)).
* Only the MariaDB server knows how to decrypt the data, in particular

  * [mariadb-binlog](../../../../../connectors/mariadb-connector-c/mariadb-binlogreplication-api-reference.md) can read encrypted binary logs only when --read-from-remote-server is used ([MDEV-8813](https://jira.mariadb.org/browse/MDEV-8813)).
  * [Percona XtraBackup](../../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md) cannot back up instances that use encrypted InnoDB. However, MariaDB's fork, [MariaDB Backup](../../../../server-management/getting-installing-and-upgrading-mariadb/migrating-to-mariadb/migrating-to-mariadb-from-sql-server/mariadb-backups-overview-for-sql-server-users.md), can back up encrypted instances.
* The disk-based [Galera gcache](https://galeracluster.com/library/documentation/state-transfer.html#write-set-cache-gcache) is not encrypted in the community version of MariaDB Server ([MDEV-9639](https://jira.mariadb.org/browse/MDEV-9639)). However, this file is encrypted in [MariaDB Enterprise Server 10.4](https://mariadb.com/docs/features/mariadb-enterprise-server/).
* The [Audit plugin](../../../../reference/plugins/mariadb-audit-plugin/release-notes-mariadb-audit-plugin/mariadb-audit-plugin-113-release-notes.md) cannot create encrypted output. Send it to syslog and configure the protection there instead.
* File-based [general query log](../../../../server-management/server-monitoring-logs/general-query-log.md) and [slow query log](../../../../server-management/server-monitoring-logs/slow-query-log/slow-query-log-overview.md) cannot be encrypted ([MDEV-9639](https://jira.mariadb.org/browse/MDEV-9639)).
* The Aria log is not encrypted ([MDEV-8587](https://jira.mariadb.org/browse/MDEV-8587)). This affects only non-temporary Aria tables though.
* The MariaDB [error log](../../../../server-management/server-monitoring-logs/error-log.md) is not encrypted. The error log can contain query text and data in some cases, including crashes, assertion failures, and cases where InnoDB write monitor output to the log to aid in debugging. It can be sent to syslog too, if needed.


## Encryption Key Management


MariaDB's data-at-rest encryption requires the use of a [key management and encryption plugin](key-management-and-encryption-plugins/encryption-key-management.md). These plugins are responsible both for the management of encryption keys and for the actual encryption and decryption of data.


MariaDB supports the use of [multiple encryption keys](key-management-and-encryption-plugins/encryption-key-management.md#using-multiple-encryption-keys). Each encryption key uses a 32-bit integer as a key identifier. If the specific plugin supports [key rotation](key-management-and-encryption-plugins/encryption-key-management.md#rotating-keys), then encryption keys can also be rotated, which creates a new version of the encryption key.


How MariaDB manages encryption keys depends on which encryption key management solution you choose. Currently, MariaDB has four options:


* [File Key Management Plugin](key-management-and-encryption-plugins/file-key-management-encryption-plugin.md)
* [AWS Key Management Plugin](key-management-and-encryption-plugins/aws-key-management-encryption-plugin-setup-guide.md)
* [Eperi Key Management Plugin](key-management-and-encryption-plugins/eperi-key-management-encryption-plugin.md)
* [Hashicorp Key Management Plugin](key-management-and-encryption-plugins/hashicorp-key-management-plugin.md)


Once you have an key management and encryption plugin set up and configured for your server, you can begin using encryption options to better secure your data.


## Encrypting Data


Encryption occurs whenever MariaDB writes pages to disk. Encrypting table data requires that you install a [key management and encryption plugin](key-management-and-encryption-plugins/encryption-key-management.md), such as the [File Key Management](key-management-and-encryption-plugins/file-key-management-encryption-plugin.md) plugin. Once you have a plugin set up and configured, you can enable encryption for your InnoDB and Aria tables.


### Encrypting Table Data


MariaDB supports data-at-rest encryption for InnoDB and Aria storage engines. Additionally, it supports encrypting the [InnoDB redo log](../../../../reference/storage-engines/innodb/innodb-redo-log.md) and internal on-disk temporary tables that use the Aria storage engine..


* [Encrypting Data for InnoDB](innodb-encryption/innodb-encryption-overview.md)
* [Encrypting Data for Aria](aria-encryption/aria-encryption-overview.md)


### Encrypting Temporary Files


MariaDB also creates temporary files on disk. For example, a binary log cache will be written to a temporary file if the binary log cache exceeds `[binlog_cache_size](../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#binlog_cache_size)` or `[binlog_stmt_cache_size](../../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md#binlog_stmt_cache_size)`, and temporary files are also often used for filesorts during query execution. Since [MariaDB 10.1.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-5-release-notes.md), these temporary files can also be encrypted if [encrypt_tmp_files=ON](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#encrypt_tmp_files) is set.


Since [MariaDB 10.1.27](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10127-release-notes.md), [MariaDB 10.2.9](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1029-release-notes.md) and [MariaDB 10.3.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1032-release-notes.md), temporary files created internally by InnoDB, such as those used for merge sorts and row logs can also be encrypted if [innodb_encrypt_log=ON](../../../../reference/storage-engines/innodb/innodb-system-variables.md) is set. These files are encrypted regardless of whether the tables involved are encrypted or not, and regardless of whether [encrypt_tmp_files](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#encrypt_tmp_files) is set or not.


### Encrypting Binary Logs


MariaDB can also encrypt [binary logs](../../../../reference/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) (including [relay logs](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md)).


* [Encrypting Binary Logs](encrypting-binary-logs.md)


## Encryption and Page Compression


Data-at-rest encryption and [InnoDB page compression](../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md) can be used
together. When they are used together, data is first compressed, and then it is encrypted. In
this case you save space and still have your data protected.


## Thanks


* Tablespace encryption was donated to the MariaDB project by Google.
* Per-table encryption and key identifier support was donated to the MariaDB project by [eperi](https://eperi.de/en).


We are grateful to these companies for their support of MariaDB!


## See Also


* [Encryption functions](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/encryption-hashing-and-compression-functions/README.md)
* [DES_DECRYPT()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/encryption-hashing-and-compression-functions/des_decrypt.md)
* [DES_ENCRYPT()](../../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/encryption-hashing-and-compression-functions/des_encrypt.md)
* A [blog post about table encryption](https://mariadb.com/blog/table-and-tablespace-encryption-mariadb-101/) with benchmark results

<span></span>
