
# Testing HandlerSocket in a Source Distribution


## [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)


In [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md), which is built using `<code>cmake</code>`, `<code>Makefile.PL</code>` is not generated automatically. If you want to run the perl tests, you will need to create it manually from `<code>Makefile.PL.in</code>`. It is fairly easy to do by replacing `<code>LIB</code>` and `<code>INC</code>` values with the correct ones. Also, `<code>libhsclient.so</code>` is not built by default; `<code>libhsclient.a</code>` can be found in `<code>plugin/handler_socket</code>` folder.


## [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md)


If you want to test or use handlersocket with a source installation of [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md),
here is one way to do this:


1. Compile with one of the build scripts that has the `<code>-max</code>` option,
 like `<code>BUILD/compile-pentium64-max</code>` or `<code>BUILD/compile-pentium64-debug-max</code>`
1. Start mysqld with the test framework
```
cd mysql-test
LD_LIBRARY_PATH=../plugin/handler_socket/libhsclient/.libs \
MTR_VERSION=1 perl mysql-test-run.pl --start-and-exit 1st \
--mysqld=--plugin-dir=../plugin/handler_socket/handlersocket/.libs \
--mysqld=--loose-handlersocket_port=9998 \
--mysqld=--loose-handlersocket_port_wr=9999 \
--master_port=9306 --mysqld=--innodb
```
1. This will end with:
```
Servers started, exiting
```
1. Load handlersocket
```
client/mysql -uroot --protocol=tcp --port=9306 \
-e 'INSTALL PLUGIN handlersocket soname "handlersocket.so"'
```
1. Configure and compile the handlersocket perl module
```
cd plugin/handler_socket/perl-Net-HandlerSocket
perl Makefile.PL
make
```
1. If you would like to install the handlersocket perl module permanently, you
should do:
```
make install
```

If you do this, you don't have to set `<code>PERL5LIB</code>` below.
1. Run the handlersocket test suite
```
cd plugin/handler_socket/regtest/test_01_lib
MYHOST=127.0.0.1 MYPORT=9306 LD_LIBRARY_PATH=../../libhsclient/.libs/ \
PERL5LIB=../common:../../perl-Net-HandlerSocket/lib:../../perl-Net-HandlerSocket/blib/arch/auto/Net/HandlerSocket/ ./run.sh
```

