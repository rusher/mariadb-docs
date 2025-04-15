
# Creating a Trace File

If `<code>mysqld</code>` is crashing, creating a trace file is a good way to find the issue.


A `<code>mysqld</code>` binary that has been compiled with debugging support can create trace files using the DBUG package created by Fred Fish. To find out if your `<code>mysqld</code>` binary has debugging support, run `<code>mysqld -V</code>` on the command line. If the version number ends in `<code>-debug</code>` then your `<code>mysqld</code>` binary was compiled with debugging support.


See [Compiling MariaDB for debugging](compiling-mariadb-for-debugging.md) for instructions on how to create your own `<code>mysqld</code>` binary with debugging enabled.


To create the trace log, start `<code>mysqld</code>` like so:


```
mysqld --debug
```

Without options for --debug, the trace file will be named `<code>/tmp/mysqld.trace</code>` in MySQL and older versions of MariaDB before 10.5 and `<code>/tmp/mariadbd.trace</code>` starting from [MariaDB 10.5](../../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md).


On Windows, the debug `<code>mysqld</code>` is called `<code>mysqld-debug</code>` and you should also use the `<code>--standalone</code>` option. So the command on Windows will look like:


```
mysqld-debug --debug --standalone
```

Once the server is started, use the regular `<code>mysql</code>` command-line client (or another client) to connect and work with the server.


After you are finished debugging, stop the server with:


```
mysqladmin shutdown
```

## DBUG Options


Trace files can grow to a significant size. You can reduce their size by telling the server to only log certain items.


The `<code>--debug</code>` flag can take extra options in the form of a colon (:) delimited string of options. Individual options can have comma-separated sub-options.


For example:


```
mysqld --debug=d,info,error,query:o,/tmp/mariadbd.trace
```

The '`<code>d</code>`' option limits the output to the named DBUG_<N> macros. In the above example, the `<code>/tmp/mariadbd.trace</code>` tracefile will contain output from the info, error, and query DBUG macros. A '`<code>d</code>`' by itself (with no sub-options) will select all DBUG_<N> macros.


The '`<code>o</code>`' option redirects the output to a file (`<code>/tmp/mariadbd.trace</code>` in the example above) and overwrites the file if it exists.


## See Also


* [Options for --debug](../../../../../../connectors/mariadb-connector-c/mariadb-connectorc-api-functions/mysql_debug.md)

