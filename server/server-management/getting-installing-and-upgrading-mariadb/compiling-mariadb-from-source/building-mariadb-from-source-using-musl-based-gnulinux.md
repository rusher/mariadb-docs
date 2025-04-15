
# Building MariaDB From Source Using musl-based GNU/Linux

## Instructions on compiling MariaDB on musl-based operating systems (Alpine)


The instructions on this page will help you compile [MariaDB](../../../../columnstore/using-mariadb-columnstore/mariadb-columnstore-with-spark.md) from source.
Links to more complete instructions for specific platforms can be found on the
[source](source-building-mariadb-on-centos.md) page.


* First, [get a copy of the MariaDB source](../../../clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code.md).
* Next, [prepare your system to be able to compile the source](build-environment-setup-for-linux.md).


## Using cmake


[MariaDB 10.1](../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md) and above is compiled using *cmake*. You can configure your
build simply by running *cmake* using special option, i.e.


```
cmake . -DWITHOUT_TOKUDB=1
```

To build and install MariaDB after running *cmake* use


```
make
sudo make install
```

Note that building with MariaDB this way will disable tokuDB, till tokuDB becomes fully supported on musl.

