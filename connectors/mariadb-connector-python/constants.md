# Constants

> Constants are declared in mariadb.constants module.

> For using constants of various types, they have to be imported first:

```python
from mariadb.constants import *
```

## CAPABILITY

MariaDB capability flags.

These flags are used to check the capabilities both of a MariaDB server or the client applicaion.

Capability flags are defined in module _mariadb.constants.CAPABILIY_

_Since version 1.1.4_

```python
import mariadb
from mariadb.constants import *

# connection parameters
conn_params= {
    "user" : "example_user",
    "password" : "GHbe_Su3B8",
    "host" : "localhost"
}

with mariadb.connect(**conn_params) as connection:
    # test if LOAD DATA LOCAL INFILE is supported
    if connection.server_capabilities & CAPABILITY.LOCAL_FILES:
        print("Server supports LOCAL INFILE")
```

_Output_:

```none
Server supports LOCAL INFILE
```

## CLIENT

MariaDB capability flags.

These flags are used to check the capabilities both of a MariaDB server or the client applicaion.

Capability flags are defined in module _mariadb.constants.CLIENT_

_Since version 1.1.0, deprecated in 1.1.4_

## CURSOR

Cursor constants are used for server side cursors. Currently only read only cursor is supported.

Cursor constants are defined in module _mariadb.constants.CURSOR_.

_Since version 1.1.0_

#### CURSOR.NONE

This is the default setting (no cursor)

#### CURSOR.READ\_ONLY

Will create a server side read only cursor. The cursor is a forward cursor, which means it is not possible to scroll back.

## ERR (Error)

Using ERR constants instead of error numbers make the code more readable. Error constants are defined in constants.ERR module

_Since version 1.1.2_

```python
import mariadb
from mariadb.constants import *

# connection parameters
conn_params= {
    "user" : "example_user",
    "password" : "wrong_password",
    "host" : "localhost"
}

# try to establish a connection
try:
    connection= mariadb.connect(**conn_params)
except mariadb.OperationalError as Err:
    if Err.errno == ERR.ER_ACCESS_DENIED_ERROR:
        print("Access denied. Wrong password!")
```

_Output_:

```none
Access denied. Wrong password!
```

## FIELD\_FLAG

MariaDB FIELD\_FLAG Constants

These constants represent the various field flags. As an addition to the DBAPI 2.0 standard (PEP-249) these flags are returned as eighth element of the cursor description attribute.

Field flags are defined in module _mariadb.constants.FIELD\_FLAG_

_Since version 1.1.0_

#### FIELD\_FLAG.NOT\_NULL

column is defined as not NULL

#### FIELD\_FLAG.PRIMARY\_KEY

column is (part of) a primary key

#### FIELD\_FLAG.UNIQUE\_KEY

column is (part of) a unique key

#### FIELD\_FLAG.MULTIPLE\_KEY

column is (part of) a key

#### FIELD\_FLAG.BLOB

column contains a binary object

#### FIELD\_FLAG.UNSIGNED

numeric column is defined as unsigned

#### FIELD\_FLAG.ZEROFILL

column has zerofill attribute

#### FIELD\_FLAG.BINARY

column is a binary

#### FIELD\_FLAG.ENUM

column is defined as enum

#### FIELD\_FLAG.AUTO\_INCREMENT

column is an auto\_increment column

#### FIELD\_FLAG.TIMESTAMP

column is defined as time stamp

#### FIELD\_FLAG.SET

column is defined as SET

#### FIELD\_FLAG.NO\_DEFAULT

column hasn’t a default value

#### FIELD\_FLAG.ON\_UPDATE\_NOW

column will be set to current timestamp on UPDATE

#### FIELD\_FLAG.NUMERIC

column contains numeric value

#### FIELD\_FLAG.PART\_OF\_KEY

column is part of a key

## FIELD\_TYPE

MariaDB FIELD\_TYPE Constants

These constants represent the field types supported by MariaDB. The field type is returned as second element of cursor description attribute.

Field types are defined in module _mariadb.constants.FIELD\_TYPE_

#### FIELD\_TYPE.TINY

column type is TINYINT (1-byte integer)

#### FIELD\_TYPE.SHORT

column type is SMALLINT (2-byte integer)

#### FIELD\_TYPE.LONG

column tyoe is INT (4-byte integer)

#### FIELD\_TYPE.FLOAT

column type is FLOAT (4-byte single precision)

#### FIELD\_TYPE.DOUBLE

column type is DOUBLE (8-byte double precision)

#### FIELD\_TYPE.NULL

column type is NULL

#### FIELD\_TYPE.TIMESTAMP

column tyoe is TIMESTAMP

#### FIELD\_TYPE.LONGLONG

column tyoe is BIGINT (8-byte Integer)

#### FIELD\_TYPE.INT24

column type is MEDIUMINT (3-byte Integer)

#### FIELD\_TYPE.DATE

column type is DATE

#### FIELD\_TYPE.TIME

column type is TIME

#### FIELD\_TYPE.DATETIME

column type is YEAR

#### FIELD\_TYPE.YEAR

#### FIELD\_TYPE.VARCHAR

column type is YEAR

#### FIELD\_TYPE.BIT

column type is BIT

#### FIELD\_TYPE.JSON

column type is JSON

#### FIELD\_TYPE.NEWDECIMAL

column type is DECIMAL

#### FIELD\_TYPE.ENUM

column type is ENUM

#### FIELD\_TYPE.SET

column type is SET

#### FIELD\_TYPE.TINY\_BLOB

column type is TINYBLOB (max. length of 255 bytes)

#### FIELD\_TYPE.MEDIUM\_BLOB

column type is MEDIUMBLOB (max. length of 16,777,215 bytes)

#### FIELD\_TYPE.LONG\_BLOB

column type is LONGBLOB (max. length 4GB bytes)

#### FIELD\_TYPE.BLOB

column type is BLOB (max. length of 65.535 bytes)

#### FIELD\_TYPE.VAR\_STRING

column type is VARCHAR (variable length)

#### FIELD\_TYPE.STRING

column type is CHAR (fixed length)

#### FIELD\_TYPE.GEOMETRY

column type is GEOMETRY

## INDICATORS

Indicator values are used in executemany() method of cursor class to indicate special values when connected to a MariaDB server 10.2 or newer.

#### INDICATOR.NULL

indicates a NULL value

#### INDICATOR.DEFAULT

indicates to use default value of column

#### INDICATOR.IGNORE

indicates to ignore value for column for UPDATE statements. If set, the column will not be updated.

#### INDICATOR.IGNORE\_ROW

indicates not to update the entire row.

## INFO

For internal use only

## TPC\_STATE

For internal use only

## STATUS

The STATUS constants are used to check the server status of the current connection.

_Since version 1.1.0_

> Example:

> ```python
> cursor.callproc("my_storedprocedure", (1,"foo"))
> ```

> if (connection.server\_status & STATUS.SP\_OUT\_PARAMS): print("retrieving output parameters from store procedure") ... else: print("retrieving data from stored procedure") ....
>
> ```
> ```

#### STATUS.IN\_TRANS

Pending transaction

#### STATUS.AUTOCOMMIT

Server operates in autocommit mode

#### STATUS.MORE\_RESULTS\_EXIST

The result from last executed statement contained two or more result sets which can be retrieved by cursors nextset() method.

#### STATUS.QUERY\_NO\_GOOD\_INDEX\_USED

The last executed statement didn’t use a good index.

#### STATUS.QUERY\_NO\_INDEX\_USED

The last executed statement didn’t use an index.

#### STATUS.CURSOR\_EXISTS

The last executed statement opened a server side cursor.

#### STATUS.LAST\_ROW\_SENT

For server side cursors this flag indicates end of a result set.

#### STATUS.DB\_DROPPED

The current database in use was dropped and there is no default database for the connection anymore.

#### STATUS.NO\_BACKSLASH\_ESCAPES

Indicates that SQL mode NO\_BACKSLASH\_ESCAPE is active, which means that the backslash character ‘' becomes an ordinary character.

#### STATUS.QUERY\_WAS\_SLOW

The previously executed statement was slow (and needs to be optimized).

#### STATUS.PS\_OUT\_PARAMS

The current result set contains output parameters of a stored procedure.

#### STATUS.SESSION\_STATE\_CHANGED

The session status has been changed.

#### STATUS.ANSI\_QUOTES

SQL mode ANSI\_QUOTES is active,

<sub>_This page is_</sub> [<sub>_covered_</sub>](license.md) <sub>_by the_</sub> [<sub>_Creative Commons Attribution 3.0 license_</sub>](https://creativecommons.org/licenses/by/3.0/legalcode)<sub>_._</sub>

{% @marketo/form formId="4316" %}
