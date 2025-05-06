
# Compile and Using MariaDB with Sanitizers (ASAN, UBSAN, TSAN, MSAN)


## What are Sanitizers?


Sanitizers are open source runtime error detectors developed by Google that are enabled during the compile step. These sanitizers add extra code during compilation that will throw exceptions when certain errors are detected.


[AddressSanitizer (aka ASAN)](https://github.com/google/sanitizers/wiki/AddressSanitizer) is a memory error detector for C/C++. It finds a lot of the same things as [valgrind](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/compiling-mariadb-for-debugging), but with a lot less overhead.


* Use after free (dangling pointer dereference)
* Heap buffer overflow
* Stack buffer overflow
* Global buffer overflow
* Use after return
* Use after scope
* Initialization order bugs
* Memory leaks


At the moment the clang based sanitizers are more comprehensive than gcc.


In addition to ASAN there are sanitizers for Undefined Behaviour, Thread and Memory related errors.


[UndefinedBehaviourSanitizer (aka UBSAN)](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html)


[ThreadSanitizer (aka TSAN)](https://clang.llvm.org/docs/ThreadSanitizer.html)


[MemorySanitizer (aka MSAN)](https://clang.llvm.org/docs/MemorySanitizer.html)


## How to Compile MariaDB with Sanitizers


Before using ASAN locally, please ensure that it is installed on the system:


You can use one of the two following build commands:


```
cmake  -DWITH_ASAN=ON /source
```

Additionally, UBSAN, TSAN, and MSAN can be enabled in a similar way:


UBSAN:


```
cmake -DWITH_UBSAN=ON /source
```

TSAN:


```
cmake -DWITH_TSAN=ON /source
```

MSAN:


Note: keep in mind that only clang supports MSAN, g++ or other compilers will not work.


```
cmake -DWITH_MSAN=ON /source
```

## Running an MSAN Build


The time consuming aspect of building with MSAN is having [https:github.com/MariaDB/buildbot/blob/main/ci_build_images/msan.instrumentedlibs.sh](https://mariadb.com/kb/en/instrumented_system_libraries). As MariaDB Foundation have built the MSAN container already for buildbot, this is how you re-use this for building locally.


First, run the container where your current directory is the source directory:


```
podman run -v $PWD:/source:z \
  --rm \
  -ti \
  --entrypoint bash \
  --mount=type=tmpfs,tmpfs-size=10G,dst=/build \
  --workdir /build \
   quay.io/mariadb-foundation/bb-worker:debian12-msan-clang-20
```

## Docker/Podman Command Table


|   |   |   |
| --- | --- | --- |
| Command Component | Purpose | Notes |
| podman run | run a container | other implementations use docker syntax (or at at least close) |
| --rm | remove container on termination |  |
| -ti | a tty and a stdin are connected | for interactive container use |
| -v "$PWD":/source:z | mount current directory as /source inside the container - :z - read selinux label |  |
| --mount=type=tmpfs,tmpfs-size=10G,dst=/build | a 10G build directory and mtr | keeps as transient, big enough for some mtr tests |
| --workdir /build | default directory |  |
| --entrypoint bash | Ensure the cmd of buildbot start isn't executed |  |
| --cap-add=SYS_PTRACE | capability for tracing used by gdb | for debugging |
| Extra options |  |  |  |
| --name containername | useful if running multiple to keep track | Used as a name for a new session in the container (podman exec -ti containername bash) |
| --shm-size=10g | Size of /dev/shm as alternate for mtr tests | Default is unsable 64k, This is large enough for most --big-tests with some parallelism |
| --privileged | Allow rr recording | Note security impacting, don't run untrusted code as root |
| -v $DATADIR:/var/lib/mysql:Z | Mount an existing datadir | For testing against some prepared data |


Notes:


* docker can be used instead of the lighter weight podman if you so desired.
* /dev/shm is mounted no-exec so it rr recording here cannot be replayed while in that location
* optionally can make /build a filesystem mount to preserve the build.


All the following instructions are executed within the container - there is a document in /etc/motd that contains the latest information. Now run the configure stage of cmake:


```
cmake \
      -DWITH_MSAN=ON  \
      -DCMAKE_{EXE,MODULE}_LINKER_FLAGS="-L${MSAN_LIBDIR} -Wl,-rpath=${MSAN_LIBDIR}" \
      -DHAVE_CXX_NEW=1  \
      -DWITH_INNODB_{BZIP2,LZ4,LZMA,LZO,SNAPPY}=OFF \
      -DWITH_ZLIB=bundled  \
      -DWITH_NUMA=NO  \
      -DWITH_SYSTEMD=no \
      -DHAVE_LIBAIO_H=0    \
      -DCMAKE_DISABLE_FIND_PACKAGE_{URING,LIBAIO}=1  \
      -DPLUGIN_{MROONGA,ROCKSDB,OQGRAPH}=NO  \
      -DWITH_EMBEDDED_SERVER=OFF \
      /source
```

|   |   |
| --- | --- |
| CMake Options | Why |
| WITH_MSAN=ON | Enables MSAN build in compile options |
| CMAKE_{EXE,MODULE}_LINKER_FLAGS | links executables and shared libraries against the instrumented libraries with a rpath so a LD_LIBRARY_PATH env isn't required |
| WITH_INNODB_{BZIP2,LZ4,LZMA,LZO,SNAPPY}=OFF | system libraries for these haven't been MSAN instrumented currently |
| HAVE_CXX_NEW | Works around a ODR violation |
| WITH_ZLIB=bundled | This hasn't been MSAN instrumented currently |
| WITH_NUMA / WITH_SYSTEMD | both uninstrumented |
| HAVE_LIBAIO_H=0 / CMAKE_DISABLE_FIND_PACKAGE_LIBAIO | AIO currently not MSAN instrumented |
| CMAKE_DISABLE_FIND_PACKAGE_URING=NO | Uninstrumented [MDEV-36482](https://jira.mariadb.org/browse/MDEV-36482), and required seccomp adjustment or --privileged to work |
| PLUGIN_OQGRAPH (and PLUGIN_COLUMNSTORE) | Dependency on boost libraries are instrumented |
| WITH_EMBEDDED_SERVER=OFF | reduce build time |
| WITH_DBUG_TRACE=OFF | reduce runtime overhead if CMAKE_BUILD_TYPE=Debug chosen |


Run the build stage:


```
cmake --build . 
...
[100%] Built target mariadbd
[100%] Linking CXX executable mariadb-backup
Creating mariabackup link
[100%] Built target mariadb-backup
```

As the MSAN has rpath defined in its compile option there is no need for LD_LIBRARY_PATH manipulation.


To run tests:


```
mysql-test/mtr   (usual mtr options)
```

As newer versions occur and improvements happen these instructions may change. Look at the execution on the [buildbot builder](https://buildbot.mariadb.org/#/builders/amd64-debian-11-msan) to see if any changes have been made.


## Running an ASAN Build


To run mariadbd with instrumentation you have to set the `ASAN_OPTIONS` environment variable before starting `mariadbd` including starting `mariadbd` when running mtr.


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


* [Compiling MariaDB for debugging](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/compiling-mariadb-for-debugging)

