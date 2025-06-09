# IS\_USED\_LOCK

## Syntax

```
IS_USED_LOCK(str)
```

## Description

Checks whether the lock named `str` is in use (that is, locked). If so,\
it returns the connection identifier of the client that holds the\
lock. Otherwise, it returns `NULL`. `str` is case insensitive.

If the [metadata\_lock\_info](../../../plugins/other-plugins/metadata-lock-info-plugin.md) plugin is installed, the [Information Schema](../../../sql-statements/administrative-sql-statements/system-tables/information-schema/) [metadata\_lock\_info](../../../sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-metadata_lock_info-table.md) table contains information about locks of this kind (as well as [metadata locks](../../../sql-statements/transactions/metadata-locking.md)).

Statements using the `IS_USED_LOCK` function are [not safe for statement-based replication](../../../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).

## See Also

* [GET\_LOCK](get_lock.md)
* [RELEASE\_LOCK](release_lock.md)
* [IS\_FREE\_LOCK](is_free_lock.md)
* [RELEASE\_ALL\_LOCKS](release_all_locks.md)

GPLv2 fill\_help\_tables.sql

{% @marketo/form formId="4316" %}
