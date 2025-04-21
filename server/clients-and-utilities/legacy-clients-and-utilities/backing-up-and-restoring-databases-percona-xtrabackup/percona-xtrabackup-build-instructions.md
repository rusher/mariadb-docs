
# Percona XtraBackup Build Instructions

Percona XtraBackup is **not supported** in MariaDB. [Mariabackup](../../../server-management/backing-up-and-restoring-databases/mariabackup/README.md) is the recommended backup method to use instead of Percona XtraBackup. See [Percona XtraBackup Overview: Compatibility with MariaDB](percona-xtrabackup-overview.md#compatibility-with-mariadb) for more information.


Build instructions for [Percona XtraBackup](percona-xtrabackup-overview.md).


Solaris 10 (SunOS 5.10) notes:


Edit utils/build.sh and add -lrt -m64 to CFLAGS and CXXFLAGS.


Make sure that you're using GNU utils for building, including make, cmake, gcc, gawk, getopt, autotools, libtool, automake, autoconf and bazaar.


If you want to change MySQL version which to build against with edit one of the following lines:


MYSQL_51_VERSION=...


MYSQL_55_VERSION=...


PS_51_VERSION=...


PS_55_VERSION=..


When ready run one of the following depending on the MySQL version which you want to build with:


AUTO_DOWNLOAD="yes" ./utils/build.sh xtradb (build against XtraDB 5.1)


AUTO_DOWNLOAD="yes" ./utils/build.sh innodb51_builtin (build against built-in InnoDB in MySQL 5.1)


AUTO_DOWNLOAD="yes" ./utils/build.sh xtradb55 (build against XtraDB 5.5)


AUTO_DOWNLOAD="yes" ./utils/build.sh innodb55 (build against InnoDB in MySQL 5.5)

