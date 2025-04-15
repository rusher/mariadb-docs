
# optimizer_adjust_secondary_key_costs

#### `<code>optimizer_adjust_secondary_key_costs</code>`


* Description: Gives the user the ability to affect how the costs for secondary keys using `<code>ref</code>` are calculated in the few cases when [MariaDB 10.6](../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md) up to [MariaDB 10.11](../../../../../release-notes/mariadb-community-server/what-is-mariadb-1011.md) makes a sub-optimal choice when optimizing `<code>ref</code>` access, either for key lookups or `<code>GROUP BY</code>`. `<code>ref</code>`, as used by [EXPLAIN](../../../../../general-resources/learning-and-training/training-and-tutorials/advanced-mariadb-articles/development-articles/outdated-pages/explain-formatjson-in-mysql.md), means that the optimizer is using key-lookup on one value to find the matching rows from a table. Unused from [MariaDB 11.0](../../../../../release-notes/mariadb-community-server/what-is-mariadb-110.md). In [MariaDB 10.6.18](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-18-release-notes.md) the variable was changed from a number to a set of strings and `<code>disable_forced_index_in_group_by</code>` (value 4) was added.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `<code>set</code>`
* Default Value: `<code>fix_card_multiplier</code>`
* Range: `<code>0</code>` to `<code>63</code>` or any combination of `<code>adjust_secondary_key_cost</code>`, `<code>disable_max_seek</code>` or `<code>disable_forced_index_in_group_by</code>`, `<code>fix_innodb_cardinality</code>`,`<code>fix_reuse_range_for_ref</code>`, `<code>fix_card_multiplier</code>`
* Introduced: [MariaDB 10.6.17](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-17-release-notes.md), [MariaDB 10.11.7](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-11-series/mariadb-10-11-7-release-notes.md)






##### MariaDB starting with [11.0](../../../../../release-notes/mariadb-community-server/what-is-mariadb-110.md)
`<code>optimizer_adjust_secondary_key_costs</code>` will be obsolete starting from [MariaDB 11.0](../../../../../release-notes/mariadb-community-server/what-is-mariadb-110.md) as the new optimizer in 11.0 does not have max_seek optimization and is already using cost based choices for index usage with GROUP BY.


The value for `<code>optimizer_adjust_secondary_key_costs</code>` is one of more of the following:



| Value | Version added | Old behavior | Change when variable is used |
| --- | --- | --- | --- |
| Value | Version added | Old behavior | Change when variable is used |
| adjust_secondary_key_cost | [10.6.17](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-17-release-notes.md) | Limit ref costs by max_seeks | The secondary key costs for ref are updated to be at least five times the clustered primary key costs if a clustered primary key exists |
| disable_max_seek | [10.6.17](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-17-release-notes.md) | ref cost on secondary keys is limited to max_seek = min('number of expected rows'/ 10, scan_time*3) | Disable 'max_seek' optimization and do a slight adjustment of filter cost |
| disable_forced_index_in_group_by | [10.6.18](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-18-release-notes.md) | Use a rule-based choice when deciding to use an index to resolve GROUP BY | The choice is now cost based |
| fix_innodb_cardinality | [10.6.19](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-19-release-notes.md) | By default InnoDB doubles the cardinality for indexes in an effort to force index usage over table scans. This can cause the optimizer to create sub-optimal plans for ranges or index entries that cover a big part of the table. | Using this option removes the doubling of cardinality in InnoDB. fix_innodb_cardinality is recommended to be used only as a server startup option, as it is enabled for a table at first usage. See [MDEV-34664](https://jira.mariadb.org/browse/MDEV-34664) for details. |
| fix_reuse_range_for_ref | [10.6.20](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-20-release-notes.md) | Number of estimated rows for 'ref' did not always match costs from range optimizer | Use cost from range optimizer for 'ref' if all used key parts are constants. The old code did not always do this |
| fix_card_multiplier | [10.6.20](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-6-series/mariadb-10-6-20-release-notes.md) | Index selectivity can be bigger than 1.0 if index statistics is not up to date. Not on by default. | Ensure that the calculated index selectivity is never bigger than 1.0. Having index selectivity bigger than 1.0 causes MariaDB to believe that there is more rows in the table than in reality, which can cause wrong plans. This option is on by default. |



One can set all options with:


```
set @@optimizer_adjust_secondary_key_costs='all';
```

## Explanations of the old behavior in MariaDB 10.x


The reason for the max_seek optimization was originally to ensure that MariaDB would use a key instead of a table scan. This works well for a lot of queries, but can cause problems when a table scan is a better choice, such as when one would have to scan more than 1/4 of the rows in the table (in which case a table scan is better).


## See Also


* The [optimizer_switch](optimizer-switch.md) system variable.

