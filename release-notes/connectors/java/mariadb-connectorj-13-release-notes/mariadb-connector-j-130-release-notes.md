# MariaDB Connector/J 1.3.0 Release notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of [MariaDB Connector/J](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) is:[**MariaDB Connector/J 3.5.3**](../mariadb-connector-j-3-5-release-notes/mariadb-connector-j-3-5-3-release-notes.md)

[Download](https://downloads.mariadb.org/connector-java/1.3.0/)[Release Notes](mariadb-connector-j-130-release-notes.md)[Changelog](../changelogs/mariadb-connector-j-13-changelogs/mariadb-connector-j-130-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 16 Nov 2015

MariaDB Connector/J 1.3.0 is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For a description of the MariaDB Connector/J see the**[**About the MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-the-mariadb-connector-j/README.md) **page.**

For a list of all changes made in this release, with links to detailed\
information on each push, see the[changelog](../changelogs/mariadb-connector-j-13-changelogs/mariadb-connector-j-130-changelog.md).

## Notable changes and additions

This release includes the following major enhancements :

* Prepared statement on server side.
* Improving memory footprint
* New Date/Time/Timestamps implementation
* New failover options

### Prepared statements on server side

A prepared statement is a feature used to execute the same (or similar) SQL\
statements repeatedly with high efficiency.

This functionality is now executed on the server side.

For example:

```java
PreparedStatement pst = connection.prepareStatement("INSERT INTO exemple VALUES (?)");
int i=1000;
while(i>0) {
    pst.setInt(1, i--);
    pst.addBatch();
}           
pst.executeBatch();
```

When executing `connection.prepareStatement` the query will be sent to the\
server. The server will return a statement ID.

When executing `executeBatch`, only this statement ID will be sent with the\
query parameter.

This improves performance when many queries are to be executed.

The following new parameters have been added :

| cachePrepStmts        | prepStmtCacheSize                                                                                                     | prepStmtCacheSqlLimit |
| --------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------- |
| cachePrepStmts        | Enable/disable prepared statement cache default is true                                                               |                       |
| prepStmtCacheSize     | Sets the number of prepared statements that the driver will cache per VM if cachePrepStmts is enabled. default is 250 |                       |
| prepStmtCacheSqlLimit | Maximum length of a prepared SQL statement that the driver will cache if cachePrepStmts is enabled. default is 2048   |                       |

The prepared statement will be cached according to the above parameters.

### Memory improvement

The memory footprint has been improved for query text and especially for\
prepared statements.

### New Date/Time/Timestamps implementation

A new parameter is added :

| useLegacyDatetimeCode |
| --------------------- |
| useLegacyDatetimeCode |

There is no change when the parameter `useLegacyDatetimeCode` is not specified\
or is `true` (it is `true` by default). When this parameter is set to`false` in the JDBC connection string, the new implementation is used.\
Therefore, the time zone of the server will be used, taking into account the\
time changes.

Example with a particular timezone:

| UTC TIME                  | PARIS TIME                | CANADA TIME               |
| ------------------------- | ------------------------- | ------------------------- |
| UTC TIME                  | PARIS TIME                | CANADA TIME               |
| 2015- 2- 29T00:45:00+0000 | 2015- 2- 29T01:45:00+1000 | 2015- 2- 28 21:45:00-3000 |
| 2015- 2- 29T01:15:00+0000 | 2015- 2- 29T03:15:00+2000 | 2015- 2- 28 22:15:00-3000 |

If Connector/Java is using the "Europe/Paris" timezone, server "Canada/Atlantic" (UTC recommended, but not mandatory).

```
TimeZone.setDefault(TimeZone.getTimeZone("Europe/Paris"));
connection.createStatement().execute("CREATE TABLE daylight (t1 TIMESTAMP(6), t2 DATETIME(6))");
PreparedStatement pst = connection.prepareStatement("INSERT INTO daylight VALUES (?, ?)");
pst.setTimestamp(1, Timestamp.valueOf("2015-03-29 01:45:00"));
pst.setTimestamp(2, Timestamp.valueOf("2015-03-29 03:15:00"));
...
```

Using `useLegacyDatetimeCode=false` or not will return the same result :

```
ResultSet res = connection.createStatement().executeQuery("SELECT * FROM daylight");
res.next();
assertEquals(res.getTimestamp(1),Timestamp.valueOf("2015-03-29 01:45:00"));
assertEquals(res.getTimestamp(2),Timestamp.valueOf("2015-03-29 01:45:00"));
res.next();
assertEquals(res.getTimestamp(1),Timestamp.valueOf("2015-03-29 03:15:00"));
assertEquals(res.getTimestamp(2),Timestamp.valueOf("2015-03-29 03:15:00"));
```

The difference will be on the saved data :

with `useLegacyDatetimeCode=false`:

| t1                         | t2                         |
| -------------------------- | -------------------------- |
| t1                         | t2                         |
| 2015-03-28 21:45:00.000000 | 2015-03-28 22:15:00.000000 |

with `useLegacyDatetimeCode=true`:

| t1                         | t2                         |
| -------------------------- | -------------------------- |
| t1                         | t2                         |
| 2015-03-29 01:45:00.000000 | 2015-03-29 03:15:00.000000 |

### New failover options

#### AssureReadOnly parameter

A new parameter is added :

| assureReadOnly |
| -------------- |
| assureReadOnly |

When switching host to a slave (by using "connection.setReadOnly(true);" for\
example), if the database permit it, the connector was always setting the\
connection in read-only mode, so an Exception will be thrown if a data\
modification is done on a slave.

To improve performance, this operation will not be performed if the parameter\
is a assureReadOnly false (default). It's up to you to configure the slaves\
servers in[read\_only mode](https://mariadb.com/blog/looking-slave-consistency-say-yes-read-only-and-no-super-and-slave-skip-errors).

#### Sequential failover parameter

A new type of failover implementation as been added : Sequential.

This permits failover WITHOUT loadbalancing.

the host will be connected in the order in which they were declared.

Example when using the jdbc url string "jdbc:mysql:replication:_host1,host2,host3/test"._\
&#xNAN;_&#x57;hen connecting, the driver will always try first host1, and if not available host2 and following._\
&#xNAN;_&#x41;fter a host fail, the driver will reconnect according to this order._

Example :

Connecting order:

* trying to connect to host1. Host1 is up, the driver will use this host.
* host1 fail. The driver will connect to Host2.
* host2 fail. If the host1 is not blacklisted anymore (timeout configure with\
  the `loadBalanceBlacklistTimeout` parameter) the driver will try to connect\
  to host1, and after host3. If host1 was blacklisted, driver would connect to\
  host3 directly.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
