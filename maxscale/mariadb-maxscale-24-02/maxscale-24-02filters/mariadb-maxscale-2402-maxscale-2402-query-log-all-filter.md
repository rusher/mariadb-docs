
# MaxScale 24.02 Query Log All Filter

# Query Log All Filter




* [Query Log All Filter](#query-log-all-filter)

  * [Overview](#overview)
  * [Configuration](#configuration)
  * [Log Rotation](#log-rotation)
  * [Filter Parameters](#filter-parameters)

    * [filebase](#filebase)
    * [match](#match)
    * [exclude](#exclude)
    * [options](#options)
    * [user](#user)
    * [source](#source)
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


* Type: string
* Mandatory: Yes
* Dynamic: No


The basename of the output file created for each session. A session index is
added to the filename for each written session file. For unified log files,
*.unified* is appended.



```
filebase=/tmp/SqlQueryLog
```



### `<code>match</code>`


* Type: [regex](../maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


Include queries that match the regex.


### `<code>exclude</code>`


* Type: [regex](../maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


Exclude queries that match the regex.


### `<code>options</code>`


* Type: [enum_mask](../maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>case</code>`, `<code>ignorecase</code>`, `<code>extended</code>`
* Default: `<code>case</code>`


The `<code>extended</code>` option enables PCRE2 extended regular expressions.


### `<code>user</code>`


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


Limit logging to sessions with this user.


### `<code>source</code>`


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `<code>""</code>`


Limit logging to sessions with this client source address.


### `<code>user_match</code>`


* Type: [regex](../maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes


Only log queries from users that match this pattern. If the `<code>user</code>` parameter is
used, the value of `<code>user_match</code>` is ignored.


Here is an example pattern that matches the users `<code>alice</code>` and `<code>bob</code>`:



```
user_match=/(^alice$)|(^bob$)/
```



### `<code>user_exclude</code>`


* Type: [regex](../maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes


Exclude all queries from users that match this pattern. If the `<code>user</code>` parameter
is used, the value of `<code>user_exclude</code>` is ignored.


Here is an example pattern that excludes the users `<code>alice</code>` and `<code>bob</code>`:



```
user_exclude=/(^alice$)|(^bob$)/
```



### `<code>source_match</code>`


* Type: [regex](../maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md)
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


* Type: [regex](../maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md)
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


* Type: [enum_mask](../maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>session</code>`, `<code>unified</code>`, `<code>stdout</code>`
* Default: `<code>session</code>`


The type of log file to use.


| Value | Description |
| --- | --- |
| Value | Description |
| session | Write to session-specific files |
| unified | Use one file for all sessions |
| stdout | Same as unified, but to stdout |


### `<code>log_data</code>`


* Type: [enum_mask](../maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>service</code>`, `<code>session</code>`, `<code>date</code>`, `<code>user</code>`, `<code>reply_time</code>`, `<code>total_reply_time</code>`, `<code>query</code>`, `<code>default_db</code>`, `<code>num_rows</code>`, `<code>reply_size</code>`, `<code>transaction</code>`, `<code>transaction_time</code>`, `<code>num_warnings</code>`, `<code>error_msg</code>`
* Default: `<code>date, user, query</code>`


Type of data to log in the log files.


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


The durations *reply_time* and *total_reply_time* are by default in milliseconds,
but can be specified to another unit using *duration_unit*.


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


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `<code>milliseconds</code>`


The unit for logging a duration. The unit can be `<code>milliseconds</code>` or `<code>microseconds</code>`.
The abbreviations `<code>ms</code>` for milliseconds and `<code>us</code>` for microseconds are also valid.
This option is available as of MaxScale version 6.2.


### `<code>use_canonical_form</code>`


* Type: [bool](../maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


When this option is true the canonical form of the query is logged. In the
canonical form all user defined constants are replaced with question marks.
This option is available as of MaxScale version 6.2.


### `<code>flush</code>`


* Type: [bool](../maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>false</code>`


Flush log files after every write.


### `<code>append</code>`


* Type: [bool](../maxscale-24-02getting-started/mariadb-maxscale-2402-maxscale-2402-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>true</code>`


### `<code>separator</code>`


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `<code>","</code>`


Defines the separator string between elements of
log entries. The value should be enclosed in quotes.


### `<code>newline_replacement</code>`


* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `<code>" "</code>`


Default value is `<code>" "</code>` (one space). SQL-queries may include line breaks, which, if
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

