
# MariaDB Online Backup

**Note:** This page is obsolete. The information is old, outdated, or otherwise currently incorrect. We are keeping the page for historical reasons only. **Do not** rely on the information in this article.



Rumours have it that MySQL/Sun/Oracle are going to drop the MySQL online backup
project, which was originally scheduled for MySQL 6.0.


Given this, it makes sense to consider resurrecting the project for MariaDB.
This page collects various resources related to this.


## Documentation


* [MySQL Forge project page](https://forge.mysql.com/wiki/OnlineBackup) for Online Backup
* [Online Backup reference manual](https://dev.mysql.com/doc/mysql-backup/en/index.html)
* [tarball](https://hasky.askmonty.org/download/onlinebackup/backup-manual.tar.gz)
 containing self-contained copy of the Online Backup reference manual (the
 license allows to copy/distribute the manual together with the source
 tarball, but not to modify it).


## Source code


* [mysql-6.0-backup branch](https://code.launchpad.net/~mysql/mysql-server/mysql-6.0-backup) on Launchpad
* [mysql-6.0 branch](https://code.launchpad.net/~mysql/mysql-server/mysql-6.0) on Launchpad
* [Source tarball](https://hasky.askmonty.org/download/onlinebackup/mysql-6.0.14-alpha.tar.gz) of mysql-6.0-backup


## Notes


### Extracting a patch for merging


It may not be trivial to extract a patch of MySQL Online Backup that can be
used as a basis for merging into MariaDB. The problem is that we do not have a
feature tree that contains only the backup feature over some base/parent tree.


There was work done at MySQL to merge online backup into MySQL 5.5 using such a
feature tree, but this tree is not public, and requests to make it public have
not been answered positively so far.


It may still be possible to extract the code, but it may be necessary to do it
manually, by extracting relevant parts of the code from 6.0 without including
other stuff that is not related to backup.


It might also be useful to search the [bugs.mysql.com](https://bugs.mysql.com/)
MySQL bug tracker for recently fixed online backup bugs, since recent fixes are
not included in the publicly available trees on Launchpad.


### Comments on the code


From looking at the documentation of Online Backup, it seems geared more
towards an optimised mysqldump facility than towards an easy-to-use facility to
back up a complete MySQL server:


* The `BACKUP` command only allows to backup selected (or all)
 databases/schemas.
* There seems to be no facility to backup the binary log
* There seems to be no facility to backup `GRANT`s or other server-global
 configuration, using [mysqldump](../../../../../../../../server/clients-and-utilities/legacy-clients-and-utilities/mysqldumpslow.md) on the "mysql" schema/database is
 suggested
* Restoring a new server from scratch seems to involve setting up a new server,
 including running [mysql_install_db](../../../../../../../../server/clients-and-utilities/legacy-clients-and-utilities/mysql_install_db.md) and adding `GRANT`s, and only then
 restoring tables and other schema objects


Compared to something like XtraBackup, full backup and restore seems to be
somewhat more involved. It may be necessary to add extra facilities or wrapper
scripts to enable to backup/restore a full database server.

