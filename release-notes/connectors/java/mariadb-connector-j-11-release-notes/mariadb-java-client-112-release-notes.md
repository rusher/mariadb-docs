# MariaDB Java Client 1.1.2 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/client-java/1.1.2/) | **Release Notes** | [Changelog](../changelogs/mariadb-connector-j-11-changelogs/mariadb-java-client-112-changelog.md) |[Java Client Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-the-mariadb-java-client/README.md)

**Release date:** 02 May 2013

MariaDB Java Client 1.1.2 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release. In general this means that there are no known serious bugs,\
except for those marked as feature requests, that no bugs were fixed\
since last release that caused a notable code changes, and that we\
believe the code is ready for general usage (based on bug inflow).

**For a description of the MariaDB Java Client see the**[**About the MariaDB Java Client**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-the-mariadb-java-client/README.md) **page.**

For a list of changes made in this release, with links to detailed\
information on each push, see the[changelog](../changelogs/mariadb-connector-j-11-changelogs/mariadb-java-client-112-changelog.md).

## Bugs fixed in this release

MariaDB Java Client 1.1.2 is a bug fix release. Some of the bugs fixed include\
the following:

* `PreparedStatement.getMetaData()` will now return correct ResultSet\
  metadata, also prior to statement execution. In this case, to retrieve\
  metadata, statement will be prepared on the server side. ([CONJ-21](https://jira.mariadb.org/browse/CONJ-21))
* Performance enhancement : `Connection.getAutoCommit()` will not more issue\
  not issue "`select @@autocommit`" query anymore. This information is also\
  available in on status flags sent with OK/EOF protocol packets.\
  Also, `Connection.setAutoCommit()` will be a no-op, if autocommit status is\
  already the same as desired one ([CONJ-30](https://jira.mariadb.org/browse/CONJ-30))
* Fixed several issues with CLOB datatype\
  and `ResultSet.setCharacterStream()` -non-ASCII character could get lost\
  after `setCharacterStream()`. CLOB was errneously sent to server as binary\
  (using `_BINARY` introducer). ([CONJ-31](https://jira.mariadb.org/browse/CONJ-31))
* CHAR BINARY and VARCHAR BINARY were errnously handled as binary type. They\
  are now correctly treated as CHAR/VARCHAR with binary collation. ([CONJ-28](https://jira.mariadb.org/browse/CONJ-28))
* `Blob.getBinaryStream()` could return blob with incorrect size ([CONJ-31](https://jira.mariadb.org/browse/CONJ-31))
* Fix server version string for MariaDB Server 10.0.2 ([CONJ-32](https://jira.mariadb.org/browse/CONJ-32))
