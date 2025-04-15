
# Limitations/Differences with a MariaDB Server Compiled for Debugging

A MariaDB server configured with `<code>--with-debug=full</code>` has the following differences from a normal MariaDB server:


* You can have maximum of 1000 tables locked at the same time in one statement. (Define `<code>MAX_LOCKS</code>` in mysys/thrlock.c). This is to detect loops in the used lists.
* You can have maximum of 1000 threads locking the same table. (Define `<code>MAX_THREADS</code>` in mysys/thrlock.c). This is to detect loops in the used lists.
* Deadlock detection of mutex will be done at runtime. If wrong mutex handling is found an error will be printed to the error log. (Define `<code>SAFE_MUTEX</code>`)
* Memory overrun/underrun and not freed memory will be reported to the error log (Define `<code>SAFEMALLOC</code>`)
* You can get a trace of what `<code>mysqld</code>` (and most other binaries) is doing by starting it with the `<code>--debug</code>` option. The trace is usually put in `<code>/tmp</code>` or `<code>C:\</code>`

