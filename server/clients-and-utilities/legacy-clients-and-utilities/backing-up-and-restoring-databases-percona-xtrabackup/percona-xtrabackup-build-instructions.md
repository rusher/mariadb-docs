# Percona XtraBackup Build Instructions

Percona XtraBackup is **not supported** in MariaDB. [Mariabackup](../../../server-usage/backup-and-restore/mariabackup/) is the recommended backup method to use instead of Percona XtraBackup. See [Percona XtraBackup Overview: Compatibility with MariaDB](percona-xtrabackup-overview.md#compatibility-with-mariadb) for more information.

Build instructions for [Percona XtraBackup](percona-xtrabackup-overview.md).

Solaris 10 (SunOS 5.10) notes:

Edit utils/build.sh and add -lrt -m64 to CFLAGS and CXXFLAGS.

Make sure that you're using GNU utils for building, including make, cmake, gcc, gawk, getopt, autotools, libtool, automake, autoconf and bazaar.

If you want to change MySQL version which to build against with edit one of the following lines:

MYSQL\_51\_VERSION=...

MYSQL\_55\_VERSION=...

PS\_51\_VERSION=...

PS\_55\_VERSION=..

When ready run one of the following depending on the MySQL version which you want to build with:

AUTO\_DOWNLOAD="yes" ./utils/build.sh xtradb (build against XtraDB 5.1)

AUTO\_DOWNLOAD="yes" ./utils/build.sh innodb51\_builtin (build against built-in InnoDB in MySQL 5.1)

AUTO\_DOWNLOAD="yes" ./utils/build.sh xtradb55 (build against XtraDB 5.5)

AUTO\_DOWNLOAD="yes" ./utils/build.sh innodb55 (build against InnoDB in MySQL 5.5)

CC BY-SA / Gnu FDL
