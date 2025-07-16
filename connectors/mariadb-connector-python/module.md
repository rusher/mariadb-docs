# The MariaDB Connector/Python module

MariaDB Connector/Python module enables python programs to access MariaDB and MySQL databases, using an API which is compliant with the Python DB API 2.0 (PEP-249).

## Constructors

### Connection

### connect(connectionclass=mariadb.connections.Connection, \*\*kwargs)

Creates a MariaDB Connection object.

By default, the standard connectionclass mariadb.connections.Connection will be created.

Parameter connectionclass specifies a subclass of mariadb.Connection object. If not specified, default will be used. This optional parameter was added in version 1.1.0.

Connection parameters are provided as a set of keyword arguments:

* **\`host\`** - The host name or IP address of the database server. If MariaDB Connector/Python was built with MariaDB Connector/C 3.3, it is also possible to provide a comma separated list of hosts for simple fail over in case of one or more hosts are not available.
* **\`user\`, \`username\`** - The username used to authenticate with the database server
* **\`password\`, \`passwd\`** - The password of the given user
* **\`database\`, \`db\`** - Database (schema) name to use when connecting with the database server
* **\`unix\_socket\`** - The location of the unix socket file to use instead of using an IP port to connect. If socket authentication is enabled, this can also be used in place of a password.
* **\`port\`** - Port number of the database server. If not specified, the default value of 3306 will be used.
* **\`connect\_timeout\`** - Connect timeout in seconds
* **\`read\_timeout\`** - Read timeout in seconds
* **\`write\_timeout\`** - Write timeout in seconds
* **\`local\_infile\`** - Enables or disables the use of LOAD DATA LOCAL INFILE statements.
* **\`compress\`** (default: False) - Uses the compressed protocol for client server communication. If the server doesn’t support compressed protocol, the default protocol will be used.
* **\`init\_command\`** - Command(s) which will be executed when connecting and reconnecting to the database server
* **\`default\_file\`** - Read options from the specified option file. If the file is an empty string, default configuration file(s) will be used
* **\`default\_group\`** - Read options from the specified group
* **\`plugin\_dir\`** - Directory which contains MariaDB client plugins.
* **\`reconnect\`** - Enables or disables automatic reconnect. Available since version 1.1.4
* **\`ssl\_key\`** - Defines a path to a private key file to use for TLS. This option requires that you use the absolute path, not a relative path. The specified key must be in PEM format
* **\`ssl\_cert\`** - Defines a path to the X509 certificate file to use for TLS. This option requires that you use the absolute path, not a relative path. The X609 certificate must be in PEM format.
* **\`ssl\_ca\`** - Defines a path to a PEM file that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for TLS. This option requires that you use the absolute path, not a relative path.
* **\`ssl\_capath\`** - Defines a path to a directory that contains one or more PEM files that contains one X509 certificate for a trusted Certificate Authority (CA)
* **\`ssl\_cipher\`** - Defines a list of permitted cipher suites to use for TLS
* **\`ssl\_crlpath\`** - Defines a path to a PEM file that should contain one or more revoked X509 certificates to use for TLS. This option requires that you use the absolute path, not a relative path.
* **\`ssl\_verify\_cert\`** - Enables server certificate verification.
* **\`ssl\`** - The connection must use TLS security, or it will fail.
* **\`tls\_version\`** - A comma-separated list (without whitespaces) of TLS versions. Valid versions are TLSv1.0, TLSv1.1,TLSv1.2 and TLSv1.3. Added in version 1.1.7.
* **\`autocommit\`** (default: False) - Specifies the autocommit settings. True will enable autocommit, False will disable it (default).
* **\`converter\`** - Specifies a conversion dictionary, where keys are FIELD\_TYPE values and values are conversion functions

#### NOTE

For a description of configuration file handling and settings please read the chapter [Configuration files](https://github.com/mariadb-corporation/mariadb-connector-c/wiki/config_files#configuration-options) of the MariaDB Connector/C documentation.

Example:

```python
import mariadb

with mariadb.connect(user="example_user", host="localhost", database="test", password="GHbe_Su3B8") as connection:
    print(connection.character_set)
```

Output:

```none
utf8mb4
```

### Connection Pool

### ConnectionPool(\*\*kwargs)

Class defining a pool of database connections

MariaDB Connector/Python supports simple connection pooling. A connection pool holds a number of open connections and handles thread safety when providing connections to threads.

The size of a connection pool is configurable at creation time, but cannot be changed afterward. The maximum size of a connection pool is limited to 64 connections.

Keyword Arguments:

* **\`pool\_name\`** (`str`) - Name of connection pool
* **\`pool\_size\`** (`int`) - Size of pool. The Maximum allowed number is 64. Default to 5
* **\`pool\_reset\_connection\`** (`bool`) - Will reset the connection before returning it to the pool. Default to True.
* **\`pool\_validation\_interval\`** (`int`) - Specifies the validation interval in milliseconds after which the status of a connection requested from the pool is checked. A value of 0 means that the status will always be checked. Default to 500 (Added in version 1.1.6)
* **\*\*kwargs** - Optional additional connection arguments, as described in mariadb.connect() method.

### Type constructors

### Binary()

Constructs an object capable of holding a binary value.

### Date(year, month, day)

Constructs an object holding a date value.

### DateFromTicks(ticks)

Constructs an object holding a date value from the given ticks value (number of seconds since the epoch). For more information see the documentation of the standard Python time module.

### Time(hour, minute, second)

Constructs an object holding a time value.

### TimeFromTicks(ticks)

Constructs an object holding a time value from the given ticks value (number of seconds since the epoch). For more information see the documentation of the standard Python time module.

### Timestamp(year, month, day, hour, minute, second)

Constructs an object holding a datetime value.

### TimestampFromTicks(ticks)

Constructs an object holding a datetime value from the given ticks value (number of seconds since the epoch). For more information see the documentation of the standard Python time module.

## Attributes

### apilevel

String constant stating the supported DB API level. The value for mariadb is `2.0`.

### threadsafety

Integer constant stating the level of thread safety. For mariadb the value is 1, which means threads can share the module but not the connection.

### paramstyle

String constant stating the type of parameter marker. For mariadb the value is qmark. For compatibility reasons mariadb also supports the format and pyformat paramstyles with the limitation that they can’t be mixed inside a SQL statement.

### mariadbapi\_version

String constant stating the version of the used MariaDB Connector/C library.

### client\_version

_Since version 1.1.0_

Returns the version of MariaDB Connector/C library in use as an integer. The number has the following format: MAJOR\_VERSION \* 10000 + MINOR\_VERSION \* 1000 + PATCH\_VERSION

### client\_version\_info

_Since version 1.1.0_ Returns the version of MariaDB Connector/C library as a tuple in the following format: (MAJOR\_VERSION, MINOR\_VERSION, PATCH\_VERSION)

## Exceptions

Compliant to DB API 2.0 MariaDB Connector/C provides information about errors through the following exceptions:

### _exception_ DataError

Exception raised for errors that are due to problems with the processed data like division by zero, numeric value out of range, etc.

### _exception_ DatabaseError

Exception raised for errors that are related to the database

### _exception_ InterfaceError

Exception raised for errors that are related to the database interface rather than the database itself

### _exception_ Warning

Exception raised for important warnings like data truncations while inserting, etc

### _exception_ PoolError

Exception raised for errors related to ConnectionPool class.

### _exception_ OperationalError

Exception raised for errors that are related to the database’s operation and not necessarily under the control of the programmer.

### _exception_ IntegrityError

Exception raised when the relational integrity of the database is affected, e.g. a foreign key check fails

### _exception_ InternalError

Exception raised when the database encounters an internal error, e.g. the cursor is not valid anymore

### _exception_ ProgrammingError

Exception raised for programming errors, e.g. table not found or already exists, syntax error in the SQL statement

### _exception_ NotSupportedError

Exception raised in case a method or database API was used which is not supported by the database

### Type objects

MariaDB Connector/Python type objects are immutable sets for type settings and defined in DBAPI 2.0 (PEP-249).

Example:

```python
import mariadb
from mariadb.constants import FIELD_TYPE

print(FIELD_TYPE.GEOMETRY == mariadb.BINARY)
print(FIELD_TYPE.DATE == mariadb.DATE)
print(FIELD_TYPE.VARCHAR == mariadb.BINARY)
```

Output:

```none
True
True
False
```

### STRING

This type object is used to describe columns in a database that are string-based (e.g. CHAR1).

### BINARY

This type object is used to describe (long) binary columns in a database (e.g. LONG, RAW, BLOBs).

### NUMBER

This type object is used to describe numeric columns in a database.

### DATETIME

This type object is used to describe date/time columns in a database.

### ROWID

This type object is not supported in MariaDB Connector/Python and represents an empty set.

<sub>_This page is_</sub> [<sub>_covered_</sub>](license.md) <sub>_by the_</sub> [<sub>_Creative Commons Attribution 3.0 license_</sub>](https://creativecommons.org/licenses/by/3.0/legalcode)<sub>_._</sub>

{% @marketo/form formId="4316" %}
