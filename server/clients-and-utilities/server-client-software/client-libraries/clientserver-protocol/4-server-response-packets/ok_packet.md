# OK_Packet

OK_Packet is sent by the server to the client and indicates a successful completion of a command sent by the client before.

#

## Direction

Server to client.

#

## Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) 0x00 : OK_Packet header or (0xFE if CLIENT_DEPRECATE_EOF is set)
* [int<lenenc>](../protocol-data-types.md#length-encoded-integers) affected rows
* [int<lenenc>](../protocol-data-types.md#length-encoded-integers) last insert id
* [int<2>](../protocol-data-types.md#fixed-length-integers) [server status](#server-status-flag)
* [int<2>](../protocol-data-types.md#fixed-length-integers) warning count
* if packet has more data

 * [string<lenenc>](../protocol-data-types.md#length-encoded-strings) info
 * if (status flags & SERVER_SESSION_STATE_CHANGED) and session_tracking_supported (see [CLIENT_SESSION_TRACK](/en/1-connecting-connecting/#capabilities))

 * [string<lenenc>](../protocol-data-types.md#length-encoded-strings) [session state info](#session-state-info)

The length-encoded info string is not always included in the packet. Check the length of the packet to detect if there is data after the warning count. For the first OK_Packet in the connection it contains (if present) the [SSL certificate verification signature](https://mariadb.org/mission-impossible-zero-configuration-ssl/). For the following OK_Packets it contains (if present) various human-readable information.

#

## Server status flag

Values of server status flag

| SERVER_STATUS_IN_TRANS | 1 | A transaction is currently active |
| SERVER_STATUS_AUTOCOMMIT | 2 | Autocommit mode is set |
| SERVER_MORE_RESULTS_EXISTS | 8 | More results exists (more packets will follow) |
| SERVER_QUERY_NO_GOOD_INDEX_USED | 16 | Set if [EXPLAIN](../../../../explain-analyzer.md) would've shown Range checked for each record |
| SERVER_QUERY_NO_INDEX_USED | 32 | The query did not use an index |
| SERVER_STATUS_CURSOR_EXISTS | 64 | When using COM_STMT_FETCH, indicate that current cursor still has result |
| SERVER_STATUS_LAST_ROW_SENT | 128 | When using COM_STMT_FETCH, indicate that current cursor has finished to send results |
| SERVER_STATUS_DB_DROPPED | 1<<8 | Database has been dropped |
| SERVER_STATUS_NO_BACKSLASH_ESCAPES | 1<<9 | Current escape mode is "no backslash escape" |
| SERVER_STATUS_METADATA_CHANGED | 1<<10 | A DDL change did have an impact on an existing PREPARE (an automatic reprepare has been executed) |
| SERVER_QUERY_WAS_SLOW | 1<<11 | The query was slower than [long_query_time](https://mariadb.com/kb/en/server-system-variables/#long_query_time) |
| SERVER_PS_OUT_PARAMS | 1<<12 | This resultset contain stored procedure output parameter |
| SERVER_STATUS_IN_TRANS_READONLY | 1<<13 | Current transaction is a read-only transaction |
| SERVER_SESSION_STATE_CHANGED | 1<<14 | Session state change. See Session change type for more information |

#

## Session state info

* while packet has remaining data

 * [int<1>](../protocol-data-types.md#fixed-length-integers) [session change type](#session-change-type)
 * if (session-change-type != SESSION_TRACK_STATE_CHANGE)

 * [int<lenenc>](../protocol-data-types.md#length-encoded-integers) total length
 * [string<lenenc>](../protocol-data-types.md#length-encoded-strings) session data's change

#

### Session change type

| 0 | SESSION_TRACK_SYSTEM_VARIABLES |
| 1 | SESSION_TRACK_SCHEMA |
| 2 | SESSION_TRACK_STATE_CHANGE |
| 3 | SESSION_TRACK_GTIDS |
| 4 | SESSION_TRACK_TRANSACTION_CHARACTERISTICS |
| 5 | SESSION_TRACK_TRANSACTION_STATE |

#

### session data's change

Each type of data has his own kind of format :

#

#### SESSION_TRACK_SCHEMA

* [string<lenenc>](../protocol-data-types.md#length-encoded-strings) new current schema

#

#### SESSION_TRACK_SYSTEM_VARIABLES

while there is remaining data :

* [string<lenenc>](../protocol-data-types.md#length-encoded-strings) variable data

for each variable data :

* [string<lenenc>](../protocol-data-types.md#length-encoded-strings) variable name
* [string<lenenc>](../protocol-data-types.md#length-encoded-strings) variable value

Possible tracked variables list is tracked by [session_track_system_variables](https://mariadb.com/kb/en/server-system-variables/)
special variable value description:

* [redirect_url](https://mariadb.com/kb/en/server-system-variables/#redirect_url): format is `mariadb/mysql:[<user>[:<password>]@]<host>[:<port>]/[<db>[?<opt1>=<value1>[&<opt2>=<value2>]]]`. Possible options: 

 * `ttl` : cache timeout in ms to remember redirection, in order to reconnect directly to new host. 0=no caching

#

#### SESSION_TRACK_STATE_CHANGE

indicates if session state changes occured. The value is represented as "1".

* [string<lenenc>](../protocol-data-types.md#length-encoded-strings) "1" if session state tracking was enabled

#

#### SESSION_TRACK_GTIDS

This tracker is not implemented by MariaDB.

#

#### SESSION_TRACK_TRANSACTION_CHARACTERISTICS

* [string<lenenc>](../protocol-data-types.md#length-encoded-strings) Transaction characteristics

The transaction characteristics is the set of SQL statements that reproduces the type and state of the current transaction. It can consist of the following SQL statements:

```
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
START TRANSACTION;
START TRANSACTION WITH CONSISTENT SNAPSHOT;
START TRANSACTION WITH CONSISTENT SNAPSHOT, READ ONLY;
START TRANSACTION WITH CONSISTENT SNAPSHOT, READ WRITE;
SET TRANSACTION READ ONLY;
SET TRANSACTION READ WRITE;
XA START <XA specification>;
```

#

#### SESSION_TRACK_TRANSACTION_STATE

* [string<lenenc>](../protocol-data-types.md#length-encoded-strings) Transaction state string

The transaction state string is always 8 characters long. The characters, in order, are:
1. No transaction: `_` Explicit transaction: `T` Implicit transaction: `I`
1. Transaction read safe: `_` Transaction read unsafe: `r`
1. Unknown transaction type: `_` Read-only transaction: `R`
1. Transaction write safe: `_` Transaction write unsafe: `w`
1. Unknown transaction type: `_` Read-write transaction: `W`
1. Transaction statement safe: `_` Transaction statement unsafe: `s`
1. Transaction does not have resultsets: `_` Transaction with resultsets: `S`
1. No locked tables: `_` Tables have been locked: `L`

#

## Notes

* Session tracking is supported from [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-102). To determine if session tracking is enabled, check if the [CLIENT_SESSION_TRACK](/en/connecting-connecting/#capabilities) flag is set in server_capabilities.