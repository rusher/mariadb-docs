
# Memory is Leaking

Operating system memory can be assigned, giving MariaDB a virtual address space, and allocated (paged in), once MariaDB starts to use this memory.


When looking at something that might be a memory leak, pay particular attention between the virtual size and the resident size.


When MariaDB has the same virtual size, but the resident size increases over time, this is a good indication that the memory buffers allocated to MariaDB are slowly being used. In this case its unlikely to be a memory leak.


Because memory leaks are hard to track down, documenting a known good version and a version that is leaking memory can make it easier to examine code changes in those versions against some other criteria like those obtained from the sections below to identify the cause.


## Performance Schema


The memory instrumentation of the performance schema can be enable with the following:


```
performance_schema=on
performance-schema-instrument='memory/%=ON'
```


This is available since [MariaDB 10.5.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1052-release-notes.md). With this enabled, [performance_schema.memory_summary_global_by_event_name](../../../../../server/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-memory_summary_global_by_event_name-table.md) can start to show where the memory leak is occurring.


## Memleak


`<code>memleak</code>` is a BPF program for Linux that is frequently packaged like bcc-tools or similar ([bpfcc-tools](https://packages.debian.org/stable/bpfcc-tools) on Debian).


The upstream documentation provides [this example](https://github.com/iovisor/bcc/blob/master/tools/memleak_example.txt).


The important aspect on measurement is to let MariaDB startup, and commence an normal workload before measurement. Starting too early or before the caches are populated is likely to result in false recording of memory allocations that will be eventually released.


Increasing the time interval of `<code>memleak</code>` is important to run longer than the usual query. If your memory is leaking over hours, then a high interval of 10 minutes so will reduce memory temporary allocated for a query. Recording for a longer time or multiple times should provide enough information to narrow down the location of the leak.


Note: Very old Linux kernels like Centos/RHEL 7 might not have sufficient hooks to measure this correctly.

