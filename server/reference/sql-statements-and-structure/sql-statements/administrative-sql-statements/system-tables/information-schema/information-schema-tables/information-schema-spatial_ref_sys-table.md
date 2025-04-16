
# Information Schema SPATIAL_REF_SYS Table

## Description


The [Information Schema](../../../../../../mariadb-internals/information-schema-plugins-show-and-flush-statements.md) `SPATIAL_REF_SYS` table stores information on each spatial reference system used in the database.


It contains the following columns:



| Column | Type | Null | Description |
| --- | --- | --- | --- |
| Column | Type | Null | Description |
| SRID | smallint(5) | NO | An integer value that uniquely identifies each Spatial Reference System within a database. |
| AUTH_NAME | varchar(512) | NO | The name of the standard or standards body that is being cited for this reference system. |
| AUTH_SRID | smallint(5) | NO | The numeric ID of the coordinate system in the above authority's catalog. |
| SRTEXT | varchar(2048) | NO | The [Well-known Text Representation](../../../../../geographic-geometric-features/wkt/wkt-geomcollfromtext.md) of the Spatial Reference System. |



Note: See [MDEV-7540](https://jira.mariadb.org/browse/MDEV-7540).


## See Aso


* [information_schema.GEOMETRY_COLUMNS](information-schema-geometry_columns-table.md) table.

