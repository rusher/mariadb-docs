
# SHOW ENGINE


## Syntax


```
SHOW ENGINE engine_name {STATUS | MUTEX}
```

## Description


`<code class="highlight fixed" style="white-space:pre-wrap">SHOW ENGINE</code>` displays operational information about a storage
engine. The following statements currently are supported:


```
SHOW ENGINE INNODB STATUS
SHOW ENGINE INNODB MUTEX
SHOW ENGINE PERFORMANCE_SCHEMA STATUS
SHOW ENGINE ROCKSDB STATUS
```

If the [Sphinx Storage Engine](../../../../storage-engines/sphinx-storage-engine/README.md) is installed, the following is also supported:


```
SHOW ENGINE SPHINX STATUS
```

See `<code>[SHOW ENGINE SPHINX STATUS](../../../../storage-engines/sphinx-storage-engine/about-sphinxse.md#show-engine-sphinx-status)</code>`.


Older (and now removed) synonyms were `<code class="highlight fixed" style="white-space:pre-wrap">SHOW INNODB STATUS</code>`
for `<code class="highlight fixed" style="white-space:pre-wrap">SHOW ENGINE INNODB STATUS</code>` and 
`<code class="highlight fixed" style="white-space:pre-wrap">SHOW MUTEX STATUS</code>` for 
`<code class="highlight fixed" style="white-space:pre-wrap">SHOW ENGINE INNODB MUTEX</code>`.


### SHOW ENGINE INNODB STATUS


`<code class="highlight fixed" style="white-space:pre-wrap">SHOW ENGINE INNODB STATUS</code>` displays extensive information
from the standard InnoDB Monitor about the state of the InnoDB storage engine.
See `<code>[SHOW ENGINE INNODB STATUS](show-engine-innodb-status.md)</code>` for more.


### SHOW ENGINE INNODB MUTEX


`<code class="highlight fixed" style="white-space:pre-wrap">SHOW ENGINE INNODB MUTEX</code>` displays InnoDB mutex statistics.


The statement displays the following output fields:


* Type: Always InnoDB.
* Name: The source file where the mutex is implemented, and the line number
 in the file where the mutex is created. The line number is dependent on the MariaDB version.
* Status: This field displays the following values if `<code>UNIV_DEBUG</code>` was defined at compilation time (for example, in include/univ.h in the InnoDB part of the source tree). Only the `<code>os_waits</code>` value is displayed if `<code>UNIV_DEBUG</code>` was not defined. Without `<code>UNIV_DEBUG</code>`, the information on which the output is based is insufficient to distinguish regular mutexes and mutexes that protect
 rw-locks (which allow multiple readers or a single writer). Consequently, the
 output may appear to contain multiple rows for the same mutex.

  * count indicates how many times the mutex was requested.
  * spin_waits indicates how many times the spinlock had to run.
  * spin_rounds indicates the number of spinlock rounds. (spin_rounds divided by
 spin_waits provides the average round count.)
  * os_waits indicates the number of operating system waits. This occurs when
 the spinlock did not work (the mutex was not locked during the spinlock and
 it was necessary to yield to the operating system and wait).
  * os_yields indicates the number of times a the thread trying to lock a mutex
 gave up its timeslice and yielded to the operating system (on the
 presumption that allowing other threads to run will free the mutex so that
 it can be locked).
  * os_wait_times indicates the amount of time (in ms) spent in operating system
 waits, if the timed_mutexes system variable is 1 (ON). If timed_mutexes is 0
 (OFF), timing is disabled, so os_wait_times is 0. timed_mutexes is off by
 default.


Information from this statement can be used to diagnose system problems. For
example, large values of spin_waits and spin_rounds may indicate scalability
problems.


The `<code>[information_schema](../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md).[INNODB_MUTEXES](../system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_mutexes-table.md)</code>` table provides similar information.


### SHOW ENGINE PERFORMANCE_SCHEMA STATUS


This statement shows how much memory is used for `<code>[performance_schema](../system-tables/performance-schema/performance-schema-tables/performance-schema-table_handles-table.md)</code>` tables and internal buffers.


The output contains the following fields:


* Type: Always `<code>performance_schema</code>`.
* Name: The name of a table, the name of an internal buffer, or the `<code>performance_schema</code>` word, followed by a dot and an attribute. Internal buffers names are enclosed by parenthesis. `<code>performance_schema</code>` means that the attribute refers to the whole database (it is a total).
* Status: The value for the attribute.


The following attributes are shown, in this order, for all tables:


* row_size: The memory used for an individual record. This value will never change.
* row_count: The number of rows in the table or buffer. For some tables, this value depends on a server system variable.
* memory: For tables and `<code>performance_schema</code>`, this is the result of `<code>row_size</code>` * `<code>row_count</code>`.


For internal buffers, the attributes are:


* count
* size


### SHOW ENGINE ROCKSDB STATUS


See also [MyRocks Performance Troubleshooting](../../../../storage-engines/myrocks/myrocks-performance-troubleshooting.md)

