# Differences in MariaDB Enterprise Server 11.4

MariaDB Enterprise Server is a premium version of MariaDB Community Server that focuses on stability, robustness, and predictability. For more information about MariaDB Enterprise Server in general please [look here](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md).

In addition to different release cycle, QA, and etc..., there are also feature differences. MariaDB Enterprise Server has different default settings to be more secure from the start and also only includes features that are fully supported and maintained.

In addition to this there are Enterprise Features and some backported features. The following are features that are in MariaDB Enterprise Server 11.4 but not in MariaDB Community Server 11.4:

Enterprise Features:

* [MariaDB Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backing-up-and-restoring-databases/mariabackup)
* [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-enterprise-audit)
* Index limit increased to 128 indexes
* Slow master shutdown as default
  * [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-galera-cluster-quickstart/README.md) (powered by Galera)
  * [Enhanced Enterprise Data-at-Rest Encryption](mariadb-enterprise-server-data-at-rest-encryption/)
  * XA Support
  * Non-Blocking operation for DDLs
  * TLS certificate expiration monitoring
  * SSL/TLS enabled by default
* [Hashicorp Vault Plugin](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-differences/hashicorp-vault-understanding-the-hashicorp-vault-encryption-plugin/README.md)
* Dynamic resize of [InnoDB redo log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-redo-log)
* Dynamic change of [InnoDB purge](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-purge) threads
* Sybase SQL mode for extended aliases

Backported Features:

* New, Detailed Replication Lag Representation
* New Information Schema Table For Password Related Data
* GTID binlog events now include the thread ID
* Automatic SST user account management for Galera
* PARSEC authentication plugin
* Extending timestamp range to 2106
* Limit size of created disk temporary files and tables

Copyright © 2025 MariaDB

{% @marketo/form formid="4316" formId="4316" %}
