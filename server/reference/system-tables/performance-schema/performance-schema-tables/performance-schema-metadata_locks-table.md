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

<table><thead><tr><th width="199.328125">Field</th><th width="108.09765625">Type</th><th width="75.2421875">Null</th><th width="61.015625">Default</th><th>Description</th></tr></thead><tbody><tr><td><code>OBJECT_TYPE</code></td><td><code>varchar(64)</code></td><td><code>NO</code></td><td><code>NULL</code></td><td>Object type. One of <code>BACKUP</code>, <code>COMMIT</code>, <code>EVENT</code>, <code>FUNCTION</code>, <code>GLOBAL</code>, <code>LOCKING SERVICE</code>, <code>PROCEDURE, SCHEMA</code>, <code>TABLE</code>, <code>TABLESPACE</code>, <code>TRIGGER</code> (unused) or <code>USER LEVEL LOCK</code>.</td></tr><tr><td><code>OBJECT_SCHEMA</code></td><td><code>varchar(64)</code></td><td><code>YES</code></td><td><code>NULL</code></td><td>Object schema.</td></tr><tr><td><code>OBJECT_NAME</code></td><td><code>varchar(64)</code></td><td><code>YES</code></td><td><code>NULL</code></td><td>Object name.</td></tr><tr><td><code>OBJECT_INSTANCE_BEGIN</code></td><td><code>bigint(20) unsigned</code></td><td><code>NO</code></td><td><code>NULL</code></td><td>Address in memory of the instrumented object.</td></tr><tr><td><code>LOCK_TYPE</code></td><td><code>varchar(32)</code></td><td><code>NO</code></td><td><code>NULL</code></td><td>Lock type. One of <code>BACKUP_FTWRL1</code>, <code>BACKUP_START</code>, <code>BACKUP_TRANS_DML</code>, <code>EXCLUSIVE</code>, <code>INTENTION_EXCLUSIVE</code>, <code>SHARED</code>, <code>SHARED_HIGH_PRIO</code>, <code>SHARED_NO_READ_WRITE</code>, <code>SHARED_NO_WRITE</code>, <code>SHARED_READ</code>, <code>SHARED_UPGRADABLE</code> or <code>SHARED_WRITE</code>.</td></tr><tr><td><code>LOCK_DURATION</code></td><td><code>varchar(32)</code></td><td><code>NO</code></td><td><code>NULL</code></td><td>Lock duration. One of <code>EXPLICIT</code> (locks released by explicit action, for example a global lock acquired with <a href="../../../sql-statements/administrative-sql-statements/flush-commands/flush.md">FLUSH TABLES WITH READ LOCK</a>) , <code>STATEMENT</code> (locks implicitly released at statement end) or <code>TRANSACTION</code> (locks implicitly released at transaction end).</td></tr><tr><td><code>LOCK_STATUS</code></td><td><code>varchar(32)</code></td><td><code>NO</code></td><td><code>NULL</code></td><td>Lock status. One of <code>GRANTED</code>, <code>KILLED</code>, <code>PENDING</code>, <code>POST_RELEASE_NOTIFY</code>, <code>PRE_ACQUIRE_NOTIFY</code>, <code>TIMEOUT</code> or <code>VICTIM</code>.</td></tr><tr><td><code>SOURCE</code></td><td><code>varchar(64)</code></td><td><code>YES</code></td><td><code>NULL</code></td><td>Source file containing the instrumented code that produced the event, as well as the line number where the instrumentation occurred. This allows one to examine the source code involved.</td></tr><tr><td><code>OWNER_THREAD_ID</code></td><td><code>bigint(20) unsigned</code></td><td><code>YES</code></td><td><code>NULL</code></td><td>Thread that requested the lock.</td></tr><tr><td><code>OWNER_EVENT_ID</code></td><td><code>bigint(20) unsigned</code></td><td><code>YES</code></td><td><code>NULL</code></td><td>Event that requested the lock.</td></tr></tbody></table>

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
