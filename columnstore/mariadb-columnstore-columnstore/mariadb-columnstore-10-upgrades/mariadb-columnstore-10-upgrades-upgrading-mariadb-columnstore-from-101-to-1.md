
# Upgrading MariaDB ColumnStore from 1.0.1 to 1.0.2

 
1. [MariaDB ColumnStore single server software upgrade from 1.0.1 to 1.0.2 "MariaDB ColumnStore single server software upgrade from 1.0.1 to 1.0.2"](#mariadb-columnstore-single-server-software-upgrade-from-101-to-102) 

  1. [Upgrade workaround "Upgrade workaround"](#upgrade-workaround)
  1. [Choosing the type of upgrade "Choosing the type of upgrade"](#choosing-the-type-of-upgrade) 

    1. [Root User Installs "Root User Installs"](#root-user-installs)
    1. [Upgrading MariaDB ColumnStore using RPMs "Upgrading MariaDB ColumnStore using RPMs"](#upgrading-mariadb-columnstore-using-rpms)
  1. [Initial download/install of MariaDB ColumnStore binary package "Initial download/install of MariaDB ColumnStore binary package"](#initial-downloadinstall-of-mariadb-columnstore-binary-package)
  1. [Upgrading MariaDB ColumnStore using the DEB package "Upgrading MariaDB ColumnStore using the DEB package"](#upgrading-mariadb-columnstore-using-the-deb-package) 

    1. [Non-Root User Installs "Non-Root User Installs"](#non-root-user-installs)
  1. [Initial download/install of MariaDB ColumnStore binary package "Initial download/install of MariaDB ColumnStore binary package"](#initial-downloadinstall-of-mariadb-columnstore-binary-package)





## MariaDB ColumnStore single server software upgrade from 1.0.1 to 1.0.2


Note: Calpont.xml modifications you manually made are not automatically carried
forward on an upgrade. These modifications will need to be incorporated back into
.XML once the upgrade has occurred.


The previous configuration file will be saved as
/usr/local/MariaDB/Columnstore/etc/Calpont.xml.rpmsave.


In 1.0.2, the configuration file name was changed to Columnstore.xml. Check the 1.0.2 Release Notes on how to perform the upgrade from the 1.0.1 to the 1.0.2. There is a work-around procedure to follow.


### Upgrade workaround


After you have completed the part of the package upgrade process (removing the old package and installing the 1.0.2 package), the following file will exist:
/usr/local/mariadb/columnstore/etc/Calpont.xml.rpmsave
Run the following commands, this is the work-around part that is only required when going from 1.0.0/1.0.1 to 1.0.2


1. cd /usr/local/mariadb/columnstore/etc/
1. cp Calpont.xml.rpmsave Columnstore.xml.rpmsave
1. sed -i 's/Calpont Version/Columnstore Version/g' Columnstore.xml.rpmsave
1. sed -i 's/Calpont.xml/Columnstore.xml/g' Columnstore.xml.rpmsave
1. sed -i 's/<\/Calpont>/<\/Columnstore>/g' Columnstore.xml.rpmsave
Then you can run the install script to upgrade the system:
1. /usr/local/mariadb/columnstore/bin/postConfigure -u


### Choosing the type of upgrade


#### Root User Installs


#### Upgrading MariaDB ColumnStore using RPMs


Upgrade MariaDB ColumnStore as user root on the server designated as PM1:


**Download the package mariadb-columnstore-1.0.2-1-centos#.x86_64.rpm.tar.gz to the server where you are installing MariaDB ColumnStore.** Shutdown the MariaDB ColumnStore system:


```
# mcsadmin shutdownsystem y
```

* Unpack the tarball, which will generate a set of RPMs that will reside in the /root/ directory.


`<code>tar -zxf mariadb-columnstore-1.0.2-1-centos#.x86_64.rpm.tar.gz</code>`


* Upgrade the RPMs. The MariaDB ColumnStore software will be installed in /usr/local/.


Note: If another version of MariaDB is currently running, this service
will need to be stopped before running this command. After the
rpm command has been executed, you can restart the service.


```
rpm -Uvh mariadb-columnstore*.rpm
```

* Run postConfigure using the upgrade option, which will utilize the configuration from
the Columnstore.xml,rpmsave


```
# /usr/local/MariaDB/Columnstore/bin/postConfigure -u
```

For RPM Upgrade, the previous configuration file will be saved as:


/usr/local/MariaDB/Columnstore/etc/Columnstore.xml.rpmsave


### Initial download/install of MariaDB ColumnStore binary package


Upgrade MariaDB ColumnStore as user root on the server designated as PM1:


* Download the package into the /usr/local directory
-mariadb-columnstore-release#.x86_64.bin.tar.gz (Binary 64-BIT)to the
server where you are installing MariaDB ColumnStore.


* Shutdown the MariaDB ColumnStore system:


`<code>cc shutdownsystem y</code>`


* Run pre-uninstall script


`<code>/usr/local/MariaDB/Columnstore/bin/pre-uninstall</code>`


* Unpack the tarball, which will generate the /usr/local/ directory.


`<code> tar -zxvf -mariadb-columnstore-release#.x86_64.bin.tar.gz</code>`


* Run post-install scripts


`<code> /usr/local/MariaDB/Columnstore/bin/post-install</code>`


* Run postConfigure using the upgrade option, which will utilize the configuration from
the Columnstore.xml,rpmsave


`<code>/usr/local/MariaDB/Columnstore/bin/postConfigure -u</code>`



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
cc shutdownsystem y
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
configuration from the Calpont.xml,rpmsave


```
/usr/local/MariaDB/Columnstore/bin/postConfigure -u
```


#### Non-Root User Installs


### Initial download/install of MariaDB ColumnStore binary package


Upgrade MariaDB ColumnStore as user root on the server designated as PM1:


* Download the package into the /home/'non-root-user" directory


mariadb-columnstore-release#.x86_64.bin.tar.gz (Binary 64-BIT)to the
server where you are installing MariaDB ColumnStore.


* Shutdown the MariaDB ColumnStore system:


`<code>cc shutdownsystem y</code>`


* Run pre-uninstall script


`<code> $HOME/MariaDB/Columnstore/bin/pre-uninstall</code>`


* Unpack the tarball, which will generate the $HOME/ directory.


`<code> tar -zxvf -mariadb-columnstore-release#.x86_64.bin.tar.gz</code>`


* Run post-install scripts 

  1. $HOME/MariaDB/Columnstore/bin/post-install`<code>
</code>`


* Run postConfigure using the upgrade option, which will utilize the configuration from
the Columnstore.xml,rpmsave


`<code> $HOME<em>MariaDB/Columnstore/bin/postConfigure -n</em></code>`

