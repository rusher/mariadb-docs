# JOIN Syntax

## Description

MariaDB supports the following `JOIN` syntaxes for\
the `table_references` part of `[SELECT](../../select.md)` statements and\
multiple-table `[DELETE](../../../changing-deleting-data/delete.md)` and `[UPDATE](../../../changing-deleting-data/update.md)` statements:

```
table_references:
    table_reference [, table_reference] ...

table_reference:
    table_factor
  | join_table

table_factor (<= MariaDB 11.6):
    tbl_name [PARTITION (partition_list)]
        [query_system_time_period_specification] [[AS] alias] [index_hint_list]
  | table_subquery [query_system_time_period_specification] [AS] alias
  | ( table_references )
  | { ON table_reference LEFT OUTER JOIN table_reference
        ON conditional_expr }

table_factor (>= MariaDB 11.7):
    tbl_name [PARTITION (partition_list)]
        [query_system_time_period_specification] [[AS] alias] [index_hint_list]
  | table_subquery [query_system_time_period_specification] [AS] alias [(column_name_list)] 
  | ( table_references )
  | { ON table_reference LEFT OUTER JOIN table_reference
        ON conditional_expr }

join_table:
    table_reference [INNER | CROSS] JOIN table_factor [join_condition]
  | table_reference STRAIGHT_JOIN table_factor
  | table_reference STRAIGHT_JOIN table_factor ON conditional_expr
  | table_reference {LEFT|RIGHT} [OUTER] JOIN table_reference join_condition
  | table_reference NATURAL [{LEFT|RIGHT} [OUTER]] JOIN table_factor

join_condition:
    ON conditional_expr
  | USING (column_list)

query_system_time_period_specification:
    FOR SYSTEM_TIME AS OF point_in_time
  | FOR SYSTEM_TIME BETWEEN point_in_time AND point_in_time
  | FOR SYSTEM_TIME FROM point_in_time TO point_in_time
  | FOR SYSTEM_TIME ALL

point_in_time:
    [TIMESTAMP] expression
  | TRANSACTION expression

index_hint_list:
    index_hint [, index_hint] ...

index_hint:
    USE {INDEX|KEY}
      [{FOR {JOIN|ORDER BY|GROUP BY}] ([index_list])
  | IGNORE {INDEX|KEY}
      [{FOR {JOIN|ORDER BY|GROUP BY}] (index_list)
  | FORCE {INDEX|KEY}
      [{FOR {JOIN|ORDER BY|GROUP BY}] (index_list)

index_list:
    index_name [, index_name] ...
```

A table reference is also known as a join expression.

Each table can also be specified as `db_name`.`tabl_name`. This allows to write queries which involve multiple databases. See [Identifier Qualifiers](../../../../../sql-statements-and-structure/sql-language-structure/identifier-qualifiers.md) for syntax details.

The syntax of `table_factor` is extended in comparison with the\
SQL Standard. The latter accepts only `table_reference`, not a\
list of them inside a pair of parentheses.

This is a conservative extension if we consider each comma in a list of\
table\_reference items as equivalent to an inner join. For example:

```
SELECT * FROM t1 LEFT JOIN (t2, t3, t4)
                 ON (t2.a=t1.a AND t3.b=t1.b AND t4.c=t1.c)
```

is equivalent to:

```
SELECT * FROM t1 LEFT JOIN (t2 CROSS JOIN t3 CROSS JOIN t4)
                 ON (t2.a=t1.a AND t3.b=t1.b AND t4.c=t1.c)
```

In MariaDB, `CROSS JOIN` is a syntactic equivalent to`INNER JOIN` (they can replace each other). In standard SQL,\
they are not equivalent. `INNER JOIN` is used with an`ON` clause, `CROSS JOIN` is used otherwise.

In general, parentheses can be ignored in join expressions containing only\
inner join operations. MariaDB also supports nested joins (see[nested-join-optimization.html](https://dev.mysql.com/doc/refman/5.1/en/nested-join-optimization.html)).

### Subqueries

A table subquery is specified as a parenthesized query and must contain a following derived table name (specified as _alias_ in the above syntax specification).\
From [MariaDB 11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-11-7-rolling-releases/what-is-mariadb-117) onwards, we can optionally specify a list of column names in parenthesis.

```
select ic1, ic2, ic3 from
      (
        select c1, c2, c3 from t1 group by c1
      ) dt2 (ic1, ic2, ic3)
    join t2 on t2.c1 = dt2.ic1
    where c2 > 0
    group by ic1
```

Here, the table subquery for t1 will be materialized and named dt2, with column names ic1, ic2, ic3. These column names are used outside the subquery.

See also [Subqueries in a FROM Clause (Derived Tables)#Correlation Column List](../subqueries/subqueries-in-a-from-clause-derived-tables.md#correlation-column-list).

### System-Versioned Tabled

See [System-versioned tables](../../../../../sql-statements-and-structure/temporal-tables/system-versioned-tables.md) for more information\
about `FOR SYSTEM_TIME` syntax.

### Index Hints

Index hints can be specified to affect how the MariaDB optimizer makes\
use of indexes. For more information, see [How to force query plans](../../../../../../ha-and-performance/optimization-and-tuning/query-optimizations/index-hints-how-to-force-query-plans.md).

## Examples

```
SELECT left_tbl.*
  FROM left_tbl LEFT JOIN right_tbl ON left_tbl.id = right_tbl.id
  WHERE right_tbl.id IS NULL;
```

GPLv2 fill\_help\_tables.sql
