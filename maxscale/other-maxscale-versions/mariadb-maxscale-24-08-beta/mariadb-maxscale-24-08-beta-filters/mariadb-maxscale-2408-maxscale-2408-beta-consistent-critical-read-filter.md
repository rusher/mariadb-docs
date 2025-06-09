
# MaxScale 24.08 Beta Consistent Critical Read Filter

# Consistent Critical Read Filter


This filter was introduced in MariaDB MaxScale 2.1.




* [Consistent Critical Read Filter](#consistent-critical-read-filter)

  * [Overview](#overview)

    * [Controlling the Filter with SQL Comments](#controlling-the-filter-with-sql-comments)
  * [Filter Parameters](#filter-parameters)

    * [time](#time)
    * [count](#count)
    * [match, ignore and options](#match-ignore-and-options)
    * [global](#global)
  * [Example Configuration](#example-configuration)




## Overview


The Consistent Critical Read (CCR) filter allows consistent critical reads to be
done through MaxScale while still allowing scaleout of non-critical reads.


When the filter detects a statement that would modify the database, it attaches
a routing hint to all following statements done by that connection. This routing
hint guides the routing module to route the statement to the primary server where
data is guaranteed to be in an up-to-date state. Writes from one session do not,
by default, propagate to other sessions.


*Note:* This filter does not work with prepared statements. Only text protocol
 queries are handled by this filter.


### Controlling the Filter with SQL Comments


The triggering of the filter can be limited further by adding MaxScale supported
comments to queries and/or by using regular expressions. The query comments take
precedence: if a comment is found it is obeyed even if a regular expression
parameter might give a different result. Even a comment cannot cause a
SELECT-query to trigger the filter. Such a comment is considered an error and
ignored.


The comments must follow the [MaxScale hint syntax](../mariadb-maxscale-24-08-beta-reference/mariadb-maxscale-2408-maxscale-2408-beta-hint-syntax.md)
and the *HintFilter* needs to be in the filter chain before the CCR-filter. If a
query has a MaxScale supported comment line which defines the parameter `ccr`,
that comment is caught by the CCR-filter. Parameter values `match` and `ignore`
are supported, causing the filter to trigger (`match`) or not trigger (`ignore`)
on receiving the write query. For example, the query



```
INSERT INTO departments VALUES ('d1234', 'NewDepartment'); -- maxscale ccr=ignore
```



would normally cause the filter to trigger, but does not because of the
comment. The `match`-comment typically has no effect, since write queries by
default trigger the filter anyway. It can be used to override an ignore-type
regular expression that would otherwise prevent triggering.


## Filter Parameters


The CCR filter has no mandatory parameters.


### `time`


The time window during which queries are routed to the primary. The duration
can be specified as documented
[here](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
but the value will always be rounded to the nearest second.
If no explicit unit has been specified, the value is interpreted as seconds
in MaxScale 2.4. In subsequent versions a value without a unit may be rejected.
The default value for this parameter is 60 seconds.


When a data modifying SQL statement is processed, a timer is set to the value of
*time*. Once the timer has elapsed, all statements are routed normally. If a new
data modifying SQL statement is processed within the time window, the timer is
reset to the value of *time*.


Enabling this parameter in combination with the *count* parameter causes both
the time window and number of queries to be inspected. If either of the two
conditions are met, the query is re-routed to the primary.


### `count`


The number of SQL statements to route to primary after detecting a data modifying
SQL statement. This feature is disabled by default.


After processing a data modifying SQL statement, a counter is set to the value
of *count* and all statements are routed to the primary. Each executed statement
after a data modifying SQL statement cause the counter to be decremented. Once
the counter reaches zero, the statements are routed normally. If a new data
modifying SQL statement is processed, the counter is reset to the value of
*count*.


### `match`, `ignore` and `options`


These [regular expression settings](../mariadb-maxscale-24-08-beta-getting-started/mariadb-maxscale-2408-maxscale-2408-beta-mariadb-maxscale-configuration-guide.md)
control which statements trigger statement re-routing. Only non-SELECT statements are
inspected. For CCRFilter, the *exclude*-parameter is instead named *ignore*, yet works
similarly.



```
match=.*INSERT.*
ignore=.*UPDATE.*
options=case,extended
```



### `global`


`global` is a boolean parameter that when enabled causes writes from one
connection to propagate to all other connections. This can be used to work
around cases where one connection writes data and another reads it, expecting
the write done by the other connection to be visible.


This parameter only works with the `time` parameter. The use of `global` and
`count` at the same time is not allowed and will be treated as an error.


## Example Configuration


Here is a minimal filter configuration for the CCRFilter which should solve most
problems with critical reads after writes.



```
[CCRFilter]
type=filter
module=ccrfilter
time=5
```



With this configuration, whenever a connection does a write, all subsequent
reads done by that connection will be forced to the primary for 5 seconds.


This prevents read scaling until the modifications have been replicated to the
replicas. For best performance, the value of *time* should be slightly greater
than the actual replication lag between the primary and its replicas. If the number
of critical read statements is known, the *count* parameter could be used to
control the number reads that are sent to the primary.


CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
