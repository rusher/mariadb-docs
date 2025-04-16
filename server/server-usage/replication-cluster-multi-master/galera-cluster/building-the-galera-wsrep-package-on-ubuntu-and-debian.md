
# Building the Galera wsrep Package on Ubuntu and Debian

The instructions on this page were used to create the *galera* package on the Ubuntu and Debian Linux distributions. This package contains the wsrep provider for [MariaDB Galera Cluster](../../../reference/sql-statements-and-structure/sql-statements/built-in-functions/special-functions/galera-functions/README.md).


The version of the wsrep provider is **25.3.5**. We also provide **25.2.9** for those that need or want it. Prior to that, the wsrep version was 23.2.7.


1. Install prerequisites:


```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get -y install check debhelper libasio-dev libboost-dev libboost-program-options-dev libssl-dev scons
```

1. Clone [galera.git](https://github.com/mariadb/galera) from [github.com/mariadb](https://github.com/mariadb) and checkout mariadb-3.x banch:


```
git init repo
cd repo
git clone -b mariadb-3.x https://github.com/MariaDB/galera.git
```

1. Build the packages by executing `build.sh` under scripts/ directory with `-p` switch:


```
cd galera
./scripts/build.sh -p
```

When finished, you will have the Debian packages for galera library and arbitrator in the parent directory.


## Running galera test suite


If you want to run the `galera` test suite (`mysql-test-run --suite=galera`), you need to install the galera library as either `/usr/lib/galera/libgalera_smm.so` or `/usr/lib64/galera/libgalera_smm.so`

