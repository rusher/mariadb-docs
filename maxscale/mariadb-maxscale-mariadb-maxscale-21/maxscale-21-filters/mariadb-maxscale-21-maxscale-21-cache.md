
# MaxScale 2.1 Cache

# Cache


This filter was introduced in MariaDB MaxScale 2.1.


## Overview


*Note that the cache is still experimental and that non-backward compatible
changes may be made.*


The cache filter is a simple cache that is capable of caching the result of
SELECTs, so that subsequent identical SELECTs are served directly by MaxScale,
without the queries being routed to any server.


The cache will be used and populated in the following circumstances:
*There is no explicit transaction active, that is, autocommit is used,* there is an *explicitly* read-only transaction (that is,`<code>START TRANSACTION
 READ ONLY</code>`) active, or
* there is a transaction active and *no* statement that modifies the database
 has been performed.


In practice, the last bullet point basically means that if a transaction has
been started with `<code>BEGIN</code>`, `<code>START TRANSACTION</code>` or `<code>START TRANSACTION READ
WRITE</code>`, then the cache will be used and populated until the first `<code>UPDATE</code>`,
`<code>INSERT</code>` or `<code>DELETE</code>` statement is encountered.


By default, it is *ensured* that the cache is **not** used in the following
circumstances:


* The `<code>SELECT</code>` uses any of the following functions: `<code>BENCHMARK</code>`,
 `<code>CONNECTION_ID</code>`, `<code>CONVERT_TZ</code>`, `<code>CURDATE</code>`, `<code>CURRENT_DATE</code>`, `<code>CURRENT_TIMESTAMP</code>`,
 `<code>CURTIME</code>`, `<code>DATABASE</code>`, `<code>ENCRYPT</code>`, `<code>FOUND_ROWS</code>`, `<code>GET_LOCK</code>`, `<code>IS_FREE_LOCK</code>`,
 `<code>IS_USED_LOCK</code>`, `<code>LAST_INSERT_ID</code>`, `<code>LOAD_FILE</code>`, `<code>LOCALTIME</code>`, `<code>LOCALTIMESTAMP</code>`,
 `<code>MASTER_POS_WAIT</code>`, `<code>NOW</code>`, `<code>RAND</code>`, `<code>RELEASE_LOCK</code>`, `<code>SESSION_USER</code>`, `<code>SLEEP</code>`,
 `<code>SYSDATE</code>`, `<code>SYSTEM_USER</code>`, `<code>UNIX_TIMESTAMP</code>`, `<code>USER</code>`, `<code>UUID</code>`, `<code>UUID_SHORT</code>`.
* The `<code>SELECT</code>` accesses any of the following fields: `<code>CURRENT_DATE</code>`,
 `<code>CURRENT_TIMESTAMP</code>`, `<code>LOCALTIME</code>`, `<code>LOCALTIMESTAMP</code>`
* The `<code>SELECT</code>` uses system or user variables.


In order to ensure that, all `<code>SELECT</code>` statements have to be parsed, which
carries a *significant* performance cost. If it is known that there are no
such statements or that it does not matter even if they are cached, that
safety measure can be turned off. Please read [performance](#performance)
for more details.


## Limitations


All of these limitations may be addressed in forthcoming releases.


### Invalidation


Currently there is **no** cache invalidation, apart from *time-to-live*.


### Prepared Statements


Resultsets of prepared statements are **not** cached.


### Security


The cache is **not** aware of grants.


The implication is that unless the cache has been explicitly configured
who the caching should apply to, the presence of the cache may provide
a user with access to data he should not have access to.


Please read the section [Security](#security-1) for more detailed information.


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

[Cached Routing Service]
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
using up all memory there is, in case there is very litte overlap among the
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


A comma separated list of arguments to be provided to the storage module,
specified in `<code>storage</code>`, when it is loaded. Note that the needed arguments
depend upon the specific module. For instance,



```
storage_options=storage_specific_option1=value1,storage_specific_option2=value2
```



#### `<code>hard_ttl</code>`


*Hard time to live*; the maximum amount of time - in seconds - the cached
result is used before it is discarded and the result is fetched from the
backend (and cached). See also `<code>soft_ttl</code>` below.



```
hard_ttl=60
```



The default value is `<code>0</code>`, which means no limit.


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
soft_ttl=60
```



The default value is `<code>0</code>`, which means no limit. If the value of `<code>soft_ttl</code>` is
larger than `<code>hard_ttl</code>` it will be adjusted down to the same value.


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
as described [here](../maxscale-21-getting-started/mariadb-maxscale-21-mariadb-maxscale-configuration-usage-scenarios.md#sizes).



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
[here](../maxscale-21-getting-started/mariadb-maxscale-21-mariadb-maxscale-configuration-usage-scenarios.md#sizes).


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
 one hand it implies that no synchonization is needed between threads,
 on the other hand that the very same data may be fetched and stored
 multiple times.



```
cached_data=thread_specific
```



Default is `<code>shared</code>`. See `<code>max_count</code>` and `<code>max_size</code>` what implication changing
this setting to `<code>thread_specific</code>` has.


#### `<code>selects</code>`


An enumeration option specifying what approach the cache should take with
respect to `<code>SELECT</code>` statements. The allowed values are:


* `<code>assume_cacheable</code>`: The cache can assume that all `<code>SELECT</code>` statements,
 without exceptions, are cacheable.
* `<code>verify_cacheable</code>`: The cache can not assume that all `<code>SELECT</code>`
 statements are cacheable, but must verify that.



```
select=assume_cacheable
```



Default is `<code>verify_cacheable</code>`. In this case, the `<code>SELECT</code>` statements will be
parsed and only those that are safe for caching - e.g. do *not* call any
non-cacheable functions or access any non-cacheable variables - will be
subject to caching.


If `<code>assume_cacheable</code>` is specified, then all `<code>SELECT</code>` statements are
assumed to be cacheable and will be parsed *only* if some specific rule
requires that.


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



# Rules


The caching rules are expressed as a JSON object.


There are two decisions to be made regarding the caching; in what circumstances
should data be stored to the cache and in what circumstances should the data in
the cache be used.


In the JSON object this is visible as follows:



```
{
    store: [ ... ],
    use: [ ... ]
}
```



The `<code>store</code>` field specifies in what circumstances data should be stored to
the cache and the `<code>use</code>` field specifies in what circumstances the data in
the cache should be used. In both cases, the value is a JSON array containg
objects.


## When to Store


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
 * the *attribute* can be `<code>database</code>`, `<code>table</code>`, `<code>column</code>` or `<code>query</code>`,
 * the *op* can be `<code>=</code>`, `<code>!=</code>`, `<code>like</code>` or `<code>unlike</code>`, and
 * the *value* a string.


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


### Qualified Names


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


### Implication of the default database.


If the rules concerns the `<code>database</code>`, then only if the statement refers
to *no* specific database, will the default database be considered.


### Regexp Matching


The string used for matching the regular expression contains as much
information as there is available. For instance, in a situation like



```
use somedb;
select fld from tbl;
```



the string matched against the regular expression will be `<code>somedb.tbl.fld</code>`.


### Examples


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


## When to Use


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
 * the *attribute* can be `<code>user</code>`,
 * the *op* can be `<code>=</code>`, `<code>!=</code>`, `<code>like</code>` or `<code>unlike</code>`, and
 * the *value* a string.


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


### Examples


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



# Security


As the cache is not aware of grants, unless the cache has been explicitly
configured who the caching should apply to, the presence of the cache
may provide a user with access to data he should not have access to.


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


# Storage


## `<code>storage_inmemory</code>`


This simple storage module uses the standard memory allocator for storing
the cached data.



```
storage=storage_inmemory
```



## `<code>storage_rocksdb</code>`


This storage module is not built by default and is not included in the
MariaDB MaxScale packages.


This storage module uses RocksDB database for storing the cached data. The
directory where the RocksDB database will be created is by default created
into the *MaxScale cache* directory, which usually is not on a RAM disk. For
maximum performance, you may want to explicitly place the RocksDB database
on a RAM disk.



```
storage=storage_rocksdb
```



### Parameters


#### `<code>cache_directory</code>`


Specifies the directory under which the filter instance specific RocksDB
databases will be placed. Note that at startup, each RocksDB database will
be deleted and recreated. That is, cache content will not be retained across
MaxScale restarts.



```
storage_options=cache_directory=/mnt/maxscale-cache
```



With the above setting a directory `<code>/mnt/macscale-cache/storage_rocksdb</code>` will
created, under which the actual instance specific cache directories are created.


#### `<code>collect_statistics</code>`


Specifies whether RocksDB should collect statistics that later can be queried
using `<code>maxadmin</code>`. It should be noted, though, that collecting RocksDB statistics
is not without a cost.
From the [RocksDB Documentation](https://github.com/facebook/rocksdb/wiki/Statistics)


*The overhead of statistics is usually small but non-negligible. We usually
observe an overhead of 5%-10%.*


The value is a boolean and the default is `<code>false</code>`.



```
storage_options=collect_statistics=true
```



# Example


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



# Performance


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


Note that the qps figures are only indicative.


| selects | Rule | qps |
| --- | --- | --- |
| selects | Rule | qps |
| assume_cacheable | none | 100 |
| assume_cacheable | regexp match | 98 |
| assume_cacheable | exact match | 60 |
| verify_cacheable | none | 60 |
| verify_cacheable | regexp match | 58 |
| verify_cacheable | exact match | 58 |


## Summary


For maximum performance:
*Arrange the situation so that `<code>selects=assume_cacheable</code>` can be
 configured, and use no rules.* If `<code>selects=assume_cacheable</code>` has been configured, use *only*
 regexp based rules.
* If `<code>selects=verify_cacheable</code>` has been configured non-regex based
 matching can be used.
