
# SHOW ENGINES

## Syntax


```
SHOW [STORAGE] ENGINES
```

## Description


`<code class="highlight fixed" style="white-space:pre-wrap">SHOW ENGINES</code>` displays status information about the server's
storage engines. This is particularly useful for checking whether a storage
engine is supported, or to see what the default engine is. 
`<code class="highlight fixed" style="white-space:pre-wrap">SHOW TABLE TYPES</code>` is a deprecated synonym.


The `<code>[information_schema.ENGINES](../system-tables/information-schema/information-schema-tables/information-schema-engines-table.md)</code>` table provides the same information.


Since storage engines are plugins, different information about them is also shown in the `<code>[information_schema.PLUGINS](../system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md)</code>` table and by the `<code>[SHOW PLUGINS](show-plugins-soname.md)</code>` statement.


Note that both MySQL's InnoDB and Percona's XtraDB replacement are labeled as `<code>InnoDB</code>`. However, if XtraDB is in use, it will be specified in the `<code>COMMENT</code>` field. See [XtraDB and InnoDB](../../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/quality/innodb-upgrade-tests/README.md). The same applies to [FederatedX](../../../../storage-engines/federatedx-storage-engine/README.md).


The output consists of the following columns:


* `<code>Engine</code>` indicates the engine's name.
* `<code>Support</code>` indicates whether the engine is installed, and whether it is the default engine for the current session.
* `<code>Comment</code>` is a brief description.
* `<code>Transactions</code>`, `<code>XA</code>` and `<code>Savepoints</code>` indicate whether [transactions](../../../../../../connectors/mariadb-connector-cpp/transactions-with-mariadb-connector-cpp.md), [XA transactions](../../transactions/xa-transactions.md) and [transaction savepoints](../../transactions/savepoint.md) are supported by the engine.


## Examples


```
SHOW ENGINES\G
*************************** 1. row ***************************
      Engine: InnoDB
     Support: DEFAULT
     Comment: Supports transactions, row-level locking, and foreign keys
Transactions: YES
          XA: YES
  Savepoints: YES
*************************** 2. row ***************************
      Engine: CSV
     Support: YES
     Comment: CSV storage engine
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 3. row ***************************
      Engine: MyISAM
     Support: YES
     Comment: MyISAM storage engine
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 4. row ***************************
      Engine: BLACKHOLE
     Support: YES
     Comment: /dev/null storage engine (anything you write to it disappears)
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 5. row ***************************
      Engine: FEDERATED
     Support: YES
     Comment: FederatedX pluggable storage engine
Transactions: YES
          XA: NO
  Savepoints: YES
*************************** 6. row ***************************
      Engine: MRG_MyISAM
     Support: YES
     Comment: Collection of identical MyISAM tables
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 7. row ***************************
      Engine: ARCHIVE
     Support: YES
     Comment: Archive storage engine
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 8. row ***************************
      Engine: MEMORY
     Support: YES
     Comment: Hash based, stored in memory, useful for temporary tables
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 9. row ***************************
      Engine: PERFORMANCE_SCHEMA
     Support: YES
     Comment: Performance Schema
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 10. row ***************************
      Engine: Aria
     Support: YES
     Comment: Crash-safe tables with MyISAM heritage
Transactions: NO
          XA: NO
  Savepoints: NO
10 rows in set (0.00 sec)
```
