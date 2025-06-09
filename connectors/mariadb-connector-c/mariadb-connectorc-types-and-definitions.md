# MariaDB Connector/C Types and Definitions

MariaDB Connector/C provides the following types and definitions.

### Enumeration Types

#### enum mysql\_option

`enum mysql_option` is used as a parameter in [mysql\_optionsv()](api-functions/mysql_optionsv.md) and [mysql\_get\_optionsv()](https://mariadb.com/kb/en/library/mysql_get_optionsv) API functions. For a list of integral constants and their meanings please check the documentation of [mysql\_get\_optionsv()](https://github.com/mariadb-corporation/docs-connectors/blob/test/mariadb-connector-c/library/mysql_get_optionsv/README.md).

#### enum enum\_mysql\_timestamp\_type

`enum enum_mysql_timestamp_type` is used in the [MYSQL\_TIME](https://mariadb.com/kb/en/MYSQL_TIME) structure and indicates the type. It has the following constants:

* MYSQL\_TIMESTAMP\_NONE
* MYSQL\_TIMESTAMP\_ERROR
* MYSQL\_TIMESTAMP\_DATE
* MYSQL\_TIMESTAMP\_DATETIME
* MYSQL\_TIMESTAMP\_TIME

#### enum mysql\_set\_option

`enum mysql_set_option` is used as a parameter in [mysql\_set\_server\_option()](api-functions/mysql_set_server_option.md) and has the following constants:

* MYSQL\_OPTIONS\_MULTI\_STATEMENTS\_ON
* MYSQL\_OPTIONS\_MULTI\_STATEMENTS\_OFF

#### enum enum\_field\_types

`enum field_types` describes the different field types used by MariaDB ] and has the following constants:

* MYSQL\_TYPE\_DECIMAL
* MYSQL\_TYPE\_TINY
* MYSQL\_TYPE\_SHORT
* MYSQL\_TYPE\_LONG
* MYSQL\_TYPE\_FLOAT
* MYSQL\_TYPE\_DOUBLE
* MYSQL\_TYPE\_NULL
* MYSQL\_TYPE\_TIMESTAMP
* MYSQL\_TYPE\_LONGLONG
* MYSQL\_TYPE\_INT24
* MYSQL\_TYPE\_DATE
* MYSQL\_TYPE\_TIME
* MYSQL\_TYPE\_DATETIME
* MYSQL\_TYPE\_YEAR
* MYSQL\_TYPE\_NEWDATE
* MYSQL\_TYPE\_VARCHAR
* MYSQL\_TYPE\_BIT
* MYSQL\_TYPE\_TIMESTAMP2
* MYSQL\_TYPE\_DATETIME2
* MYSQL\_TYPE\_TIME2
* MYSQL\_TYPE\_JSON
* MYSQL\_TYPE\_NEWDECIMAL
* MYSQL\_TYPE\_ENUM
* MYSQL\_TYPE\_SET
* MYSQL\_TYPE\_TINY\_BLOB
* MYSQL\_TYPE\_MEDIUM\_BLOB
* MYSQL\_TYPE\_LONG\_BLOB
* MYSQL\_TYPE\_BLOB
* MYSQL\_TYPE\_VAR\_STRING
* MYSQL\_TYPE\_STRING
* MYSQL\_TYPE\_GEOMETRY

#### enum mysql\_enum\_shutdown\_level

`enum mysql_enum_shutdown_level` is used as a parameter in [mysql\_server\_shutdown()](https://mariadb.com/kb/en/library/mysql_server_shutdown) and has the following constants:

* SHUTDOWN\_DEFAULT
* KILL\_QUERY
* KILL\_CONNECTION

#### enum enum\_stmt\_attr\_type

`enum_stmt_attr_type` is used to set different statement options. For a detailed description please check [mysql\_stmt\_attr\_set()](api-prepared-statement-functions/mysql_stmt_attr_set.md) function.

#### enum enum\_cursor\_type

`enum_cursor_type` specifies the cursor type and is used in [mysql\_stmt\_attr\_set()](api-prepared-statement-functions/mysql_stmt_attr_set.md) function. Currently the following constants are supported:

* CURSOR\_TYPE\_READ\_ONLY
* CURSOR\_TYPE\_NO\_CURSOR

#### enum enum\_indicator\_type

`enum_indicator_type` describes the type of indicator used for prepared statements bulk operations.

|                              |                            |
| ---------------------------- | -------------------------- |
| STMT\_INDICATOR\_NTS         | String is zero terminated  |
| STMT\_INDICATOR\_NONE        | No indicator in use        |
| STMT\_INDICATOR\_NULL        | Value is NULL              |
| STMT\_INDICATOR\_DEFAULT     | Use default value          |
| STMT\_INDICATOR\_IGNORE      | Ignore the specified value |
| STMT\_INDICATOR\_IGNORE\_ROW | Skip the current row       |

### Definitions

#### Field Flags

The following field flags are used in [MYSQL\_FIELD](mariadb-connectorc-data-structures.md) structure.

|                          |       |                                                                  |
| ------------------------ | ----- | ---------------------------------------------------------------- |
| Flag                     | Value | Description                                                      |
| NOT\_NULL\_FLAG          | 1     | Field can't be NULL                                              |
| PRI\_KEY\_FLAG           | 2     | Field is part of primary key                                     |
| UNIQUE\_KEY\_FLAG        | 4     | Field is part of unique key                                      |
| MULTIPLE\_KEY\_FLAG      | 8     | Field is part of a key                                           |
| BLOB\_FLAG               | 16    | Field is a blob                                                  |
| UNSIGNED\_FLAG           | 32    | Field is unsigned integer                                        |
| ZEROFILL\_FLAG           | 64    | Field is zero filled                                             |
| BINARY\_FLAG             | 128   | Field is binary                                                  |
| ENUM\_FLAG               | 256   | Field is enum                                                    |
| AUTO\_INCREMENT\_FLAG    | 512   | Field is an autoincrement field                                  |
| TIMESTAMP\_FLAG          | 1024  | Field is a timestamp                                             |
| SET\_FLAG                | 2048  | Field is a set                                                   |
| NO\_DEFAULT\_VALUE\_FLAG | 4096  | Field has no default value                                       |
| ON\_UPDATE\_NOW\_FLAG    | 8192  | If a field is updated it will get the current time value (NOW()) |
| NUM\_FLAG                | 32768 | Field is numeric                                                 |

#### Server Status

The server\_status can be obtained by the [mariadb\_get\_infov()](api-functions/mariadb_get_infov.md) function using the `MARIADB_CONNECTION_SERVER_STATUS` option.

|                                        |       |                                                                                                   |
| -------------------------------------- | ----- | ------------------------------------------------------------------------------------------------- |
| SERVER\_STATUS\_IN\_TRANS              | 1     | A transaction is currently active                                                                 |
| SERVER\_STATUS\_AUTOCOMMIT             | 2     | Autocommit mode is set                                                                            |
| SERVER\_MORE\_RESULTS\_EXISTS          | 8     | more results exists (more packet follow)                                                          |
| SERVER\_QUERY\_NO\_GOOD\_INDEX\_USED   | 16    |                                                                                                   |
| SERVER\_QUERY\_NO\_INDEX\_USED         | 32    |                                                                                                   |
| SERVER\_STATUS\_CURSOR\_EXISTS         | 64    | when using COM\_STMT\_FETCH, indicate that current cursor still has result                        |
| SERVER\_STATUS\_LAST\_ROW\_SENT        | 128   | when using COM\_STMT\_FETCH, indicate that current cursor has finished to send results            |
| SERVER\_STATUS\_DB\_DROPPED            | 1<<8  | database has been dropped                                                                         |
| SERVER\_STATUS\_NO\_BACKSLASH\_ESCAPES | 1<<9  | current escape mode is "no backslash escape"                                                      |
| SERVER\_STATUS\_METADATA\_CHANGED      | 1<<10 | A DDL change did have an impact on an existing PREPARE (an automatic reprepare has been executed) |
| SERVER\_QUERY\_WAS\_SLOW               | 1<<11 | Last statement took more than the time value specified in server variable long\_query\_time.      |
| SERVER\_PS\_OUT\_PARAMS                | 1<<12 | this resultset contain stored procedure output parameter                                          |
| SERVER\_STATUS\_IN\_TRANS\_READONLY    | 1<<13 | current transaction is a read-only transaction                                                    |
| SERVER\_SESSION\_STATE\_CHANGED        | 1<<14 | session state change. see Session change type for more information                                |

#### Macros

|                            |                                            |
| -------------------------- | ------------------------------------------ |
| IS\_PRI\_KEY(flag)         | True if the field is part of a primary key |
| IS\_NOT\_NULL(flags)       | True if the field is defined as not NULL   |
| IS\_BLOB(flags)            | True if the field is a text or blob field  |
| IS\_NUM(column\_type)      | True if the column type is numeric         |
| IS\_LONGDATA(column\_type) | True if the column is a blob or text field |

{% @marketo/form formid="4316" %}
