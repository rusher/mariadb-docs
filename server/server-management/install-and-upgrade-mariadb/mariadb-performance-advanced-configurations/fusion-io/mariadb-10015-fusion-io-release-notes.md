# MariaDB 10.0.15 Fusion-io Release Notes

**Note:** This page describes features in an _**unreleased**_ version of MariaDB._**Unreleased**_ means there are no official packages or\
binaries available for download which contain the features. If you want to try out any of the new features described here you will\
need to [get](../../../../clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code.md) and [compile](../../compiling-mariadb-from-source/) the\
code yourself.

[Download](https://ftp.osuosl.org/pub/mariadb/mariadb-10.0.15-fusion-io/)[Release Notes](mariadb-10015-fusion-io-release-notes.md)[Changelog](mariadb-10015-fusion-io-changelog.md)[Fusion-io Introduction](fusion-io-introduction.md)

**Release date:** 12 Dec 2014

**For an overview of** [**MariaDB 10.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0) **Fusion-io see the**[**Fusion-io Introduction**](fusion-io-introduction.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

Since the [MariaDB 10.0.9 Fusion-io preview](https://blog.mariadb.org/significant-performance-boost-with-new-mariadb-page-compression-on-fusionio/) release, the following notable changes have been made.

* Merged with [MariaDB 10.0.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10015-release-notes) release
* Added support for 4K sector size if supported
  * Added status variables for 1K, 2K, 4K, 8K, 16K, and 32K trims
* Added innodb-compression-algorithm configuration variable to select default compression method
* Added support for
  * LZO compression
  * LZMA compression
  * bzip2 compression

## Other Changes

For a complete list of changes made in [MariaDB 10.0.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10015-release-notes), with links to detailed\
information on each push, see the [changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/changelogs/changelogs-mariadb-100-series/mariadb-10015-changelog).

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the[Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/readme-1)\
page.

CC BY-SA / Gnu FDL
