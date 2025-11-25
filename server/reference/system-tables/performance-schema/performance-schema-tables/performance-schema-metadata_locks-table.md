# Performance Schema metadata\_locks Table

{% hint style="info" %}
The `metadata_locks` table is available from MariaDB 10.5.2.
{% endhint %}

The `metadata_locks` table contains [metadata lock](../../../sql-statements/transactions/metadata-locking.md) information.

To enable metadata lock instrumention, at runtime:

```sql
UPDATE performance_schema.setup_instruments SET enabled='YES', timed='YES' 
  WHERE name LIKE 'wait/lock/metadata%';
```

Or in the [configuration file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
performance-schema-instrument='wait/lock/metadata/sql/mdl=ON'
```

The table is by default autosized, but the size can be configured with the [performance\_schema\_max\_metadata\_locks](../performance-schema-system-variables.md#performance_schema_max_metadata_locks) system variable.

The table is read-only, and [TRUNCATE TABLE](../../../sql-statements/table-statements/truncate-table.md) cannot be used to empty the table.

The table contains the following columns:

| Field                   | Type                  | Null  | Default | Description                                                                                                                                                                                                                                                                                                                                            |
| ----------------------- | --------------------- | ----- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `OBJECT_TYPE`           | `varchar(64)`         | `NO`  | `NULL`  | Object type. One of `BACKUP`, `COMMIT`, `EVENT`, `FUNCTION`, `GLOBAL`, `LOCKING SERVICE`, `PROCEDURE, SCHEMA`, `TABLE`, `TABLESPACE`, `TRIGGER` (unused) or `USER LEVEL LOCK`.                                                                                                                                                                         |
| `OBJECT_SCHEMA`         | `varchar(64)`         | `YES` | `NULL`  | Object schema.                                                                                                                                                                                                                                                                                                                                         |
| `OBJECT_NAME`           | `varchar(64)`         | `YES` | `NULL`  | Object name.                                                                                                                                                                                                                                                                                                                                           |
| `OBJECT_INSTANCE_BEGIN` | `bigint(20) unsigned` | `NO`  | `NULL`  | Address in memory of the instrumented object.                                                                                                                                                                                                                                                                                                          |
| `LOCK_TYPE`             | `varchar(32)`         | `NO`  | `NULL`  | Lock type. One of `BACKUP_FTWRL1`, `BACKUP_START`, `BACKUP_TRANS_DML`, `EXCLUSIVE`, `INTENTION_EXCLUSIVE`, `SHARED`, `SHARED_HIGH_PRIO`, `SHARED_NO_READ_WRITE`, `SHARED_NO_WRITE`, `SHARED_READ`, `SHARED_UPGRADABLE` or `SHARED_WRITE`.                                                                                                              |
| `LOCK_DURATION`         | `varchar(32)`         | `NO`  | `NULL`  | Lock duration. One of `EXPLICIT` (locks released by explicit action, for example a global lock acquired with [FLUSH TABLES WITH READ LOCK](../../../sql-statements/administrative-sql-statements/flush-commands/flush.md)) , `STATEMENT` (locks implicitly released at statement end) or `TRANSACTION` (locks implicitly released at transaction end). |
| `LOCK_STATUS`           | `varchar(32)`         | `NO`  | `NULL`  | Lock status. One of `GRANTED`, `KILLED`, `PENDING`, `POST_RELEASE_NOTIFY`, `PRE_ACQUIRE_NOTIFY`, `TIMEOUT` or `VICTIM`.                                                                                                                                                                                                                                |
| `SOURCE`                | `varchar(64)`         | `YES` | `NULL`  | Source file containing the instrumented code that produced the event, as well as the line number where the instrumentation occurred. This allows one to examine the source code involved.                                                                                                                                                              |
| `OWNER_THREAD_ID`       | `bigint(20) unsigned` | `YES` | `NULL`  | Thread that requested the lock.                                                                                                                                                                                                                                                                                                                        |
| `OWNER_EVENT_ID`        | `bigint(20) unsigned` | `YES` | `NULL`  | Event that requested the lock.                                                                                                                                                                                                                                                                                                                         |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
