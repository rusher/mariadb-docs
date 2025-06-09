# MariaDB Java Client 1.1.7 Changelog

The most recent [_**Stable**_](../../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/client-java/1.1.7/) |[Release Notes](../../mariadb-connector-j-11-release-notes/mariadb-java-client-117-release-notes.md) |**Changelog** |[Java Client Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-the-mariadb-java-client/README.md)

**Release date:** 3 Apr 2014

For the highlights of this release, see the[release notes](../../mariadb-connector-j-11-release-notes/mariadb-java-client-117-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #507](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/507)\
  Sat 2014-03-29 11:13:13 +0100
  * Bumped version number
* [Revision #506](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/506) \[merge]\
  Sat 2014-03-29 11:02:23 +0100
  * Implementation for LOAD DATA LOCAL INFILE based on a patch written by Tim Ruhl ([local-infile-inputstream](https://code.launchpad.net/~timruhl/mariadb-java-client/local-infile-inputstream))
  * [Revision #502.3.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/502.3.1)\
    Tue 2014-03-25 12:17:05 -0400
    * Implement load data local infile
* [Revision #505](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/505)\
  Sat 2014-03-29 09:32:01 +0100
  * Fixed "MySQL Protocol limit reached" error (when sending data > 2GB) by setting MAX\_SEQNO to max integer value.
* [Revision #504](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/504) \[merge]\
  Wed 2014-03-26 13:07:56 -0400
  * Merge: Add unwrap and isWrapperFor methods in MySQLStatement
  * [Revision #502.2.3](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/502.2.3)\
    Wed 2014-03-26 13:01:21 -0400
    * Add test case for Statement unwrap and isWrapperFor
  * [Revision #502.2.2](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/502.2.2)\
    Tue 2014-03-25 07:59:49 -0400
    * Javadoc update
  * [Revision #502.2.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/502.2.1)\
    Tue 2014-03-25 07:56:53 -0400
    * Add unwrap and isWrapperFor
* [Revision #503](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/503) \[merge]\
  Wed 2014-03-26 12:19:30 -0400
  * Merge from Massimo Siani: Return null for 'zero' timestamps
  * [Revision #502.1.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/502.1.1)\
    Tue 2014-03-25 13:00:46 -0400
    * Return null for 'zero' timestamps
* [Revision #502](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/502)\
  Thu 2014-03-13 19:06:38 +0100
  * Fix for [CONJ-84](https://jira.mariadb.org/browse/CONJ-84): If a select list contains the same column more than once, findColumn returns the last instance of the column. Special thanks to Kris Iyer for his patch!
* [Revision #501](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/501) \[merge]\
  Tue 2014-02-25 20:40:16 +0100
  * Merge from Massimo Siani: Avoid getting 'unknown command' with Galera cluster
  * [Revision #500.1.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/500.1.1)\
    Wed 2014-02-19 06:29:12 -0500
    * Avoid to use select when queries are not allowed
