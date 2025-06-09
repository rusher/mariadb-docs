# MariaDB Connector/J 1.3.5 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/1.3.5/)[Release Notes](mariadb-connector-j-135-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-13-changelogs/mariadb-connector-j-135-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 09 Feb 2016

MariaDB Connector/J 1.3.5 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_\
release.

**For a description of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

For a list of all changes made in this release, with links to detailed\
information on each push, see the[changelog](../changelogs/mariadb-connector-j-13-changelogs/mariadb-connector-j-135-changelog.md).

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

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

{% @marketo/form formid="4316" formId="4316" %}
