# Changes and Improvements in MariaDB 12.0

[MariaDB 12.0](what-is-mariadb-120.md) is an upcoming [rolling release](../mariadb-release-model.md).

## Upgrading

* See [Upgrading Between Major MariaDB Versions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-between-major-mariadb-versions) and [Upgrading from MariaDB 10.11 to MariaDB 11.0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-11-to-mariadb-11-0).

## New Features

### Catalogs

* MariaDB [catalogs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/user-account-management/catalogs) are a multi-tenancy feature where a single instance MariaDB server handles multiple independent tenants (customers), who have their own users, schemas etc. See [MDEV-31542](https://jira.mariadb.org/browse/MDEV-31542) "Add multi-tenancy catalogs to MariaDB" for details.

### mariadb Client

* Can set an alternative directory path for searching scripts invoked via the source command, with the [--script-dir](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mariadb-command-line-client#-script-dir) mariadb client option ([MDEV-23818](https://jira.mariadb.org/browse/MDEV-23818))

## Security Vulnerabilities Fixed in [MariaDB 12.0](what-is-mariadb-120.md)

For a complete list of security vulnerabilities (CVEs) fixed across all\
versions of MariaDB, see the [Security Vulnerabilities Fixed in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security)\
page.\
Add listcve macro here - removed for performance reasons

## List of All [MariaDB 12.0](what-is-mariadb-120.md) Releases

| Date       | Release | Status | Release Notes | Changelog |
| ---------- | ------- | ------ | ------------- | --------- |
| Date       | Release | Status | Release Notes | Changelog |
| Unreleased |         | Alpha  |               |           |

{% @marketo/form formid="4316" formId="4316" %}
