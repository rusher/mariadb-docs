# mysql.column_stats Table

The `mysql.column_stats` table is one of three tables storing data used for [Engine-independent table statistics](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md). The others are [mysql.table_stats](/en/mysqltable_stats-table/) and [mysql.index_stats](/en/mysqlindex_stats-table/).

It is populated when the [ANALYZE TABLE](../../../table-statements/analyze-table.md) statement is run, although not by default. See [Collecting Statistics with the ANALYZE TABLE Statement](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md#collecting-statistics-with-the-analyze-table-statement) for details.

Note that statistics for blob and text columns are not collected. If explicitly specified, a warning is returned.

It is possible to manually update the table and, unlike most system tables, there are some scenarios where this could be useful. See [Manual updates to statistics tables](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md#manual-updates-to-statistics-tables) for details.

This table uses the [Aria](../../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/aria-encryption/aria-enabling-encryption.md) storage engine.

The `mysql.column_stats` table contains the following fields:

| Field | Type | Null | Key | Default | Description |
| --- | --- | --- | --- | --- | --- |
| Field | Type | Null | Key | Default | Description |
| db_name | varchar(64) | NO | PRI | NULL | Database the table is in. |
| table_name | varchar(64) | NO | PRI | NULL | Table name. |
| column_name | varchar(64) | NO | PRI | NULL | Name of the column. |
| min_value | varchar(255) | YES | | NULL | Minimum value in the table (in text form). |
| max_value | varchar(255) | YES | | NULL | Maximum value in the table (in text form). |
| nulls_ratio | decimal(12,4) | YES | | NULL | Fraction of NULL values (0- no NULLs, 0.5 - half values are NULLs, 1 - all values are NULLs). |
| avg_length | decimal(12,4) | YES | | NULL | Average length of column value, in bytes. Counted as if one ran SELECT AVG(LENGTH(col)). This doesn't count NULL bytes, assumes endspace removal for CHAR(n), etc. |
| avg_frequency | decimal(12,4) | YES | | NULL | Average number of records with the same value |
| hist_size | tinyint(3) unsigned | YES | | NULL | Histogram size in bytes, from 0-255, or, from [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-108), number of buckets if the histogram type is JSON_HB. |
| hist_type | enum('SINGLE_PREC_HB', 'DOUBLE_PREC_HB') (>= [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-108))enum('SINGLE_PREC_HB', 'DOUBLE_PREC_HB','JSON_HB') (<= [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-107)) | YES | | NULL | Histogram type. See the [histogram_type](../../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#histogram_type) system variable. |
| histogram | blob (>= [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-107))varbinary(255) (<=[MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server/what-is-mariadb-107)) | YES | | NULL | |