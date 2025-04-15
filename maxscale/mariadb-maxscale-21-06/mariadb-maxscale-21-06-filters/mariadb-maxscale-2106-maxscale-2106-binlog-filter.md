
# MaxScale 21.06 Binlog Filter

# Binlog Filter


This filter was introduced in MariaDB MaxScale 2.3.0.




* [Binlog Filter](#binlog-filter)

  * [Overview](#overview)
  * [Configuration](#configuration)

    * [match](#match)
    * [exclude](#exclude)
    * [rewrite_src](#rewrite_src)
    * [rewrite_dest](#rewrite_dest)
  * [Example Configuration](#example-configuration)




## Overview


The `<code>binlogfilter</code>` can be combined with a `<code>binlogrouter</code>` service to selectively
replicate the binary log events to slave servers.


The filter uses two settings, *match* and *exclude*, to determine which events
are replicated. If a binlog event does not match or is excluded, the event is
replaced with an empty data event. The empty event is always 35 bytes which
translates to a space reduction in most cases.


When statement-based replication is used, any query events that are filtered out
are replaced with a SQL comment. This causes the query event to do nothing and
thus the event will not modify the contents of the database. The GTID position
of the replicating database will still advance which means that downstream
servers replicating from it keep functioning correctly.


The filter works with both row based and statement based replication but we
recommend using row based replication with the binlogfilter. This guarantees
that there are no ambiguities in the event filtering.


## Configuration


### `<code>match</code>`


* Type: [regex](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


Include queries that match the regex. See next entry, `<code>exclude</code>`, for more information.


### `<code>exclude</code>`


* Type: [regex](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


Exclude queries that match the regex.


If neither `<code>match</code>` nor `<code>exclude</code>` are defined, the filter does nothing and all events
are replicated. This filter does not accept regular expression options as a separate
setting, such settings must be defined in the patterns themselves. See the
[PCRE2 api documentation](https://www.pcre.org/current/doc/html/pcre2api.html#SEC20) for
more information.


The two settings are matched against the database and table name concatenated
with a period. For example, the string the patterns are matched against for the
database `<code>test</code>` and table `<code>t1</code>` is `<code>test.t1</code>`.


For statement based replication, the pattern is matched against all the tables
in the statements. If any of the tables matches the *match* pattern, the event
is replicated. If any of the tables matches the *exclude* pattern, the event is
not replicated.


### `<code>rewrite_src</code>`


* Type: [regex](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


See the next entry, `<code>rewrite_dest</code>`, for more information.


### `<code>rewrite_dest</code>`


* Type: [regex](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: None


`<code>rewrite_src</code>` and `<code>rewrite_dest</code>` control the statement rewriting of the binlogfilter.
The `<code>rewrite_src</code>` setting is a PCRE2 regular expression that is matched against
the default database and the SQL of statement based replication events (query
events). `<code>rewrite_dest</code>` is the replacement string which supports the normal
PCRE2 backreferences (e.g the first capture group is `<code>$1</code>`, the second is `<code>$2</code>`,
etc.).


Both `<code>rewrite_src</code>` and `<code>rewrite_dest</code>` must be defined to enable statement rewriting.


When statement rewriting is enabled
[GTID-based replication](../../../server/server-usage/replication-cluster-multi-master/standard-replication/gtid.md)
must be used. The filter will disallow replication for all slaves that attempt
to replicate with traditional file-and-position based replication.


The replacement is done both on the default database as well as the SQL
statement in the query event. This means that great care must be taken when
defining the rewriting rules. To prevent accidental modification of the SQL into
a form that is no longer valid, use database and table names that never occur in
the inserted data and is never used as a constant value.


## Example Configuration


With the following configuration, only events belonging to database `<code>customers</code>`
are replicated. In addition to this, events for the table `<code>orders</code>` are excluded
and thus are not replicated.



```
[BinlogFilter]
type=filter
module=binlogfilter
match=/customers[.]/
exclude=/[.]orders/

[BinlogServer]
type=service
router=binlogrouter
server_id=33
filters=BinlogFilter

[BinlogListener]
type=listener
service=BinlogServer
port=4000
```



For more information about the binlogrouter and how to use it, refer to the
[binlogrouter documentation](../mariadb-maxscale-21-06-routers/mariadb-maxscale-2106-maxscale-2106-binlogrouter-24.md).
