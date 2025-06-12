---
description: >-
  Optimize MariaDB Server performance through hardware. This section covers
  selecting appropriate CPU, memory, and storage configurations to maximize your
  database's speed and throughput.
---

# Hardware Optimization

Better hardware is one of the easiest ways to improve performance.

As a general rule of thumb, hardware should be improved in the following order:

## Memory

Memory is the most important factor as it allows you to adjust the [Server System Variables](system-variables/server-system-variables.md). More memory means larger key and table caches can be stored in memory so that disk access, an order of magnitude slower, is reduced.

Simply adding more memory may not result in drastic improvements if the server variables are not set to make use of the extra available memory.

Using more RAM slots on the motherboard increases the bus frequency, and there will be more latency between the RAM and the CPU. So, using the highest RAM size per slot is preferable.

## Storage

Fast storage access is critical, as ultimately it's where the data resides. The key figure is the random seek time, a measurement of how fast the physical can retrieve data to access the data, so choose storage with as low a random seek time as possible.

Memory can make up for slow storage, but only that table data is accessed.

You can also add dedicated storage for temporary files and transaction logs.

## Network

## CPU

Although hardware bottlenecks often fall elsewhere, faster processors allow calculations to be performed more quickly, and the results sent back to the client more quickly. Besides processor speed, the processor's bus speed and cache size are also important factors to consider. Pipelining/ prefetching of instructions/data and other aspects of CPU architecture also have a significant effect.

If in doubt, ways conduct a benchmark that resembles the database workload of intended use.

## See Also

* [Configuring Linux for MariaDB](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-performance-advanced-configurations/configuring-linux-for-mariadb.md)

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
