
# Upgrading MariaDB ColumnStore from 1.0.3 to 1.0.4

 
1. [MariaDB ColumnStore software upgrade 1.0.3 to 1.0.4 "MariaDB ColumnStore software upgrade 1.0.3 to 1.0.4"](#mariadb-columnstore-software-upgrade-103-to-104) 

  1. [Choosing the type of upgrade "Choosing the type of upgrade"](#choosing-the-type-of-upgrade) 

    1. [Root User Installs "Root User Installs"](#root-user-installs)
    1. [Upgrading MariaDB ColumnStore using RPMs "Upgrading MariaDB ColumnStore using RPMs"](#upgrading-mariadb-columnstore-using-rpms)
  1. [Initial download/install of MariaDB ColumnStore binary package "Initial download/install of MariaDB ColumnStore binary package"](#initial-downloadinstall-of-mariadb-columnstore-binary-package)
  1. [Upgrading MariaDB ColumnStore using the DEB package "Upgrading MariaDB ColumnStore using the DEB package"](#upgrading-mariadb-columnstore-using-the-deb-package) 

    1. [Non-Root User Installs "Non-Root User Installs"](#non-root-user-installs)
  1. [Initial download/install of MariaDB ColumnStore binary package "Initial download/install of MariaDB ColumnStore binary package"](#initial-downloadinstall-of-mariadb-columnstore-binary-package)





## MariaDB ColumnStore software upgrade 1.0.3 to 1.0.4


Note: Columnstore.xml modifications you manually made are not automatically carried
forward on an upgrade. These modifications will need to be incorporated back into
.XML once the upgrade has occurred.


The previous configuration file will be saved as /usr/local/mariadb/columnstore/etc/Columnstore.xml.rpmsave.


### Choosing the type of upgrade


#### Root User Installs


#### Upgrading MariaDB ColumnStore using RPMs


Upgrade MariaDB ColumnStore as user root on the server designated as PM1:


**Download the package mariadb-columnstore-1.0.4-1-centos#.x86_64.rpm.tar.gz to the PM1 server where you are installing MariaDB ColumnStore.** Shutdown the MariaDB ColumnStore system:


```
# mcsadmin shutdownsystem y
```

* Unpack the tarball, which will generate a set of RPMs that will reside in the /root/ directory.


`<code>tar -zxf mariadb-columnstore-1.0.4-1-centos#.x86_64.rpm.tar.gz</code>`


* Upgrade the RPMs. The MariaDB ColumnStore software will be installed in /usr/local/.


```
rpm -e --nodeps $(rpm -qa | grep '^mariadb-columnstore')
rpm -ivh mariadb-columnstore-*1.0.4*rpm
```

* Run postConfigure using the upgrade option, which will utilize the configuration from
the Columnstore.xml,rpmsave


```
# /usr/local/mariadb/columnstore/bin/postConfigure -u
```

For RPM Upgrade, the previous configuration file will be saved as:


/usr/local/mariadb/columnstore/etc/Columnstore.xml.rpmsave


### Initial download/install of MariaDB ColumnStore binary package


Upgrade MariaDB ColumnStore as user root on the server designated as PM1:


* Download the package into the /usr/local directory
-mariadb-columnstore-release#.x86_64.bin.tar.gz (Binary 64-BIT)to the
server where you are installing MariaDB ColumnStore.


* Shutdown the MariaDB ColumnStore system:


`<code>mcsadmin shutdownsystem y</code>`


* Run pre-uninstall script


`<code>/usr/local/mariadb/columnstore/bin/pre-uninstall</code>`


* Unpack the tarball, in the /usr/local/ directory.


`<code> tar -zxvf -mariadb-columnstore-release#.x86_64.bin.tar.gz</code>`


* Run post-install scripts


`<code> /usr/local/mariadb/columnstore/bin/post-install</code>`


* Run postConfigure using the upgrade option, which will utilize the configuration from
the Columnstore.xml,rpmsave


`<code>/usr/local/mariadb/columnstore/bin/postConfigure -u</code>`



### Upgrading MariaDB ColumnStore using the DEB package

A DEB upgrade would be done on a system that supports DEBs like Debian or Ubuntu
systems.
Upgrade MariaDB ColumnStore as user root on the server designated as PM1:

* Download the package into the /root directory


```
mariadb-columnstore-release#.amd64.deb.tar.gz
```
 (DEB 64-BIT) to the server where you are installing MariaDB ColumnStore.

* Shutdown the MariaDB ColumnStore system:


```
mcsadmin shutdownsystem y
```

* Unpack the tarball, which will generate DEBs.


```
tar -zxf mariadb-columnstore-release#.amd64.deb.tar.gz
```

* Remove, purge and install all MariaDB ColumnStore debs


```
cd /root/
dpkg -r mariadb-columnstore*deb
dpkg -P mariadb-columnstore*deb
```

* Run postConfigure using the upgrade option, which will utilize the
configuration from the Columnstore.xml,rpmsave


```
/usr/local/mariadb/columnstore/bin/postConfigure -u
```


#### Non-Root User Installs


### Initial download/install of MariaDB ColumnStore binary package


Upgrade MariaDB ColumnStore as user root on the server designated as PM1:


* Download the package into the /home/'non-root-user" directory


mariadb-columnstore-release#.x86_64.bin.tar.gz (Binary 64-BIT)to the
server where you are installing MariaDB ColumnStore.


* Shutdown the MariaDB ColumnStore system:


`<code>mcsadmin shutdownsystem y</code>`


* Run pre-uninstall script


`<code> $HOME/mariadb/columnstore/bin/pre-uninstall -i /home/guest/mariadb/columnstore</code>`


* Unpack the tarball, which will generate the $HOME/ directory.


`<code> tar -zxvf -mariadb-columnstore-release#.x86_64.bin.tar.gz</code>`


* Run post-install scripts 

  1. $HOME/mariadb/columnstore/bin/post-install -i /home/guest/mariadb/columnstore`<code>
</code>`


* Run postConfigure using the upgrade option, which will utilize the configuration from
the Columnstore.xml,rpmsave


`<code> $HOME/mariadb/columnstore/bin/postConfigure -u -i /home/guest/mariadb/columnstore</code>`

