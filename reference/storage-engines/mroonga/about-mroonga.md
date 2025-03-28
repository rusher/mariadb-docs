# About Mroonga

| Mroonga Version | Introduced | Maturity |
| --- | --- | --- |
| Mroonga Version | Introduced | Maturity |
| 7.07 | [MariaDB 10.2.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-102-series/mariadb-10211-release-notes), [MariaDB 10.1.29](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-101-series/mariadb-10129-release-notes) | Stable |
| 5.04 | [MariaDB 10.1.6](/en/mariadb-1016-release-notes/) | Stable |
| 5.02 | [MariaDB 10.0.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-100-series/mariadb-10018-release-notes), [MariaDB 10.1.5](/en/mariadb-1015-release-notes/) | Stable |
| 5.0 | [MariaDB 10.0.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-100-series/mariadb-10017-release-notes) | Stable |
| 4.06 | [MariaDB 10.0.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-100-series/mariadb-10015-release-notes) | Stable |

Mroonga is a full text search storage engine based on Groonga, which is an open-source CJK-ready (Chinese, Japanese, and Korean) fulltext search engine using column base. See [http://groonga.org](http://groonga.org) for more.

With Mroonga, you can have a CJK-ready full text search feature, and it is faster than the [MyISAM](../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk-table-information.md) and [InnoDB](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) [full text search](/en/full-text-indexes/) for both updating and searching.

Mroonga also supports Groonga's fast geolocation search by using MariaDB's geolocation SQL syntax.

Mroonga currently only supports Linux x86_64 (Intel64/AMD64).

#

# How to Install

Enable Mroonga with the following statement:

```
INSTALL SONAME 'ha_mroonga';
```

On Debian and Ubuntu mroonga engine will be installed with

```
sudo apt-get install mariadb-plugin-mroonga
```

See [Plugin overview](../../plugins/plugin-overview.md) for details on installing and uninstalling plugins.

[SHOW ENGINES](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-engines.md) can be used to check whether Mroonga is installed correctly:

```
SHOW ENGINES;
...
*************************** 8. row ***************************
 Engine: Mroonga
 Support: YES
 Comment: CJK-ready fulltext search, column store
Transactions: NO
 XA: NO
 Savepoints: NO
...
```

Once the plugin is installed, add a UDF (User-Defined Function) named "last_insert_grn_id", that returns the record ID assigned by groonga in INSERT, by the following SQL.

```
CREATE FUNCTION last_insert_grn_id RETURNS INTEGER SONAME 'ha_mroonga.so';
```

#

# Limitations

* The maximum size of a single key is 4096 bytes.
* The maximum size of all keys is 4GB.
* The maximum number of records in a fulltext index is 268,435,455
* The maximum number of distinct terms in a fulltext index is 268,435,455
* The maximum size of a fulltext index is 256GB

Note that the maximum sizes are not hard limits, and may vary according to circumstance.

For more details, see [http://mroonga.org/docs/reference/limitations.html](http://mroonga.org/docs/reference/limitations.html).

#

# Available Character Sets

Mroonga supports a limited number of [character sets](/en/data-types-character-sets-and-collations/). These include:

* ASCII
* BINARY
* CP932
* EUCJPMS
* KOI8R
* LATIN1
* SJIS
* UJIS
* UTF8
* UTF8MB4

#

# More Information

Further documentation for Mroonga can be found at [http://mroonga.org/docs/](http://mroonga.org/docs/)