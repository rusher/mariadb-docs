
# Installing MariaDB AX / MariaDB ColumnStore from the Package Repositories - 1.2.X

 
1. [Introduction "Introduction"](#introduction)
1. [MariaDB AX Packages "MariaDB AX Packages"](#mariadb-ax-packages) 

  1. [CentOS 6 "CentOS 6"](#centos-6)
  1. [CentOS 7 "CentOS 7"](#centos-7)
  1. [SUSE 12 "SUSE 12"](#suse-12)
  1. [Debian 8 "Debian 8"](#debian-8)
  1. [Debian 9 "Debian 9"](#debian-9)
  1. [Ubuntu 16 "Ubuntu 16"](#ubuntu-16)
  1. [Ubuntu 18 "Ubuntu 18"](#ubuntu-18)
1. [MariaDB ColumnStore Packages "MariaDB ColumnStore Packages"](#mariadb-columnstore-packages) 

  1. [CentOS 6 "CentOS 6"](#centos-6)
  1. [CentOS 7 "CentOS 7"](#centos-7)
  1. [SUSE 12 "SUSE 12"](#suse-12)
  1. [Debian 8 "Debian 8"](#debian-8)
  1. [Debian 9 "Debian 9"](#debian-9)
  1. [Ubuntu 16 "Ubuntu 16"](#ubuntu-16)
  1. [Ubuntu 18 "Ubuntu 18"](#ubuntu-18)
1. [MariaDB ColumnStore API (Bulk Write SDK) Package "MariaDB ColumnStore API (Bulk Write SDK) Package"](#mariadb-columnstore-api-bulk-write-sdk-package) 

  1. [CentOS 7 "CentOS 7"](#centos-7)
  1. [Debian 8 "Debian 8"](#debian-8)
  1. [Debian 9 "Debian 9"](#debian-9)
  1. [Ubuntu 16 "Ubuntu 16"](#ubuntu-16)
  1. [Ubuntu 18 "Ubuntu 18"](#ubuntu-18)
  1. [Windows 10 "Windows 10"](#windows-10)
1. [MariaDB ColumnStore Tools Package "MariaDB ColumnStore Tools Package"](#mariadb-columnstore-tools-package) 

  1. [CentOS 6 "CentOS 6"](#centos-6)
  1. [CentOS 7 "CentOS 7"](#centos-7)
  1. [SUSE 12 "SUSE 12"](#suse-12)
  1. [Debian 8 "Debian 8"](#debian-8)
  1. [Debian 9 "Debian 9"](#debian-9)
  1. [Ubuntu 16 "Ubuntu 16"](#ubuntu-16)
  1. [Ubuntu 18 "Ubuntu 18"](#ubuntu-18)
  1. [Windows 10 "Windows 10"](#windows-10)
1. [MariaDB MaxScale Packages "MariaDB MaxScale Packages"](#mariadb-maxscale-packages) 

  1. [CentOS 6 "CentOS 6"](#centos-6)
  1. [CentOS 7 "CentOS 7"](#centos-7)
  1. [SUSE 12 "SUSE 12"](#suse-12)
  1. [Debian 8 "Debian 8"](#debian-8)
  1. [Debian 9 "Debian 9"](#debian-9)
  1. [Ubuntu 16 "Ubuntu 16"](#ubuntu-16)
  1. [Ubuntu 18 "Ubuntu 18"](#ubuntu-18)
1. [MariaDB Connector Packages "MariaDB Connector Packages"](#mariadb-connector-packages) 

  1. [ODBC Connector "ODBC Connector"](#odbc-connector)
  1. [Java Connector "Java Connector"](#java-connector)
1. [MariaDB ColumnStore Data Adapters Packages "MariaDB ColumnStore Data Adapters Packages"](#mariadb-columnstore-data-adapters-packages) 

  1. [CentOS 7 "CentOS 7"](#centos-7)
  1. [Debian 8 "Debian 8"](#debian-8)
  1. [Debian 9 "Debian 9"](#debian-9)
  1. [Ubuntu 16 "Ubuntu 16"](#ubuntu-16)
  1. [Ubuntu 18 "Ubuntu 18"](#ubuntu-18)



# Introduction


Installing MariaDB AX and MariaDB ColumnStore individual packages can be done from the yum, apt-get, and zypper Repositories based on the OS.


MariaDB AX packages which consist of:


* MariaDB ColumnStore Platform
* MariaDB ColumnStore API (Bulk Write SDK)
* MariaDB ColumnStore Data-Adapters
* MariaDB ColumnStore Tools
* MariaDB Maxscale
* MariaDB Connectors

  * MariaDB Maxscale CDC Connector
  * MariaDB ODBC Connector
  * MariaDB Java-client Connector jar file


You can install packages from the Repositories for Single-Server installs and for Multi-Server installs utilizing the Non-Distributed feature where the packages are installed on all the servers in the cluster before the configuration and setup is performed.


NOTE: Document shows installing the latest GA version of each package by using 'latest' in the download paths. You can also install other version by entering the specific release ID, like 1.2.2-1.


# MariaDB AX Packages


This section shows how to setup and install all associated packages for MariaDB AX.


Start by doing the MariaDB Connector Packages. Go to that section and install the connectors first.


## CentOS 6


### Adding the MariaDB AX YUM repository


Add new file with repository information, /etc/yum.repos.d/mariadb-columnstore.repo


```
[mariadb-columnstore]
name=MariaDB ColumnStore
baseurl=https://downloads.mariadb.com/MariaDB/mariadb-columnstore/latest/yum/centos/6/x86_64/
gpgkey=https://downloads.mariadb.com/MariaDB/mariadb-columnstore/RPM-GPG-KEY-MariaDB-ColumnStore
gpgcheck=1
```

Add new file with repository information, /etc/yum.repos.d/mariadb-columnstore-tools.repo


```
[mariadb-columnstore-tools]
name=MariaDB ColumnStore Tools
baseurl=https://downloads.mariadb.com/MariaDB/mariadb-columnstore-tools/latest/yum/centos/6/x86_64/
gpgkey=https://downloads.mariadb.com/MariaDB/mariadb-columnstore/RPM-GPG-KEY-MariaDB-ColumnStore
gpgcheck=1
```

Add new file with repository information, /etc/yum.repos.d/mariadb-maxscale.repo


```
[mariadb-maxscale]
name=MariaDB MaxScale
baseurl=https://downloads.mariadb.com/MaxScale/latest/centos/6/x86_64
gpgkey=https://downloads.mariadb.com/MaxScale/MariaDB-MaxScale-GPG-KEY
gpgcheck=1
```

### Installing MariaDB AX


With the repo file in place you can now install MariaDB ColumnStore like so:


```
sudo yum --enablerepo=mariadb-columnstore clean metadata
sudo yum groups mark remove "MariaDB ColumnStore"
sudo yum groupinstall "MariaDB ColumnStore"
sudo yum --enablerepo=mariadb-columnstore-tools clean metadata
sudo yum install mariadb-columnstore-tools
sudo yum --enablerepo=mariadb-maxscale clean metadata
sudo yum install maxscale maxscale-cdc-connector
```

## CentOS 7


### Adding the MariaDB AX YUM repository


Add new file with repository information, /etc/yum.repos.d/mariadb-columnstore.repo


```
[mariadb-columnstore]
name=MariaDB ColumnStore
baseurl=https://downloads.mariadb.com/MariaDB/mariadb-columnstore/latest/yum/centos/7/x86_64/
gpgkey=https://downloads.mariadb.com/MariaDB/mariadb-columnstore/RPM-GPG-KEY-MariaDB-ColumnStore
gpgcheck=1
```

Add new file with repository information, /etc/yum.repos.d/mariadb-columnstore-api.repo


```
[mariadb-columnstore-api]
name=MariaDB ColumnStore API
baseurl=https://downloads.mariadb.com/MariaDB/mariadb-columnstore-api/latest/yum/centos/7/x86_64/
gpgkey=https://downloads.mariadb.com/MariaDB/mariadb-columnstore/RPM-GPG-KEY-MariaDB-ColumnStore
gpgcheck=1
```

### Adding the MariaDB ColumnStore Tools YUM repository


Add new file with repository information, /etc/yum.repos.d/mariadb-columnstore-tools.repo


```
[mariadb-columnstore-tools]
name=MariaDB ColumnStore Tools
baseurl=https://downloads.mariadb.com/MariaDB/mariadb-columnstore-tools/latest/yum/centos/7/x86_64/
gpgkey=https://downloads.mariadb.com/MariaDB/mariadb-columnstore/RPM-GPG-KEY-MariaDB-ColumnStore
gpgcheck=1
```

Add new file with repository information, /etc/yum.repos.d/mariadb-maxscale.repo


```
[mariadb-maxscale]
name=MariaDB MaxScale
baseurl=https://downloads.mariadb.com/MaxScale/latest/centos/7/x86_64
gpgkey=https://downloads.mariadb.com/MaxScale/MariaDB-MaxScale-GPG-KEY
gpgcheck=1
```

### Adding the MariaDB ColumnStore Data Adapters YUM repository


Add new file with repository information, /etc/yum.repos.d/mariadb-columnstore-data-adapters.repo


```
[mariadb-columnstore-data-adapters]
name=MariaDB ColumnStore Data Adapters
baseurl=https://downloads.mariadb.com/MariaDB/data-adapters/mariadb-streaming-data-adapters/latest/yum/centos/7/x86_64/
gpgkey=https://downloads.mariadb.com/MariaDB/mariadb-columnstore/RPM-GPG-KEY-MariaDB-ColumnStore
gpgcheck=1
```

### Installing MariaDB AX


With the repo file in place you can now install MariaDB ColumnStore like so:


```
sudo yum --enablerepo=mariadb-columnstore clean metadata
sudo yum groups mark remove "MariaDB ColumnStore"
sudo yum groupinstall "MariaDB ColumnStore"
sudo yum --enablerepo=mariadb-columnstore-api clean metadata
sudo yum install epel-release
sudo yum install mariadb-columnstore-api*
sudo yum --enablerepo=mariadb-columnstore-tools clean metadata
sudo yum install mariadb-columnstore-tools
sudo yum --enablerepo=mariadb-maxscale clean metadata
sudo yum install maxscale maxscale-cdc-connector
sudo yum --enablerepo=mariadb-columnstore-data-adapters clean metadata
sudo yum install mariadb-columnstore-data-adapters-maxscale-cdc-adapter
sudo yum install mariadb-columnstore-data-adapters-avro-kafka-adapter
```

## SUSE 12


### Adding the MariaDB ColumnStore ZYPPER repository


Add new file with repository information, /etc/zypp/repos.d/mariadb-columnstore.repo


```
[mariadb-columnstore]
name=mariadb-columnstore
enabled=1
autorefresh=0
baseurl=https://downloads.mariadb.com/MariaDB/mariadb-columnstore/latest/yum/sles/12/x86_64
type=rpm-md
```

Add new file with repository information, /etc/zypp/repos.d/mariadb-columnstore-tools.repo


```
[mariadb-columnstore-tools]
name=mariadb-columnstore-tools
enabled=1
autorefresh=0
baseurl=https://downloads.mariadb.com/MariaDB/mariadb-columnstore-tools/latest/yum/sles/12/x86_64
type=rpm-md
```

Add new file with repository information, /etc/zypp/repos.d/mariadb-maxscale.repo


```
[mariadb-maxscale]
name=mariadb-maxscale
enabled=1
autorefresh=0
baseurl=https://downloads.mariadb.com/MaxScale/latest/sles/12/x86_64
type=rpm-md
```

Download the MariaDB ColumnStore and MaxScale keys


```
rpm --import https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key
rpm --import https://downloads.mariadb.com/MaxScale/MariaDB-MaxScale-GPG-KEY
```

### Installing MariaDB ColumnStore


With the repo file in place you can now install MariaDB ColumnStore like so:


```
sudo zypper refresh
sudo zypper install mariadb-columnstore*
sudo zypper install mariadb-columnstore-tools
sudo zypper install maxscale maxscale-cdc-connector
```

## Debian 8


### Adding the MariaDB ColumnStore APT-GET repository


Install package:


```
sudo apt-get install apt-transport-https
```

Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore/latest/repo/debian8 jessie main
```

Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-api.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore-api/latest/repo/debian8 jessie main
```

Add new file with repository information, /etc/apt/sources.list.d/debian-backports.list


```
deb http://httpredir.debian.org/debian jessie-backports main contrib non-free
```

Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-tools.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore-tools/latest/repo/debian8 jessie main
```

Add new file with repository information, /etc/apt/sources.list.d/mariadb-maxscale.list


```
deb https://downloads.mariadb.com/MaxScale/latest/debian jessie main
```

Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-data-adapters.list


```
deb https://downloads.mariadb.com/MariaDB/data-adapters/mariadb-streaming-data-adapters/latest/repo/debian8 jessie main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

Download the MariaDB MaxScale key


```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 28C12247
```

### Installing MariaDB ColumnStore


With the repo file in place you can now install MariaDB ColumnStore like so:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore*
sudo apt-get install mariadb-columnstore-api*
sudo apt-get install mariadb-columnstore-tools
sudo apt-get install maxscale maxscale-cdc-connector
sudo apt-get install mariadb-columnstore-maxscale-cdc-adapters
sudo apt-get install mariadb-columnstore-kafka-avro-adapters
```

## Debian 9


### Adding the MariaDB ColumnStore APT-GET repository


Install package:


```
sudo apt-get install apt-transport-https dirmngr
```

Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore/latest/repo/debian9 stretch main
```

Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-api.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore-api/latest/repo/debian9 stretch main
```

Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-tools.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore-tools/latest/repo/debian9 stretch main
```

Add new file with repository information, /etc/apt/sources.list.d/mariadb-maxscale.list


```
deb https://downloads.mariadb.com/MaxScale/latest/debian stretch main
```

```
deb https://downloads.mariadb.com/MariaDB/data-adapters/mariadb-streaming-data-adapters/latest/repo/debian9 stretch main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

Download the MariaDB MaxScale key


```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 28C12247
```

### Installing MariaDB ColumnStore


With the repo file in place you can now install MariaDB ColumnStore like so:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore*
sudo apt-get install mariadb-columnstore-api*
sudo apt-get install mariadb-columnstore-tools
sudo apt-get install maxscale maxscale-cdc-connector
sudo apt-get install mariadb-columnstore-maxscale-cdc-adapters
sudo apt-get install mariadb-columnstore-kafka-avro-adapters
```

## Ubuntu 16


### Adding the MariaDB ColumnStore APT-GET repository


Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore/latest/repo/ubuntu16 xenial main
```

```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore-api/latest/repo/ubuntu16 xenial main
```

Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-tools.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore-tools/latest/repo/ubuntu16 xenial main
```

Add new file with repository information, /etc/apt/sources.list.d/mariadb-maxscale.list


```
deb https://downloads.mariadb.com/MaxScale/latest/ubuntu xenial main
```

Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-data-adapters.list


```
deb https://downloads.mariadb.com/MariaDB/data-adapters/mariadb-streaming-data-adapters/latest/repo/ubuntu16 xenial main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

Download the MariaDB MaxScale key


```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 28C12247
```

### Installing MariaDB ColumnStore


With the repo file in place you can now install MariaDB ColumnStore like so:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore*
sudo apt-get install mariadb-columnstore-api*
sudo apt-get install mariadb-columnstore-tools
sudo apt-get install maxscale maxscale-cdc-connector
sudo apt-get install mariadb-columnstore-maxscale-cdc-adapters
sudo apt-get install mariadb-columnstore-kafka-avro-adapters
```

## Ubuntu 18


### Adding the MariaDB ColumnStore APT-GET repository


Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore/latest/repo/ubuntu18 bionic main
```

```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore-api/latest/repo/ubuntu18 bionic main
```

Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-tools.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore-tools/latest/repo/ubuntu18 bionic main
```

Add new file with repository information, /etc/apt/sources.list.d/mariadb-maxscale.list


```
deb https://downloads.mariadb.com/MaxScale/latest/ubuntu bionic main
```

Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-data-adapters.list


```
deb https://downloads.mariadb.com/MariaDB/data-adapters/mariadb-streaming-data-adapters/latest/repo/ubuntu18 bionic main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

Download the MariaDB MaxScale key


```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 28C12247
```

### Installing MariaDB ColumnStore


With the repo file in place you can now install MariaDB ColumnStore like so:


```
sudo apt-get update
sudo add-apt-repository universe
sudo apt-get install mariadb-columnstore*
sudo apt-get install mariadb-columnstore-api*
sudo apt-get install mariadb-columnstore-tools
sudo apt-get install maxscale maxscale-cdc-connector
sudo apt-get install mariadb-columnstore-maxscale-cdc-adapters
sudo apt-get install mariadb-columnstore-kafka-avro-adapters
```

# MariaDB ColumnStore Packages


Before install, make sure you go through the preparation guide to complete the system setup before installs the packages


[preparing-for-columnstore-installation-11x.md](preparing-and-installing-mariadb-columnstore-11x/preparing-for-columnstore-installation-11x.md)


## CentOS 6


### Adding the MariaDB ColumnStore YUM repository


Add new file with repository information, /etc/yum.repos.d/mariadb-columnstore.repo


```
[mariadb-columnstore]
name=MariaDB ColumnStore
baseurl=https://downloads.mariadb.com/MariaDB/mariadb-columnstore/latest/yum/centos/6/x86_64/
gpgkey=https://downloads.mariadb.com/MariaDB/mariadb-columnstore/RPM-GPG-KEY-MariaDB-ColumnStore
gpgcheck=1
```

### Installing MariaDB ColumnStore


With the repo file in place you can now install MariaDB ColumnStore like so:


```
sudo yum --enablerepo=mariadb-columnstore clean metadata
sudo yum groups mark remove "MariaDB ColumnStore"
sudo yum groupinstall "MariaDB ColumnStore"
```

You can also install this way:


```
sudo yum --enablerepo=mariadb-columnstore clean metadata
sudo yum install mariadb-columnstore*
```

## CentOS 7


### Adding the MariaDB ColumnStore YUM repository


Add new file with repository information, /etc/yum.repos.d/mariadb-columnstore.repo


```
[mariadb-columnstore]
name=MariaDB ColumnStore
baseurl=https://downloads.mariadb.com/MariaDB/mariadb-columnstore/latest/yum/centos/7/x86_64/
gpgkey=https://downloads.mariadb.com/MariaDB/mariadb-columnstore/RPM-GPG-KEY-MariaDB-ColumnStore
gpgcheck=1
```

### Installing MariaDB ColumnStore


With the repo file in place you can now install MariaDB ColumnStore like so:


```
sudo yum --enablerepo=mariadb-columnstore clean metadata
sudo yum groups mark remove "MariaDB ColumnStore"
sudo yum groupinstall "MariaDB ColumnStore"
```

You can also install this way:


```
sudo yum --enablerepo=mariadb-columnstore clean metadata
sudo yum install mariadb-columnstore*
```

## SUSE 12


### Adding the MariaDB ColumnStore ZYPPER repository


Add new file with repository information, /etc/zypp/repos.d/mariadb-columnstore.repo


```
[mariadb-columnstore]
name=mariadb-columnstore
enabled=1
autorefresh=0
baseurl=https://downloads.mariadb.com/MariaDB/mariadb-columnstore/latest/yum/sles/12/x86_64
type=rpm-md
```

Download the MariaDB ColumnStore key


```
rpm --import https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key
```

### Installing MariaDB ColumnStore


With the repo file in place you can now install MariaDB ColumnStore like so:


```
sudo zypper refresh
sudo zypper install mariadb-columnstore*
```

## Debian 8


### Adding the MariaDB ColumnStore APT-GET repository


Install package:


```
sudo apt-get install apt-transport-https
```

Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore/latest/repo/debian8 jessie main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

### Installing MariaDB ColumnStore


With the repo file in place you can now install MariaDB ColumnStore like so:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore*
```

## Debian 9


### Adding the MariaDB ColumnStore APT-GET repository


Install package:


```
sudo apt-get install apt-transport-https dirmngr
```

Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore/latest/repo/debian9 stretch main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

### Installing MariaDB ColumnStore


With the repo file in place you can now install MariaDB ColumnStore like so:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore*
```

## Ubuntu 16


### Adding the MariaDB ColumnStore APT-GET repository


Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore/latest/repo/ubuntu16 xenial main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

### Installing MariaDB ColumnStore


With the repo file in place you can now install MariaDB ColumnStore like so:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore*
```

## Ubuntu 18


### Adding the MariaDB ColumnStore APT-GET repository


Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore/latest/repo/ubuntu18 bionic main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

### Installing MariaDB ColumnStore


With the repo file in place you can now install MariaDB ColumnStore like so:


```
sudo apt-get update
sudo add-apt-repository universe
sudo apt-get install mariadb-columnstore*
```

### After installation


After the installation completes, follow the configuration and startup steps in the Single-Node and Multi-Node Installation guides using the [Non-Distributed Install feature](preparing-and-installing-mariadb-columnstore-11x/installing-and-configuring-a-multi-server-columnstore-system-11x.md).


# MariaDB ColumnStore API (Bulk Write SDK) Package


Additional information on the ColumnStore API (Bulk Write SDK):


[columnstore-bulk-write-sdk.md](../columnstore-data-ingestion/columnstore-bulk-write-sdk.md)


## CentOS 7


### Adding the MariaDB ColumnStore API YUM repository


Add new file with repository information, /etc/yum.repos.d/mariadb-columnstore-api.repo


```
[mariadb-columnstore-api]
name=MariaDB ColumnStore API
baseurl=https://downloads.mariadb.com/MariaDB/mariadb-columnstore-api/latest/yum/centos/7/x86_64/
gpgkey=https://downloads.mariadb.com/MariaDB/mariadb-columnstore/RPM-GPG-KEY-MariaDB-ColumnStore
gpgcheck=1
```

### Installing MariaDB ColumnStore API


With the repo file in place you can now install MariaDB ColumnStore API like so:


```
sudo yum install epel-release
sudo yum --enablerepo=mariadb-columnstore-api clean metadata
sudo yum install mariadb-columnstore-api*
```

#### MariaDB ColumnStore API C++


To install only the C++ part of the API use:


```
sudo yum install epel-release
sudo yum --enablerepo=mariadb-columnstore-api clean metadata
sudo yum install mariadb-columnstore-api-cpp
sudo yum install mariadb-columnstore-api-cpp-devel
```

#### MariaDB ColumnStore API Java


To install only the Java part of the API use:


```
sudo yum install epel-release
sudo yum --enablerepo=mariadb-columnstore-api clean metadata
sudo yum install mariadb-columnstore-api-java
```

#### MariaDB ColumnStore API Python 2


To install only the Python 2 part of the API use:


```
sudo yum install epel-release
sudo yum --enablerepo=mariadb-columnstore-api clean metadata
sudo yum install mariadb-columnstore-api-python
```

#### MariaDB ColumnStore API Python 3


To install only the Python 3 part of the API use:


```
sudo yum install epel-release
sudo yum --enablerepo=mariadb-columnstore-api clean metadata
sudo yum install mariadb-columnstore-api-python3
```

#### MariaDB ColumnStore API Spark


To install only the Spark part of the API, and the Scala ColumnStore Exporter library use:


```
sudo yum install epel-release
sudo yum --enablerepo=mariadb-columnstore-api clean metadata
sudo yum install mariadb-columnstore-api-spark
```

#### MariaDB ColumnStore API PySpark


To install only the PySpark part of the API the Python ColumnStore exporter use:


```
sudo yum install epel-release
sudo yum --enablerepo=mariadb-columnstore-api clean metadata
sudo yum install mariadb-columnstore-api-pyspark
```

#### MariaDB ColumnStore API PySpark 3


To install only the PySpark 3 part of the API the Python 3 ColumnStore exporter use:


```
sudo yum install epel-release
sudo yum --enablerepo=mariadb-columnstore-api clean metadata
sudo yum install mariadb-columnstore-api-pyspark3
```

## Debian 8


### Adding the MariaDB ColumnStore API APT-GET repository


Install package:


```
sudo apt-get install apt-transport-https
```

Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-api.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore-api/latest/repo/debian8 jessie main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

Add new file with repository information, /etc/apt/sources.list.d/debian-backports.list


```
deb http://httpredir.debian.org/debian jessie-backports main contrib non-free
```

### Installing MariaDB ColumnStore API


With the repo file in place you can now install MariaDB ColumnStore API like so:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api*
```

#### MariaDB ColumnStore API C++


To install only the C++ part of the API use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-cpp
sudo apt-get install mariadb-columnstore-api-cpp-devel
```

#### MariaDB ColumnStore API Java


To install only the Java part of the API use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-java
```

#### MariaDB ColumnStore API Python 2


To install only the Python 2 part of the API use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-python
```

#### MariaDB ColumnStore API Python 3


To install only the Python 3 part of the API use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-python3
```

#### MariaDB ColumnStore API Spark


To install only the Spark part of the API, and the Scala ColumnStore Exporter library use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-spark
```

#### MariaDB ColumnStore API PySpark


To install only the PySpark part of the API the Python ColumnStore exporter use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-pyspark
```

#### MariaDB ColumnStore API PySpark 3


To install only the PySpark 3 part of the API the Python 3 ColumnStore exporter use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-pyspark3
```

## Debian 9


### Adding the MariaDB ColumnStore API APT-GET repository


Install package:


```
sudo apt-get install apt-transport-https dirmngr
```

Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-api.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore-api/latest/repo/debian9 stretch main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

### Installing MariaDB ColumnStore API


With the repo file in place you can now install MariaDB ColumnStore API like so:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api*
```

#### MariaDB ColumnStore API C++


To install only the C++ part of the API use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-cpp
sudo apt-get install mariadb-columnstore-api-cpp-devel
```

#### MariaDB ColumnStore API Java


To install only the Java part of the API use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-java
```

#### MariaDB ColumnStore API Python 2


To install only the Python 2 part of the API use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-python
```

#### MariaDB ColumnStore API Python 3


To install only the Python 3 part of the API use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-python3
```

#### MariaDB ColumnStore API Spark


To install only the Spark part of the API, and the Scala ColumnStore Exporter library use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-spark
```

#### MariaDB ColumnStore API PySpark


To install only the PySpark part of the API the Python ColumnStore exporter use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-pyspark
```

#### MariaDB ColumnStore API PySpark 3


To install only the PySpark 3 part of the API the Python 3 ColumnStore exporter use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-pyspark3
```

## Ubuntu 16


### Adding the MariaDB ColumnStore API APT-GET repository


Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-api.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore-api/latest/repo/ubuntu16 xenial main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

## Ubuntu 18


### Adding the MariaDB ColumnStore API APT-GET repository


Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-api.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore-api/latest/repo/ubuntu18 bionic main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

### Installing MariaDB ColumnStore API


With the repo file in place you can now install MariaDB ColumnStore API like so:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api*
```

#### MariaDB ColumnStore API C++


To install only the C++ part of the API use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-cpp
sudo apt-get install mariadb-columnstore-api-cpp-devel
```

#### MariaDB ColumnStore API Java


To install only the Java part of the API use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-java
```

#### MariaDB ColumnStore API Python 2


To install only the Python 2 part of the API use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-python
```

#### MariaDB ColumnStore API Python 3


To install only the Python 3 part of the API use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-python3
```

#### MariaDB ColumnStore API Spark


To install only the Spark part of the API, and the Scala ColumnStore Exporter library use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-spark
```

#### MariaDB ColumnStore API PySpark


To install only the PySpark part of the API the Python ColumnStore exporter use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-pyspark
```

#### MariaDB ColumnStore API PySpark 3


To install only the PySpark 3 part of the API the Python 3 ColumnStore exporter use:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-api-pyspark3
```

## Windows 10


Install via MSI (Windows Installer)


[](https://downloads.mariadb.com/MariaDB/mariadb-columnstore-api/latest/winx64-packages/)


# MariaDB ColumnStore Tools Package


Additional information on the Backup and Restore Tool:


[backup-and-restore-for-mariadb-columnstore-110-onwards.md](../managing-columnstore/managing-columnstore-system/mariadb-columnstore-backup-and-restore/backup-and-restore-for-mariadb-columnstore-110-onwards.md)


Additional information on mcsimport:


[columnstore-remote-bulk-data-import-mcsimport.md](../columnstore-data-ingestion/columnstore-remote-bulk-data-import-mcsimport.md)


## CentOS 6


### Adding the MariaDB ColumnStore Tools YUM repository


Add new file with repository information, /etc/yum.repos.d/mariadb-columnstore-tools.repo


```
[mariadb-columnstore-tools]
name=MariaDB ColumnStore Tools
baseurl=https://downloads.mariadb.com/MariaDB/mariadb-columnstore-tools/latest/yum/centos/6/x86_64/
gpgkey=https://downloads.mariadb.com/MariaDB/mariadb-columnstore/RPM-GPG-KEY-MariaDB-ColumnStore
gpgcheck=1
```

**Note:** The CentOS 6 package of mariadb-columnstore-tools doesn't include mcsimport.


### Installing MariaDB ColumnStore Tools


With the repo file in place you can now install MariaDB ColumnStore Tools like so:


```
sudo yum --enablerepo=mariadb-columnstore-tools clean metadata
sudo yum install mariadb-columnstore-tools
```

## CentOS 7


### Adding the MariaDB ColumnStore Tools YUM repository


Add new file with repository information, /etc/yum.repos.d/mariadb-columnstore-tools.repo


```
[mariadb-columnstore-tools]
name=MariaDB ColumnStore Tools
baseurl=https://downloads.mariadb.com/MariaDB/mariadb-columnstore-tools/latest/yum/centos/7/x86_64/
gpgkey=https://downloads.mariadb.com/MariaDB/mariadb-columnstore/RPM-GPG-KEY-MariaDB-ColumnStore
gpgcheck=1
```

### Installing MariaDB ColumnStore Tools


With the repo file in place you can now install MariaDB ColumnStore Tools like so:


```
sudo yum --enablerepo=mariadb-columnstore-tools clean metadata
sudo yum install mariadb-columnstore-tools
```

**Note:** The CentOS 7 package of mariadb-columnstore-tools includes mcsimport which requires mariadb-columnstore-api-cpp and its repository.


## SUSE 12


### Adding the MariaDB ColumnStore Tools ZYPPER repository


Add new file with repository information, /etc/zypp/repos.d/mariadb-columnstore-tools.repo


```
[mariadb-columnstore-tools]
name=mariadb-columnstore-tools
enabled=1
autorefresh=0
baseurl=https://downloads.mariadb.com/MariaDB/mariadb-columnstore-tools/latest/yum/sles/12/x86_64
type=rpm-md
```

Download the MariaDB ColumnStore key


```
rpm --import https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key
```

### Installing MariaDB ColumnStore


With the repo file in place you can now install MariaDB ColumnStore like so:


```
sudo zypper refresh
sudo zypper install mariadb-columnstore-tools
```

**Note:** The SUSE 12 package of mariadb-columnstore-tools doesn't include mcsimport.


## Debian 8


### Adding the MariaDB ColumnStore Tools APT-GET repository


Install package:


```
sudo apt-get install apt-transport-https
```

Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-tools.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore-tools/latest/repo/debian8 jessie main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

### Installing MariaDB ColumnStore Tools


With the repo file in place you can now install MariaDB ColumnStore Tools like so:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-tools
```

**Note:** The Debian 8 package of mariadb-columnstore-tools includes mcsimport which requires mariadb-columnstore-api-cpp and its repository.


## Debian 9


### Adding the MariaDB ColumnStore Tools APT-GET repository


Install package:


```
sudo apt-get install apt-transport-https dirmngr
```

Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-tools.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore-tools/latest/repo/debian9 stretch main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

### Installing MariaDB ColumnStore Tools


With the repo file in place you can now install MariaDB ColumnStore Tools like so:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-tools
```

**Note:** The Debian 9 package of mariadb-columnstore-tools includes mcsimport which requires mariadb-columnstore-api-cpp and its repository.


## Ubuntu 16


### Adding the MariaDB ColumnStore Tools APT-GET repository


Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-tools.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore-tools/latest/repo/ubuntu16 xenial main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

## Ubuntu 18


### Adding the MariaDB ColumnStore Tools APT-GET repository


Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-tools.list


```
deb https://downloads.mariadb.com/MariaDB/mariadb-columnstore-tools/latest/repo/ubuntu18 bionic main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

### Installing MariaDB ColumnStore Tools


With the repo file in place you can now install MariaDB ColumnStore Tools like so:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-tools
```

**Note:** The Ubuntu 16 and 18 packages of mariadb-columnstore-tools include mcsimport which requires mariadb-columnstore-api-cpp and its repository.


## Windows 10


Install via MSI (Windows Installer)


[](https://downloads.mariadb.com/ColumnStore-Tools/latest/winx64-packages/)


# MariaDB MaxScale Packages


## CentOS 6


### Adding the MariaDB MaxScale YUM repository


Add new file with repository information, /etc/yum.repos.d/mariadb-maxscale.repo


```
[mariadb-maxscale]
name=MariaDB MaxScale
baseurl=https://downloads.mariadb.com/MaxScale/latest/centos/6/x86_64
gpgkey=https://downloads.mariadb.com/MaxScale/MariaDB-MaxScale-GPG-KEY
gpgcheck=1
```

### Installing MariaDB MaxScale


With the repo file in place you can now install MariaDB MaxScale like so:


You can also install this way:


```
sudo yum --enablerepo=mariadb-maxscale clean metadata
sudo yum install maxscale maxscale-cdc-connector
```

## CentOS 7


### Adding the MariaDB MaxScale YUM repository


Add new file with repository information, /etc/yum.repos.d/mariadb-maxscale.repo


```
[mariadb-maxscale]
name=MariaDB MaxScale
baseurl=https://downloads.mariadb.com/MaxScale/latest/centos/7/x86_64
gpgkey=https://downloads.mariadb.com/MaxScale/MariaDB-MaxScale-GPG-KEY
gpgcheck=1
```

### Installing MariaDB MaxScale


You can also install this way:


```
sudo yum --enablerepo=mariadb-maxscale clean metadata
sudo yum install maxscale maxscale-cdc-connector
```

## SUSE 12


### Adding the MariaDB MaxScale ZYPPER repository


Add new file with repository information, /etc/zypp/repos.d/mariadb-maxscale.repo


```
[mariadb-maxscale]
name=mariadb-maxscale
enabled=1
autorefresh=0
baseurl=https://downloads.mariadb.com/MaxScale/latest/sles/12/x86_64
type=rpm-md
```

Download the MariaDB MaxScale key


```
rpm --import https://downloads.mariadb.com/MaxScale/MariaDB-MaxScale-GPG-KEY
```

### Installing MariaDB MaxScale


With the repo file in place you can now install MariaDB MaxScale like so:


```
sudo zypper refresh
sudo zypper install maxscale maxscale-cdc-connector
```

## Debian 8


### Adding the MariaDB MaxScale APT-GET repository


Install package:


```
sudo apt-get install apt-transport-https
```

Add new file with repository information, /etc/apt/sources.list.d/mariadb-maxscale.list


```
deb https://downloads.mariadb.com/MaxScale/latest/debian jessie main
```

Download the MariaDB MaxScale key


```
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 28C12247
```

### Installing MariaDB MaxScale


Additional information on setting to Maxscale:


[](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-21-06/)


With the repo file in place you can now install MariaDB MaxScale like so:


```
sudo apt-get update
sudo apt-get install maxscale maxscale-cdc-connector
```

## Debian 9


### Adding the MariaDB MaxScale APT-GET repository


Install package:


```
sudo apt-get install apt-transport-https dirmngr
```

Add new file with repository information, /etc/apt/sources.list.d/mariadb-maxscale.list


```
deb https://downloads.mariadb.com/MaxScale/latest/debian stretch main
```

Download the MariaDB MaxScale key


```
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 28C12247
```

### Installing MariaDB MaxScale


With the repo file in place you can now install MariaDB MaxScale like so:


```
sudo apt-get update
sudo apt-get install maxscale maxscale-cdc-connector
```

## Ubuntu 16


### Adding the MariaDB MaxScale APT-GET repository


Add new file with repository information, /etc/apt/sources.list.d/mariadb-maxscale.list


```
deb https://downloads.mariadb.com/MaxScale/latest/ubuntu xenial main
```

Download the MariaDB MaxScale key


```
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 28C12247
```

## Ubuntu 18


### Adding the MariaDB MaxScale APT-GET repository


Add new file with repository information, /etc/apt/sources.list.d/mariadb-maxscale.list


```
deb https://downloads.mariadb.com/MaxScale/latest/ubuntu bionic main
```

Download the MariaDB MaxScale key


```
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 28C12247
```

### Installing MariaDB MaxScale


With the repo file in place you can now install MariaDB MaxScale like so:


```
sudo apt-get update
sudo apt-get install maxscale maxscale-cdc-connector
```

# MariaDB Connector Packages


## ODBC Connector


Additional Information on the ODBC connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/)


How to Install the ODBC Connector:


[](https://mariadb.com/kb/en/library/about-mariadb-connector-odbc/)


## Java Connector


Additional information on the Java Connector:


[](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/)


How to Install the Java Connector:


[installing-mariadb-connectorj](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/installing-mariadb-connectorj)


# MariaDB ColumnStore Data Adapters Packages


Additional information on the Data Adapters:


[columnstore-streaming-data-adapters.md](../columnstore-data-ingestion/columnstore-streaming-data-adapters.md)


NOTE: MaxScale CDC Connector requires the MariaDB MaxScale package be installed first.


The MariaDB ColumnStore Data Adapters Packages are:


* Kafka Adapters
* Maxscale CDC Adapters


Kafka install package dependencies:


* N/A


Maxscale CDC install package dependencies::


* MaxScale CDC Connector
* MariaDB ColumnStore API
* MariaDB MaxScale


## CentOS 7


### Adding the MariaDB ColumnStore Data Adapters YUM repository


Add new file with repository information, /etc/yum.repos.d/mariadb-columnstore-data-adapters.repo


```
[mariadb-columnstore-data-adapters]
name=MariaDB ColumnStore Data Adapters
baseurl=https://downloads.mariadb.com/MariaDB/data-adapters/mariadb-streaming-data-adapters/latest/yum/centos/7/x86_64/
gpgkey=https://downloads.mariadb.com/MariaDB/mariadb-columnstore/RPM-GPG-KEY-MariaDB-ColumnStore
gpgcheck=1
```

### Installing MariaDB ColumnStore Data Adapters


With the repo file in place you can now install MariaDB ColumnStore Maxscale CDC Data Adapters like so:


```
sudo yum --enablerepo=mariadb-columnstore-data-adapters clean metadata
sudo yum install mariadb-columnstore-data-adapters-maxscale-cdc-adapter
```

With the repo file in place you can now install MariaDB ColumnStore Kafka Data Adapters like so:


```
sudo yum --enablerepo=mariadb-columnstore-data-adapters clean metadata
sudo yum install mariadb-columnstore-data-adapters-avro-kafka-adapter
```

## Debian 8


### Adding the MariaDB ColumnStore Data Adapters APT-GET repository


Install package:


```
sudo apt-get install apt-transport-https
```

Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-data-adapters.list


```
deb https://downloads.mariadb.com/MariaDB/data-adapters/mariadb-streaming-data-adapters/latest/repo/debian8 jessie main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

### Installing MariaDB ColumnStore Data Adapters


With the repo file in place you can now install MariaDB ColumnStore Maxscale CDC Data Adapters like so:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-maxscale-cdc-adapters
```

With the repo file in place you can now install MariaDB ColumnStore Kafka Data Adapters like so:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-kafka-avro-adapters
```

## Debian 9


### Adding the MariaDB ColumnStore Data Adapters APT-GET repository


Install package:


```
sudo apt-get install apt-transport-https dirmngr
```

Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-data-adapters.list


```
deb https://downloads.mariadb.com/MariaDB/data-adapters/mariadb-streaming-data-adapters/latest/repo/debian9 stretch main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

### Installing MariaDB ColumnStore Data Adapters


With the repo file in place you can now install MariaDB ColumnStores Maxscale CDC Data Adapters like so:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-maxscale-cdc-adapters
```

With the repo file in place you can now install MariaDB ColumnStores Kafka Data Adapters like so:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-kafka-avro-adapters
```

## Ubuntu 16


### Adding the MariaDB ColumnStore Data Adapters APT-GET repository


Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-data-adapters.list


```
deb https://downloads.mariadb.com/MariaDB/data-adapters/mariadb-streaming-data-adapters/latest/repo/ubuntu16 xenial main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

## Ubuntu 18


### Adding the MariaDB ColumnStore Data Adapters APT-GET repository


Add new file with repository information, /etc/apt/sources.list.d/mariab-columnstore-data-adapters.list


```
deb https://downloads.mariadb.com/MariaDB/data-adapters/mariadb-streaming-data-adapters/latest/repo/ubuntu18 bionic main
```

Download the MariaDB ColumnStore key


```
wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-columnstore/MariaDB-ColumnStore.gpg.key | sudo apt-key add -
```

### Installing MariaDB ColumnStore Data Adapters


With the repo file in place you can now install MariaDB ColumnStore Maxscale CDC Data Adapters like so:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-maxscale-cdc-adapters
```

With the repo file in place you can now install MariaDB ColumnStore Kafka Data Adapters like so:


```
sudo apt-get update
sudo apt-get install mariadb-columnstore-kafka-avro-adapters
```
