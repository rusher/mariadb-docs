
# MaxScale 24.08 Beta Query Log All Filter

# Query Log All Filter




* [Query Log All Filter](#query-log-all-filter)

  * [Overview](#overview)
  * [Configuration](#configuration)
  * [Log Rotation](#log-rotation)
  * [Filter Parameters](#filter-parameters)

    * [filebase](#filebase)
    * [match, exclude and options](#match-exclude-and-options)
    * [user and source](#user-and-source)
    * [user_match](#user_match)
    * [user_exclude](#user_exclude)
    * [source_match](#source_match)
    * [source_exclude](#source_exclude)
    * [log_type](#log_type)
    * [log_data](#log_data)
    * [duration_unit](#duration_unit)
    * [use_canonical_form](#use_canonical_form)
    * [flush](#flush)
    * [append](#append)
    * [separator](#separator)
    * [newline_replacement](#newline_replacement)
  * [Limitations](#limitations)
  * [Examples](#examples)

    * [Example 1 - Query without primary key](#example-1-query-without-primary-key)




## Overview


The Query Log All (QLA) filter logs query content. Logs are written to a file in
CSV format. Log elements are configurable and include the time submitted and the
SQL statement text, among others.


## Configuration


A minimal configuration is below.



```
[MyLogFilter]
type=filter
module=qlafilter
filebase=/tmp/SqlQueryLog

[MyService]
type=service
router=readconnroute
servers=server1
user=myuser
password=mypasswd
filters=MyLogFilter
```



## Log Rotation


The `<code>qlafilter</code>` logs can be rotated by executing the `<code>maxctrl rotate logs</code>`
command. This will cause the log files to be reopened when the next message is
written to the file. This applies to both unified and session type logging.


## Filter Parameters


The QLA filter has one mandatory parameter, `<code>filebase</code>`, and a number of optional
parameters. These were introduced in the 1.0 release of MariaDB MaxScale.


### `<code>filebase</code>`


The basename of the output file created for each session. A session index is
added to the filename for each written session file. For unified log files,
*.unified* is appended. This is a mandatory parameter.



```
filebase=/tmp/SqlQueryLog
```



### `<code>match</code>`, `<code>exclude</code>` and `<code>options</code>`


These
[regular expression settings](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
limit which queries are logged.



```
match=select.*from.*customer.*where
exclude=^insert
options=case,extended
```



### `<code>user</code>` and `<code>source</code>`


These optional parameters limit logging on a session level. If `<code>user</code>` is
defined, only the sessions with a matching client username are logged. If
`<code>source</code>` is defined, only sessions with a matching client source address are
logged.



```
user=john
source=127.0.0.1
```



### `<code>user_match</code>`


* Type: [regex](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes


Only log queries from users that match this pattern. If the `<code>user</code>` parameter is
used, the value of `<code>user_match</code>` is ignored.


Here is an example pattern that matches the users `<code>alice</code>` and `<code>bob</code>`:



```
user_match=/(^alice$)|(^bob$)/
```



### `<code>user_exclude</code>`


* Type: [regex](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes


Exclude all queries from users that match this pattern. If the `<code>user</code>` parameter
is used, the value of `<code>user_exclude</code>` is ignored.


Here is an example pattern that excludes the users `<code>alice</code>` and `<code>bob</code>`:



```
user_exclude=/(^alice$)|(^bob$)/
```



### `<code>source_match</code>`


* Type: [regex](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes


Only log queries from hosts that match this pattern. If the `<code>source</code>` parameter
is used, the value of `<code>source_match</code>` is ignored.


Here is an example pattern that matches the loopback interface as well as the
address `<code>192.168.0.109</code>`:



```
source_match=/(^127[.]0[.]0[.]1)|(^192[.]168[.]0[.]109)/
```



### `<code>source_exclude</code>`


* Type: [regex](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes


Exclude all queries from hosts that match this pattern. If the `<code>source</code>`
parameter is used, the value of `<code>source_exclude</code>` is ignored.


Here is an example pattern that excludes the loopback interface as well as the
address `<code>192.168.0.109</code>`:



```
source_exclude=/(^127[.]0[.]0[.]1)|(^192[.]168[.]0[.]109)/
```



### `<code>log_type</code>`


The type of log file to use. The default value is *session*.


| Value | Description |
| --- | --- |
| Value | Description |
| session | Write to session-specific files |
| unified | Use one file for all sessions |
| stdout | Same as unified, but to stdout |



```
log_type=session
```



The log types can be combined, e.g. setting `<code>log_type=session,stdout</code>`
will write both session-specific files, and all sessions to stdout.


### `<code>log_data</code>`


Type of data to log in the log files. The parameter value is a comma separated
list of the following elements. By default the *date*, *user* and *query*
options are enabled.


| Value | Description |
| --- | --- |
| Value | Description |
| service | Service name |
| session | Unique session id (ignored for session files) |
| date | Timestamp |
| user | User and hostname of client |
| reply_time | Duration from client query to first server reply |
| total_reply_time | Duration from client query to last server reply (v6.2) |
| query | The SQL of the query if it contains it |
| default_db | The default (current) database |
| num_rows | Number of rows in the result set (v6.2) |
| reply_size | Number of bytes received from the server (v6.2) |
| transaction | BEGIN, COMMIT and ROLLBACK (v6.2) |
| transaction_time | The duration of a transaction (v6.2) |
| num_warnings | Number of warnings in the server reply (v6.2) |
| error_msg | Error message from the server (if any) (v6.2) |
| server | The server where the query was routed (if any) (v22.08) |
| command | The protocol command that was executed (v24.02) |



```
log_data=date, user, query, total_reply_time
```



The durations *reply_time* and *total_reply_time* are by default in milliseconds,
but can be specified to be in microseconds using *duration_unit*.


The log entry is written when the last reply from the server is received.
Prior to version 6.2 the entry was written when the query was received from
the client, or if *reply_time* was specified, on first reply from the server.


**NOTE** The *error_msg* is the raw message from the server. Even if *use_canonical_form*
is set the error message may contain user defined constants. For example:



```
MariaDB [test]> select secret from T where x password="clear text pwd";
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual
that corresponds to your MariaDB server version for the right syntax to
use near 'password="clear text pwd"' at line 1
```



Starting with MaxScale 24.02, the `<code>query</code>` parameter now correctly logs
the execution of binary protocol commands as SQL
([MXS-4959](https://jira.mariadb.org/browse/MXS-4959)). The execution of
batched statements (COM_STMT_BULK_LOAD) used by some connectors is not
logged.


### `<code>duration_unit</code>`


The unit for logging a duration. The unit can be `<code>milliseconds</code>` or `<code>microseconds</code>`.
The abbreviations `<code>ms</code>` for milliseconds and `<code>us</code>` for microseconds are also valid.
The default is `<code>milliseconds</code>`.
This option is available as of MaxScale version 6.2.



```
duration_unit=microseconds
```



### `<code>use_canonical_form</code>`


When this option is true the canonical form of the query is logged. In the
canonical form all user defined constants are replaced with question marks.
The default is false, i.e. log the sql as is.
This option is available as of MaxScale version 6.2.



```
use_canonical_form=true
```



### `<code>flush</code>`


Flush log files after every write. The default is false.



```
flush=true
```



### `<code>append</code>`


Append new entries to log files instead of overwriting them. The default is
true.
**NOTE**: the default was changed from false to true, as of the following
versions: 2.4.18, 2.5.16 and 6.2.



```
append=true
```



### `<code>separator</code>`


Default value is "," (a comma). Defines the separator string between elements of
a log entry. The value should be enclosed in quotes.



```
separator=" | "
```



### `<code>newline_replacement</code>`


Default value is " " (one space). SQL-queries may include line breaks, which, if
printed directly to the log, may break automatic parsing. This parameter defines
what should be written in the place of a newline sequence (\r, \n or \r\n). If
this is set as the empty string, then newlines are not replaced and printed as
is to the output. The value should be enclosed in quotes.



```
newline_replacement=" NL "
```



## Limitations


* Trailing parts of SQL queries that are larger than 16MiB are not
 logged. This means that the log output might contain truncated SQL.
* Batched execution using COM_STMT_BULK_EXECUTE is not converted into
 their textual form. This is done due to the large volumes of data that
 are usually involved with batched execution.


## Examples


### Example 1 - Query without primary key


Imagine you have observed an issue with a particular table and you want to
determine if there are queries that are accessing that table but not using the
primary key of the table. Let's assume the table name is PRODUCTS and the
primary key is called PRODUCT_ID. Add a filter with the following definition:



```
[ProductsSelectLogger]
type=filter
module=qlafilter
match=SELECT.*from.*PRODUCTS .*
exclude=WHERE.*PRODUCT_ID.*
filebase=/var/logs/qla/SelectProducts

[Product-Service]
type=service
router=readconnroute
servers=server1
user=myuser
password=mypasswd
filters=ProductsSelectLogger
```



The result of using this filter with the service used by the application would
be a log file of all select queries querying PRODUCTS without using the
PRODUCT_ID primary key in the predicates of the query. Executing `<code>SELECT * FROM
PRODUCTS</code>` would log the following into `<code>/var/logs/qla/SelectProducts</code>`:



```
07:12:56.324 7/01/2016, SELECT * FROM PRODUCTS
```

