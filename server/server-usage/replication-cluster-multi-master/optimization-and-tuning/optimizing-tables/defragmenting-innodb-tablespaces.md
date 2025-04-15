# Defragmenting InnoDB Tablespaces

#

# Overview

When rows are deleted from an [InnoDB](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-troubleshooting.md) table, the rows are simply marked as deleted and not physically deleted. The free space is not returned to the operating system for re-use.

The purge thread will physically delete index keys and rows, but the free space introduced is still not returned to operating system. This can lead to gaps in the pages. If you have variable length rows, new rows may be larger than old rows and cannot make use of the available space.

You can run [OPTIMIZE TABLE](optimize-table.md) or [ALTER TABLE <table> ENGINE=InnoDB](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md) to reconstruct the table. Unfortunately running `OPTIMIZE TABLE` against an InnoDB table stored in the shared table-space file `ibdata1` does two things:

* Makes the table’s data and indexes contiguous inside `ibdata1`.
* Increases the size of `ibdata1` because the contiguous data and index pages are appended to `ibdata1`.

#

# InnoDB Defragmentation

The feature described below has been deprecated in [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-110) and was removed in [MariaDB 11.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/release-notes-mariadb-11-1-series/mariadb-11-1-0-release-notes). See [MDEV-30544](https://jira.mariadb.org/browse/MDEV-30544) and [MDEV-30545](https://jira.mariadb.org/browse/MDEV-30545).

[MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-1011) merged Facebook's defragmentation code prepared for MariaDB by Matt, Seong Uck Lee from Kakao. The only major difference to Facebook's code and Matt’s patch is that MariaDB does not introduce new literals to SQL and makes no changes to the server code. Instead, [OPTIMIZE TABLE](optimize-table.md) is used and all code changes are inside the InnoDB/XtraDB storage engines.

The behaviour of `OPTIMIZE TABLE` is unchanged by default, and to enable this new feature, you need to set the [innodb_defragment](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment) system variable to `1`.

```
[mysqld]
...
innodb-defragment=1
```

No new tables are created and there is no need to copy data from old tables to new tables. Instead, this feature loads `n` pages (determined by [innodb-defragment-n-pages](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_n_pages)) and tries to move records so that pages would be full of records and then frees pages that are fully empty after the operation.

Note that tablespace files (including ibdata1) will not shrink as the result of defragmentation, but one will get better memory utilization in the InnoDB buffer pool as there are fewer data pages in use.

A number of new system and status variables for controlling and monitoring the feature are introduced.

#

## System Variables

* [innodb_defragment](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment): Enable InnoDB defragmentation.
* [innodb_defragment_n_pages](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_n_pages): Number of pages considered at once when merging multiple pages to defragment.
* [innodb_defragment_stats_accuracy](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_stats_accuracy): Number of defragment stats changes there are before the stats are written to persistent storage.
* [innodb_defragment_fill_factor_n_recs](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_fill_factor_n_recs): Number of records of space that defragmentation should leave on the page.
* [innodb_defragment_fill_factor](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_fill_factor): Indicates how full defragmentation should fill a page.
* [innodb_defragment_frequency](../../../../reference/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_frequency): Maximum times per second for defragmenting a single index.

#

## Status Variables

* [Innodb_defragment_compression_failures](../system-variables/innodb-status-variables.md#innodb_defragment_compression_failures): Number of defragment re-compression failures
* [Innodb_defragment_failures](../system-variables/innodb-status-variables.md#innodb_defragment_failures): Number of defragment failures.
* [Innodb_defragment_count](../system-variables/innodb-status-variables.md#innodb_defragment_count): Number of defragment operations.

#

# Example

```
set @@global.innodb_file_per_table = 1;
set @@global.innodb_defragment_n_pages = 32;
set @@global.innodb_defragment_fill_factor = 0.95;
CREATE TABLE tb_defragment (
pk1 bigint(20) NOT NULL,
pk2 bigint(20) NOT NULL,
fd4 text,
fd5 varchar(50) DEFAULT NULL,
PRIMARY KEY (pk1),
KEY ix1 (pk2)
) ENGINE=InnoDB;

delimiter //
create procedure innodb_insert_proc (repeat_count int)
begin
 declare current_num int;
 set current_num = 0;
 while current_num < repeat_count do
 INSERT INTO tb_defragment VALUES (current_num, 1, REPEAT('Abcdefg', 20), REPEAT('12345',5));
 INSERT INTO tb_defragment VALUES (current_num+1, 2, REPEAT('HIJKLM', 20), REPEAT('67890',5));
 INSERT INTO tb_defragment VALUES (current_num+2, 3, REPEAT('HIJKLM', 20), REPEAT('67890',5));
 INSERT INTO tb_defragment VALUES (current_num+3, 4, REPEAT('HIJKLM', 20), REPEAT('67890',5));
 set current_num = current_num + 4;
 end while;
end//
delimiter ;
commit;

set autocommit=0;
call innodb_insert_proc(50000);
commit;
set autocommit=1;
```

After these CREATE and INSERT operations, the following information can be seen from the INFORMATION SCHEMA:

```
select count(*) as Value from information_schema.innodb_buffer_page 
 where table_name like '%tb_defragment%' and index_name = 'PRIMARY';
Value
313

select count(*) as Value from information_schema.innodb_buffer_page 
 where table_name like '%tb_defragment%' and index_name = 'ix1';
Value
72

select count(stat_value) from mysql.innodb_index_stats 
 where table_name like '%tb_defragment%' and stat_name in ('n_pages_freed');
count(stat_value)
0

select count(stat_value) from mysql.innodb_index_stats 
 where table_name like '%tb_defragment%' and stat_name in ('n_page_split');
count(stat_value)
0

select count(stat_value) from mysql.innodb_index_stats 
 where table_name like '%tb_defragment%' and stat_name in ('n_leaf_pages_defrag');
count(stat_value)
0

SELECT table_name, data_free/1024/1024 AS data_free_MB, table_rows FROM information_schema.tables 
 WHERE engine LIKE 'InnoDB' and table_name like '%tb_defragment%';
table_name data_free_MB table_rows
tb_defragment 4.00000000 50051

SELECT table_name, index_name, sum(number_records), sum(data_size) FROM information_schema.innodb_buffer_page 
 where table_name like '%tb_defragment%' and index_name like 'PRIMARY';
table_name index_name sum(number_records) sum(data_size)
`test`.`tb_defragment` PRIMARY 25873 4739939

SELECT table_name, index_name, sum(number_records), sum(data_size) FROM information_schema.innodb_buffer_page 
 where table_name like '%tb_defragment%' and index_name like 'ix1';
table_name index_name sum(number_records) sum(data_size)
`test`.`tb_defragment` ix1 50071 1051775
```

Deleting three-quarters of the records, leaving gaps, and then optimizing:

```
delete from tb_defragment where pk2 between 2 and 4;

optimize table tb_defragment;
Table	Op	Msg_type	Msg_text
test.tb_defragment	optimize	status	OK
show status like '%innodb_def%';
Variable_name	Value
Innodb_defragment_compression_failures	0
Innodb_defragment_failures	1
Innodb_defragment_count	4
```

Now some pages have been freed, and some merged:

```
select count(*) as Value from information_schema.innodb_buffer_page 
 where table_name like '%tb_defragment%' and index_name = 'PRIMARY';
Value
0

select count(*) as Value from information_schema.innodb_buffer_page 
 where table_name like '%tb_defragment%' and index_name = 'ix1';
Value
0

select count(stat_value) from mysql.innodb_index_stats 
 where table_name like '%tb_defragment%' and stat_name in ('n_pages_freed');
count(stat_value)
2

select count(stat_value) from mysql.innodb_index_stats 
 where table_name like '%tb_defragment%' and stat_name in ('n_page_split');
count(stat_value)
2

select count(stat_value) from mysql.innodb_index_stats 
 where table_name like '%tb_defragment%' and stat_name in ('n_leaf_pages_defrag');
count(stat_value)
2

SELECT table_name, data_free/1024/1024 AS data_free_MB, table_rows FROM information_schema.tables 
 WHERE engine LIKE 'InnoDB';
table_name data_free_MB table_rows
innodb_index_stats 0.00000000 8
innodb_table_stats 0.00000000 0
tb_defragment 4.00000000 12431

SELECT table_name, index_name, sum(number_records), sum(data_size) FROM information_schema.innodb_buffer_page 
 where table_name like '%tb_defragment%' and index_name like 'PRIMARY';
table_name index_name sum(number_records) sum(data_size)
`test`.`tb_defragment` PRIMARY 690 102145

SELECT table_name, index_name, sum(number_records), sum(data_size) FROM information_schema.innodb_buffer_page 
 where table_name like '%tb_defragment%' and index_name like 'ix1';
table_name index_name sum(number_records) sum(data_size)
`test`.`tb_defragment` ix1 5295 111263
```

See [Defragmenting unused space on InnoDB tablespace](https://blog.mariadb.org/defragmenting-unused-space-on-innodb-tablespace/) on the Mariadb.org blog for more details.