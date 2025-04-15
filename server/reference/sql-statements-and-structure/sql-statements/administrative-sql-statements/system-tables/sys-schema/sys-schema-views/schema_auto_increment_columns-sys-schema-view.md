
# schema_auto_increment_columns Sys Schema View


##### MariaDB starting with [10.6](../../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md)
The [Sys Schema](sys-schema-views-host_summary_by_statement_latency-and-xhost_summary_by_sta.md) was introduced in [MariaDB 10.6](../../../../../../../../release-notes/mariadb-community-server/what-is-mariadb-106.md)


## Description


Information about [AUTO_INCREMENT](../../../../../../storage-engines/innodb/auto_increment-handling-in-innodb.md) columns, sorted by descending usage ratio and maximum column value. Does not include columns in the mysql, sys, information_schema and performance_schema schemas.


Contains the following columns:



| Column | Description |
| --- | --- |
| Column | Description |
| table_schema | Schema name containing the table with the auto_increment attribute. |
| table_name | Table containing the auto_increment attribute. |
| column_name | Name of the column containing the auto_increment attribute. |
| data_type | [Data type](../../../../../../data-types/data-types-overview/data-types-subcategory/data-types-dec.md) of the auto_increment column, for example [tinyint](../../../../../../data-types/data-types-numeric-data-types/tinyint.md). |
| column_type | [Data type](../../../../../../data-types/data-types-overview/data-types-subcategory/data-types-dec.md) of the auto_increment column, plus additional information for example tinyint(3) unsigned. |
| is_signed | 1 if the column is [signed](../../../../../../data-types/data-types-numeric-data-types/numeric-data-type-overview.md#signed-unsigned-and-zerofill),0 if not. |
| is_unsigned | 1 if the column is unsigned,0 if it is. |
| max_value | Maximum possible value for the column, for example 255 for an unsigned tinyint. |
| auto_increment | Current auto_increment value for the column. |
| auto_increment_ratio | Ratio of used to maximum value for the auto_increment column. |



## Example


```
CREATE OR REPLACE TABLE animals (
    id TINYINT NOT NULL AUTO_INCREMENT,
    name CHAR(30) NOT NULL,
    PRIMARY KEY (id)
);

 INSERT INTO animals (name) VALUES
    ('dog'),('cat'),('penguin'),
    ('fox'),('whale'),('ostrich');

SELECT * FROM sys.schema_auto_increment_columns\G
*************************** 1. row ***************************
        table_schema: test
          table_name: animals
         column_name: id
           data_type: tinyint
         column_type: tinyint(4)
           is_signed: 1
         is_unsigned: 0
           max_value: 127
      auto_increment: 7
auto_increment_ratio: 0.0551
```
