# mariadb-report

`mariadb-report` makes a friendly report of important MariaDB status values.

Prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-105), the client was called `mysqlreport`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.

Actually, `mariadb-report` makes a friendly report of nearly every status value from SHOW STATUS. Unlike SHOW STATUS which simply dumps over 100 values to the screen in one long list, mariadb-report interprets and
 formats the values and presents the basic values and many more inferred values in a human-readable format. Numerous example reports
 are available in the archive of the old [hackmysql.com/mysqlreport](http://hackmysql.com/mysqlreport), [archived here](https://github.com/daniel-nichter/hackmysql.com/tree/master/mysqlreport).

The benefit of mariadb-report is that it allows you to very quickly see a wide array of performance indicators for your MariaDB server
 which would otherwise need to be calculated by hand from all the various SHOW STATUS values. For example, the Index Read Ratio is an
 important value but it's not present in SHOW STATUS; it's an inferred value (the ratio of Key_reads to Key_read_requests).

This documentation outlines all the command line options in mariadb-report, most of which control which reports are printed. This document does not address how to interpret these reports; that topic is covered in the document Guide To Understanding mysqlreport, [archived here](https://github.com/daniel-nichter/hackmysql.com/blob/master/mysqlreport/mysqlreportguide.html).

#

# Usage

```
mariadb-report [options]
```

#

# mariadb-report options

Technically, command line options are in the form `--option`, but `-option` works too. All options can be abbreviated if the abbreviation is unique. For example, option `--host` can be abbreviated to `--ho` but not `--h` because `--h` is ambiguous: it could mean `--host` or `--help`.

| Option | Description |
| --- | --- |
| Option | Description |
| --all | Equivalent to --dtq --dms --com 3 --sas --qcache. (Notice --tab is not invoked by --all.) |
| --com N | Print top N number of non-DMS Com_ [status values](../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md) in descending order (after DMS in Questions report). If N is not given, default is 3. Such non-DMS Com_ values include [Com_change_db](../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#com_change_db), [Com_show_tables](../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#com_show_tables), [Com_rollback](../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md#com_rollback), etc. |
| --dms | Print Data Manipulation Statements (DMS) report (under DMS in Questions report). DMS are those from the [Data Manipulation](/en/data-manipulation/) section. mariadb-report considers only [SELECT](../server-usage/replication-cluster-multi-master/standard-replication/selectively-skipping-replication-of-binlog-events.md), [INSERT](../server-usage/programming-customizing-mariadb/views/inserting-and-updating-with-views.md), [REPLACE](replace-utility.md), [UPDATE](../reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/update.md), and [DELETE](../reference/sql-statements-and-structure/sql-statements/data-manipulation/changing-deleting-data/delete.md). Each DMS is listed in descending order by count. |
| --dtq | Print Distribution of Total Queries (DTQ) report (under Total in Questions report). Queries (or Questions) can be divided into four main areas: DMS (see --dms), Com_ (see --com ), COM_QUIT (see COM_QUIT and Questions, [archived here](https://github.com/daniel-nichter/hackmysql.com/blob/master/mysqlreport/mysqlreportguide.html)), and Unknown. --dtq lists the number of queries in each of these areas in descending order. |
| --email ADDRESS | After printing the report to screen, email the report to ADDRESS. This option requires sendmail in /usr/sbin/, therefore it does not work on Windows. /usr/sbin/sendmail can be a sym link to qmail, for example, or any MTA that emulates sendmail's -t command line option and operation. The FROM: field is "mariadb-report", SUBJECT: is "MySQL status report". |
| --flush-status | Execute a [FLUSH STATUS](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) after generating the reports. If you do not have permissions in MariaDB to do this an error from DBD::mysql::st will be printed after the reports. |
| --help | Output help information and exit. |
| --host ADDRESS | Host address. |
| --infile FILE | Instead of getting [SHOW STATUS](../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-status.md) values from MariaDB, read values from FILE. FILE is often a copy of the output of SHOW STATUS including formatting characters (+, -). mariadb-report expects FILE to have the format " value number " where value is only alpha and underscore characters (A-Z and _) and number is a positive integer. Anything before, between, or after value and number is ignored. mariadb-report also needs the following MariaDB server variables: [version](../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#version), [table_cache](../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache), [max_connections](../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_connections), [key_buffer_size](../reference/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size), [query_cache_size](../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#query_cache_size). These values can be specified in INFILE in the format "name = value" where name is one of the aforementioned server variables and value is a positive integer with or without a trailing M and possible periods (for version). For example, to specify an 18M key_buffer_size: key_buffer_size = 18M. Or, a 256 table_cache: table_cache = 256. The M implies Megabytes not million, so 18M means 18,874,368 not 18,000,000. If these server variables are not specified the following defaults are used (respectively) which may cause strange values to be reported: 0.0.0, 64, 100, 8M, 0. |
| --no-mycnf | Makes mariadb-report not read /.my.cnf which it does by default otherwise. --user and --password always override values from /.my.cnf. |
| --outfile FILE | After printing the report to screen, print the report to FILE too. Internally, mariadb-report always writes the report to a temp file first: /tmp/mysqlreport.PID on *nix, c:sqlreport.PID on Windows (PID is the script's process ID). Then it prints the temp file to screen. Then if --outfile is specified, the temp file is copied to OUTFILE. After --email (above), the temp file is deleted. |
| --password | As of version 2.3 --password can take the password on the command line like --password FOO. Using --password alone without giving a password on the command line causes mariadb-report to prompt for a password. |
| --port PORT | Port number. |
| --qcache | Print [Query Cache](../server-usage/replication-cluster-multi-master/optimization-and-tuning/buffers-caches-and-threads/query-cache.md) report. |
| --sas | Print report for Select_ and Sort_ [status values](../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-status-variables.md) (after Questions report). See MySQL Select and Sort Status Variables, archived [here](https://github.com/daniel-nichter/hackmysql.com/blob/master/mysqlreport/mysqlreportguide.html). |
| --socket SOCKET | For connections to localhost, the Unix socket file to use, or, on Windows, the name of the named pipe to use. |
| --tab | Print Threads, Aborted, and Bytes status reports (after Created temp report). The Threads report reports on all Threads_ status values. |
| --user USERNAME | Username. |