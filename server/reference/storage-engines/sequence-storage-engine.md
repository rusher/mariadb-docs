
# Sequence Storage Engine


This article is about the Sequence storage engine. For details about sequence objects, see [Sequences](../sql-statements-and-structure/sequences/README.md).


A **Sequence** engine allows the creation of ascending or descending sequences of numbers (positive integers) with a given starting value, ending value and increment.


It creates completely virtual, ephemeral tables automatically when you need them. There is no way to create a Sequence table explicitly. Nor are they ever written to disk or create `<code>.frm</code>` files. They are read-only, [transactional](../../../connectors/mariadb-connector-cpp/transactions-with-mariadb-connector-cpp.md), and [support XA](../sql-statements-and-structure/sql-statements/transactions/xa-transactions.md).


## Installing


The Sequence engine is installed by default, and [SHOW ENGINES](../sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-engines.md) will list the Sequence storage engine as supported:


```
SHOW ENGINES\G
...
*************************** 5. row ***************************
      Engine: MyISAM
     Support: YES
     Comment: MyISAM storage engine
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 6. row ***************************
      Engine: SEQUENCE
     Support: YES
     Comment: Generated tables filled with sequential values
Transactions: YES
          XA: YES
  Savepoints: YES
*************************** 7. row ***************************
      Engine: MRG_MyISAM
     Support: YES
     Comment: Collection of identical MyISAM tables
Transactions: NO
          XA: NO
  Savepoints: NO

...
```

## Usage and Examples


To use a Sequence table, you simply select from it, as in


```
SELECT * FROM seq_1_to_5;
+-----+
| seq |
+-----+
|   1 |
|   2 |
|   3 |
|   4 |
|   5 |
+-----+
```

To use a sequence in a statement, you select from the table named by a pattern **seq_**`<code>FROM</code>`**_to_**`<code>TO</code>` or **seq_**`<code>FROM</code>`**_to_**`<code>TO</code>`**_step_**`<code>STEP</code>`.


In the case of an odd step, the sequence will commence with the `<code>FROM</code>`, and end at the final result before `<code>TO</code>`.


```
SELECT * FROM seq_1_to_15_step_3;
+-----+
| seq |
+-----+
|   1 |
|   4 |
|   7 |
|  10 |
|  13 |
+-----+
```

A sequence can go backwards too. In this case the final value will always be the `<code>TO</code>` value, so that a descending sequence has the same values as an ascending sequence:


```
SELECT * FROM seq_5_to_1_step_2;
+-----+
| seq |
+-----+
|   5 |
|   3 |
|   1 |
+-----+
```

```
SELECT * FROM seq_15_to_1_step_3;
+-----+
| seq |
+-----+
|  13 |
|  10 |
|   7 |
|   4 |
|   1 |
+-----+
```

```
SELECT * FROM seq_15_to_2_step_3;
+-----+
| seq |
+-----+
|  14 |
|  11 |
|   8 |
|   5 |
|   2 |
+-----+
```

This engine is particularly useful with joins and subqueries. For example, this query finds all prime numbers below 50:


```
SELECT seq FROM seq_2_to_50 s1 WHERE 0 NOT IN
     (SELECT s1.seq % s2.seq FROM seq_2_to_50 s2 WHERE s2.seq <= sqrt(s1.seq));
+-----+
| seq |
+-----+
|   2 |
|   3 |
|   5 |
|   7 |
|  11 |
|  13 |
|  17 |
|  19 |
|  23 |
|  29 |
|  31 |
|  37 |
|  41 |
|  43 |
|  47 |
+-----+
```

And almost (without 2, the only even prime number) the same result with joins:


```
SELECT s1.seq FROM seq_2_to_50 s1 JOIN seq_2_to_50 s2 
  WHERE s1.seq > s2.seq AND s1.seq % s2.seq <> 0 
  GROUP BY s1.seq HAVING s1.seq - COUNT(*) = 2;
+-----+
| seq |
+-----+
|   3 |
|   5 |
|   7 |
|  11 |
|  13 |
|  17 |
|  19 |
|  23 |
|  29 |
|  31 |
|  37 |
|  41 |
|  43 |
|  47 |
+-----+
```

Sequence tables can also be useful in date calculations. For example, to find the day of the week that a particular date has fallen on over a 40 year period (perhaps for birthday planning ahead!):


```
SELECT DAYNAME('1980-12-05' + INTERVAL (seq) YEAR) day,
    '1980-12-05' + INTERVAL (seq) YEAR date FROM seq_0_to_40;
+-----------+------------+
| day       | date       |
+-----------+------------+
| Friday    | 1980-12-05 |
| Saturday  | 1981-12-05 |
| Sunday    | 1982-12-05 |
...
| Friday    | 2014-12-05 |
| Saturday  | 2015-12-05 |
| Monday    | 2016-12-05 |
| Tuesday   | 2017-12-05 |
| Wednesday | 2018-12-05 |
| Thursday  | 2019-12-05 |
| Saturday  | 2020-12-05 |
+-----------+------------+
```

Although Sequence tables can only directly make use of positive integers, they can indirectly be used to return negative results by making use of the [CAST](../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/cast.md) statement. For example:


```
SELECT CAST(seq AS INT) - 5 x FROM seq_5_to_1;
+----+
| x  |
+----+
|  0 |
| -1 |
| -2 |
| -3 |
| -4 |
+----+
```

[CAST](../sql-statements-and-structure/sql-statements/built-in-functions/string-functions/cast.md) is required to avoid a `<code>BIGINT UNSIGNED value is out of range</code>` error.


Sequence tables, while virtual, are still tables, so they must be in a database. This means that a default database must be selected (for example, via the [USE](../../../general-resources/learning-and-training/training-and-tutorials/beginner-mariadb-articles/useful-mariadb-queries.md) command) to be able to query a Sequence table. The [information_schema](../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) database cannot be used as the default for a Sequence table.


## Table Name Conflicts


If the SEQUENCE storage engine is installed, it is not possible to create a table with a name which follows the SEQUENCE pattern:


```
CREATE TABLE seq_1_to_100 (col INT) ENGINE = InnoDB;
ERROR 1050 (42S01): Table 'seq_1_to_100' already exists
```

However, a SEQUENCE table can be converted to another engine and the new table can be referred in any statement:


```
ALTER TABLE seq_1_to_100 ENGINE = BLACKHOLE;

SELECT * FROM seq_1_to_100;
Empty set (0.00 sec)
```

While a SEQUENCE table cannot be dropped, it is possible to drop the converted table. The SEQUENCE table with the same name will still exist:


```
DROP TABLE seq_1_to_100;

SELECT COUNT(*) FROM seq_1_to_100;
+----------+
| COUNT(*) |
+----------+
|      100 |
+----------+
1 row in set (0.00 sec)
```

A temporary table with a SEQUENCE-like name can always be created and used:


```
CREATE TEMPORARY TABLE seq_1_to_100 (col INT) ENGINE = InnoDB;

SELECT * FROM seq_1_to_100;
Empty set (0.00 sec)
```

## See Also


* For details about sequence objects, see [Sequences](../sql-statements-and-structure/sequences/README.md).
* [Sometimes its the little things](https://mariadb.com/blog/sometimes-its-little-things) - Dean Ellis tries out the Sequence engine.
* [MariaDB’s Sequence Storage Engine](https://falseisnotnull.wordpress.com/2013/06/23/mariadbs-sequence-storage-engine/) - Federico Razzoli writes more in-depth on the engine.

