
# optimizer_switch

[optimizer_switch](../system-variables/server-system-variables.md#optimizer_switch) is a server variable that one can use to enable/disable specific optimizations.


## Syntax


To set or unset the various optimizations, use the following syntax:


```
SET [GLOBAL|SESSION] optimizer_switch='cmd[,cmd]...';
```

The *cmd* takes the following format:



| Syntax | Description |
| --- | --- |
| Syntax | Description |
| default | Reset all optimizations to their default values. |
| optimization_name=default | Set the specified optimization to its default value. |
| optimization_name=on | Enable the specified optimization. |
| optimization_name=off | Disable the specified optimization. |



There is no need to list all flags - only those that are specified in the command will be affected.


## Available Flags


Below is a list of all *optimizer_switch* flags available in MariaDB:



| Flag and MariaDB default | Supported in MariaDB since |
| --- | --- |
| Flag and MariaDB default | Supported in MariaDB since |
| [condition_pushdown_for_derived=on](optimizations-for-derived-tables/condition-pushdown-into-derived-table-optimization.md) | [MariaDB 10.2.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-1022-release-notes.md) |
| [condition_pushdown_for_subquery=on](subquery-optimizations/condition-pushdown-into-in-subqueries.md) | [MariaDB 10.4.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1040-release-notes.md) |
| condition_pushdown_from_having=on | [MariaDB 10.4.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1043-release-notes.md) |
| [cset_narrowing=on/off](charset-narrowing-optimization.md) | [MariaDB 10.6.16](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-16-release-notes.md), [MariaDB 10.11.6](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-6-release-notes.md), [MariaDB 11.0.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes.md), [MariaDB 11.1.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes.md) and [MariaDB 11.2.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes.md) |
| [derived_merge=on](optimizations-for-derived-tables/derived-table-merge-optimization.md) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| [derived_with_keys](optimizations-for-derived-tables/derived-table-with-key-optimization.md)=on | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| default | [MariaDB 5.1](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md) |
| duplicateweedout=on | [MariaDB 11.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md) |
| engine_condition_pushdown=off | [MariaDB 5.5](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) (deprecated in [MariaDB 10.1](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1010.md), removed in [MariaDB 11.3](../../../../../release-notes/mariadb-community-server/what-is-mariadb-113.md)) |
| [exists_to_in=on](subquery-optimizations/exists-to-in-optimization.md) | [MariaDB 10.0](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) |
| [extended_keys=on](../../../../ref/mariadb-internals/mariadb-internals-documentation-query-optimizer/extended-keys.md) | [MariaDB 5.5.21](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5521-release-notes.md) |
| [firstmatch=on](optimization-strategies/firstmatch-strategy.md) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| [index_condition_pushdown=on](index-condition-pushdown.md) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| [hash_join_cardinality=off](hash_join_cardinality-optimizer_switch-flag.md) | [MariaDB 10.6.13](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-13-release-notes.md) ([MDEV-30812](https://jira.mariadb.org/browse/MDEV-30812)) |
| index_merge=on | [MariaDB 5.1](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md) |
| index_merge_intersection=on | [MariaDB 5.1](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md) |
| [index_merge_sort_intersection=off](index_merge-sort_intersection.md) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| index_merge_sort_union=on | [MariaDB 5.1](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md) |
| index_merge_union=on# | [MariaDB 5.1](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md) |
| [in_to_exists=on](subquery-optimizations/non-semi-join-subquery-optimizations.md#the-in-to-exists-transformation) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| [join_cache_bka=on](../../../../ref/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms.md) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| [join_cache_hashed=on](../../../../ref/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms.md) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| [join_cache_incremental=on](../../../../ref/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms.md) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| [loosescan=on](optimization-strategies/loosescan-strategy.md) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| materialization=on ([semi-join](optimization-strategies/semi-join-materialization-strategy.md), [non-semi-join](subquery-optimizations/non-semi-join-subquery-optimizations.md#materialization-for-non-correlated-in-subqueries)) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| [mrr=off](../mariadb-internal-optimizations/multi-range-read-optimization.md) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| [mrr_cost_based=off](../mariadb-internal-optimizations/multi-range-read-optimization.md) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| [mrr_sort_keys=off](../mariadb-internal-optimizations/multi-range-read-optimization.md) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| [not_null_range_scan=off](not_null_range_scan-optimization.md) | [MariaDB 10.5](../../../../../release-notes/mariadb-community-server/what-is-mariadb-105.md) |
| [optimize_join_buffer_size=on](../../../../ref/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms.md) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| [orderby_uses_equalities=on](optimization-strategies/improvements-to-order-by.md) | [MariaDB 10.1.15](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10115-release-notes.md) |
| [outer_join_with_cache=on](../../../../ref/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms.md) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| [partial_match_rowid_merge=on](subquery-optimizations/non-semi-join-subquery-optimizations.md) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| [partial_match_table_scan=on](subquery-optimizations/non-semi-join-subquery-optimizations.md) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| [rowid_filter=on](rowid-filtering-optimization.md) | [MariaDB 10.4.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-1043-release-notes.md) |
| [sargable_casefold=on](sargable-upper.md) | [MariaDB 11.3.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md) |
| [semijoin=on](subquery-optimizations/semi-join-subquery-optimizations.md) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| [semijoin_with_cache=on](../../../../ref/mariadb-internals/mariadb-internals-documentation-query-optimizer/block-based-join-algorithms.md) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| [split_materialized=on](optimizations-for-derived-tables/lateral-derived-optimization.md)[[1](#_note-0)] | [MariaDB 10.3.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1034-release-notes.md) |
| [subquery_cache=on](subquery-optimizations/subquery-cache.md) | [MariaDB 5.3](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md) |
| [table_elimination=on](table-elimination/table-elimination-user-interface.md) | [MariaDB 5.1](../../../../../release-notes/mariadb-community-server/old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md) |



1. [↑](#_ref-0) replaced [split_grouping_derived](https://github.com/MariaDB/server/commit/b14e2b044b), introduced in [MariaDB 10.3.1](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-1031-release-notes.md)


## Defaults



| From version | Default optimizer_switch setting |
| --- | --- |
| From version | Default optimizer_switch setting |
| [MariaDB 11.8.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-8-series/mariadb-11-8-0-release-notes.md) | index_merge=on, index_merge_union=on, index_merge_sort_union=on, index_merge_intersection=on, index_merge_sort_intersection=off, index_condition_pushdown=on, derived_merge=on, derived_with_keys=on, firstmatch=on, loosescan=on, duplicateweedout=on, materialization=on, in_to_exists=on, semijoin=on, partial_match_rowid_merge=on, partial_match_table_scan=on, subquery_cache=on, mrr=off, mrr_cost_based=off, mrr_sort_keys=off, outer_join_with_cache=on, semijoin_with_cache=on, join_cache_incremental=on, join_cache_hashed=on, join_cache_bka=on, optimize_join_buffer_size=on, table_elimination=on, extended_keys=on, exists_to_in=on, orderby_uses_equalities=on, condition_pushdown_for_derived=on, split_materialized=on, condition_pushdown_for_subquery=on, rowid_filter=on, condition_pushdown_from_having=on, not_null_range_scan=off, hash_join_cardinality=on, cset_narrowing=on, sargable_casefold=on |
| [MariaDB 11.7.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-7-rolling-releases/mariadb-11-7-0-release-notes.md) | index_merge=on, index_merge_union=on, index_merge_sort_union=on, index_merge_intersection=on, index_merge_sort_intersection=off, index_condition_pushdown=on, derived_merge=on, derived_with_keys=on, firstmatch=on, loosescan=on, materialization=on, in_to_exists=on, semijoin=on, partial_match_rowid_merge=on, partial_match_table_scan=on, subquery_cache=on, mrr=off, mrr_cost_based=off, mrr_sort_keys=off, outer_join_with_cache=on, semijoin_with_cache=on, join_cache_incremental=on, join_cache_hashed=on, join_cache_bka=on, optimize_join_buffer_size=on, table_elimination=on, extended_keys=on, exists_to_in=on, orderby_uses_equalities=on, condition_pushdown_for_derived=on, split_materialized=on, condition_pushdown_for_subquery=on, rowid_filter=on, condition_pushdown_from_having=on, not_null_range_scan=off, hash_join_cardinality=on, cset_narrowing=on, sargable_casefold=on |
| [MariaDB 11.3.1](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-1-release-notes.md) | index_merge=on, index_merge_union=on, index_merge_sort_union=on, index_merge_intersection=on, index_merge_sort_intersection=off, index_condition_pushdown=on, derived_merge=on, derived_with_keys=on, firstmatch=on, loosescan=on, materialization=on, in_to_exists=on, semijoin=on, partial_match_rowid_merge=on, partial_match_table_scan=on, subquery_cache=on, mrr=off, mrr_cost_based=off, mrr_sort_keys=off, outer_join_with_cache=on, semijoin_with_cache=on, join_cache_incremental=on, join_cache_hashed=on, join_cache_bka=on, optimize_join_buffer_size=on, table_elimination=on, extended_keys=on, exists_to_in=on, orderby_uses_equalities=on, condition_pushdown_for_derived=on, split_materialized=on, condition_pushdown_for_subquery=on, rowid_filter=on, condition_pushdown_from_having=on, not_null_range_scan=off, hash_join_cardinality=on, cset_narrowing=off, sargable_casefold=on |
| [MariaDB 10.6.16](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-16-release-notes.md), [MariaDB 10.11.6](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-6-release-notes.md), [MariaDB 11.0.4](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes.md), [MariaDB 11.1.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes.md) and [MariaDB 11.2.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes.md) | index_merge=on, index_merge_union=on, index_merge_sort_union=on, index_merge_intersection=on, index_merge_sort_intersection=off, index_condition_pushdown=on, derived_merge=on, derived_with_keys=on, firstmatch=on, loosescan=on, materialization=on, in_to_exists=on, semijoin=on, partial_match_rowid_merge=on, partial_match_table_scan=on, subquery_cache=on, mrr=off, mrr_cost_based=off, mrr_sort_keys=off, outer_join_with_cache=on, semijoin_with_cache=on, join_cache_incremental=on, join_cache_hashed=on, join_cache_bka=on, optimize_join_buffer_size=on, table_elimination=on, extended_keys=on, exists_to_in=on, orderby_uses_equalities=on, condition_pushdown_for_derived=on, split_materialized=on, condition_pushdown_for_subquery=on, rowid_filter=on, condition_pushdown_from_having=on, not_null_range_scan=off, hash_join_cardinality=on, cset_narrowing=off |
| [MariaDB 11.0.2](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-11-0-series/mariadb-11-0-2-release-notes.md) | index_merge=on, index_merge_union=on, index_merge_sort_union=on, index_merge_intersection=on, index_merge_sort_intersection=off, engine_condition_pushdown=off, index_condition_pushdown=on, derived_merge=on, derived_with_keys=on, firstmatch=on, loosescan=on, materialization=on, in_to_exists=on, semijoin=on, partial_match_rowid_merge=on, partial_match_table_scan=on, subquery_cache=on, mrr=off, mrr_cost_based=off, mrr_sort_keys=off, outer_join_with_cache=on, semijoin_with_cache=on, join_cache_incremental=on, join_cache_hashed=on, join_cache_bka=on, optimize_join_buffer_size=on, table_elimination=on, extended_keys=on, exists_to_in=on, orderby_uses_equalities=on, condition_pushdown_for_derived=on, split_materialized=on, condition_pushdown_for_subquery=on, rowid_filter=on,condition_pushdown_from_having=on, not_null_range_scan=off, hash_join_cardinality=on |
| [MariaDB 10.6.13](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-13-release-notes.md), [MariaDB 10.11.3](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-3-release-notes.md) | index_merge=on, index_merge_union=on, index_merge_sort_union=on, index_merge_intersection=on, index_merge_sort_intersection=off, engine_condition_pushdown=off, index_condition_pushdown=on, derived_merge=on, derived_with_keys=on, firstmatch=on, loosescan=on, materialization=on, in_to_exists=on, semijoin=on, partial_match_rowid_merge=on, partial_match_table_scan=on, subquery_cache=on, mrr=off, mrr_cost_based=off, mrr_sort_keys=off, outer_join_with_cache=on, semijoin_with_cache=on, join_cache_incremental=on, join_cache_hashed=on, join_cache_bka=on, optimize_join_buffer_size=on, table_elimination=on, extended_keys=on, exists_to_in=on, orderby_uses_equalities=on, condition_pushdown_for_derived=on, split_materialized=on, condition_pushdown_for_subquery=on, rowid_filter=on,condition_pushdown_from_having=on, not_null_range_scan=off, hash_join_cardinality=off |
| [MariaDB 10.5.0](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-1050-release-notes.md) | index_merge=on, index_merge_union=on, index_merge_sort_union=on, index_merge_intersection=on, index_merge_sort_intersection=off, engine_condition_pushdown=off, index_condition_pushdown=on, derived_merge=on, derived_with_keys=on, firstmatch=on, loosescan=on, materialization=on, in_to_exists=on, semijoin=on, partial_match_rowid_merge=on, partial_match_table_scan=on, subquery_cache=on, mrr=off, mrr_cost_based=off, mrr_sort_keys=off, outer_join_with_cache=on, semijoin_with_cache=on, join_cache_incremental=on, join_cache_hashed=on, join_cache_bka=on, optimize_join_buffer_size=on, table_elimination=on, extended_keys=on, exists_to_in=on, orderby_uses_equalities=on, condition_pushdown_for_derived=on, split_materialized=on, condition_pushdown_for_subquery=on, rowid_filter=on,condition_pushdown_from_having=on, not_null_range_scan=off |



## See Also


* [Quickly finding optimizer_switch values that are on or off](../../../../ref/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/sys-schema/sys-schema-stored-procedures/optimizer_switch-helper-functions.md)
* [The optimizer converts certain big IN predicates into IN subqueries](subquery-optimizations/conversion-of-big-in-predicates-into-subqueries.md)
* [optimizer_adjust_secondary_key_cost](optimizer_adjust_secondary_key_costs.md)
* [Optimizer hints in SELECT](../../../../ref/sql-statements-and-structure/sql-statements/data-manipulation/selecting-data/optimizer-hints.md)

