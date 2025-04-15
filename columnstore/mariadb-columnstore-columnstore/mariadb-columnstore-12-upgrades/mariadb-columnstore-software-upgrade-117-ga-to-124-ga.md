
# MariaDB ColumnStore software upgrade 1.1.7 GA to 1.2.4 GA

 
1. [MariaDB ColumnStore software upgrade 1.1.7 GA to 1.2.4 GA "MariaDB ColumnStore software upgrade 1.1.7 GA to 1.2.4 GA"](#mariadb-columnstore-software-upgrade-117-ga-to-124-ga) 

  1. [Changes in 1.2.1 and later "Changes in 1.2.1 and later"](#changes-in-121-and-later) 

    1. [libjemalloc dependency "libjemalloc dependency"](#libjemalloc-dependency)
    1. [Non-distributed is the default distribution mode in postConfigure "Non-distributed is the default distribution mode in postConfigure"](#non-distributed-is-the-default-distribution-mode-in-postconfigure)
    1. [Non-root user sudo setup "Non-root user sudo setup"](#non-root-user-sudo-setup)
    1. [Running the mysql_upgrade script "Running the mysql_upgrade script"](#running-the-mysql_upgrade-script)
    1. [Executing the upgrade stored procedure "Executing the upgrade stored procedure"](#executing-the-upgrade-stored-procedure)
  1. [Setup "Setup"](#setup) 

    1. [Columnstore.xml / my.cnf "Columnstore.xml / my.cnf"](#columnstorexml-mycnf)
    1. [MariaDB root user database password "MariaDB root user database password"](#mariadb-root-user-database-password)
  1. [Choosing the type of upgrade "Choosing the type of upgrade"](#choosing-the-type-of-upgrade) 

    1. [Root User Installs "Root User Installs"](#root-user-installs) 

      1. [Upgrading MariaDB ColumnStore using the tarball of RPMs (distributed mode) "Upgrading MariaDB ColumnStore using the tarball of RPMs (distributed mode)"](#upgrading-mariadb-columnstore-using-the-tarball-of-rpms-distributed-mode)
      1. [Upgrading MariaDB ColumnStore using RPM Package Repositories (non-distributed mode) "Upgrading MariaDB ColumnStore using RPM Package Repositories (non-distributed mode)"](#upgrading-mariadb-columnstore-using-rpm-package-repositories-non-distributed-mode)
      1. [Upgrading MariaDB ColumnStore using the binary tarball (distributed mode) "Upgrading MariaDB ColumnStore using the binary tarball (distributed mode)"](#upgrading-mariadb-columnstore-using-the-binary-tarball-distributed-mode)
      1. [Upgrading MariaDB ColumnStore using the DEB tarball (distributed mode) "Upgrading MariaDB ColumnStore using the DEB tarball (distributed mode)"](#upgrading-mariadb-columnstore-using-the-deb-tarball-distributed-mode)
      1. [Upgrading MariaDB ColumnStore using DEB Package Repositories (non-distributed mode) "Upgrading MariaDB ColumnStore using DEB Package Repositories (non-distributed mode)"](#upgrading-mariadb-columnstore-using-deb-package-repositories-non-distributed-mode)
    1. [Non-Root User Installs "Non-Root User Installs"](#non-root-user-installs) 

      1. [Upgrade MariaDB ColumnStore from the binary tarball without sudo access (non-distributed mode) "Upgrade MariaDB ColumnStore from the binary tarball without sudo access (non-distributed mode)"](#upgrade-mariadb-columnstore-from-the-binary-tarball-without-sudo-access-non-distributed-mode)
      1. [Upgrade MariaDB ColumnStore from the binary tarball (distributed mode) "Upgrade MariaDB ColumnStore from the binary tarball (distributed mode)"](#upgrade-mariadb-columnstore-from-the-binary-tarball-distributed-mode)





## MariaDB ColumnStore software upgrade 1.1.7 GA to 1.2.4 GA


This upgrade also applies to 1.2.0 Alpha to 1.2.4 GA upgrades


### Changes in 1.2.1 and later


#### libjemalloc dependency


ColumnStore 1.2.3 onwards requires libjemalloc to be installed. For Ubuntu & Debian based distributions this is installed using the package "libjemalloc1" in the standard repositories.


For CentOS the package is in RedHat's EPEL repository:


```
sudo yum -y install epel-release
sudo yum install jemalloc
```

#### Non-distributed is the default distribution mode in postConfigure


The default distribution mode has changed from 'distributed' to 'non-distributed'. During an upgrade, however, the default is to use the distribution mode used in the original installation. The options '-d' and '-n' can always be used to override the default.


#### Non-root user sudo setup


Root-level permissions are no longer required to install or upgrade ColumnStore for some types of installations. Installations requiring some level of sudo access, and the instructions, are listed here: [preparing-for-and-installing-columnstore-version-121.md](../../columnstore-getting-started/preparing-and-installing-mariadb-columnstore-12x/preparing-for-and-installing-columnstore-version-121.md)


#### Running the mysql_upgrade script


As part of the upgrade process to 1.2.4, the user is required to run the mysql_upgrade script on all of the following nodes.


* All User Modules on a system configured with separate User and Performance Modules
* All Performance Modules on a system configured with separate User and Performance Modules and Local Query Feature is enabled
* All Performance Modules on a system configured with combined User and Performance Modules


mysql_upgrade should be run once the upgrade has been completed.


This is an example of how it run on a root user install:


```
/usr/local/mariadb/columnstore/mysql/bin/mysql_upgrade --defaults-file=/usr/local/mariadb/columnstore/mysql/my.cnf --force
```

This is an example of how it run on a non-root user install, assuming ColumnStore is installed under the user's home directory:


```
$HOME/mariadb/columnstore/mysql/bin/mysql_upgrade --defaults-file=$HOME/mariadb/columnstore/mysql/my.cnf --force
```

In addition you should run the upgrade stored procedure below for a major version upgrade.


#### Executing the upgrade stored procedure


If you are upgrading from 1.1.7 or have upgraded in the past you should run the MariaDB ColumnStore stored procedure. This updates the MariaDB FRM files by altering every ColumnStore table with a blank table comment. This will not affect options set using table comments but will erase any table comment the user has manually set.


You only need to execute this as part of a major version upgrade. It is executed using the following query which should be executed by a user which has access to alter every ColumnStore table:


```
call columnstore_info.columnstore_upgrade();
```

### Setup


In this section, we will refer to the directory ColumnStore is installed in as <CSROOT>. If you installed the RPM or DEB package, then your <CSROOT> will be /usr/local. If you installed it from the tarball, <CSROOT> will be where you unpacked it.


#### Columnstore.xml / my.cnf


Configuration changes made manually are not automatically carried forward during the upgrade. These modifications will need to be made again manually after the upgrade is complete.


After the upgrade process the configuration files will be saved at:


* <CSROOT>/mariadb/columnstore/etc/Columnstore.xml.rpmsave
* <CSROOT>/mariadb/columnstore/mysql/my.cnf.rpmsave


#### MariaDB root user database password


If you have specified a root user database password (which is good practice), then you must configure a .my.cnf file with user credentials for the upgrade process to use. Create a .my.cnf file in the user home directory with 600 file permissions with the following content (updating PASSWORD as appropriate):


```
[mysqladmin]
user = root
password = PASSWORD
```

### Choosing the type of upgrade


Note, softlinks may cause a problem during the upgrade if you use the RPM or DEB packages. If you have linked a directory above /usr/local/mariadb/columnstore, the softlinks will be deleted and the upgrade will fail. In that case you will need to upgrade using the binary tarball instead. If you have only linked the data directories (ie /usr/local/MariaDB/columnstore/data*), the RPM/DEB package upgrade will work.


#### Root User Installs


##### Upgrading MariaDB ColumnStore using the tarball of RPMs (distributed mode)


Upgrade MariaDB ColumnStore as user root on the server designated as PM1:


**Download the package mariadb-columnstore-1.2.4-1-centos#.x86_64.rpm.tar.gz to the PM1 server where you are installing MariaDB ColumnStore.**


**Shutdown the MariaDB ColumnStore system:**


```
# mcsadmin shutdownsystem y
```

* Unpack the tarball, which will generate a set of RPMs that will reside in the /root/ directory.


```
# tar -zxf mariadb-columnstore-1.2.4-1-centos#.x86_64.rpm.tar.gz
```

* Uninstall the old packages, then install the new packages. The MariaDB ColumnStore software will be installed in /usr/local/.


```
# rpm -e --nodeps $(rpm -qa | grep '^mariadb-columnstore')
# rpm -ivh mariadb-columnstore-*1.2.4*rpm
```

* Run postConfigure using the upgrade option


```
# /usr/local/mariadb/columnstore/bin/postConfigure -u
```

* Run the mysql_upgrade script on the nodes documented above for a root user install


[mariadb-columnstore-software-upgrade-117-ga-to-124-ga.md](mariadb-columnstore-software-upgrade-117-ga-to-124-ga.md)


##### Upgrading MariaDB ColumnStore using RPM Package Repositories (non-distributed mode)


The system can be upgraded when it was previously installed from the Package Repositories. This will need to be run on each module in the system.


Additional information can be found in this document on how to setup and install using the 'yum' package repo command:


[installing-mariadb-ax-mariadb-columnstore-from-the-package-repositories-11x.md](../../columnstore-getting-started/installing-mariadb-ax-mariadb-columnstore-from-the-package-repositories-11x.md)


Upgrade MariaDB ColumnStore as user root on the server designated as PM1:


**Shutdown the MariaDB ColumnStore system:**


```
# mcsadmin shutdownsystem y
```

* Uninstall MariaDB ColumnStore Packages


```
# yum remove mariadb-columnstore*
```

* Install MariaDB ColumnStore Packages


```
# yum --enablerepo=mariadb-columnstore clean metadata
# yum install mariadb-columnstore*
```

NOTE: On all modules except for PM1, start the columnstore service


```
# /usr/local/mariadb/columnstore/bin/columnstore start
```

* Run postConfigure using the upgrade and non-distributed options


```
# /usr/local/mariadb/columnstore/bin/postConfigure -u -n
```

* Run the mysql_upgrade script on the nodes documented above for a root user install


[mariadb-columnstore-software-upgrade-117-ga-to-124-ga.md](mariadb-columnstore-software-upgrade-117-ga-to-124-ga.md)


##### Upgrading MariaDB ColumnStore using the binary tarball (distributed mode)


Upgrade MariaDB ColumnStore as user root on the server designated as PM1:


* Download the package into the /usr/local directory mariadb-columnstore-1.2.4-1.x86_64.bin.tar.gz


* Shutdown the MariaDB ColumnStore system:


```
# mcsadmin shutdownsystem y
```

* Run pre-uninstall script


```
# /usr/local/mariadb/columnstore/bin/pre-uninstall
```

* Unpack the tarball in the /usr/local/ directory.


```
# tar -zxvf mariadb-columnstore-1.2.4-1.x86_64.bin.tar.gz
```

* Run post-install scripts


```
# /usr/local/mariadb/columnstore/bin/post-install
```

* Run postConfigure using the upgrade option


```
# /usr/local/mariadb/columnstore/bin/postConfigure -u
```

* Run the mysql_upgrade script on the nodes documented above for a root user install


[mariadb-columnstore-software-upgrade-117-ga-to-124-ga.md](mariadb-columnstore-software-upgrade-117-ga-to-124-ga.md)


##### Upgrading MariaDB ColumnStore using the DEB tarball (distributed mode)


Upgrade MariaDB ColumnStore as user root on the server designated as PM1:


* Download the package into the /root directory mariadb-columnstore-1.2.4-1.amd64.deb.tar.gz


* Shutdown the MariaDB ColumnStore system:


```
# mcsadmin shutdownsystem y
```

* Unpack the tarball, which contains DEBs.


```
# tar -zxf mariadb-columnstore-1.2.4-1.amd64.deb.tar.gz
```

* Remove and install all MariaDB ColumnStore debs


```
# cd /root/
# dpkg -r  $(dpkg --list | grep 'mariadb-columnstore' | awk '{print $2}')
# dpkg --install mariadb-columnstore-*1.2.4-1*deb
```

* Run postConfigure using the upgrade option


```
# /usr/local/mariadb/columnstore/bin/postConfigure -u
```

* Run the mysql_upgrade script on the nodes documented above for a root user install


[mariadb-columnstore-software-upgrade-117-ga-to-124-ga.md](mariadb-columnstore-software-upgrade-117-ga-to-124-ga.md)


##### Upgrading MariaDB ColumnStore using DEB Package Repositories (non-distributed mode)


The system can be upgraded when it was previously installed from the Package Repositories. This will need to be run on each module in the system


Additional information can be found in this document on how to setup and install using the 'apt-get' package repo command:


[installing-mariadb-ax-mariadb-columnstore-from-the-package-repositories-11x.md](../../columnstore-getting-started/installing-mariadb-ax-mariadb-columnstore-from-the-package-repositories-11x.md)


Upgrade MariaDB ColumnStore as user root on the server designated as PM1:


**Shutdown the MariaDB ColumnStore system:**


```
# mcsadmin shutdownsystem y
```

* Uninstall MariaDB ColumnStore Packages


```
# apt-get remove mariadb-columnstore*
```

* Install MariaDB ColumnStore Packages


```
# apt-get update
# sudo apt-get install mariadb-columnstore*
```

NOTE: On all modules except for PM1, start the columnstore service


```
# /usr/local/mariadb/columnstore/bin/columnstore start
```

* Run postConfigure using the upgrade and non-distributed options


```
# /usr/local/mariadb/columnstore/bin/postConfigure -u -n
```

* Run the mysql_upgrade script on the nodes documented above for a root user install


[mariadb-columnstore-software-upgrade-117-ga-to-124-ga.md](mariadb-columnstore-software-upgrade-117-ga-to-124-ga.md)


#### Non-Root User Installs


##### Upgrade MariaDB ColumnStore from the binary tarball without sudo access (non-distributed mode)


This upgrade method applies when root/sudo access is not an option.


The uninstall script for 1.1.7 requires root access to perform some operations. These operations are the following:


* removing /etc/profile.d/columnstore{Alias,Env}.sh to remove aliases and environment variables from all users.
* running '<CSROOT>/mysql/columnstore/bin/syslogSetup.sh uninstall' to remove ColumnStore from the logging system
* removing the columnstore startup script
* remove /etc/ld.so.conf.d/columnstore.conf to ColumnStore directories from the ld library search path


Because you are upgrading ColumnStore and not uninstalling it, they are not necessary. If at some point you wish to uninstall it, you (or your sysadmin) will have to perform those operations by hand.


The upgrade instructions:


* Download the binary tarball to the current installation location on all nodes. See [](https://downloads.mariadb.com/ColumnStore/)


* Shutdown the MariaDB ColumnStore system:


```
$ mcsadmin shutdownsystem y
```

* Copy Columnstore.xml to Columnstore.xml.rpmsave, and my.cnf to my.cnf.rpmsave


```
$ cp <CSROOT>/mariadb/columnstore/etc/Columnstore{.xml,.xml.rpmsave} 
$ cp <CSROOT>/mariadb/columnstore/mysql/my{.cnf,.cnf.rpmsave}
```

* On all nodes, untar the new files in the same location as the old ones


```
$ tar zxf columnstore-1.2.4-1.x86_64.bin.tar.gz
```

* On all nodes, run post-install, specifying where ColumnStore is installed


```
$ <CSROOT>/mariadb/columnstore/bin/post-install --installdir=<CSROOT>/mariadb/columnstore
```

* On all nodes except for PM1, start the columnstore service


```
$ <CSROOT>/mariadb/columnstore/bin/columnstore start
```

* On PM1 only, run postConfigure, specifying the upgrade, non-distributed installation mode, and the location of the installation


```
$ <CSROOT>/mariadb/columnstore/bin/postConfigure -u -n -i <CSROOT>/mariadb/columnstore
```

* Run the mysql_upgrade script on the nodes documented above for a non-root user install


[mariadb-columnstore-software-upgrade-117-ga-to-124-ga.md](mariadb-columnstore-software-upgrade-117-ga-to-124-ga.md)


##### Upgrade MariaDB ColumnStore from the binary tarball (distributed mode)


Upgrade MariaDB ColumnStore as user USER on the server designated as PM1:


* Download the package into the user's home directory mariadb-columnstore-1.2.4-1.x86_64.bin.tar.gz


* Shutdown the MariaDB ColumnStore system:


```
$ mcsadmin shutdownsystem y
```

* Run the pre-uninstall script; this will require sudo access as you are running a script from 1.1.7.


```
$ <CSROOT>/mariadb/columnstore/bin/pre-uninstall --installdir=<CSROOT>/mariadb/columnstore
```

* Make the sudo changes as noted at the beginning of this document


* Unpack the tarball in the same place as the original installation


```
$ tar -zxvf mariadb-columnstore-1.2.4-1.x86_64.bin.tar.gz
```

* Run post-install scripts


```
$ <CSROOT>/mariadb/columnstore/bin/post-install --installdir=<CSROOT>/mariadb/columnstore
```

* Run postConfigure using the upgrade option


```
$ <CSROOT>/mariadb/columnstore/bin/postConfigure -u -i <CSROOT>/mariadb/columnstore
```

* Run the mysql_upgrade script on the nodes documented above for a non-root user install


[mariadb-columnstore-software-upgrade-117-ga-to-124-ga.md](mariadb-columnstore-software-upgrade-117-ga-to-124-ga.md)

