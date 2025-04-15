
# Compiling MariaDB for Debugging


Compiling MariaDB with full debug information includes all code symbols and also new code to do internal testing of structures and allow one to trace MariaDB execution. A full debug binary will be notably slower than a normal binary (30%).


## Compiling MariaDB for Debugging Using the `<code>CMAKE_BUILD_TYPE</code>` Option


On Unix systems, you can build a debug build by executing `<code>cmake</code>` and by setting the `<code>CMAKE_BUILD_TYPE</code>` option to `<code>Debug</code>`. For example:


```
cmake -DCMAKE_BUILD_TYPE=Debug .
```

## Compiling MariaDB for Debugging Using Build Scripts


The other option is to use the scripts in the BUILD directory that will compile MariaDB with most common debug options and plugins:


```
./BUILD/compile-pentium64-debug-max
```

or alternatively if you want to use the [Valgrind](https://www.valgrind.org) memory checking tool with the [MariaDB test system](../../../../../../server/reference/mariadb-internals/using-mariadb-with-your-programs-api/libmysqld/mariadb-test-and-mariadb-test-embedded.md):


```
./BUILD/compile-pentium64-valgrind-max
```

There are separate build scripts for different configurations in the BUILD directory.


You can find a list of the needed packages/libraries for building on Linux [here](/kb/en/Build_Environment_Setup_for_Linux/).


### Example of Compiling MariaDB for Debugging Using Build Scripts


* Scripts containing "debug" in the name are for developers that want to build, develop and test MariaDB.
* Scripts containing "valgrind" in the name are for running mariadbd under [valgrind](https://valgrind.org). Compiling for valgrind means that we are using another implementation of MEM_ROOT to allow valgrind to better detect memory overruns. In addition, some memory areas are marked as used/not used to remove some false positives.
* Scripts containing "max" in the name include all normal plugins.


Here is an example of how to compile MariaDB for debugging in your home directory with [MariaDB 5.2.9](../../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-2-series/mariadb-529-release-notes.md) as an example:


```
cd ~
mkdir mariadb
cd mariadb
tar xvf mariadb-5.2.9.tar.gz
ln -s mariadb-5.2.9 current
cd current
./BUILD/compile-pentium64-debug-max
```

The last command will produce a debug version of `<code class="highlight fixed" style="white-space:pre-wrap">sql/mysqld</code>`.
If you have a system other than 64 bit Intel/AMD on Linux you can use a
different `<code class="highlight fixed" style="white-space:pre-wrap">BUILD/...-debug-max</code>` file. If this fails, you can
try with:


```
cmake --build  .  --config Debug
make -j4
```

## Building Optimized Build With Debug Symbols


To build MariaDB with symbols, to get better stack traces and to be able to debug the binary with `<code>gdb</code>`, you need to supply the `<code>-g3</code>` option to the `<code>gcc</code>` compiler.


Just compiling with `<code>-g3</code>` will make the binary much bigger but the slowdown of the server should be negligible.


One way to do this is to edit the script


```
BUILD/compile-pentium64-max
```

and add the -g3 last on the line with `<code>extra_flags</code>`, like this:


```
extra_flags="$pentium64_cflags $fast_cflags -g3"
```

After that you can compile MariaDB with debugging symbols by just execution the above script.


## Doing a Debug Build on Debian/Ubuntu


To build a "mysqld" binary with debugging enabled that uses the same parameters as the ones used in Debian/Ubuntu binary packages, you must do as follows (you must have a deb-src line of one of the MariaDB repositories on your /etc/apt/sources.list in order to do that):


```
apt-get build-dep mariadb-10.2
apt-get install cmake libaio1 libaio-dev
apt-get source mariadb-10.2
cd mariadb-10.2*
./debian/rules configure
./BUILD/compile-pentuim64-debug-all
```

Then you will have your "debugging enabled" mysqld binary in the sql/ directory.


This binary can directly replace the one provided by the binary package that is placed on "/usr/bin/mysqld".


### Temporarily Installing your Debug Build


The commands shown below replace the release `<code>mysqld</code>` binary with the debug `<code>mysqld</code>` binary that you compiled. Most importantly, they replace the binary in a way which makes it trivial to revert back to the
original release `<code>mysqld</code>` binary.


First, [stop MariaDB](https://mariadb.com/kb/en/).


Then, use the `<code>mv</code>` utility to rename the release `<code>mysqld</code>` binary:


```
sudo mv /usr/sbin/mysqld /usr/sbin/mysqld-orig
```

Note: Do not use the `<code>cp</code>` utility because that will change the file modification timestamp.


Then, install the debug `<code>mysqld</code>` binary from your source tree:


```
sudo install ~/mariadb-10.3.14/sql/mysqld /usr/sbin/mysqld-debug
```

Then, link the `<code>mysqld</code>` path to the path of your debug `<code>mysqld</code>` binary:


```
sudo ln -s /usr/sbin/mysqld-debug /usr/sbin/mysqld
```

Then, [start MariaDB](https://mariadb.com/kb/en/).


Be sure to replace `<code>/usr/sbin/mysqld</code>` with the path to your `<code>mysqld</code>` binary and to also replace `<code><code>~</code>/mariadb-10.3.14/sql/mysqld</code>` with the path to your debug `<code>mysqld</code>` binary.


### Reinstalling your Release Build


If you want to restore your original `<code>mysqld</code>` binary, you can do it with the following process::


First, [stop MariaDB](https://mariadb.com/kb/en/).


Then, execute the following command to delete the symbolic link:


```
sudo rm /usr/sbin/mysqld
```

Then, execute the following command to move the original `<code>mysqld</code>` release binary back into place:


```
sudo mv /usr/sbin/mysqld-orig /usr/sbin/mysqld
```

Then, [start MariaDB](https://mariadb.com/kb/en/).


Be sure to replace `<code>/usr/sbin/mysqld</code>` with the path to your `<code>mysqld</code>` binary


Notice that the debug `<code>mysqld</code>` binary located at `<code>/usr/sbin/mysqld-debug</code>` was not deleted. Only the symbolic link to this file was deleted. The debug `<code>mysqld</code>` binary is still present if it is needed again in the future.


## Different Compilation Options


### Changing DBUG_ASSERT to Print to Error Log


A debug binary has lots of code checks and asserts, that are not checked in production. This is done to get more performance when running in production.
In some cases, when one is trying to find a hard-to-repeat bug, it could be beneficial to have these checks in production builds too.


Compiling with `<code>-DDBUG_ASSERT_AS_PRINTF</code>` will change DBUG_ASSERT() to print any failed check to the [error log](../../../../../../server/server-management/server-monitoring-logs/error-log.md).


```
cmake . -DDBUG_ASSERT_AS_PRINTF
```

Enabling the above option should not have any notable impact on performance (probably < 1% slowdown).
This is achieved by grouping asserts in MariaDB server code into two groups:


* Fast checks, using `<code>DBUG_ASSERT()</code>`: These are converted to printing to error log.
* Slow checks, using `<code>DBUG_SLOW_ASSERT()</code>`. These will always be removed in production builds.


## See Also


* [Build environment setup for Linux](/kb/en/Build_Environment_Setup_for_Linux/)
* [Debugging MariaDB with a debugger](debugging-mariadb-with-a-debugger.md)
* [Creating a trace file](creating-a-trace-file.md)
* [Using ASAN with MariaDB](../../../../../../server/server-management/getting-installing-and-upgrading-mariadb/compiling-mariadb-from-source/compile-and-using-mariadb-with-sanitizers-asan-ubsan-tsan-msan.md)

