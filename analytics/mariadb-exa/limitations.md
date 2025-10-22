---
icon: road-barrier
---

# Limitations

While MariaDB Exa (powered by Exasol) provides exceptional performance for analytical workloads, there are several functional and operational limitations to be aware of when integrating it with MariaDB, MaxScale, and Kafka Connect for CDC-based replication.

## Table and Schema Management

* **Pre-creation required:** All target tables must be manually created in Exasol before data replication begins. The connector does not auto-create or alter tables.
* **Schema evolution unsupported:** If a new table is added in MariaDB that matches an existing topic pattern, you must manually create the table in Exasol and restart the connector for the change to take effect.
* **Primary key requirement:** Every table being captured by CDC must define a primary key. Tables without primary keys are not supported by the JDBC Sink for upsert operations.
* **Per-table connectors:** Each table requires its own sink connector configuration for reliable data ingestion.

## CDC and Replication Behavior

* **Deletes and key modes:** In the sink connector configurations, when delete.enabled=true, the property primary.key.mode must be set to record\_key.
* **ColumnStore tables not replicated and not supported:** DML operations on ColumnStore tables are not written to binary logs. Only the initial snapshot (inventory phase) is transferred — subsequent changes are not replicated.
* **Connector state sensitivity:**
  * If the connector loses state (e.g., due to recreation or topic deletion), previously known table schemas may not be recognized, causing errors like:\
    `DebeziumException: Encountered change event for table <table> whose schema isn't known to this connector`
  * If the connector loses state (e.g., due to recreation or topic deletion), previously known table schemas may not be recognized, causing errors like:\
    `Commit of offsets timed out [WorkerSinkTask]`

## SQL and DDL Feature Gaps

### Unsupported Schema Features

The following schema features are not supported:

* `COLLATE` clause.
* Character set `LATIN1` .

### Unsupported Data Types

The following data types are not supported:

* `DATETIME`: Convert to `TIMESTAMP` .
* `LONGTEXT`: Convert to `VARCHAR(2000000)`.\
  Note: \~1/1000th the capacity
* `ENUM`: Convert to `VARCHAR` .

### Unsupported AUTO\_INCREMENT

* `AUTO_INCREMENT`: Exasol uses `IDENTITY` columns instead.
* These can contain gaps and are not guaranteed to be unique.
* The counter can be changed with `ALTER TABLE ... MODIFY COLUMN ... IDENTITY` .

### Unsupported Other Features

* `ON UPDATE` clauses.
* Triggers and stored procedures.

## SQL Syntax Differences

### Reserved Words

Exasol reserves over 460 keywords. Common words like schema, hour, and year must be quoted with double quotes ("column") — not backticks (\`). Example:

SELECT "year", "schema" FROM my\_table;

You can list all reserved words via:

SELECT \* FROM EXA\_SQL\_KEYWORDS WHERE RESERVED = TRUE;

### SET Statements

The following constructs are not supported:

```sql
SET x := y;
SET x=1, y=2;
```

Use DEFINE instead:

```sql
DEFINE x=1;
DEFINE y=2;
```

### Variable Assignment From SELECT

Not supported:

```sql
SELECT 1, 2 INTO @a, @b FROM dual;
```

Instead, use:

```sql
DEFINE x = (SELECT 1 FROM dual);
```

### Integer Precision Syntax

When defining integers, omit display width:

```sql
-- Incorrect
INT(8)
[42000] syntax error, unexpected '(', expecting ',' or ')'
```

```sql
-- Correct
INT
```

## Data Import and Null Handling

### NULL Conversions

MariaDB represents `NULL` values as `\N` in export files. Exasol `TIMESTAMP` columns do not accept `\N` — they must be converted explicitly (e.g., replace `\N` with `NULL` during import).

### Error on Mismatched Schema

When table definitions differ between source and Exasol, connector startup may fail with an error:

```
Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment]
due to: Unable to resolve name [com.exasol.hibernate.dialect.ExasolDialect]
```
