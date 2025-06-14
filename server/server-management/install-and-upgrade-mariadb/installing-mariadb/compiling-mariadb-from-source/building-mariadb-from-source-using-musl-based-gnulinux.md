# Building MariaDB From Source Using musl-based GNU/Linux

## Instructions on compiling MariaDB on musl-based operating systems (Alpine)

The instructions on this page will help you compile [MariaDB](https://github.com/mariadb-corporation/docs-server/blob/test/en/mariadb/README.md) from source.\
Links to more complete instructions for specific platforms can be found on the[source](./) page.

* First, [get a copy of the MariaDB source](../../../../clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code.md).
* Next, [prepare your system to be able to compile the source](build-environment-setup-for-linux.md).

## Using cmake

[MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1) and above is compiled using _cmake_. You can configure your\
build simply by running _cmake_ using special option, i.e.

```
cmake . -DWITHOUT_TOKUDB=1
```

To build and install MariaDB after running _cmake_ use

```
make
sudo make install
```

Note that building with MariaDB this way will disable tokuDB, till tokuDB becomes fully supported on musl.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
