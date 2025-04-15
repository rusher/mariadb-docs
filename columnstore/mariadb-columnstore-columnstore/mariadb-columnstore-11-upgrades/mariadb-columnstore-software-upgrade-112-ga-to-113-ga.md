
# MariaDB ColumnStore software upgrade 1.1.2 GA to 1.1.3 GA

 
1. [MariaDB ColumnStore software upgrade 1.1.2 GA to 1.1.3 GA "MariaDB ColumnStore software upgrade 1.1.2 GA to 1.1.3 GA"](#mariadb-columnstore-software-upgrade-112-ga-to-113-ga) 

  1. [Choosing the type of upgrade "Choosing the type of upgrade"](#choosing-the-type-of-upgrade) 

    1. [Root User Installs "Root User Installs"](#root-user-installs)
    1. [Upgrading MariaDB ColumnStore using RPMs "Upgrading MariaDB ColumnStore using RPMs"](#upgrading-mariadb-columnstore-using-rpms)
  1. [Initial download/install of MariaDB ColumnStore binary package "Initial download/install of MariaDB ColumnStore binary package"](#initial-downloadinstall-of-mariadb-columnstore-binary-package)
  1. [Upgrading MariaDB ColumnStore using the DEB package "Upgrading MariaDB ColumnStore using the DEB package"](#upgrading-mariadb-columnstore-using-the-deb-package) 

    1. [Non-Root User Installs "Non-Root User Installs"](#non-root-user-installs)
  1. [Initial download/install of MariaDB ColumnStore binary package "Initial download/install of MariaDB ColumnStore binary package"](#initial-downloadinstall-of-mariadb-columnstore-binary-package)





## MariaDB ColumnStore software upgrade 1.1.2 GA to 1.1.3 GA


Additional Dependency Packages exist for 1.1.3, so make sure you install those based on the "Preparing for ColumnStore Installation" Guide.


Note: Columnstore.xml modifications you manually made are not automatically carried
forward on an upgrade. These modifications will need to be incorporated back into
.XML once the upgrade has occurred.


The previous configuration file will be saved as /usr/local/mariadb/columnstore/etc/Columnstore.xml.rpmsave.


If you have specified a root database password (which is good practice), then you must configure a .my.cnf file with user credentials for the upgrade process to use. Create a .my.cnf file in the user home directory with 600 file permissions with the following content (updating PASSWORD as appropriate):


```
[mysqladmin] 
user = root
password = PASSWORD
```

### Choosing the type of upgrade


As noted on the Preparing guide, you can installing MariaDB ColumnStore with the use of soft-links. If you have the softlinks be setup at the Data Directory Levels, like mariadb/columnstore/data and mariadb/columnstore/dataX, then your upgrade will happen without any issues.
In the case where you have a softlink at the top directory, like /usr/local/mariadb, you will need to upgrade using the binary package. If you updating using the rpm package and tool, this softlink will be deleted when you perform the upgrade process and the upgrade will fail.


#### Root User Installs


#### Upgrading MariaDB ColumnStore using RPMs


Upgrade MariaDB ColumnStore as user root on the server designated as PM1:


**Download the package mariadb-columnstore-1.1.3-1-centos#.x86_64.rpm.tar.gz to the PM1 server where you are installing MariaDB ColumnStore.** Shutdown the MariaDB ColumnStore system:


```
# mcsadmin shutdownsystem y
```

* Unpack the tarball, which will generate a set of RPMs that will reside in the /root/ directory.


```
# tar -zxf mariadb-columnstore-1.1.3-1-centos#.x86_64.rpm.tar.gz
```

* Upgrade the RPMs. The MariaDB ColumnStore software will be installed in /usr/local/.


```
# rpm -e --nodeps $(rpm -qa | grep '^mariadb-columnstore')
# rpm -ivh mariadb-columnstore-*1.1.3*rpm
```

* Run postConfigure using the upgrade option, which will utilize the configuration from
the Columnstore.xml.rpmsave


```
# /usr/local/mariadb/columnstore/bin/postConfigure -u
```

For RPM Upgrade, the previous configuration file will be saved as:


/usr/local/mariadb/columnstore/etc/Columnstore.xml.rpmsave


### Initial download/install of MariaDB ColumnStore binary package


Upgrade MariaDB ColumnStore as user root on the server designated as PM1:


* Download the package into the /usr/local directory
-mariadb-columnstore-1.1.3-1.x86_64.bin.tar.gz (Binary 64-BIT)to the
server where you are installing MariaDB ColumnStore.


* Shutdown the MariaDB ColumnStore system:


```
# mcsadmin shutdownsystem y
```

* Run pre-uninstall script


```
# /usr/local/mariadb/columnstore/bin/pre-uninstall
```

* Unpack the tarball, in the /usr/local/ directory.


```
# tar -zxvf -mariadb-columnstore-1.1.3-1.x86_64.bin.tar.gz
```

* Run post-install scripts


```
# /usr/local/mariadb/columnstore/bin/post-install
```

* Run postConfigure using the upgrade option, which will utilize the configuration from
the Columnstore.xml,rpmsave


```
# /usr/local/mariadb/columnstore/bin/postConfigure -u
```

### Upgrading MariaDB ColumnStore using the DEB package


A DEB upgrade would be done on a system that supports DEBs like Debian or Ubuntu
systems.


Upgrade MariaDB ColumnStore as user root on the server designated as PM1:


* Download the package into the /root directory


mariadb-columnstore-1.1.3-1.amd64.deb.tar.gz


(DEB 64-BIT) to the server where you are installing MariaDB ColumnStore.


* Shutdown the MariaDB ColumnStore system:


```
# mcsadmin shutdownsystem y
```

* Unpack the tarball, which will generate DEBs.


```
# tar -zxf mariadb-columnstore-1.1.3-1.amd64.deb.tar.gz
```

* Remove, purge and install all MariaDB ColumnStore debs


```
# cd /root/
# dpkg -r  $(dpkg --list | grep 'mariadb-columnstore' | awk '{print $2}')
# dpkg -P  $(dpkg --list | grep 'mariadb-columnstore' | awk '{print $2}')

# dpkg --install mariadb-columnstore-*1.1.3-1*deb
```

* Run postConfigure using the upgrade option, which will utilize the
configuration from the Columnstore.xml,rpmsave


```
# /usr/local/mariadb/columnstore/bin/postConfigure -u
```

#### Non-Root User Installs


### Initial download/install of MariaDB ColumnStore binary package


Upgrade MariaDB ColumnStore as user root on the server designated as PM1:


* Download the package into the /home/'non-root-user" directory


mariadb-columnstore-1.1.3-1.x86_64.bin.tar.gz (Binary 64-BIT)to the
server where you are installing MariaDB ColumnStore.


* Shutdown the MariaDB ColumnStore system:


```
# mcsadmin shutdownsystem y
```

* Run pre-uninstall script


```
# $HOME/mariadb/columnstore/bin/pre-uninstall 
--installdir= /home/guest/mariadb/columnstore
```

* Unpack the tarball, which will generate the $HOME/ directory.


```
# tar -zxvf -mariadb-columnstore-1.1.3-1.x86_64.bin.tar.gz
```

* Run post-install scripts


```
# $HOME/mariadb/columnstore/bin/post-install 
--installdir=/home/guest/mariadb/columnstore
```

* Run postConfigure using the upgrade option, which will utilize the configuration from
the Columnstore.xml,rpmsave


```
# $HOME/mariadb/columnstore/bin/postConfigure -u -i /home/guest/mariadb/columnstore
```
