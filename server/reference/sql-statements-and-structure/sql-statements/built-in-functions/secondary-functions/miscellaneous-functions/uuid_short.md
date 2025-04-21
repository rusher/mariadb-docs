
# UUID_SHORT

## Syntax


```
UUID_SHORT()
```


## Description


Returns a "short" universally unique identifier as a 64-bit unsigned integer (rather
than a string-form 128-bit identifier as returned by the [UUID()](uuid.md) function).


The value of `UUID_SHORT()` is guaranteed to be unique if the
following conditions hold:


* The server_id of the current host is unique among your set of master and
 slave servers
* `server_id` is between 0 and 255
* You don't set back your system time for your server between mariadbd restarts
* You do not invoke `UUID_SHORT()` on average more than 16
 million times per second between mariadbd restarts


The UUID_SHORT() return value is constructed this way:


```
(server_id & 255) << 56
+ (server_startup_time_in_seconds << 24)
+ incremented_variable++;
```

Statements using the UUID_SHORT() function are not [safe for statement-based replication](../../../../../../server-usage/replication-cluster-multi-master/standard-replication/unsafe-statements-for-statement-based-replication.md).


## Examples


```
SELECT UUID_SHORT();
+-------------------+
| UUID_SHORT()      |
+-------------------+
| 21517162376069120 |
+-------------------+
```

```
create table t1 (a bigint unsigned default(uuid_short()) primary key);
insert into t1 values(),();
select * from t1;
+-------------------+
| a                 |
+-------------------+
| 98113699159474176 |
| 98113699159474177 |
+-------------------+
```

## See Also


* [UUID()](uuid.md) ; Return full (128 bit) Universally Unique Identifier
* [AUTO_INCREMENT](../../../../../data-types/auto_increment.md)
* [Sequences](../../../../sequences/README.md) - an alternative to auto_increment available from [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)
* [SYS_GUID](sys_guid.md) - UUID without the `-` character for Oracle compatibility
* [UUID data type](../../../../../data-types/string-data-types/uuid-data-type.md)

