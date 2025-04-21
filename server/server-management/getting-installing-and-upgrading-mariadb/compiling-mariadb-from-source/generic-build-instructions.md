
# Generic Build Instructions

The instructions on this page will help you compile [MariaDB](/kb/en/mariadb/) from source.
Links to more complete instructions for specific platforms can be found on the
[source](README.md) page.


First, [get a copy of the MariaDB source](../../../clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code.md).


Next, [prepare your system to be able to compile the source](build-environment-setup-for-linux.md).


If you don't want to run MariaDB as yourself, then you should create a
`mysql` user. The example below uses this user.


## Using cmake


[MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) and above is compiled using *cmake*.


It is recommended to create a build directory **beside** your source directory


```
mkdir build-mariadb
cd build-mariadb
```

**NOTE**
If you have built MariaDB in the past and have recently updated the repository, you should perform a complete cleanup of old artifacts (such as cmake configured files). In the base repository run:


```
git clean -xffd && git submodule foreach --recursive git clean -xffd
```

You can configure your build simply by running *cmake* without any special options, like


```
cmake ../server
```

where `server` is where you installed MariaDB. If you are building in the source directory, just omit `../server`.


If you want it to be configured exactly as a normal MariaDB server release is built, use


```
cmake ../server -DBUILD_CONFIG=mysql_release
```

This will configure the build to generate binary tarballs similar to release tarballs from downloads.mariadb.org. Unfortunately this doesn't work on old platforms, like OpenSuse Leap 15.0, because MariaDB binary tarballs are built to minimize external dependencies, and that needs static libraries that might not be provided by the platform by default, and would need to be installed manually.


To do a build suitable for debugging use:


```
cmake ../server -DCMAKE_BUILD_TYPE=Debug
```

By default, MariaDB is compiled with the `-Werror` flag, which causes compiling to abort
if there is a compiler warning. You can disable that by configuring with
`-DMYSQL_MAINTAINER_MODE=OFF`.


```
cmake ../server -DCMAKE_BUILD_TYPE=Debug -DMYSQL_MAINTAINER_MODE=OFF.
```

All *cmake* configuration options for MariaDB can be displayed with:


```
cmake ../server -LH
```

To build and install MariaDB after running *cmake* use


```
cmake --build .
sudo cmake --install .
```

If the commands above fail, you can enable more compilation information by doing:


```
cmake --build . --verbose
```

If you want to generate a binary tarball, run


```
cpack
```

## Using BUILD Scripts


There are also `BUILD` scripts for the most common systems for those that doesn't want to dig into cmake options. These are optimized for in source builds.


The scripts are of type 'compile-#cpu#-how_to_build'. Some common scripts-are



| Script | Description |
| --- | --- |
| Script | Description |
| compile-pentium64 | Compile an optimized binary optimized for 64 bit pentium (works also for amd64) |
| compile-pentium-debug | Compile a debug binary optimized for 64 bit pentium |
| compile-pentium-valgrind-max | Compile a debug binary that can be used with [valgrind](https://www.valgrind.org/) to find wrong memory accesses and memory leaks. Should be used if one want's to run the mysql-test-run test suite with the --valgrind option |



Some common suffixes used for the scripts:



| Suffix | Description |
| --- | --- |
| Suffix | Description |
| 32 | Compile for 32 bit cpu's |
| 64 | Compile for 64 bit cpu's |
| -max | Enable (almost) all features and plugins that MariaDB supports |
| -gprof | binary is compiled with profiling (gcc --pg) |
| -gcov | binary is compiled with code coverage (gcc -fprofile-arcs -ftest-coverage) |
| -valgrind | The binary is compiled for debugging and optimized to be used with [valgrind](https://www.valgrind.org/). |
| -debug | The binary is compiled with all symbols (gcc -g) and the [DBUG](https://app.gitbook.com/s/iJPrPCGi329TSR8WIXJW/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/creating-a-trace-file) log system is enabled. |



All `BUILD` scripts support the following options:



| Suffix | Description |
| --- | --- |
| Suffix | Description |
| -h, --help | Show this help message. |
| -n, --just-print | Don't actually run any commands; just print them. |
| -c, --just-configure | Stop after running configure. Combined with --just-print shows configure options. |
| --extra-configs=xxx | Add this to configure options |
| --extra-flags=xxx | Add this C and CXX flags |
| --extra-cflags=xxx | Add this to C flags |
| --extra-cxxflags=xxx | Add this to CXX flags |
| --verbose | Print out full compile lines |
| --with-debug=full | Build with full debug(no optimizations, keep call stack). |



A typical compilation used by a developer would be:


```
shell> ./BUILD/compile-pentium64-debug
```

This configures the source for debugging and runs make. The server binary will be `sql/mariadbd` or `sql/mysqld`.


## Starting MariaDB for the First Time


After installing MariaDB (using `sudo make install`), but prior to starting MariaDB for the first time, one should:


1. Ensure the directory where you want MariaDB to store it's data is owned by the `mariadb` user (if the user doesn't exist, you'll need to create it)
1. Create a [MariaDB configuration config file](../configuring-mariadb-with-option-files.md) (/.my.cnf or /etc/my.cnf) with the configuration options you desire. A suggested minimum configuration file, to specify where you want your data to be stored, would be:


```
[mariadbd]
datadir=/usr/local/mariadb/data/
```

1. run the [mariadb-install-db](../../../clients-and-utilities/mariadb-install-db.md) script to generate the needed system tables


Here is an example:


```
# The following assumes that the 'mariadb' user exists and that we installed MariaDB
# in /usr/local/mariadb
chown -R mariadb /usr/local/mariadb/
cd /usr/local/mariadb/
./scripts/mariadb-install-db --user=mariadb
/usr/local/mariadb/bin/mariadb-safe --user=mariadb &
```

If needed, you can also use the --datadir=/usr/local/mariadb/data/ options with `mariadbd-install-db` and `mariadbd-safe`


## Testing MariaDB


If you want to test your compiled MariaDB, you can do either of:


Run unit tests:


```
cmake --build . --target test
```

Or run mtr tests:


```
mysql-test/mysql-test-run --force
```

Each of the above are run from the build directory. There is no need to '`make install`/`cmake --install .`' MariaDB prior to running them.


**NOTE:** If you are doing more extensive testing or debugging of MariaDB (like with real application data and workloads) you may want to start and run MariaDB directly from the source directory instead of installing it with '`sudo make install`'. If so, see
[Running MariaDB from the Source Directory](../starting-and-stopping-mariadb/running-mariadb-from-the-build-directory.md).


## Increasing Version Number or Tagging a Version


If you have made code changes and want to increase the version number or tag our version with a specific tag you can do this by editing the `VERSION` file. Tags are shown when running the '`mariadbd --version`' command.


## Non-ascii Symbols


MariaDB builds with `readline`; using an alternative such as `Editline` may result in problems with non-ascii symbols.


## Post-install Tasks


* [Installing system tables (mariadb-install-db)](../installing-system-tables-mariadb-install-db.md)
* [Starting and Stopping MariaDB Automatically](../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md)

