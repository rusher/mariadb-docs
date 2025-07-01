# MariaDB Connector/J 1.3.5 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../3.5/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/1.3.5/)[Release Notes](mariadb-connector-j-135-release-notes.md)[Changelog](../changelogs/1.3/mariadb-connector-j-135-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 09 Feb 2016

MariaDB Connector/J 1.3.5 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For a description of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

For a list of all changes made in this release, with links to detailed\
information on each push, see the[changelog](../changelogs/1.3/mariadb-connector-j-135-changelog.md).

This version is a bugfix release

## Notable changes and additions

### Major

* [CONJ-243](https://jira.mariadb.org/browse/CONJ-243) : correction getString on tinyInt false value

### Minor

* failover : Assure connection when a failover append during connection initialization :
* [CONJ-245](https://jira.mariadb.org/browse/CONJ-245): Check connection status before executing query
* Connection.prepareStatement() taking column indexes or names return generated keys

## Behavior change

* [CONJ-246](https://jira.mariadb.org/browse/CONJ-246): permit aurora single node cluster.

To permit development/integration on a single-node cluster, only one host can be defined with aurora configuration :

```
jdbc:(mysql|mariadb):aurora://<hostDescription>/[database][?<key1>=<value1>[&<key2>=<value2>]]
```

Driver will try to reconnect automatically after a failover.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
