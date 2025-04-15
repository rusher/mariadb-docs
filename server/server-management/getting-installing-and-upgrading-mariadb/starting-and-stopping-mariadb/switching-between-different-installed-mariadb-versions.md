
# Switching Between Different Installed MariaDB Versions

This article is about managing many different installed MariaDB versions
and running them one at a time. This is useful when doing benchmarking,
testing, or for when developing different MariaDB versions.


This is most easily done using the tar files from
[mariadb.org/download/](https://mariadb.org/download/).


## Stopping a pre-installed MySQL/MariaDB from interfering with your tests


If MySQL/MariaDB is already installed and running, you have two options:


1. Use test MariaDB servers with a different port & socket.

  * In this case you are probably best off creating a specific section for
 MariaDB in your `<code class="highlight fixed" style="white-space:pre-wrap">~/.my.cnf</code>` file.
1. Stop mysqld with `<code class="highlight fixed" style="white-space:pre-wrap">/etc/rc.d/mysql stop</code>`
 or `<code class="highlight fixed" style="white-space:pre-wrap">mariadb-admin shutdown</code>`.


Note that you don't have to uninstall or otherwise remove MySQL!


## How to create a binary distribution (tar file)


Here is a short description of how to generate a tar file from a source
distribution. If you have
[downloaded](https://downloads.askmonty.org/mariadb/) a binary tar file, you
can skip this section.


The steps to create a binary tar file are:


* Decide where to put the source. A good place is under `<code class="highlight fixed" style="white-space:pre-wrap">/usr/local/src/mariadb-5.#</code>`.
* [Get the source](../../../clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code.md)
* [Compile the source](../compiling-mariadb-from-source/compiling-mariadb-from-source-mariadb-source-configuration-options.md)
* [Create the binary tar ball](../compiling-mariadb-from-source/creating-the-mariadb-binary-tarball.md).


You will then be left with a tar file named something like:
`<code class="highlight fixed" style="white-space:pre-wrap">mariadb-11.0.1-MariaDB-linux-x86_64.tar.gz</code>`


## Creating a directory structure for the different installations


Install the binary tar files under `<code class="highlight fixed" style="white-space:pre-wrap">/usr/local/</code>` with
the following directory names (one for each MariaDB version you want to use), for example:


* `<code class="highlight fixed" style="white-space:pre-wrap">mariadb-10.5</code>`
* `<code class="highlight fixed" style="white-space:pre-wrap">mariadb-10.6</code>`
* `<code class="highlight fixed" style="white-space:pre-wrap">mariadb-10.11</code>`
* `<code class="highlight fixed" style="white-space:pre-wrap">mariadb-11.0</code>`
* `<code class="highlight fixed" style="white-space:pre-wrap">mariadb-11.1</code>`


The above assumes you are just testing major versions of MariaDB. If you are
testing specific versions, use directory names like `<code>mariadb-11.0.1</code>`


With the directories in place, create a sym-link named `<code>mariadb</code>` which points
at the `<code>mariadb-XXX</code>` directory you are currently testing. When you want to
switch to testing a different version, just update the sym-link.


Example:


```
cd /usr/local
tar xfz /tmp/mariadb-11.0.1-linux-systemd-x86_64.tar.gz
mv -vi mariadb-11.0.1-MariaDB-systemd-linux-x86_64 mariadb-11.0
ln -vs mariadb-11.0 mariadb
```

## Setting up the data directory


When setting up the data directory, you have the option of either using a
shared database directory or creating a unique database directory for each
server version. For testing, a common directory is probably easiest. Note that
you can only have one `<code class="highlight fixed" style="white-space:pre-wrap">mysqld</code>` server running against one data
directory.


### Setting up a common data directory


The steps are:


1. Create the `<code>mysql</code>` system user if you don't have it already!
 (On Linux you do it with the `<code>useradd</code>` command).
1. Create the directory (we call it `<code>mariadb-data</code>` in the example below) or
 add a symlink to a directory which is in some other place.
1. Create the `<code>mysql</code>` permission tables with [mariadb-install-db](../mariadb-install-db-exe.md)


```
cd /usr/local/
mkdir mariadb-data
cd mariadb
./bin/mariadb-install-db --no-defaults --datadir=/usr/local/mariadb-data
chown -R mysql mariadb-data mariadb-data/*
```

The reason to use `<code class="highlight fixed" style="white-space:pre-wrap">--no-defaults</code>` is to ensure that we don't
inherit incorrect options from some old my.cnf.


### Setting up different data directories


To create a different `<code class="highlight fixed" style="white-space:pre-wrap">data</code>` directories for each installation:


```
cd mariadb
./scripts/mariadb-install-db --no-defaults
chown -R mysql mariadb-data mariadb-data/*
```

This will create a directory `<code class="highlight fixed" style="white-space:pre-wrap">data</code>` inside the
current directory.


If you want to use another disk you should do:


```
cd mariadb
ln -s path-to-empty-directory-for-data data
./scripts/mariadb-install-db --no-defaults --datadir=./data
chown -R mysql mariadb-data mariadb-data/*
```

## Running a MariaDB server


The normal steps are:


```
rm mariadb
ln -s mariadb-# mariadb
cd mariadb
./bin/mysqld_safe --no-defaults --datadir=/usr/local/mariadb-data &
```

## Setting up a .my.cnf file for running multiple MariaDB main versions


If you are going to start/stop MariaDB a lot of times, you should create
a `<code class="highlight fixed" style="white-space:pre-wrap">~/.my.cnf</code>` file for the common options you are using.


The following example shows how to use a non-standard TCP-port and socket (to
not interfere with a main MySQL/MariaDB server) and how to setup different
options for each main server:


```
[client-server]
socket=/tmp/mysql.sock
port=3306
[mysqld]
datadir=/usr/local/mariadb-data

[mariadb-11.0]
# Options for MariaDB 11.0
[mariadb-11.1]
# Options for MariaDB 11.1
```

If you create an `<code class="highlight fixed" style="white-space:pre-wrap">~/.my.cnf</code>` file, you should start
`<code class="highlight fixed" style="white-space:pre-wrap">mysqld</code>` with `<code class="highlight fixed" style="white-space:pre-wrap">--defaults-file=~/.my.cnf</code>`
instead of `<code class="highlight fixed" style="white-space:pre-wrap">--no-defaults</code>` in the examples above.

