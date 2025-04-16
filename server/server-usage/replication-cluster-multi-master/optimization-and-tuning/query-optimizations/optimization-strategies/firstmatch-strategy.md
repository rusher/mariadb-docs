
# FirstMatch Strategy


`<code>FirstMatch</code>` is an execution strategy for [Semi-join subqueries](../subquery-optimizations/semi-join-subquery-optimizations.md).


## The idea


It is very similar to how `<code>IN/EXISTS</code>` subqueries were executed in MySQL 5.x.


Let's take the usual example of a search for countries with big cities:


```
select * from Country 
where Country.code IN (select City.Country 
                       from City 
                       where City.Population > 1*1000*1000)
      and Country.continent='Europe'
```

Suppose, our execution plan is to find countries in Europe, and then, for each found country, check if it has any big cities. Regular inner join execution will look as follows:


![firstmatch-inner-join](../../../../../.gitbook/assets/firstmatch-strategy/+image/firstmatch-inner-join.png "firstmatch-inner-join")


Since Germany has two big cities (in this diagram), it will be put into the query output twice. This is not correct, `<code class="fixed" style="white-space:pre-wrap">SELECT ... FROM Country</code>` should not produce the same country record twice. The `<code>FirstMatch</code>` strategy avoids the production of duplicates by short-cutting execution as soon as the first genuine match is found:


![firstmatch-firstmatch](../../../../../.gitbook/assets/firstmatch-strategy/+image/firstmatch-firstmatch.png "firstmatch-firstmatch")


Note that the short-cutting has to take place after "Using where" has been applied. It would have been wrong to short-cut after we found Trier.


## FirstMatch in action


The `<code>EXPLAIN</code>` for the above query will look as follows:


```
MariaDB [world]> explain select * from Country where Country.code IN 
  (select City.Country from City where City.Population > 1*1000*1000)
    and Country.continent='Europe';
+----+-------------+---------+------+--------------------+-----------+---------+--------------------+------+----------------------------------+
| id | select_type | table   | type | possible_keys      | key       | key_len | ref                | rows | Extra                            |
+----+-------------+---------+------+--------------------+-----------+---------+--------------------+------+----------------------------------+
|  1 | PRIMARY     | Country | ref  | PRIMARY,continent  | continent | 17      | const              |   60 | Using index condition            |
|  1 | PRIMARY     | City    | ref  | Population,Country | Country   | 3       | world.Country.Code |   18 | Using where; FirstMatch(Country) |
+----+-------------+---------+------+--------------------+-----------+---------+--------------------+------+----------------------------------+
2 rows in set (0.00 sec)
```

`<code class="fixed" style="white-space:pre-wrap">FirstMatch(Country)</code>` in the Extra column means that *as soon as we have produced one matching record combination, short-cut the execution and jump back to the Country* table.


`<code>FirstMatch</code>`'s query plan is very similar to one you would get in MySQL:


```
MySQL [world]> explain select * from Country  where Country.code IN 
  (select City.Country from City where City.Population > 1*1000*1000) 
   and Country.continent='Europe';
+----+--------------------+---------+----------------+--------------------+-----------+---------+-------+------+------------------------------------+
| id | select_type        | table   | type           | possible_keys      | key       | key_len | ref   | rows | Extra                              |
+----+--------------------+---------+----------------+--------------------+-----------+---------+-------+------+------------------------------------+
|  1 | PRIMARY            | Country | ref            | continent          | continent | 17      | const |   60 | Using index condition; Using where |
|  2 | DEPENDENT SUBQUERY | City    | index_subquery | Population,Country | Country   | 3       | func  |   18 | Using where                        |
+----+--------------------+---------+----------------+--------------------+-----------+---------+-------+------+------------------------------------+
2 rows in set (0.01 sec)
```

and these two particular query plans will execute in the same time.


## Difference between FirstMatch and IN->EXISTS


The general idea behind the `<code>FirstMatch</code>` strategy is the same as the one behind the `<code>IN->EXISTS</code>` transformation, however, `<code>FirstMatch</code>` has several advantages:


* Equality propagation works across semi-join bounds, but not subquery bounds. Therefore, converting a subquery to semi-join and using `<code>FirstMatch</code>` can still give a better execution plan. (TODO example)


* There is only one way to apply the `<code>IN->EXISTS</code>` strategy and MySQL will do it unconditionally. With `<code>FirstMatch</code>`, the optimizer can make a choice between whether it should run the `<code>FirstMatch</code>` strategy as soon as all tables used in the subquery are in the join prefix, or at some later point in time. (TODO: example)


## FirstMatch factsheet


* The `<code>FirstMatch</code>` strategy works by executing the subquery and short-cutting its execution as soon as the first match is found.
* This means, subquery tables must be after all of the parent select's tables that are referred from the subquery predicate.
* `<code>EXPLAIN</code>` shows `<code>FirstMatch</code>` as "`<code>FirstMatch(tableN)</code>`".
* The strategy can handle correlated subqueries.
* But it cannot be applied if the subquery has meaningful `<code>GROUP BY</code>` and/or aggregate functions.
* Use of the `<code>FirstMatch</code>` strategy is controlled with the `<code class="fixed" style="white-space:pre-wrap">firstmatch=on|off</code>` flag in the [optimizer_switch](../../system-variables/server-system-variables.md#optimizer_switch) variable.


## See Also


* [Semi-join subquery optimizations](../subquery-optimizations/semi-join-subquery-optimizations.md)


In-depth material:


* [WL#3750: initial specification for FirstMatch](https://forge.mysql.com/worklog/task.php?id=3750)

