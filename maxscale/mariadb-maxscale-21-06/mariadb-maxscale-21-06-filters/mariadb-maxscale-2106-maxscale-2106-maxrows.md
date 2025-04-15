
# MaxScale 21.06 Maxrows

# Maxrows


This filter was introduced in MariaDB MaxScale 2.1.




* [Maxrows](#maxrows)

  * [Overview](#overview)
  * [Configuration](#configuration)

    * [Filter Parameters](#filter-parameters)

      * [max_resultset_rows](#max_resultset_rows)
      * [max_resultset_size](#max_resultset_size)
      * [max_resultset_return](#max_resultset_return)
      * [debug](#debug)
  * [Example Configuration](#example-configuration)




## Overview


The Maxrows filter is capable of restricting the amount of rows that a SELECT,
 a prepared statement or stored procedure could return to the client application.


If a resultset from a backend server has more rows than the configured limit
or the resultset size exceeds the configured size,
 an empty result will be sent to the client.


## Configuration


The Maxrows filter is easy to configure and to add to any existing service.



```
[MaxRows]
type=filter
module=maxrows

[MaxRows-Routing-Service]
type=service
...
filters=MaxRows
```



### Filter Parameters


The Maxrows filter has no mandatory parameters.
Optional parameters are:


#### `<code>max_resultset_rows</code>`


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: (no limit)


Specifies the maximum number of rows a resultset can have in order to be
returned to the user.


If a resultset is larger than this an empty result will be sent instead.



```
max_resultset_rows=1000
```



#### `<code>max_resultset_size</code>`


* Type: [size](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `<code>64Ki</code>`


Specifies the maximum size a resultset can have in order
to be sent to the client. A resultset larger than this, will
not be sent: an empty resultset will be sent instead.



```
max_resultset_size=128Ki
```



#### `<code>max_resultset_return</code>`


* Type: [enum](../mariadb-maxscale-21-06-getting-started/mariadb-maxscale-2106-maxscale-2106-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `<code>empty</code>`, `<code>error</code>`, `<code>ok</code>`
* Default: `<code>empty</code>`


Specifies what the filter sends to the client when the
rows or size limit is hit, possible values:


* an empty result set
* an error packet with input SQL
* an OK packet


Example output with ERR packet:



```
MariaDB [(test)]> select * from test.t4;
ERROR 1415 (0A000): Row limit/size exceeded for query: select * from test.t4
```



#### `<code>debug</code>`


* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `<code>0</code>`


An integer value, using which the level of debug logging made by the Maxrows
filter can be controlled. The value is actually a bitfield with different bits
denoting different logging.


* `<code>0</code>` (`<code>0b00000</code>`) No logging is made.
* `<code>1</code>` (`<code>0b00001</code>`) A decision to handle data form server is logged.
* `<code>2</code>` (`<code>0b00010</code>`) Reached max_resultset_rows or max_resultset_size is logged.


To log everything, give `<code>debug</code>` a value of `<code>3</code>`.



```
debug=2
```



## Example Configuration


Here is an example of filter configuration where the maximum number of returned
rows is 10000 and maximum allowed resultset size is 256KB



```
[MaxRows]
type=filter
module=maxrows
max_resultset_rows=10000
max_resultset_size=256000
```

