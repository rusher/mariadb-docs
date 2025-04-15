
# UUID_v7


##### MariaDB starting with [11.7](../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md)
From [MariaDB 11.7](../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-117.md), it is possible to generate UUIDv4 and UUIDv7, in addition to UUIDv1.


## Syntax


```
UUID_v7()
```


## Description


Returns a Universally Unique Identifier (UUID) version 7. To generate a version 1 UUID, see the [UUID](uuid.md) function. To generate a version 4 UUID, see [UUID_v4](uuid_v4.md).


A UUID is designed as a number that is globally unique in space and time. Two calls to `<code>UUID()</code>` are expected to generate two different values, even if these calls are performed on two separate computers that are not connected to each other.


A UUID is a 128-bit number represented by a utf8 string of five
hexadecimal numbers in `<code class="highlight fixed" style="white-space:pre-wrap">aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee</code>`
format:


Statements using the UUID_v7() function are [not safe for statement-based replication](../../../../../../server-usage/replication-cluster-multi-master/standard-replication/unsafe-statements-for-statement-based-replication.md).


## Examples


```
SELECT UUID(),UUID_v4(),UUID_v7()\G 
*************************** 1. row ***************************
  UUID(): 63ae8c92-799a-11ef-98b2-f859713e4be4
UUID_v4(): a2443495-1b94-415b-b6fa-fe8e79ba4812
UUID_v7(): 01921e85-f198-7490-9b89-7dd0d468543b
```

## See Also


* [UUID()](uuid.md) v1
* [UUID_v4()](uuid_v4.md)
* [UUID_SHORT()](uuid_short.md) - Return short (64 bit) Universal Unique Identifier
* [SYS_GUID](sys_guid.md) - UUID without the `<code>-</code>` character for Oracle compatibility
* [UUID data type](../../../../../data-types/string-data-types/uuid-data-type.md)
* [MDEV-11339](https://jira.mariadb.org/browse/MDEV-11339) (Support UUID v4 generation)
* [MDEV-32637](https://jira.mariadb.org/browse/MDEV-32637) (Implement native UUID7 function)
* [uuid7.com](https://uuid7.com/)

