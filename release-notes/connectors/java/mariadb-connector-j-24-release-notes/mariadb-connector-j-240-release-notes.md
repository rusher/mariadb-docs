# MariaDB Connector/J 2.4.0 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.com/Connectors/java/connector-java-2.4.0)[Release Notes](mariadb-connector-j-240-release-notes.md)[Changelog](../changelogs/mariadb-connectorj-24-changelogs/mariadb-connector-j-240-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 29 Jan 2019

MariaDB Connector/J 2.4.0 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

NOTE: MariaDB Connector/J 2.4.0 is fully compatible with the latest release of version 2.3. Further maintenance releases will not be provided for version 2.3.

\[[CONJ-654](https://jira.mariadb.org/browse/CONJ-654)] change metadata behaviour: DatabaseMetaData.getDatabaseProductName() nows return "MariaDB"/"MySQL" according to server.\
This can cause some incompatibilities with some libraries and products that do not yet know Database Type "MariaDB"

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

### Evolutions

* [CONJ-675](https://jira.mariadb.org/browse/CONJ-675): permit multiple alternative authentication methods for the same user ([future MariaDB 10.4 feature](https://jira.mariadb.org/browse/MDEV-11340))
* [CONJ-678](https://jira.mariadb.org/browse/CONJ-678): permit indication of truststore/keystore type (JKS/PKCS12), then not relying on java default type
* [CONJ-378](https://jira.mariadb.org/browse/CONJ-378): GSSAPI: client can provide SPN
* [CONJ-667](https://jira.mariadb.org/browse/CONJ-667): Support MYSQL\_TYPE\_JSON datatype
* [CONJ-652](https://jira.mariadb.org/browse/CONJ-652): buffering available socket buffer for faster results (specifically for huge resultset)
* [CONJ-659](https://jira.mariadb.org/browse/CONJ-659): improve text performance parsing date/time/timestamp resultset
* [CONJ-670](https://jira.mariadb.org/browse/CONJ-670): ability to always refresh SSL certificate

### New options

| useReadAheadInput    | keyStoreType                                                                                                                                                        | trustStoreType | servicePrincipalName |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | -------------------- |
| useReadAheadInput    | use a buffered inputSteam that read socket available data. Default: true                                                                                            |                |                      |
| keyStoreType         | indicate key store type (JKS/PKCS12). default is null, then using java default type.                                                                                |                |                      |
| trustStoreType       | indicate trust store type (JKS/PKCS12). default is null, then using java default type                                                                               |                |                      |
| servicePrincipalName | when using GSSAPI authentication, SPN (Service Principal Name) use the server SPN information. When set, connector will use this value, ignoring server information |                |                      |

### Bug fixes

* [CONJ-646](https://jira.mariadb.org/browse/CONJ-646): possible NullPointerException when connection lost to database using aurora configuration with one node
* [CONJ-672](https://jira.mariadb.org/browse/CONJ-672): batch using multi-send can hang when using query timeout
* [CONJ-544](https://jira.mariadb.org/browse/CONJ-544): disable SSL session resumption when using SSL
* [CONJ-589](https://jira.mariadb.org/browse/CONJ-589): correcting Clob.length() for utf8mb4
* [CONJ-649](https://jira.mariadb.org/browse/CONJ-649): datasource connectTimeout URL parameter is not honoured
* [CONJ-650](https://jira.mariadb.org/browse/CONJ-650): Correction on resultset.getObject(columnName, byte\[].class) when value is NULL
* [CONJ-665](https://jira.mariadb.org/browse/CONJ-665): old MySQL (<5.5.3) doesn't support utf8mb4, using utf8 on 3 bytes as connection charset by default
* [CONJ-671](https://jira.mariadb.org/browse/CONJ-671): MariaDb bulk threads occupy full cpu(99%) while db connections broken
* [CONJ-673](https://jira.mariadb.org/browse/CONJ-673): abording a connection while fetching a query still does read whole resultset
* [CONJ-669](https://jira.mariadb.org/browse/CONJ-669): SQLSyntaxErrorException when querying on empty column name
* [CONJ-674](https://jira.mariadb.org/browse/CONJ-674): make dumpQueriesOnException = false by default as per documentation

### Minor

* [CONJ-644](https://jira.mariadb.org/browse/CONJ-644): small optimization when validating galera connection
* [CONJ-625](https://jira.mariadb.org/browse/CONJ-625): add coverage test
* [CONJ-654](https://jira.mariadb.org/browse/CONJ-654): DatabaseMetaData.getDriverName() returns connector/J with a lowercase c, DatabaseMetaData.getDatabaseProductName() "MariaDB"/"MySQL" according to server

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.
