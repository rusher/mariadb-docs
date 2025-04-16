
# MariaDB Optimization for MySQL Users

MariaDB contains many new options and optimizations which, for
compatibility or other reasons, are not enabled in the default install.
Enabling them helps you gain extra performance from the same hardware
when upgrading from MySQL to MariaDB. This article contains information
on options and settings which you should enable, or at least look in
to, when making the switch.


```
aria-pagecache-buffer-size=##
```

If you are using a log of on-disk temporary tables, increase the above to as much as you can afford. See [Aria Storage Engine](../../../../reference/storage-engines/aria/aria-storage-engine.md) for more details.


```
key-cache-segments=8
```

If you use/have a lot of MyISAM files, increase the above to 4 or 8. See [Segmented Key Cache](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmarks/segmented-key-cache-performance.md) and [Segmented Key Cache Performance](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/benchmarks-and-long-running-tests/benchmarks/segmented-key-cache-performance.md) for more information.


```
thread-handling=pool-of-threads
```

Threadpool is a great way to increase performance in situations where queries are relatively short and the load is CPU bound (e.g. OLTP workloads). To enable it, add the above to your my.cnf file. See [Threadpool in 5.5](../buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb-51-53.md) for more information.

