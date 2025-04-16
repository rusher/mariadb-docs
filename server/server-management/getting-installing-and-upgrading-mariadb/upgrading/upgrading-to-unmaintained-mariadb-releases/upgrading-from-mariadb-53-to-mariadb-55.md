
# Upgrading from MariaDB 5.3 to MariaDB 5.5


## What you need to know


There are no changes in table or index formats between [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) and [MariaDB
5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md), so on most servers the upgrade should be painless.


### How to upgrade


The suggested upgrade procedure is:


1. For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md) instead.
1. Shutdown [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md)
1. Take a backup (this is the perfect time to take a backup of your databases)
1. Uninstall [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md)
1. Install [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) [[1](#_note-0)]
1. Run [mysql_upgrade](../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade.md)

  * Ubuntu and Debian packages do this automatically when they are installed; Red Hat, CentOS, and Fedora packages do not
  * `mysql_upgrade` does two things:

    1. Upgrades the permission tables in the `mysql` database with some new fields
    1. Does a very quick check of all tables and marks them as compatible with [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)
  * In most cases this should be a fast operation (depending of course on the number of tables)
1. Add new options to [my.cnf](../../configuring-mariadb-with-option-files.md) to enable features

  * If you change `my.cnf` then you need to restart `mysqld`


### Incompatible changes between 5.3 and 5.5


As mentioned previously, on most servers upgrading from 5.5 should be painless.
However, there are some things that have changed which could affect an upgrade:


#### XtraDB options that have changed default values



| Option | Old value | New value |
| --- | --- | --- |
| Option | Old value | New value |
| [innodb_change_buffering](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | inserts | all |
| [innodb_flush_neighbor_pages](../../../../reference/storage-engines/innodb/innodb-system-variables.md) | 1 | area |



#### Options that have been removed or renamed


Percona, the provider of [XtraDB](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md), does not provide all earlier XtraDB features in the 5.5 code base. Because of that, [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) can't provide them either. The following options are not supported by XtraDB 5.5. If you are using them in any of your my.cnf files, you should remove them before upgrading to 5.5.


* [innodb_adaptive_checkpoint](../../../../reference/storage-engines/innodb/innodb-system-variables.md); Use
 [innodb_adaptive_flushing_method](../../../../reference/storage-engines/innodb/innodb-system-variables.md) instead.
* [innodb_auto_lru_dump](../../../../reference/storage-engines/innodb/innodb-system-variables.md); Use [innodb_buffer_pool_restore_at_startup](../../../../reference/storage-engines/innodb/innodb-system-variables.md) instead (and [innodb_buffer_pool_load_at_startup](../../../../reference/storage-engines/innodb/innodb-system-variables.md) in [MariaDB 10.0](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)).
* [innodb_blocking_lru_restore](../../../../reference/storage-engines/innodb/innodb-system-variables.md); Use
 [innodb_blocking_buffer_pool_restore](../../../../reference/storage-engines/innodb/innodb-system-variables.md) instead.
* [innodb_enable_unsafe_group_commit](../../../../reference/storage-engines/innodb/innodb-system-variables.md)
* [innodb_expand_import](../../../../reference/storage-engines/innodb/innodb-system-variables.md); Use
 [innodb_import_table_from_xtrabackup](../../../../reference/storage-engines/innodb/innodb-system-variables.md) instead.
* [innodb_extra_rsegments](../../../../reference/storage-engines/innodb/innodb-system-variables.md); Use [innodb_rollback_segments](../../../../reference/storage-engines/innodb/innodb-system-variables.md) instead.
* [innodb_extra_undoslots](../../../../reference/storage-engines/innodb/innodb-system-variables.md)
* [innodb_fast_recovery](../../../../reference/storage-engines/innodb/innodb-system-variables.md)
* [innodb_flush_log_at_trx_commit_session](../../../../reference/storage-engines/innodb/innodb-system-variables.md)
* [innodb_overwrite_relay_log_info](../../../../reference/storage-engines/innodb/innodb-system-variables.md)
* [innodb_pass_corrupt_table](../../../../reference/storage-engines/innodb/innodb-system-variables.md); Use
 [innodb_corrupt_table_action](../../../../reference/storage-engines/innodb/innodb-system-variables.md) instead.
* [innodb_use_purge_thread](../../../../reference/storage-engines/innodb/innodb-system-variables.md)
* [xtradb_enhancements](../../../../reference/storage-engines/innodb/innodb-system-variables.md)


## Notes


1. [↑](#_ref-0) If using a MariaDB `apt` or `yum` [repository](https://downloads.mariadb.org/mariadb/repositories/), it is often enough to replace instances of '5.3' with '5.5' and then run an update/upgrade. For example, in Ubuntu/Debian update the MariaDB `sources.list` entry from something that looks similar to this:
```
deb http://ftp.osuosl.org/pub/mariadb/repo/5.3/ubuntu trusty main
```
To something like this:
```
deb http://ftp.osuosl.org/pub/mariadb/repo/5.5/ubuntu trusty main
```
And then run 
```
apt-get update && apt-get upgrade
```
And in Red Hat, CentOS, and Fedora, change the `baseurl` line from something that looks like this:
```
baseurl = http://yum.mariadb.org/5.3/centos6-amd64
```
To something that looks like this:
```
baseurl = http://yum.mariadb.org/5.5/centos6-amd64
```
 And then run 
```
yum update
```


## See also


* [The features in MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)
* [Perconas guide of how to upgrade to 5.5](https://www.percona.com/doc/percona-server/5.5/upgrading_guide_51_55.html)

