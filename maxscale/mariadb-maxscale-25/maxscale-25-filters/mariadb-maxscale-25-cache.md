
# Cache

# Cache


This filter was introduced in MariaDB MaxScale 2.1.




* [Cache](#cache)

  * [Overview](#overview)
  * [Limitations](#limitations)

    * [Prepared Statements](#prepared-statements)
    * [Multi-statements](#multi-statements)
    * [Security](#security)
  * [Invalidation](#invalidation)

    * [Best Efforts](#best-efforts)
  * [Configuration](#configuration)

    * [Filter Parameters](#filter-parameters)

      * [storage](#storage)
      * [storage_options](#storage_options)
      * [hard_ttl](#hard_ttl)
      * [soft_ttl](#soft_ttl)
      * [max_resultset_rows](#max_resultset_rows)
      * [max_resultset_size](#max_resultset_size)
      * [max_count](#max_count)
      * [max_size](#max_size)
      * [rules](#rules)
      * [cached_data](#cached_data)
      * [selects](#selects)
      * [cache_in_transactions](#cache_in_transactions)
      * [debug](#debug)
      * [enabled](#enabled)
      * [invalidate](#invalidate)
      * [clear_cache_on_parse_errors](#clear_cache_on_parse_errors)
      * [users](#users)
      * [timeout](#timeout)
    * [Runtime Configuration](#runtime-configuration)

      * [@maxscale.cache.populate](#maxscalecachepopulate)
      * [@maxscale.cache.use](#maxscalecacheuse)
      * [@maxscale.cache.soft_ttl](#maxscalecachesoft_ttl)
      * [@maxscale.cache.hard_ttl](#maxscalecachehard_ttl)
      * [Client Driven Caching](#client-driven-caching)
  * [Threads, Users and Invalidation](#threads-users-and-invalidation)

    * [Invalidation](#invalidation_1)

      * [cached_data=thread_specific](#cached_datathread_specific)
      * [cache_data=shared](#cache_datashared)
  * [Rules](#rules_1)

    * [When to Store](#when-to-store)

      * [Qualified Names](#qualified-names)
      * [Implication of the default database](#implication-of-the-default-database)
      * [Regexp Matching](#regexp-matching)
      * [Examples](#examples)
    * [When to Use](#when-to-use)

      * [Examples](#examples_1)
  * [Security](#security_1)
  * [Storage](#storage_1)

    * [storage_inmemory](#storage_inmemory)
    * [storage_memcached](#storage_memcached)

      * [Limitations](#limitations_1)
      * [Security](#security_2)
    * [storage_redis](#storage_redis)

      * [Limitations](#limitations_2)
      * [Invalidation](#invalidation_2)
      * [Security](#security_3)
  * [Example](#example)

    * [Configuration](#configuration_1)
    * [cache_rules.json](#cache_rulesjson)
  * [Performance](#performance)

    * [Summary](#summary)




## Overview


From MaxScale version 2.2.11 onwards, the cache filter is no longer
considered experimental. The following changes to the default behaviour
have also been made:


* The default value of `<code>cached_data</code>` is now `<code>thread_specific</code>` (used to be
 `<code>shared</code>`).
* The default value of `<code>selects</code>` is now `<code>assume_cacheable</code>` (used to be
 `<code>verify_cacheable</code>`).


The cache filter is a simple cache that is capable of caching the result of
SELECTs, so that subsequent identical SELECTs are served directly by MaxScale,
without the queries being routed to any server.


By *default* the cache will be used and populated in the following circumstances:


* There is no explicit transaction active, that is, autocommit is used,
* there is an explicitly read-only transaction (that is,`<code>START TRANSACTION
 READ ONLY</code>`) active, or
* there is a transaction active and no statement that modifies the database
 has been performed.


In practice, the last bullet point basically means that if a transaction has
been started with `<code>BEGIN</code>`, `<code>START TRANSACTION</code>` or `<code>START TRANSACTION READ
WRITE</code>`, then the cache will be used and populated until the first `<code>UPDATE</code>`,
`<code>INSERT</code>` or `<code>DELETE</code>` statement is encountered.


That is, in default mode the cache effectively causes the system to behave
as if the *isolation level* would be `<code>READ COMMITTED</code>`, irrespective of what
the isolation level of the backends actually is.


The default behaviour can be altered using the configuration parameter
[cache_in_transactions](#cache_in_transactions).


By default it is assumed that all `<code>SELECT</code>` statements are cacheable, which
means that also statements like `<code>SELECT LOCALTIME</code>` are cached. Please check
[selects](#selects) for how to change the default behaviour.


## Limitations


All of these limitations may be addressed in forthcoming releases.


### Prepared Statements


Resultsets of prepared statements are **not** cached.


### Multi-statements


Multi-statements are always sent to the backend and their result is
**not** cached.


### Security


The cache is **not** aware of grants.


The implication is that unless the cache has been explicitly configured
who the caching should apply to, the presence of the cache may provide
a user with access to data he should not have access to.


Please read the section [Security](#security-1) for more detailed information.


However, from 2.5 onwards it is possible to configure the cache to cache
the data of each user separately, which effectively means that there can
be no unintended sharing. Please see [users](#users) for how to change
the default behaviour.


## Invalidation


Since MaxScale 2.5, the cache is capable of invalidating entries in the
cache when a modification (UPDATE, INSERT or DELETE) that may affect those
entries is made.


The cache invalidation works on the table-level, that is, a modification
made to a particular table will cause all cache entries that refer to that
table to be invalidated, irrespective of whether the modification actually
has an impact on the cache entries or not. For instance, suppose the result
of the following SELECT has been cached



```
SELECT * FROM t WHERE a=1;
```



An insert like



```
INSERT INTO t SET a=42;
```



will cause the cache entry containing the result of that SELECT to be
invalidated even if the INSERT actually does not affect it. Please see
[invalidate](#invalidate) for how to enable the invalidation.


When invalidation has been enabled MaxScale must be able to completely
parse a SELECT statement for its results to be stored in the cache. The
reason is that in order to be able to invalidate cache entries, MaxScale
must know what tables a SELECT statement depends upon. Consequently, if
(and only if) invalidation has been enabled and MaxScale fails to parse a
statement, the result of that particular statement will not be cached.


When invalidation has been enabled, MaxScale will also parse all UPDATE,
INSERT and DELETE statements, in order to find out what tables are
modified. If that parsing fails, MaxScale will *by default* clear the
entire cache. The reason is that unless MaxScale can completely parse
the statement it cannot know what tables are modified and hence not what
cache entries should be invalidated. Consequently, to prevent stale data
from being returned, the entire cache is cleared. The default behaviour
can be changed using the configuration parameter
[clear_cache_on_parse_errors](#clear_cache_on_parse_errors).


Note that what threading approach is used has a big impact on the
invalidation. Please see
[Threads, Users and Invalidation](#threads-users-and-invalidation)
for how the threading approach affects the invalidation.


Note also that since the invalidation may not, depending on how the
cache has been configured, be visible to all sessions of all users, it
is still important to configure a reasonable [soft](#soft_ttl) and
[hard](#hard_ttl) TTL.


### Best Efforts


The invalidation offered by the MaxScale cache can be said to be of
*best efforts* quality. The reason is that in order to ensure that the
cache in all circumstances reflects the state in the actual database,
would require that the operations involving the cache and the MariaDB
server are synchronized, which would cause an unacceptable overhead.


What *best efforts* means in this context is best illustrated using an example.


Suppose a client executes the statement `<code>SELECT * FROM tbl</code>` and that the result
is cached. Next time that or any other client executes the same statement, the
result is returned from the cache and the MariaDB server will not be accessed
at all.


If a client now executes the statement `<code>INSERT INTO tbl VALUES (...)</code>`, the
cached value for the `<code>SELECT</code>` statement above and all other statements that are
dependent upon `<code>tbl</code>` will be invalidated. That is, the next time someone executes
the statement `<code>SELECT * FROM tbl</code>` the result will again be fetched from the
MariaDB server and stored to the cache.


However, suppose some client executes the statement `<code>SELECT COUNT(*) FROM tbl</code>`
at the same time someone else executes the `<code>INSERT ...</code>` statement. A possible
chain of events is as follows:



```
Timeline 1                 Timeline 2

Clients execute       INSERT ...                 SELECT COUNT(*) FROM tbl
MaxScale -> DB                                   SELECT COUNT(*) FROM tbl
MaxScale -> DB        INSERT ...
```



That is, the `<code>SELECT</code>` is performed in the database server *before* the
`<code>INSERT</code>`. However, since the timelines are proceeding independently of
each other, the events may be re-ordered as far as the cache is concerned.



```
MaxScale -> Cache     Delete invalidated values
MaxScale -> Cache                                Store result and invalidation key
```



That is, the cached value for `<code>SELECT COUNT(*) FROM tbl</code>` will reflect the
situation *before* the insert and will thus not be correct.


The stale result will be returned until the value has reached its *time-to-live*
or its invalidation is caused by some update operation.


## Configuration


The cache is simple to add to any existing service. However, some experimentation
may be required in order to find the configuration settings that provide
the maximum benefit.



```
[Cache]
type=filter
module=cache
hard_ttl=30
soft_ttl=20
rules=...
...

[Cached-Routing-Service]
type=service
...
filters=Cache
```



Each configured cache filter uses a storage of its own. That is, if there
are two services, each configured with a specific cache filter, then,
even if queries target the very same servers the cached data will not
be shared.


Two services can use the same cache filter, but then either the services
should use the very same servers *or* a completely different set of servers,
where the used table names are different. Otherwise there can be unintended
sharing.


### Filter Parameters


The cache filter has no mandatory parameters but a range of optional ones.
Note that it is advisable to specify `<code>max_size</code>` to prevent the cache from
using up all memory there is, in case there is very little overlap among the
queries.


#### `<code>storage</code>`


The name of the module that provides the storage for the cache. That
module will be loaded and provided with the value of `<code>storage_options</code>` as
argument. For instance:



```
storage=storage_inmemory
```



The default is `<code>storage_inmemory</code>`.


See [Storage](#storage-1) for what storage modules are available.


#### `<code>storage_options</code>`


A string that is provided verbatim to the storage module specified in `<code>storage</code>`,
when the module is loaded. Note that the needed arguments and their format depend
upon the specific module.


#### `<code>hard_ttl</code>`


*Hard time to live*; the maximum amount of time the cached
result is used before it is discarded and the result is fetched from the
backend (and cached). See also `<code>soft_ttl</code>` below.



```
hard_ttl=60s
```



The default value is `<code>0s</code>`, which means no limit.


The duration can be specified as explained
[here](../maxscale-25-getting-started/mariadb-maxscale-25-mariadb-maxscale-configuration-guide.md#durations).
If no explicit unit has been specified, the value is interpreted as seconds
in MaxScale 2.4. In subsequent versions a value without a unit may be rejected.


#### `<code>soft_ttl</code>`


*Soft time to live*; the amount of time - in seconds - the cached result is
used before it is refreshed from the server. When `<code>soft_ttl</code>` has passed, the
result will be refreshed when the *first* client requests the value.


However, as long as `<code>hard_ttl</code>` has not passed, *all* other clients requesting
the same value will use the result from the cache while it is being fetched
from the backend. That is, as long as `<code>soft_ttl</code>` but not `<code>hard_ttl</code>` has passed,
even if several clients request the same value at the same time, there will be
just one request to the backend.



```
soft_ttl=60s
```



The default value is `<code>0</code>`, which means no limit. If the value of `<code>soft_ttl</code>` is
larger than `<code>hard_ttl</code>` it will be adjusted down to the same value.


The duration can be specified as explained
[here](../maxscale-25-getting-started/mariadb-maxscale-25-mariadb-maxscale-configuration-guide.md#durations).
If no explicit unit has been specified, the value is interpreted as seconds
in MaxScale 2.4. In subsequent versions a value without a unit may be rejected.


#### `<code>max_resultset_rows</code>`


Specifies the maximum number of rows a resultset can have in order to be
stored in the cache. A resultset larger than this, will not be stored.



```
max_resultset_rows=1000
```



The default value is `<code>0</code>`, which means no limit.


#### `<code>max_resultset_size</code>`


Specifies the maximum size of a resultset, for it to be stored in the cache.
A resultset larger than this, will not be stored. The size can be specified
as described [here](../maxscale-25-getting-started/mariadb-maxscale-25-mariadb-maxscale-configuration-guide.md#sizes).



```
max_resultset_size=128Ki
```



The default value is `<code>0</code>`, which means no limit.


Note that the value of `<code>max_resultset_size</code>` should not be larger than the
value of `<code>max_size</code>`.


#### `<code>max_count</code>`


The maximum number of items the cache may contain. If the limit has been
reached and a new item should be stored, then an older item will be evicted.


Note that if `<code>cached_data</code>` is `<code>thread_specific</code>` then this limit will be
applied to each cache *separately*. That is, if a thread specific cache
is used, then the total number of cached items is #threads * the value
of `<code>max_count</code>`.



```
max_count=1000
```



The default value is `<code>0</code>`, which means no limit.


#### `<code>max_size</code>`


The maximum size the cache may occupy. If the limit has been reached and a new
item should be stored, then some older item(s) will be evicted to make space.
The size can be specified as described
[here](../maxscale-25-getting-started/mariadb-maxscale-25-mariadb-maxscale-configuration-guide.md#sizes).


Note that if `<code>cached_data</code>` is `<code>thread_specific</code>` then this limit will be
applied to each cache *separately*. That is, if a thread specific cache
is used, then the total size is #threads * the value of `<code>max_size</code>`.



```
max_size=100Mi
```



The default value is `<code>0</code>`, which means no limit.


#### `<code>rules</code>`


Specifies the path of the file where the caching rules are stored. A relative
path is interpreted relative to the *data directory* of MariaDB MaxScale.



```
rules=/path/to/rules-file
```



#### `<code>cached_data</code>`


An enumeration option specifying how data is shared between threads. The
allowed values are:


* `<code>shared</code>`: The cached data is shared between threads. On the one hand
 it implies that there will be synchronization between threads, on
 the other hand that all threads will use data fetched by any thread.
* `<code>thread_specific</code>`: The cached data is specific to a thread. On the
 one hand it implies that no synchronization is needed between threads,
 on the other hand that the very same data may be fetched and stored
 multiple times.



```
cached_data=shared
```



Default is `<code>thread_specific</code>`. See `<code>max_count</code>` and `<code>max_size</code>` what implication
changing this setting to `<code>shared</code>` has.


#### `<code>selects</code>`


An enumeration option specifying what approach the cache should take with
respect to `<code>SELECT</code>` statements. The allowed values are:


* `<code>assume_cacheable</code>`: The cache can assume that all `<code>SELECT</code>` statements,
 without exceptions, are cacheable.
* `<code>verify_cacheable</code>`: The cache can not assume that all `<code>SELECT</code>`
 statements are cacheable, but must verify that.



```
selects=verify_cacheable
```



Default is `<code>assume_cacheable</code>`. In this case, all `<code>SELECT</code>` statements are
assumed to be cacheable and will be parsed *only* if some specific rule
requires that.


If `<code>verify_cacheable</code>` is specified, then all `<code>SELECT</code>` statements will be
parsed and only those that are safe for caching - e.g. do *not* call any
non-cacheable functions or access any non-cacheable variables - will be
subject to caching.


If `<code>verify_cacheable</code>` has been specified, the cache will not be used in
the following circumstances:


* The `<code>SELECT</code>` uses any of the following functions: `<code>BENCHMARK</code>`,
 `<code>CONNECTION_ID</code>`, `<code>CONVERT_TZ</code>`, `<code>CURDATE</code>`, `<code>CURRENT_DATE</code>`, `<code>CURRENT_TIMESTAMP</code>`,
 `<code>CURTIME</code>`, `<code>DATABASE</code>`, `<code>ENCRYPT</code>`, `<code>FOUND_ROWS</code>`, `<code>GET_LOCK</code>`, `<code>IS_FREE_LOCK</code>`,
 `<code>IS_USED_LOCK</code>`, `<code>LAST_INSERT_ID</code>`, `<code>LOAD_FILE</code>`, `<code>LOCALTIME</code>`, `<code>LOCALTIMESTAMP</code>`,
 `<code>MASTER_POS_WAIT</code>`, `<code>NOW</code>`, `<code>RAND</code>`, `<code>RELEASE_LOCK</code>`, `<code>SESSION_USER</code>`, `<code>SLEEP</code>`,
 `<code>SYSDATE</code>`, `<code>SYSTEM_USER</code>`, `<code>UNIX_TIMESTAMP</code>`, `<code>USER</code>`, `<code>UUID</code>`, `<code>UUID_SHORT</code>`.
* The `<code>SELECT</code>` accesses any of the following fields: `<code>CURRENT_DATE</code>`,
 `<code>CURRENT_TIMESTAMP</code>`, `<code>LOCALTIME</code>`, `<code>LOCALTIMESTAMP</code>`
* The `<code>SELECT</code>` uses system or user variables.


Note that parsing all `<code>SELECT</code>` statements carries a *significant* performance
cost. Please read [performance](#performance) for more details.


#### `<code>cache_in_transactions</code>`


An enumeration option specifying how the cache should behave when there
are active transactions:


* `<code>never</code>`: When there is an active transaction, no data will be returned
 from the cache, but all requests will always be sent to the backend.
 The cache will be populated inside explicitly read-only transactions.
 Inside transactions that are not explicitly read-only, the cache will
 be populated until the first non-SELECT statement.
* `<code>read_only_transactions</code>`: The cache will be used and populated inside
 explicitly read-only transactions. Inside transactions that are not
 explicitly read-only, the cache will be populated, but not used
 until the first non-SELECT statement.
* `<code>all_transactions</code>`: The cache will be used and populated inside
 explicitly read-only transactions. Inside transactions that are not
 explicitly read-only, the cache will be used and populated until the
 first non-SELECT statement.



```
cache_in_transactions=never
```



Default is `<code>all_transactions</code>`.


The values `<code>read_only_transactions</code>` and `<code>all_transactions</code>` have roughly the
same effect as changing the isolation level of the backend to `<code>read_committed</code>`.


#### `<code>debug</code>`


An integer value, using which the level of debug logging made by the cache
can be controlled. The value is actually a bitfield with different bits
denoting different logging.


* `<code>0</code>` (`<code>0b00000</code>`) No logging is made.
* `<code>1</code>` (`<code>0b00001</code>`) A matching rule is logged.
* `<code>2</code>` (`<code>0b00010</code>`) A non-matching rule is logged.
* `<code>4</code>` (`<code>0b00100</code>`) A decision to use data from the cache is logged.
* `<code>8</code>` (`<code>0b01000</code>`) A decision not to use data from the cache is logged.
* `<code>16</code>` (`<code>0b10000</code>`) Higher level decisions are logged.


Default is `<code>0</code>`. To log everything, give `<code>debug</code>` a value of `<code>31</code>`.



```
debug=31
```



#### `<code>enabled</code>`


Specifies whether the cache is initially enabled or disabled.



```
enabled=false
```



Default is `<code>true</code>`.


The value affects the initial state of the MaxScale user
variables using which the behaviour of the cache can be modified
at runtime. Please see
[Runtime Configuration](#runtime-configuration)
for details.


#### `<code>invalidate</code>`


An enumeration option specifying how the cache should invalidate
cache entries.


```
* `never`: No invalidation is performed. This is the default.
* `current`: When a modification is made, entries in the cache used by
  the current session are invalidated. Other sessions that use the same
  cache will also be affected, but sessions that use another cache will
  not.
```


The effect of `<code>current</code>` depends upon the value of `<code>cached_data</code>`. If the value
is `<code>shared</code>`, that is, all threads share the same cache, then the effect of an
invalidation is immediately visible to all sessions, as there is just one cache.
However, if the value is `<code>thread_specific</code>`, then an invalidation will affect only
the cache that the session happens to be using.


If it is important and *sufficient* that an application immediately sees a change
that it itself has caused, then a combination of `<code>invalidate=current</code>`
and `<code>cached_data=thread_specific</code>` can be used.


If it is important that an application *immediately* sees all changes, irrespective
of who has caused them, then a combination of `<code>invalidate=current</code>`
and `<code>cached_data=shared</code>` *must* be used.


#### `<code>clear_cache_on_parse_errors</code>`


This boolean option specifies how the cache should behave in case of
parsing errors when invalidation has been enabled.


* `<code>true</code>`: If the cache fails to parse an UPDATE/INSERT/DELETE
 statement then all cached data will be cleared.
* `<code>false</code>`: A failure to parse an UPDATE/INSERT/DELETE statement
 is ignored and no invalidation will take place due that statement.


The default value is `<code>true</code>`.


Changing the value to `<code>false</code>` may mean that stale data is returned from
the cache, if an UPDATE/INSERT/DELETE cannot be parsed and the statement
affects entries in the cache.


#### `<code>users</code>`


An enumeration option specifying how the cache should cache data for
different users.


```
* `mixed`: The data of different users is stored in the same
  cache. This is the default and may cause that a user can
  access data he should not have access to.
* `isolated`: Each user has a unique cache and there can be
  no unintended sharing.
```


Note that if `<code>isolated</code>` has been specified, then each user will
conceptually have a cache of his own, which is populated
independently from each other. That is, if two users make the
same query, then the data will be fetched twice and also stored
twice. So, a `<code>isolated</code>` cache will in general use more memory and
cause more traffic to the backend compared to a `<code>mixed</code>` cache.


#### `<code>timeout</code>`


The *timeout* used when performing operations to distributed storages
such as *redis* or *memcached*.



```
timeout=7000ms
```



The default value is `<code>5000ms</code>`, that is 5 seconds.


The duration can be specified as explained
[here](../maxscale-25-getting-started/mariadb-maxscale-25-mariadb-maxscale-configuration-guide.md#durations).


### Runtime Configuration


#### `<code>@maxscale.cache.populate</code>`


Using the variable `<code>@maxscale.cache.populate</code>` it is possible to specify at
runtime whether the cache should be populated or not. Its initial value is
the value of the configuration parameter `<code>enabled</code>`. That is, by default the
value is `<code>true</code>`.


The purpose of this variable is make it possible for an application to decide
statement by statement whether the cache should be populated.



```
SET @maxscale.cache.populate=true;
SELECT a, b FROM tbl;
SET @maxscale.cache.populate=false;
SELECT a, b FROM tbl;
```



In the example above, the first `<code>SELECT</code>` will always be sent to the
server and the result will be cached, provided the actual cache rules
specifies that it should be. The second `<code>SELECT</code>` may be served from the
cache, depending on the value of `<code>@maxscale.cache.use</code>` (and the cache
rules).


The value of `<code>@maxscale.cache.populate</code>` can be queried



```
SELECT @maxscale.cache.populate;
```



but only *after* it has been explicitly set once.


#### `<code>@maxscale.cache.use</code>`


Using the variable `<code>@maxscale.cache.use</code>` it is possible to specify at
runtime whether the cache should be used or not. Its initial value is
the value of the configuration parameter `<code>enabled</code>`. That is, by default the
value is `<code>true</code>`.


The purpose of this variable is make it possible for an application to decide
statement by statement whether the cache should be used.



```
SET @maxscale.cache.use=true;
SELECT a, b FROM tbl;
SET @maxscale.cache.use=false;
SELECT a, b FROM tbl;
```



The first `<code>SELECT</code>` will be served from the cache, providing the rules
specify that the statement should be cached, the cache indeed contains
the result and the date is not stale (as specified by the *TTL*).


If the data is stale, the `<code>SELECT</code>` will be sent to the server **and**
the cache entry will be updated, irrespective of the value of
`<code>@maxscale.cache.populate</code>`.


If `<code>@maxscale.cache.use</code>` is `<code>true</code>` but the result is not found in the
cache, and the result is subsequently fetched from the server, the
result will **not** be added to the cache, unless
`<code>@maxscale.cache.populate</code>` is also `<code>true</code>`.


The value of `<code>@maxscale.cache.use</code>` can be queried



```
SELECT @maxscale.cache.use;
```



but only after it has explicitly been set once.


#### `<code>@maxscale.cache.soft_ttl</code>`


Using the variable `<code>@maxscale.cache.soft_ttl</code>` it is possible at runtime
to specify *in seconds* what *soft ttl* should be applied. Its initial
value is the value of the configuration parameter `<code>soft_ttl</code>`. That is,
by default the value is 0.


The purpose of this variable is make it possible for an application to decide
statement by statement what *soft ttl* should be applied.



```
set @maxscale.cache.soft_ttl=600;
SELECT a, b FROM unimportant;
set @maxscale.cache.soft_ttl=60;
SELECT c, d FROM important;
```



When data is `<code>SELECT</code>`ed from the unimportant table `<code>unimportant</code>`, the data
will be returned from the cache provided it is no older than 10 minutes,
but when data is `<code>SELECT</code>`ed from the important table `<code>important</code>`, the
data will be returned from the cache provided it is no older than 1 minute.


Note that `<code>@maxscale.cache.hard_ttl</code>` overrules `<code>@maxscale.cache.soft_ttl</code>`
in the sense that if the former is less that the latter, then *soft ttl*
will, when used, be adjusted down to the value of *hard ttl*.


The value of `<code>@maxscale.cache.soft_ttl</code>` can be queried



```
SELECT @maxscale.cache.soft_ttl;
```



but only after it has explicitly been set once.


#### `<code>@maxscale.cache.hard_ttl</code>`


Using the variable `<code>@maxscale.cache.hard_ttl</code>` it is possible at runtime
to specify *in seconds* what *hard ttl* should be applied. Its initial
value is the value of the configuration parameter `<code>hard_ttl</code>`. That is,
by default the value is 0.


The purpose of this variable is make it possible for an application to decide
statement by statement what *hard ttl* should be applied.


Note that as `<code>@maxscale.cache.hard_ttl</code>` overrules `<code>@maxscale.cache.soft_ttl</code>`,
is is important to ensure that the former is at least as large as the latter
and for best overall performance that it is larger.



```
set @maxscale.cache.soft_ttl=600, @maxscale.cache.hard_ttl=610;
SELECT a, b FROM unimportant;
set @maxscale.cache.soft_ttl=60, @maxscale.cache.hard_ttl=65;
SELECT c, d FROM important;
```



The value of `<code>@maxscale.cache.hard_ttl</code>` can be queried



```
SELECT @maxscale.cache.hard_ttl;
```



but only after it has explicitly been set once.


#### Client Driven Caching


With `<code>@maxscale.cache.populate</code>` and `<code>@maxscale.cache.use</code>` is it possible
to make the caching completely client driven.


Provide no `<code>rules</code>` file, which means that *all* `<code>SELECT</code>` statements are
subject to caching and that all users receive data from the cache. Set
the startup mode of the cache to *disabled*.



```
[TheCache]
type=filter
module=cache
enabled=false
```



Now, in order to *mark* statements that should be cached, set
`<code>@maxscale.cache.populate</code>` to `<code>true</code>`, and perform those `<code>SELECT</code>`s.



```
SET @maxscale.cache.populate=true;
SELECT a, b FROM tbl1;
SELECT c, d FROM tbl2;
SELECT e, f FROM tbl3;
SET @maxscale.cache.populate=false;
```



Note that those `<code>SELECT</code>`s must return something in order for the
statement to be *marked* for caching.


After this, the value of `<code>@maxscale.cache.use</code>` will decide whether
or not the cache is considered.



```
SET @maxscale.cache.use=true;
SELECT a, b FROM tbl1;
SET @maxscale.cache.use=false;
```



With `<code>@maxscale.cache.use</code>` being `<code>true</code>`, the cache is considered
and the result returned from there, if not stale. If it is stale,
the result is fetched from the server and the cached entry is updated.


By setting a very long *TTL* it is possible to prevent the cache
from ever considering an entry to be stale and instead manually
cause the cache to be updated when needed.



```
UPDATE tbl1 SET a = ...;
SET @maxscale.cache.populate=true;
SELECT a, b FROM tbl1;
SET @maxscale.cache.populate=false;
```



## Threads, Users and Invalidation


What caching approach is used and how different users are treated
has a significant impact on the behaviour of the cache. In the
following the implication of different combinations is explained.


| cached_data/users | mixed | isolated |
| --- | --- | --- |
| cached_data/users | mixed | isolated |
| thread_specific | No thread contention. Data/work duplicated across threads. May cause unintended sharing. | No thread contention. Data/work duplicated across threads and users. No unintended sharing. Requires the most amount of memory. |
| shared | Thread contention under high load. No duplicated data/work. May cause unintended sharing. Requires the least amount of memory. | Thread contention under high load. Data/work duplicated across users. No unintended sharing. |


### Invalidation


Invalidation takes place only in the current cache, so how *visible*
the invalidation is, depends upon the configuration value of
`<code>cached_data</code>`.


#### `<code>cached_data=thread_specific</code>`


The invalidation is visible only to the sessions that are handled by
the same worker thread where the invalidation occurred. Sessions of the
same or other users that are handled by different worker threads will
not see the new value before the TTL causes the value to be refreshed.


#### `<code>cache_data=shared</code>`


The invalidation is immediately visible to all sessions of all users.


## Rules


The caching rules are expressed as a JSON object or as an array of JSON objects.


There are two decisions to be made regarding the caching; in what circumstances
should data be stored to the cache and in what circumstances should the data in
the cache be used.


Expressed in JSON this looks as follows



```
{
    store: [ ... ],
    use: [ ... ]
}
```



or, in case an array is used, as



```
[
    {
        store: [ ... ],
        use: [ ... ]
    },
    { ... }
]
```



The `<code>store</code>` field specifies in what circumstances data should be stored to
the cache and the `<code>use</code>` field specifies in what circumstances the data in
the cache should be used. In both cases, the value is a JSON array containing
objects.


If an array of rule objects is specified, then, when looking for a rule that
matches, the `<code>store</code>` field of each object are evaluated in sequential order
until a match is found. Then, the `<code>use</code>` field of that object is used when
deciding whether data in the cache should be used.


### When to Store


By default, if no rules file have been provided or if the `<code>store</code>` field is
missing from the object, the results of all queries will be stored to the
cache, subject to `<code>max_resultset_rows</code>` and `<code>max_resultset_size</code>` cache filter
parameters.


By providing a `<code>store</code>` field in the JSON object, the decision whether to
store the result of a particular query to the cache can be controlled in
a more detailed manner. The decision to cache the results of a query can
depend upon


* the database,
* the table,
* the column, or
* the query itself.


Each entry in the `<code>store</code>` array is an object containing three fields,



```
{
    "attribute": <string>,
    "op": <string>
    "value": <string>
}
```



where,


* the attribute can be `<code>database</code>`, `<code>table</code>`, `<code>column</code>` or `<code>query</code>`,
* the op can be `<code>=</code>`, `<code>!=</code>`, `<code>like</code>` or `<code>unlike</code>`, and
* the value a string.


If *op* is `<code>=</code>` or `<code>!=</code>` then *value* is used as a string; if it is `<code>like</code>`
or `<code>unlike</code>`, then *value* is interpreted as a *pcre2* regular expression.
Note though that if *attribute* is `<code>database</code>`, `<code>table</code>` or `<code>column</code>`, then
the string is interpreted as a name, where a dot `<code>.</code>` denotes qualification
or scoping.


The objects in the `<code>store</code>` array are processed in order. If the result
of a comparison is *true*, no further processing will be made and the
result of the query in question will be stored to the cache.


If the result of the comparison is *false*, then the next object is
processed. The process continues until the array is exhausted. If there
is no match, then the result of the query is not stored to the cache.


Note that as the query itself is used as the key, although the following
queries



```
select * from db1.tbl
```



and



```
use db1;
select * from tbl
```



target the same table and produce the same results, they will be cached
separately. The same holds for queries like



```
select * from tbl where a = 2 and b = 3;
```



and



```
select * from tbl where b = 3 and a = 2;
```



as well. Although they conceptually are identical, there will be two
cache entries.


Note that if a column has been specified in a rule, then a statement
will match *irrespective* of where that particular column appears.
For instance, if a rule specifies that the result of statements referring
to the the column *a* should be cached, then the following statement will
match



```
select a from tbl;
```



and so will



```
select b from tbl where a > 5;
```



#### Qualified Names


When using `<code>=</code>` or `<code>!=</code>` in the rule object in conjunction with `<code>database</code>`,
`<code>table</code>` and `<code>column</code>`, the provided string is interpreted as a name, that is,
dot (`<code>.</code>`) denotes qualification or scope.


In practice that means that if *attribute* is `<code>database</code>` then *value* may
not contain a dot, if *attribute* is `<code>table</code>` then *value* may contain one
dot, used for separating the database and table names respectively, and
if *attribute* is `<code>column</code>` then *value* may contain one or two dots, used
for separating table and column names, or database, table and column names.


Note that if a qualified name is used as a *value*, then all parts of the
name must be available for a match. Currently Maria DB MaxScale may not
always be capable of deducing in what table a particular column is. If
that is the case, then a value like `<code>tbl.field</code>` may not necessarily
be a match even if the field is `<code>field</code>` and the table actually is `<code>tbl</code>`.


#### Implication of the default database


If the rules concerns the `<code>database</code>`, then only if the statement refers
to *no* specific database, will the default database be considered.


#### Regexp Matching


The string used for matching the regular expression contains as much
information as there is available. For instance, in a situation like



```
use somedb;
select fld from tbl;
```



the string matched against the regular expression will be `<code>somedb.tbl.fld</code>`.


#### Examples


Cache all queries targeting a particular database.



```
{
    "store": [
        {
            "attribute": "database",
            "op": "=",
            "value": "db1"
        }
    ]
}
```



Cache all queries *not* targeting a particular table



```
{
    "store": [
        {
            "attribute": "table",
            "op": "!=",
            "value": "tbl1"
        }
    ]
}
```



That will exclude queries targeting table *tbl1* irrespective of which
database it is in. To exclude a table in a particular database, specify
the table name using a qualified name.



```
{
    "store": [
        {
            "attribute": "table",
            "op": "!=",
            "value": "db1.tbl1"
        }
    ]
}
```



Cache all queries containing a WHERE clause



```
{
    "store": [
        {
            "attribute": "query",
            "op": "like",
            "value": ".*WHERE.*"
        }
    ]
}
```



Note that that will actually cause all queries that contain WHERE anywhere,
to be cached.


### When to Use


By default, if no rules file have been provided or if the `<code>use</code>` field is
missing from the object, all users may be returned data from the cache.


By providing a `<code>use</code>` field in the JSON object, the decision whether to use
data from the cache can be controlled in a more detailed manner. The decision
to use data from the cache can depend upon


* the user.


Each entry in the `<code>use</code>` array is an object containing three fields,



```
{
    "attribute": <string>,
    "op": <string>
    "value": <string>
}
```



where,


* the attribute can be `<code>user</code>`,
* the op can be `<code>=</code>`, `<code>!=</code>`, `<code>like</code>` or `<code>unlike</code>`, and
* the value a string.


If *op* is `<code>=</code>` or `<code>!=</code>` then *value* is interpreted as a MariaDB account
string, that is, `<code>%</code>` means indicates wildcard, but if *op* is `<code>like</code>` or
`<code>unlike</code>` it is simply assumed *value* is a pcre2 regular expression.


For instance, the following are equivalent:



```
{
    "attribute": "user",
    "op": "=",
    "value": "'bob'@'%'"
}

{
    "attribute": "user",
    "op": "like",
    "value": "bob@.*"
}
```



Note that if *op* is `<code>=</code>` or `<code>!=</code>` then the usual assumptions apply,
that is, a value of `<code>bob</code>` is equivalent with `<code>'bob'@'%'</code>`. If *like*
or *unlike* is used, then no assumptions apply, but the string is
used verbatim as a regular expression.


The objects in the `<code>use</code>` array are processed in order. If the result
of a comparison is *true*, no further processing will be made and the
data in the cache will be used, subject to the value of `<code>ttl</code>`.


If the result of the comparison is *false*, then the next object is
processed. The process continues until the array is exhausted. If there
is no match, then data in the cache will not be used.


Note that `<code>use</code>` is relevant only if the query is subject to caching,
that is, if all queries are cached or if a query matches a particular
rule in the `<code>store</code>` array.


#### Examples


Use data from the cache for all users except `<code>admin</code>` (actually `<code>'admin'@'%'</code>`),
regardless of what host the `<code>admin</code>` user comes from.



```
{
    "use": [
        {
            "attribute": "user",
            "op": "!=",
            "value": "admin"
        }
    ]
}
```



## Security


As the cache is not aware of grants, unless the cache has been explicitly
configured who the caching should apply to, the presence of the cache
may provide a user with access to data he should not have access to.
Note that the following applies *only* if `<code>users=mixed</code>` has been configured.
If `<code>users=isolated</code>` has been configured, then there can never be any
unintended sharing between users.


Suppose there is a table `<code>access</code>` that the user *alice* has access to,
but the user *bob* does not. If *bob* tries to access the table, he will
get an error as reply:



```
MySQL [testdb]> select * from access;
ERROR 1142 (42000): SELECT command denied to user 'bob'@'localhost' for table 'access'
```



If we now setup caching for the table, using the simplest possible rules
file, *bob* will get access to data from the table, provided he executes
a select identical with one *alice* has executed.


For instance, suppose the rules look as follows:



```
{
    "store": [
        {
            "attribute": "table",
            "op": "=",
            "value": "access"
        }
    ]
}
```



If *alice* now queries the table, she will get the result, which also will
be cached:



```
MySQL [testdb]> select * from access;
+------+------+
| a    | b    |
+------+------+
|   47 |   11 |
+------+------+
```



If *bob* now executes the very same query, and the result is still in the
cache, it will be returned to him.



```
MySQL [testdb]> select current_user();
+----------------+
| current_user() |
+----------------+
| bob@127.0.0.1  |
+----------------+
1 row in set (0.00 sec)

MySQL [testdb]> select * from access;
+------+------+
| a    | b    |
+------+------+
|   47 |   11 |
+------+------+
```



That can be prevented, by explicitly declaring in the rules that the caching
should be applied to *alice* only.



```
{
    "store": [
        {
            "attribute": "table",
            "op": "=",
            "value": "access"
        }
    ],
    "use": [
        {
            "attribute": "user",
            "op": "=",
            "value": "'alice'@'%'"
        }
    ]
}
```



With these rules in place, *bob* is again denied access, since queries
targeting the table `<code>access</code>` will in his case not be served from the cache.


## Storage


There are two types of storages that can be used; *local* and *shared*.


The only *local* storage implementation is `<code>storage_inmemory</code>` that simply
stores the cache values in memory. The storage is not persistent and is
destroyed when MaxScale terminates. Since the storage exists in the MaxScale
process, it is very fast and provides almost always a performance benefit.


Currently there are two *shared* storages; `<code>storage_memcached</code>` and
`<code>storage_redis</code>` that are implemented using [memcached](https://memcached.org/)
and [redis](https://redis.io/) respectively.


The shared storages are accessed across the network and consequently it is
*not* self-evident that their use will provide any performance benefit.
Namely, irrespective of whether the data is fetched from the cache or from
the server there will be a network hop and often that network hop is, as far
as the performance goes, what costs the most.


The presence of a shared cache *may* provide a performance benefit
*if the network between MaxScale and the storage server (memcached or
 Redis) is faster than the network between MaxScale and the database
 server,* if the used SELECT statements are heavy (that is, take a significant
 amount of time) to process for the database server, or
* if the presence of the cache reduces the overall load of an
 otherwise overloaded database server.


As a general rule a *shared* storage should not be used without first
assessing its value using a realistic workload.


### `<code>storage_inmemory</code>`


This simple storage module uses the standard memory allocator for storing
the cached data.



```
storage=storage_inmemory
```



This storage module takes no arguments.


### `<code>storage_memcached</code>`


This storage module uses [memcached](https://memcached.org/) for storing the
cached data.


Multiple MaxScale instances can share the same memcached server and items
cached by one MaxScale instance will be used by the other. Note that all
MaxScale instances should have exactly the same configuration, as otherwise
there can be unintended sharing.



```
storage=storage_memcached
```



`<code>storage_memcache</code>` has the following mandatory arguments:


* `<code>server</code>` using which the location of the server is specified as `<code>host[:port]</code>`.
 If no port is provided, the default Memcached port of `<code>11211</code>` is used.


`<code>storage_memcached</code>` has the following optional arguments:


* `<code>max_value_size</code>` using which the maximum size of a cached value is specified.
 By default, the maximum size of a value stored to memcached is 1MB, but that
 configured to be something else. The value of `<code>max_value_size</code>` will be used
 for capping `<code>max_resultset_size</code>`, that is, unless memcached is configured to
 allow larger values that 1M and `<code>max_value_size</code>` has been set accordingly,
 only resultsets up to 1MB in size will be cached. The value can be specified
 as documented [here](https://mariadb.com/kb/Getting-Started/Configuration-Guide/#sizes).


Example:



```
storage_options="server=192.168.1.31:11211, max_value_size=10M"
```



#### Limitations


* Invalidation is not supported.
* Configuration values given to `<code>max_size</code>` and `<code>max_count</code>` are ignored.


#### Security


*Neither* the data in the memcached server *nor* the traffic between MaxScale and
the memcached server is encrypted. Consequently, *anybody* with access to the
memcached server or to the network have access to the cached data.


### `<code>storage_redis</code>`


This storage module uses [redis](https://redis.io/) for storing the
cached data.


Multiple MaxScale instances can share the same redis server and items
cached by one MaxScale instance will be used by the other. Note that all
MaxScale instances should have exactly the same configuration, as otherwise
there can be unintended sharing.



```
storage=storage_redis
```



If `<code>storage_redis</code>` cannot connect to the Redis server, caching will silently
be disabled and a connection attempt will be made after a [timeout](#timeout)
interval.


Note that since each connection attempt itself has the same timeout, reconnection
attempts will thus be made at `<code>2 * timeout</code>` intervals. The same approach is followed
also if the connection is lost during the lifetime of the session.


`<code>storage_redis</code>` has the following mandatory arguments:


* `<code>server</code>` using which the location of the server is specified as `<code>host[:port]</code>`.
 If no port is provided, the default Redis port of `<code>6379</code>` is used.


Example:



```
storage_options="server=192.168.1.31:6379"
```



Note that Redis should be configured with no idle timeout or with a timeout that
is very large. Otherwise MaxScale may have to repeatedly connect to Redis, which
will hurt both the functionality and the performance.


#### Limitations


* There is no distinction between soft and hard ttl, but only hard ttl is used.
* Configuration values given to `<code>max_size</code>` and `<code>max_count</code>` are ignored.


#### Invalidation


`<code>storage_redis</code>` supports invalidation, but the caveats documented [here](#best-efforts)
are of greater significance since also the communication between the cache and the
cache storage is asynchronous and takes place over the network.


*NOTE* If invalidation is turned on after caching has been used (in non-invalidation
mode), redis must be flushed as otherwise there will be entries in the cache that
will not be affected by the invalidation.



```
$ redis-cli flushall
```



#### Security


*Neither* the data in the redis server *nor* the traffic between MaxScale and
the redis server is encrypted. Consequently, *anybody* with access to the
redis server or to the network have access to the cached data.


## Example


In the following we define a cache *MyCache* that uses the cache storage module
`<code>storage_inmemory</code>` and whose *soft ttl* is `<code>30</code>` seconds and whose *hard ttl* is
`<code>45</code>` seconds. The cached data is shared between all threads and the maximum size
of the cached data is `<code>50</code>` mebibytes. The rules for the cache are in the file
`<code>cache_rules.json</code>`.


### Configuration



```
[MyCache]
type=filter
module=cache
storage=storage_inmemory
soft_ttl=30
hard_ttl=45
cached_data=shared
max_size=50Mi
rules=cache_rules.json

[MyService]
type=service
...
filters=MyCache
```



### `<code>cache_rules.json</code>`


The rules specify that the data of the table `<code>sbtest</code>` should be cached.



```
{
    "store": [
        {
            "attribute": "table",
            "op": "=",
            "value": "sbtest"
        }
    ]
}
```



## Performance


Perhaps the most significant factor affecting the performance of the cache is
whether the statements need to be parsed or not. By default, all statements are
parsed in order to exclude `<code>SELECT</code>` statements that use non-cacheable functions,
access non-cacheable variables or refer to system or user variables.


If it is known that no such statements are used or if it does not matter if the
results are cached, that safety measure can be turned off. To do that, add the
following line to the cache configuration:



```
[MyCache]
...
selects=assume_cacheable
```



With that configuration, the cache itself will not cause the statements to be
parsed.


But note that even with `<code>assume_cacheable</code>` configured, a rule referring
specifically to a *database*, *table* or *column* will still cause the
statement to be parsed.


For instance, a simple rule like



```
{
    "store": [
        {
            "attribute": "database",
            "op": "=",
            "value": "db1"
        }
    ]
}
```



cannot be fulfilled without parsing the statement.


If the rule is instead expressed using a regular expression



```
{
    "store": [
        {
            "attribute": "query",
            "op": "like",
            "value": "FROM db1\\..*"
        }
    ]
}
```



then the statement will again not be parsed.


However, even if regular expression matching performance wise is cheaper
than parsing, it still carries a cost. In the following is a table with numbers
giving a rough picture of the relative cost of different approaches.


In the table, *regexp match* means that the cacheable statements
were picked out using a rule like



```
{
    "attribute": "query",
    "op": "like",
    "value": "FROM dbname"
}
```



while *exact match* means that the cacheable statements were picked out using a
rule like



```
{
    "attribute": "database",
    "op": "=",
    "value": "dbname"
}
```



The exact match rule requires all statements to be parsed.


Note that the qps figures are only indicative and that the difference under
high load may be significantly *greater*.


| selects | Rule | qps |
| --- | --- | --- |
| selects | Rule | qps |
| assume_cacheable | none | 100 |
| assume_cacheable | regexp match | 98 |
| assume_cacheable | exact match | 60 |
| verify_cacheable | none | 60 |
| verify_cacheable | regexp match | 58 |
| verify_cacheable | exact match | 58 |


### Summary


For maximum performance:


* Arrange the situation so that the default `<code>selects=assume_cacheable</code>`
 can be used, and use no rules.
* If `<code>selects=assume_cacheable</code>` is used, use only regexp based rules.
* If `<code>selects=verify_cacheable</code>` has been configured, non-regex based
 matching can be used.
