# The ConnectionPool class

### _class_ ConnectionPool(\*args, \*\*kwargs)

Class defining a pool of database connections

MariaDB Connector/Python supports simple connection pooling. A connection pool holds a number of open connections and handles thread safety when providing connections to threads.

The size of a connection pool is configurable at creation time, but cannot be changed afterward. The maximum size of a connection pool is limited to 64 connections.

Keyword Arguments:

* **\`pool\_name\`** (`str`) - Name of connection pool
* **\`pool\_size\`** (`int`) - Size of pool. The Maximum allowed number is 64. Default to 5
* **\`pool\_reset\_connection\`** (`bool`) - Will reset the connection before returning it to the pool. Default to True.
* **\`pool\_validation\_interval\`** (`int`) - Specifies the validation interval in milliseconds after which the status of a connection requested from the pool is checked. A value of 0 means that the status will always be checked. Default to 500 (Added in version 1.1.6)
* **\*\*kwargs** - Optional additional connection arguments, as described in mariadb.connect() method.

## ConnectionPool methods

#### ConnectionPool.add\_connection(connection=None)

Adds a connection object to the connection pool.

In case that the pool doesn’t have a free slot or is not configured, a PoolError exception will be raised.

#### ConnectionPool.close()

Closes connection pool and all connections.

#### ConnectionPool.get\_connection()

Returns a connection from the connection pool or raises a PoolError exception if a connection is not available.

#### ConnectionPool.set\_config(\*\*kwargs)

Sets the connection configuration for the connection pool. For valid connection arguments, check the mariadb.connect() method.

Note: This method doesn’t create connections in the pool. To fill the pool, one has to use add\_connection() ḿethod.

## ConnectionPool attributes

#### ConnectionPool.connection\_count

Returns the number of connections in connection pool.

_Since version 1.1.0_

#### ConnectionPool.max\_size

Returns the maximum size for connection pools.

#### ConnectionPool.pool\_size

Returns the size of the connection pool.

#### ConnectionPool.pool\_name

Returns the name of the connection pool.

<sub>_This page is_</sub> [<sub>_covered_</sub>](license.md) <sub>_by the_</sub> [<sub>_Creative Commons Attribution 3.0 license_</sub>](https://creativecommons.org/licenses/by/3.0/legalcode)<sub>_._</sub>

{% @marketo/form formId="4316" %}
