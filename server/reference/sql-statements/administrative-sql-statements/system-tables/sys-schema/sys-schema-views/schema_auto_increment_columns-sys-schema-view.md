# schema\_auto\_increment\_columns Sys Schema View

**MariaDB starting with** [**10.6**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106)

The [Sys Schema](../) was introduced in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106)

## Description

Information about [AUTO\_INCREMENT](../../../../../data-types/auto_increment.md) columns, sorted by descending usage ratio and maximum column value. Does not include columns in the mysql, sys, information\_schema and performance\_schema schemas.

Contains the following columns:

| Column                 | Description                                                                                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Column                 | Description                                                                                                                                            |
| table\_schema          | Schema name containing the table with the auto\_increment attribute.                                                                                   |
| table\_name            | Table containing the auto\_increment attribute.                                                                                                        |
| column\_name           | Name of the column containing the auto\_increment attribute.                                                                                           |
| data\_type             | [Data type](../../../../../data-types/) of the auto\_increment column, for example [tinyint](../../../../../data-types/numeric-data-types/tinyint.md). |
| column\_type           | [Data type](../../../../../data-types/) of the auto\_increment column, plus additional information for example tinyint(3) unsigned.                    |
| is\_signed             | 1 if the column is [signed](../../../../../data-types/numeric-data-types/numeric-data-type-overview.md#signed-unsigned-and-zerofill),0 if not.         |
| is\_unsigned           | 1 if the column is unsigned,0 if it is.                                                                                                                |
| max\_value             | Maximum possible value for the column, for example 255 for an unsigned tinyint.                                                                        |
| auto\_increment        | Current auto\_increment value for the column.                                                                                                          |
| auto\_increment\_ratio | Ratio of used to maximum value for the auto\_increment column.                                                                                         |

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

CC BY-SA / Gnu FDL
