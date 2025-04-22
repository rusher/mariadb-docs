
# Compile and Using MariaDB with Sanitizers (ASAN, UBSAN, TSAN, MSAN)


## What are Sanitizers?


Sanitizers are open source runtime error detectors developed by Google that are enabled during the compile step. These sanitizers add extra code during compilation that will throw exceptions when certain errors are detected.


[AddressSanitizer (aka ASAN)](https://github.com/google/sanitizers/wiki/AddressSanitizer) is a memory error detector for C/C++. It finds a lot of the same things as [valgrind](https://app.gitbook.com/s/iJPrPCGi329TSR8WIXJW/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/compiling-mariadb-for-debugging), but with a lot less overhead.


* Use after free (dangling pointer dereference)
* Heap buffer overflow
* Stack buffer overflow
* Global buffer overflow
* Use after return
* Use after scope
* Initialization order bugs
* Memory leaks


To use ASAN you need a gcc version that supports ASAN. gcc 4.8.5 and up are known to work.


In addition to ASAN there are sanitizers for Undefined Behaviour, Thread and Memory related errors.


[UndefinedBehaviourSanitizer (aka UBSAN)](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html)


[ThreadSanitizer (aka TSAN)](https://clang.llvm.org/docs/ThreadSanitizer.html)


[MemorySanitizer (aka MSAN)](https://clang.llvm.org/docs/MemorySanitizer.html)


## How to Compile MariaDB with Sanitizers


Before using ASAN locally, please ensure that it is installed on the system:


```
yum install -y /usr/lib64/libasan.so.6.0.0
```

ASAN is supported in [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1) and up.


You can use one of the two following build commands:


```
cmake . -DWITH_ASAN=ON
```

or from [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) and up:


```
./BUILD/compile-pentium64-asan-max
```

Additionally, UBSAN, TSAN, and MSAN can be enabled in a similar way:


UBSAN:


```
yum install -y /usr/lib64/libubsan.so.1.0.0
cmake . -DWITH_UBSAN=ON
```

TSAN:


```
yum install -y /usr/lib64/libtsan.so.0.0.0
cmake . -DWITH_TSAN=ON
```

MSAN:


Note: keep in mind that only clang supports MSAN, g++ or other compilers will not work.


```
cmake . -DWITH_MSAN=ON
```

## Running an MSAN Build


The time consuming aspect of building with MSAN is having instrumented system libraries. As MariaDB Foundation have built the MSAN container already for buildbot, this is how you re-use this for building locally.


First, run the container where your current directory is the source directory:


```
podman run -v $PWD:/source:z -ti --user buildbot --entrypoint bash --shm-size 5G --env MSAN_SYMBOLIZER_PATH=/msan-libs/bin/llvm-symbolizer-msan --env  MSAN_OPTIONS=abort_on_error=1:poison_in_dtor=0 quay.io/mariadb-foundation/bb-worker:debian11-msan
```

Note: docker can be used instead of the lighter weight podman if you so desire.


The shm-size is for the MTR tests which exceed the 64k default shm-size.


All the following instructions are executed within the container. Now run the configure stage of cmake:


```
cmake /source -DCMAKE_C_COMPILER=clang-15 -DCMAKE_CXX_COMPILER=clang++-15 '-DCMAKE_C_FLAGS=-O2 -Wno-unused-command-line-argument -fdebug-macro' '-DCMAKE_CXX_FLAGS=-stdlib=libc++ -O2 -Wno-unused-command-line-argument -fdebug-macro' -DWITH_EMBEDDED_SERVER=OFF -DWITH_UNIT_TESTS=OFF -DCMAKE_BUILD_TYPE=Debug -DWITH_INNODB_BZIP2=OFF -DWITH_INNODB_LZ4=OFF -DWITH_INNODB_LZMA=OFF -DWITH_INNODB_LZO=OFF -DWITH_INNODB_SNAPPY=OFF -DPLUGIN_ARCHIVE=NO -DPLUGIN_TOKUDB=NO -DPLUGIN_MROONGA=NO -DPLUGIN_OQGRAPH=NO -DPLUGIN_ROCKSDB=NO -DPLUGIN_CONNECT=NO -DPLUGIN_SPIDER=NO -DWITH_SAFEMALLOC=OFF -DWITH_ZLIB=bundled -DWITH_SSL=bundled -DWITH_PCRE=bundled -DHAVE_LIBAIO_H=0 -DCMAKE_DISABLE_FIND_PACKAGE_URING=1 -DCMAKE_DISABLE_FIND_PACKAGE_LIBAIO=1 -DWITH_MSAN=ON -DWITH_DBUG_TRACE=OFF
```

Run the build stage:


```
cmake --build . --parallel 
...
[100%] Built target mariadbd
[100%] Linking CXX executable mariadb-backup
Creating mariabackup link
[100%] Built target mariadb-backup
```

As the important MTR step needs to use the instrumented libraries MTR is run using the LD_LIBRARY_PATH to use those.


```
LD_LIBRARY_PATH=/msan-libs mysql-test/mtr  --mem --big-test --force --retry=0 --skip-test=.*compression.*  --parallel=auto
```

As newer versions occur and improvements happen these instructions may change. Look at the execution on the [buildbot builder](https://buildbot.mariadb.org/#/builders/amd64-debian-11-msan) to see if any changes have been made.


## Running an ASAN Build


To run mariadbd with instrumentation you have to set the `ASAN_OPTIONS` environment variable before starting `mariadbd`. Either in your shell or in your [mariadbd_safe](../../../clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe.md) script.


```
export ASAN_OPTIONS=abort_on_error=1
```

The above command will abort any instrumented executable if any errors are found, which is good for debugging. If you set abort_on_error=0 all server errors are logged to your error log file (mysqld.err).


To catch errors for other processes than the server, you can set more options, like this:


```
export ASAN_OPTIONS=abort_on_error=1:log_path=/tmp/asan
```

If you are seeing an incomplete stack trace for a memory allocation, you may rerun the failing test with


```
export ASAN_OPTIONS=abort_on_error=1:log_path=/tmp/asan:fast_unwind_on_malloc=0
```

To get core dumps of failures:


```
export ASAN_OPTIONS=abort_on_error=1:disable_coredump=0
```

To see all the options (or to check if an executable is instrumented), you may try the following:


```
ASAN_OPTIONS=help=1 extra/perror 0
```

### Using Valgrind


The [MariaDB test system](../../../clients-and-utilities/mariadb-test/README.md) can use [Valgrind](https://www.valgrind.org) for finding memory leaks and wrong memory accesses. Valgrind is an instrumentation framework for building dynamic analysis tools. If Valgrind is installed on your system, you can simply use [mysql-test-run --valgrind](../../../clients-and-utilities/mariadb-test/mariadb-test-run-pl-options.md) to run the test under Valgrind.


## See Also


* [Compiling MariaDB for debugging](https://app.gitbook.com/s/iJPrPCGi329TSR8WIXJW/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/compiling-mariadb-for-debugging)

