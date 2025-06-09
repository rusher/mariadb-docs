
# Performance Schema Digests

The Performance Schema digest is a normalized form of a statement, with the specific data values removed. It allows statistics to be gathered for similar kinds of statements.


For example:


```
SELECT * FROM customer WHERE age < 20
SELECT * FROM customer WHERE age < 30
```

With the data values removed, both of these statements normalize to:


```
SELECT * FROM customer WHERE age < ?
```

which is the digest text. The digest text is used to compute a digest. For example:


```
DIGEST_TEXT: SELECT * FROM `performance_schema` . `users`
DIGEST: 0f70cec4015f2a346df4ac0e9475d9f1
```

By contrast, the following two statements would not have the same digest as, while the data values are the same, they call upon different tables.


```
SELECT * FROM customer1 WHERE age < 20
SELECT * FROM customer2 WHERE age < 20
```

The digest text is limited to 1024 bytes. Queries exceeding this limit are truncated with '...', meaning that long queries that would otherwise have different digests may share the same digest.


Digest information is used in a number of performance scheme tables. These include


* [events_statements_current](performance-schema-tables/performance-schema-events_statements_current-table.md)
* [events_statements_history](performance-schema-tables/performance-schema-events_statements_history-table.md)
* [events_statements_history_long](performance-schema-tables/performance-schema-events_statements_history_long-table.md)
* [events_statements_summary_by_digest](performance-schema-tables/performance-schema-events_statements_summary_by_digest-table.md) (a summary table by schema and digest)


CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
