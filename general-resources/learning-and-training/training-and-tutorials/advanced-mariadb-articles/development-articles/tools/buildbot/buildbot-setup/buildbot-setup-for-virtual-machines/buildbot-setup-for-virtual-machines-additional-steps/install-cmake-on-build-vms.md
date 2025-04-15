
# Install cmake on build VMs

[MariaDB 5.5](../../../../../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) Requires cmake. Install cmake on all -build VMs (and other Unix-like machines) with:


```
wget http://www.cmake.org/files/v2.8/cmake-2.8.8.tar.gz
tar -zxvf cmake-2.8.8.tar.gz
cd cmake-2.8.8;./configure
make
sudo make install
```
