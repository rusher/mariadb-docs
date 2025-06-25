# Differences in MariaDB Enterprise Server 10.4

MariaDB Enterprise Server is a premium version of MariaDB Community Server that focuses on stability, robustness, and predictability. For more information about MariaDB Enterprise Server in general please [look here](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md).

MariaDB Enterprise Server enables a predictable development and operations experience through an enterprise lifecycle. This enterprise lifecycle incorporates optimized builds, predictable release behavior, and vendor support. For more information about the Enterprise Server Lifecycle [look here](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md).

In addition to different release cycle, QA, and etc..., there are also feature differences. MariaDB Enterprise Server has different default settings to be more secure from the start and also only includes features that are fully supported and maintained.

In addition to this there are Enterprise Features and some backported features. The following are features that are in MariaDB Enterprise Server 10.4 but not in MariaDB Community Server 10.4:

Enterprise Features:

* [MariaDB Enterprise Backup](broken-reference)
* [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-enterprise-audit)
* Index limit increased to 128 indexes
* Slow master shutdown as default
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-galera-cluster-quickstart/README.md) (powered by Galera)
  * [Enhanced Enterprise Data-at-Rest Encryption](mariadb-enterprise-server-data-at-rest-encryption/)
* [Hashicorp Vault Plugin](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-differences/hashicorp-vault-understanding-the-hashicorp-vault-encryption-plugin/README.md)

Backported Features:

* [S3 Storage Engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine)
* New option [--require\_secure\_transport](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#require_secure_transport)
* GTID support for MariaDB Enterprise Cluster (powered by Galera)
* Crash recovery for semi-synchronous replication
* [mariadb-dump option --as-of](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump#options) to dump data as of a given time for system versioned tables
* JSON functions
  * [JSON\_NORMALIZE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_normalize)
  * [JSON\_EQUALS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_equals)
  * [JSON\_OVERLAPS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_overlaps)
  * [JSON\_SCHEMA\_VALID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_schema_valid)
* [Password Reuse Prevention Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/password-reuse-check-plugin)

{% @marketo/form formid="4316" formId="4316" %}
