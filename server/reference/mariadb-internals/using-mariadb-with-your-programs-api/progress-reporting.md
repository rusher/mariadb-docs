
# Progress Reporting

MariaDB supports progress reporting for some long running commands.


## What is Progress Reporting?


Progress reporting means that:


* There is a `<code>Progress</code>` column
 in [SHOW PROCESSLIST](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-processlist.md) which shows the total progress
 (0-100%)
* [INFORMATION_SCHEMA.PROCESSLIST](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) has three columns which allow you to see in which process stage we are and how much of that stage is completed:

  * `<code>STAGE</code>`
  * `<code>MAX_STAGE</code>`
  * `<code>PROGRESS</code>` (within current stage).
* The client receives progress messages which it can display to the user to
 indicate how long the command will take.


We have separate progress reporting for stages because different stages take
different amounts of time.


## Supported Commands


Currently, the following commands can send progress report messages to the
client:


* [ALTER TABLE](../../sql-statements-and-structure/sql-statements/data-definition/alter/alter-tablespace.md)
* [CREATE INDEX](../../sql-statements-and-structure/sql-statements/data-definition/create/create-index.md)
* [DROP INDEX](../../sql-statements-and-structure/sql-statements/data-definition/drop/drop-index.md)
* [LOAD DATA INFILE](../../sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) (not `<code>LOAD DATA LOCAL INFILE</code>`, as in that case we
 don't know the size of the file).


Some Aria storage engine operations also support progress messages:


* [CHECK TABLE](../../sql-statements-and-structure/sql-statements/table-statements/check-table.md)
* [REPAIR TABLE](../../sql-statements-and-structure/sql-statements/table-statements/repair-table.md)
* [ANALYZE TABLE](../../sql-statements-and-structure/sql-statements/table-statements/analyze-table.md)
* [OPTIMIZE TABLE](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/optimizing-tables/optimize-table.md)


### Limitations


Although the above commands support progress reporting, there are some limitations to what progress is reported. To be specific, when executing one of these commands against an InnoDB table with [ALGORITHM=INPLACE](../../storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-inplace-alter-algorithm.md) (which is the default in [MariaDB 10.0](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)+), progress is only reported during the merge sort phase while reconstructing indexes.


## Enabling and Disabling Progress Reporting


`<code>mysqld</code>` (the MariaDB server) automatically sends progress report messages to clients that support the new protocol, using the value of the [progress_report_time](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#progress_report_time) variable. They are sent every
max(`<code>global.progress_report_time</code>` , `<code>progress_report_time</code>`) seconds (by default 5). You can disable the sending of progress report messages to the client by setting either the local variable (affects only the current connection) or the global variable (affects all connections) to `<code>0</code>`.


If the extra column in `<code>SHOW PROCESSLIST</code>` gives you a compatibility problem,
you can disable it by starting `<code>mysqld</code>` with the `<code class="fixed" style="white-space:pre-wrap">--old</code>` flag.


## Clients Which Support Progress Reporting


* The [mariadb command line client](../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md)
* The `<code>mytop</code>` that comes with MariaDB has a `<code>'%'</code>` column which shows
 the progress.


## Progress Reporting in the mysql Command Line Client


Progress reporting is enabled by default in the [mariadb client](../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md). You can
disable it with `<code class="fixed" style="white-space:pre-wrap">--disable-progress-reports</code>`. It is automatically disabled in
batch mode.


When enabled, for every supported command you get a progress report like:


```
ALTER TABLE my_mail ENGINE=aria;
Stage: 1 of 2 'copy to tmp table'  5.37% of stage done
```

This is updated every [progress_report_time](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#progress_report_time) seconds (the default is 5). If the global `<code>progress_report_time</code>` is higher, this will be used. You can also disable error reporting by setting the variable to `<code>0</code>`.


## How to Add Support for Progress Reporting to a Client


You need to use the [MariaDB 5.3](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) or later client library. You can check that the library
supports progress reporting by doing:


```
#ifdef CLIENT_PROGRESS
```

To enable progress reporting to the client you need to add
`<code>CLIENT_PROGRESS</code>` to the `<code>connect_flag</code>` in `<code>mysql_real_connect()</code>`:


```
mysql_real_connect(mysql, host, user, password,
                   database, opt_mysql_port, opt_mysql_unix_port,
                   connect_flag | CLIENT_PROGRESS);
```

Then you need to provide a callback function for progress reports:


```
static void report_progress(const MYSQL *mysql, uint stage, uint max_stage,
                            double progress, const char *proc_info,
                            uint proc_info_length);

mysql_options(&mysql, MYSQL_PROGRESS_CALLBACK, (void*) report_progress);
```

The above `<code>report_progress</code>` function will be called for each
progress message.


This is the implementation used by `<code>mysql.cc</code>`:


```
uint last_progress_report_length;

static void report_progress(const MYSQL *mysql, uint stage, uint max_stage,
                            double progress, const char *proc_info,
                            uint proc_info_length)
{
  uint length= printf("Stage: %d of %d '%.*s' %6.3g%% of stage done",
                      stage, max_stage, proc_info_length, proc_info, 
                      progress);
  if (length < last_progress_report_length)
    printf("%*s", last_progress_report_length - length, "");
  putc('\r', stdout);
  fflush(stdout);
  last_progress_report_length= length;
}
```

If you want only one number for the total progress, you can calculate it with:


```
double total_progress=
 ((stage -1) / (double) max_stage * 100.00 + progress / max_stage);
```

**Note:** `<code>proc_info</code>` is totally independent of stage. You can have many
different `<code>proc_info</code>` values within a stage. The idea behind `<code>proc_info</code>` is
to give the user more information about what the server is doing.


## How to Add Support for Progress Reporting to a Storage Engine


The functions to use for progress reporting are:


```
void thd_progress_init(MYSQL_THD thd, unsigned int max_stage);
```

Initialize progress reporting with stages. This is mainly used for
commands that are totally executed within the engine, like `<code>CHECK TABLE</code>`.
You should not use this for operations that could be called by, for example,
`<code>ALTER TABLE</code>` as this has already called the function.


`<code>max_stage</code>` is the number of stages your storage engine will have.


```
void thd_progress_report(MYSQL_THD thd, unsigned long long progress,
                         unsigned long long max_progress);
```

The above is used for reporting progress.


* `<code>progress</code>` is how much of the file/rows/keys you have gone through.
* `<code>max_progress</code>` is the max number of rows you will go through.


You can call this with varying numbers, but normally the ratio
`<code>progress/max_progress</code>` should be increasing.


This function can be called even if you are not using stages, for example when
enabling keys as part of `<code>ALTER TABLE</code>` or `<code>ADD INDEX</code>`.


```
void thd_progress_next_stage(MYSQL_THD thd);
```

To go to the next stage in a multi-stage process initiated by
`<code>thd_progress_init()</code>`:


```
void thd_progress_end(MYSQL_THD thd);
```

End progress reporting; Sets 'Progress' back to 0 in `<code>SHOW PROCESSLIST</code>`.


```
const char *thd_proc_info(thd, 'stage name');
```

This sets the name of the current status/stage that is displayed in
`<code>SHOW PROCESSLIST</code>` and in the client. It's recommended that you call
this between stages and thus before `<code>thd_progress_report()</code>` and
`<code>thd_progress_next_stage()</code>`.


This functions returns the last used `<code>proc_info</code>`. It's recommended that
you restore `<code>proc_info</code>` to its original value when you are done
processing.


**Note:** `<code>thd_proc_info()</code>` is totally independent of stage. You can have
many different `<code>proc_info</code>` values within a stage to give the user more
information about what is going on.


## Examples to Look at in the MariaDB Source:


* `<code>client/mysql.cc</code>` for an example of how to use reporting.
* `<code>libmysql/client.c:cli_safe_read()</code>` to see how progress packets are handled
 in client
* `<code>sql/protocol.cc::net_send_progress_packet()</code>` for how progress packets are
 handled in server.


## Format of Progress Packets


The progress packet is sent as an error packet with error number `<code>65535</code>`.


It contains the following data (in addition to the error header):



| Option | Number of bytes | Other info |
| --- | --- | --- |
| Option | Number of bytes | Other info |
| 1 | 1 | Number of strings. For future |
| Stage | 1 | Stage from 1 - Max_stage |
| Max_stage | 1 | Max number of stages |
| Progress | 3 | Progress in % * 1000 |
| Status_length | 1-2 | Packet length of string in net_field_length() format |
| Status | Status_length | Status / Stage name |



## See Also


* [What is MariaDB 5.3](../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md)

