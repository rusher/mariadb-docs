# MySqlConnector for ADO.NET

MySqlConnector is an ADO.NET data provider with support for MariaDB Server. It is licensed under the [MIT License](https://github.com/mysql-net/MySqlConnector/blob/master/LICENSE/).

* [Installation via NuGet](https://www.nuget.org/packages/MySqlConnector/)
* [Documentation](https://mysql-net.github.io/MySqlConnector/)
* [Version History](https://mysql-net.github.io/MySqlConnector/overview/version-history/)
* [GitHub](https://github.com/mysql-net/MySqlConnector/)
* [On Travis](https://travis-ci.org/mysql-net/MySqlConnector/pull_requests/)

### MariaDB Contributions

* Support [zero-configuration SSL](https://mariadb.org/mission-impossible-zero-configuration-ssl/) with MariaDB: [#1500](https://github.com/mysql-net/MySqlConnector/pull/1500)
  * For MariaDB Server 11.4+
  * Available from version [2.4.0](https://github.com/mysql-net/MySqlConnector/releases/tag/2.4.0)
* Rewrite server redirection logic based on latest MariaDB specification: [#1499](https://github.com/mysql-net/MySqlConnector/pull/1499)
  * For MariaDB Server 11.3+
  * Available from version [2.4.0](https://github.com/mysql-net/MySqlConnector/releases/tag/2.4.0)
* Performance: Avoid SET NAMES commands when not necessary: [#1497](https://github.com/mysql-net/MySqlConnector/pull/1497)
  * For MariaDB Server 11.5+
  * Available from version [2.4.0](https://github.com/mysql-net/MySqlConnector/releases/tag/2.4.0)
* Performance improvements
  * Implement faster parsing for result sets with multiple rows: [#1330](https://github.com/mysql-net/MySqlConnector/pull/1330)
  * Support per-query variables for CommandBehavior.SchemaOnly and SingleRow: [#1312](https://github.com/mysql-net/MySqlConnector/pull/1312)
  * Support skipping metadata for prepared statements with [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106) and later: [#1301](https://github.com/mysql-net/MySqlConnector/pull/1301)
  * Available from version [2.3.0](https://github.com/mysql-net/MySqlConnector/releases/tag/2.3.0)
* Support new MariaDB version numbers: [#1259](https://github.com/mysql-net/MySqlConnector/issues/1259)
  * For MariaDB Server 11.0+
  * Available from version [2.2.6](https://github.com/mysql-net/MySqlConnector/releases/tag/2.2.6)
* Support [MariaDB GSSAPI authentication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi): [#577](https://github.com/mysql-net/MySqlConnector/pull/577)
  * Available from version [0.47.0](https://github.com/mysql-net/MySqlConnector/releases/tag/0.47.0)


{% @marketo/form formid="4316" %}
