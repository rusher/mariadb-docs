# MariaDB Java Client 1.1.5 Changelog

The most recent [_**Stable**_](../../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/client-java/1.1.5/) |[Release Notes](../../mariadb-connector-j-11-release-notes/mariadb-java-client-115-release-notes.md) |**Changelog** |[Java Client Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-the-mariadb-java-client/README.md)

**Release date:** 18 Sep 2013

For the highlights of this release, see the[release notes](../../mariadb-connector-j-11-release-notes/mariadb-java-client-115-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #486](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/486)\
  Wed 2013-09-18 00:46:34 +0200
  * bump version
* [Revision #485](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/485)\
  Wed 2013-09-18 00:40:00 +0200
  * [CONJ-64](https://jira.mariadb.org/browse/CONJ-64) - can't connect to MySQL 5.5 (while connection to [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) works\
    ok)
  * The regression is caused by erroneously set `CLIENT_PLUGIN` flag in the\
    client authentication packet.

{% @marketo/form formid="4316" formId="4316" %}
