
# mariadbd-safe

The `<code>mariadbd-safe</code>` startup script is in MariaDB distributions on Linux and Unix. It is a wrapper that starts `<code>mariadbd</code>` with some extra safety features. For example, if `<code>mariadbd-safe</code>` notices that `<code>mariadbd</code>` has crashed, then `<code>mariadbd-safe</code>` will automatically restart `<code>mariadbd</code>`.


`<code>mariadbd-safe</code>` is the recommended way to start `<code>mariadbd</code>` on Linux and Unix distributions that do not support `<code>[systemd](systemd.md)</code>`. Additionally, the [mysql.server](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-servers-table.md) init script used by [sysVinit](sysvinit.md) starts `<code>mariadbd</code>` with `<code>mariadbd-safe</code>` by default.


Prior to [MariaDB 10.5](../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md), the client used to be called `<code>mysqld_safe</code>`, and can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.





## Using mariadbd-safe


The command to use `<code>mariadbd-safe</code>` and the general syntax is:


```
mariadbd-safe [ --no-defaults | --defaults-file | --defaults-extra-file | --defaults-group-suffix | --print-defaults ] <options> <mariadbd_options>
```

### Options


Many of the options supported by `<code>mariadbd-safe</code>` are identical to
options supported by `<code>[mariadbd](mariadbd-options.md)</code>`. If an unknown option is provided to `<code>mariadbd-safe</code>` on the command-line, then it is passed to `<code>mariadbd</code>`.


`<code>mariadbd-safe</code>` supports the following options:



| Option | Description |
| --- | --- |
| Option | Description |
| --help | Display a help message and exit. |
| --autoclose | (NetWare only) On NetWare, mariadbd-safe provides a screen presence. When you unload (shut down) the mariadbd-safe NLM, the screen does not by default go away. Instead, it prompts for user input: NLM has terminated; Press any key to close the screen. If you want NetWare to close the screen automatically instead, use the --autoclose option to mariadbd-safe. |
| --basedir=path | The path to the MariaDB installation directory. |
| --core-file-size=size | The size of the core file that mariadbd should be able to create. The option value is passed to ulimit -c. |
| --crash-script=file | Script to call in the event of mariadbd crashing. |
| --datadir=path | The path to the data directory. |
| --defaults-extra-file=path | The name of an option file to be read in addition to the usual option files. This must be the first option on the command line if it is used. If the file does not exist or is otherwise inaccessible, the server will exit with an error. |
| --defaults-file=file_name | The name of an option file to be read instead of the usual option files. This must be the first option on the command line if it is used. |
| --defaults-group-suffix=# | In addition to the default option groups, also read option groups with this suffix. |
| --flush-caches | Flush and purge buffers/caches before starting the server. |
| --ledir=path | If mariadbd-safe cannot find the server, use this option to indicate the path name to the directory where the server is located. |
| --log-error=file_name | Write the error log to the given file. |
| --malloc-lib=lib | Preload shared library lib if available. See [debugging MariaDB](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/debugging-a-running-server-on-linux.md) for an example. |
| --mysqld=prog_nam | The name of the server program (in the ledir directory) that you want to start. This option is needed if you use the MariaDB binary distribution but have the data directory outside of the binary distribution. If mariadbd-safe cannot find the server, use the --ledir option to indicate the path name to the directory where the server is located. |
| --mysqld-version=suffix | This option is similar to the --mysqld option, but you specify only the suffix for the server program name. The basename is assumed to be mysqld. For example, if you use--mysqld-version=debug, mariadbd-safe starts the mariadbd-debug program in the ledir directory. If the argument to --mysqld-version is empty, mariadbd-safe uses mysqld in the ledir directory. |
| --nice=priority | Use the nice program to set the server´s scheduling priority to the given value. |
| --no-defaults | Do not read any option files. This must be the first option on the command line if it is used. |
| --no-watch, --nowatch, --no-auto-restart | Exit after starting mariadbd. |
| --numa-interleave | Run mariadbd with its memory interleaved on all NUMA nodes. |
| --open-files-limit=count | The number of files that mariadbd should be able to open. The option value is passed to ulimit -n. Note that you need to start mariadbd-safe as root for this to work properly. |
| --pid-file=file_name | The path name of the process ID file. |
| --plugin-dir=dir_name | Directory for client-side plugins. |
| --port=port_num | The port number that the server should use when listening for TCP/IP connections. The port number must be 1024 or higher unless the server is started by the root system user. |
| --print-defaults | Print the program argument list and exit. |
| --skip-kill-mysqld | Do not try to kill stray mariadbd processes at startup. This option works only on Linux. |
| --socket=path | The Unix socket file that the server should use when listening for local connections. |
| --syslog, --skip-syslog | --syslog causes error messages to be sent to syslog on systems that support the logger program. --skip-syslog suppresses the use of syslog; messages are written to an error log file. |
| --syslog-tag=tag | For logging to syslog, messages from mariadbd-safe and mariadbd are written with a tag of mariadbd-safe and mariadbd, respectively. To specify a suffix for the tag, use --syslog-tag=tag, which modifies the tags to be mariadbd-safe-tag and mariadbd-tag. |
| --timezone=timezone | Set the TZ time zone [environment variable](../mariadb-environment-variables.md) to the given option value. Consult your operating system documentation for legal time zone specification formats. Also see [Time Zones](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md). |
| --user={user_name or user_id} | Run the mariadbd server as the user having the name user_name or the numeric user ID user_id. (“User” in this context refers to a system login account, not a MariaDB user listed in the grant tables.) |



### Option Files


In addition to reading options from the command-line, `<code>mariadbd-safe</code>` can also read options from [option files](../configuring-mariadb-with-option-files.md). If an unknown option is provided to `<code>mariadbd-safe</code>` in an option file, then it is ignored.


The following options relate to how MariaDB command-line tools handles option files. They must be given as the **first argument** on the command-line:



| Option | Description |
| --- | --- |
| Option | Description |
| --print-defaults | Print the program argument list and exit. |
| --no-defaults | Don't read default options from any option file. |
| --defaults-file=# | Only read default options from the given file #. |
| --defaults-extra-file=# | Read this file after the global files are read. |
| --defaults-group-suffix=# | In addition to the default option groups, also read option groups with this suffix. |



#### Option Groups


`<code>mariadbd-safe</code>` reads options from the following [option groups](../configuring-mariadb-with-option-files.md#option-groups) from [option files](../configuring-mariadb-with-option-files.md):



| Group | Description |
| --- | --- |
| Group | Description |
| [mysqld_safe] | Options read by mysqld_safe, which includes both MariaDB Server and MySQL Server. |
| [safe_mysqld] | Options read by mysqld_safe, which includes both MariaDB Server and MySQL Server. |
| [mariadbd-safe] | Options read by mariadbd_safe_safe from MariaDB Server. Available starting with [MariaDB 10.4.6](../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1046-release-notes.md). |
| [mariadb-safe] | Options read by mysqld_safe from MariaDB Server. Deprecated, please avoid using this. |



The `<code>[safe_mariadbd]</code>` option group is primarily supported for backward compatibility. You should rename such option groups to `<code>[mariadbd-safe]</code>` in MariaDB installations to prevent breakage in the future if this compatibility is removed.


`<code>mariadbd-safe</code>` also reads options from the following server [option groups](../configuring-mariadb-with-option-files.md#option-groups) from [option files](../configuring-mariadb-with-option-files.md):



| Group | Description |
| --- | --- |
| Group | Description |
| [mysqld] | Options read by mysqld, which includes both MariaDB Server and MySQL Server. |
| [server] | Options read by MariaDB Server. |
| [mysqld-X.Y] | Options read by a specific version of mysqld, which includes both MariaDB Server and MySQL Server. For example, [mysqld-5.5]. |
| [mariadb] | Options read by MariaDB Server. |
| [mariadb-X.Y] | Options read by a specific version of MariaDB Server. |
| [client-server] | Options read by all MariaDB [client programs](/kb/en/clients-utilities/) and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. |
| [galera] | Options read by a galera-capable MariaDB Server. Available on systems compiled with Galera support. |



For example, if you specify the `<code>[log_error](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#log_error)</code>` option in a server option group in an option file, like this:


```
[mariadb]
log_error=error.log
```

Then `<code>mariadbd-safe</code>` will also use this value for its own `<code>--log-error</code>` option:


### Configuring the Open Files Limit


When using `<code>mariadbd-safe</code>`, the system's open files limit can be changed by providing the `<code>--open-files-limit</code>` option either on the command-line or in an option file. For example:


```
[mariadbd-safe]
open_files_limit=4294967295
```

The option value is passed to `<code>ulimit -n</code>`. Note that you need to start `<code>mariadbd-safe</code>` as root for this to work properly. However, you can't currently set this to `<code>unlimited</code>`. See [MDEV-18410](https://jira.mariadb.org/browse/MDEV-18410) about that.


When `<code>mariadbd-safe</code>` starts `<code>mariadbd</code>`, it also uses this option to set the value of the `<code>[open_files_limit](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#open_files_limit)</code>` system variable for `<code>mariadbd</code>`.


### Configuring the Core File Size


When using `<code>mariadbd-safe</code>`, if you would like to [enable core dumps](../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/debugging-mariadb/enabling-core-dumps.md), the system's core file size limit can be changed by providing the `<code>--core-file-size</code>` option either on the command-line or in an option file. For example:


```
[mariadbd-safe]
core_file_size=unlimited
```

The option value is passed to `<code>ulimit -c</code>`. Note that you need to start `<code>mariadbd-safe</code>` as root for this to work properly.


### Configuring MariaDB to Write the Error Log to Syslog


When using `<code>mariadbd-safe</code>`, if you would like to redirect the error log to the [syslog](https://linux.die.net/man/8/rsyslogd), then that can easily be done by using the `<code>--syslog</code>` option. `<code>mariadbd-safe</code>` redirects two types of log messages to the syslog--its own log messages, and log messages for `<code>mariadbd</code>`.


* `<code>mariadbd-safe</code>` configures its own log messages to go to the `<code>daemon</code>` syslog facility. The log level for these messages is either `<code>notice</code>` or `<code>error</code>`, depending on the specific type of log message. The default tag is `<code>mariadbd-safe</code>`.


* `<code>mariadbd-safe</code>` also configures the log messages for `<code>mariadbd</code>` to go to the `<code>daemon</code>` syslog facility. The log level for these messages is `<code>error</code>`. The default tag is `<code>mariadbd</code>`.


Sometimes it can be helpful to add a suffix to the syslog tag, such as if you are running multiple instances of MariaDB on the same host. To add a suffix to each syslog tag, use the `<code>--syslog-tag</code>` option.


## Specifying mariadbd


By default, `<code>mariadbd-safe</code>` tries to start an executable named `<code>mariadbd</code>`.


You can also specify another executable for `<code>mariadbd-safe</code>` to start instead of `<code>mariadbd</code>` by providing the `<code>--mariadbd</code>` or `<code>--mariadbd-version</code>` options either on the command-line or in an option file.


By default, it will look for `<code>mariadbd</code>` in the following locations in the following order:


* `<code>$BASEDIR/libexec/mysqld</code>`
* `<code>$BASEDIR/sbin/mysqld</code>`
* `<code>$BASEDIR/bin/mysqld</code>`
* `<code>$PWD/bin/mysqld</code>`
* `<code>$PWD/libexec/mysqld</code>`
* `<code>$PWD/sbin/mysqld</code>`
* `<code>@libexecdir@/mysql</code>`


Where `<code>$BASEDIR</code>` is set by the `<code>--basedir</code>` option, `<code>$PWD</code>` is the current working directory where `<code>mariadbd-safe</code>` was invoked, and `<code>@libexecdir@</code>` is set at compile-time by the `<code>INSTALL_BINDIR</code>` option for `<code>[cmake](../compiling-mariadb-from-source/generic-build-instructions.md#using-cmake)</code>`.


You can also specify where the executable is located by providing the `<code>--ledir</code>` option either on the command-line or in an option file.


## Specifying datadir


By default, `<code>mariadbd-safe</code>` will look for the `<code>datadir</code>` in the following locations in the following order:


* `<code>$BASEDIR/data/mysql</code>`
* `<code>$BASEDIR/data</code>`
* `<code>$BASEDIR/var/mysql</code>`
* `<code>$BASEDIR/var</code>`
* `<code>@localstatedir@</code>`


Where `<code>$BASEDIR</code>` is set by the `<code>--basedir</code>` option, and `<code>@localstatedir@</code>` is set at compile-time by the `<code>INSTALL_MYSQLDATADIR</code>` option for `<code>[cmake](../compiling-mariadb-from-source/generic-build-instructions.md#using-cmake)</code>`.


You can also specify where the `<code>datadir</code>` is located by providing the `<code>--datadir</code>` option either on the command-line or in an option file.


## Logging


When you use `<code>mariadbd-safe</code>` to start `<code>mariadbd</code>`, `<code>mariadbd-safe</code>` logs to the same destination as `<code>mariadbd</code>`.


`<code>mariadbd-safe</code>` has several log-related options:


* `<code>--syslog</code>`: Write error messages to syslog on systems that
 support the logger program.
* `<code>--skip-syslog</code>`: Do not write error messages to syslog.
 Messages are written to the default error log file (host_name.err in the data
 directory), or to a named file if the `<code class="fixed" style="white-space:pre-wrap">--log-error</code>` option
 is given.
* `<code>--log-error=file_name</code>`: Write error messages to the named
 error file.


If none of these options is provided, then the default is `<code>--skip-syslog</code>`.


If `<code>--syslog</code>` and `<code>--log-error</code>` are both provided, then a warning is issued and `<code>--log-error</code>` takes precedence.


`<code>mariadbd-safe</code>` also writes notices to `<code>stdout</code>` and errors to `<code>stderr</code>`.


## Editing mariadbd-safe


`<code>mariadbd-safe</code>` is a `<code>sh</code>` script, so if you need to change its behavior, then it can easily be edited. However, you should not normally edit the script. A lot of behavior can be changed by providing options either on the command-line or in an option file.


If you do edit `<code>mariadbd-safe</code>`, then you should be aware of the fact that a package upgrade can overwrite your changes. If you would like to preserve your changes, be sure to have a backup.


## NetWare


On NetWare, mariadbd-safe is a NetWare Loadable Module (NLM)
that is ported from the original Unix shell script. It starts the server as
follows:


1. Runs a number of system and option checks.
1. Runs a check on MyISAM tables.
1. Provides a screen presence for the MariaDB server.
1. Starts mariadbd, monitors it, and restarts it if it terminates in error.
1. Sends error messages from mariadbd to the host_name.err file in the data directory.
1. Sends mariadbd-safe screen output to the host_name.safe file
 in the data directory.


## See Also


* [How to increase max number of open files on Linux](https://www.cyberciti.biz/faq/linux-increase-the-maximum-number-of-open-files). This can be used to solve issues like this warning from mariadbd: `<code class="fixed" style="white-space:pre-wrap">Changed limits: max_open_files: 1024 (requested 5000)"</code>`
* [mariadbd Options](mariadbd-options.md)
* [systemd](systemd.md)

