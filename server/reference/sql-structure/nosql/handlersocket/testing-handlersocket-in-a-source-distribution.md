# Testing HandlerSocket in a Source Distribution

## [MariaDB 5.5](broken-reference)

In [MariaDB 5.5](broken-reference), which is built using `cmake`, `Makefile.PL` is not generated automatically. If you want to run the perl tests, you will need to create it manually from `Makefile.PL.in`. It is fairly easy to do by replacing `LIB` and `INC` values with the correct ones. Also, `libhsclient.so` is not built by default; `libhsclient.a` can be found in `plugin/handler_socket` folder.

## [MariaDB 5.3](broken-reference)

If you want to test or use handlersocket with a source installation of [MariaDB 5.3](broken-reference),\
here is one way to do this:

1. Compile with one of the build scripts that has the `-max` option,\
   like `BUILD/compile-pentium64-max` or `BUILD/compile-pentium64-debug-max`
2. Start mysqld with the test framework

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

1. If you would like to install the handlersocket perl module permanently, you\
   should do:

```
make install
```

If you do this, you don't have to set `PERL5LIB` below.

1. Run the handlersocket test suite

```
cd plugin/handler_socket/regtest/test_01_lib
MYHOST=127.0.0.1 MYPORT=9306 LD_LIBRARY_PATH=../../libhsclient/.libs/ \
PERL5LIB=../common:../../perl-Net-HandlerSocket/lib:../../perl-Net-HandlerSocket/blib/arch/auto/Net/HandlerSocket/ ./run.sh
```

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
