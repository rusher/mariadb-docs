
# The maria/5.3-gis tree on Launchpad.

**Note:** This page is obsolete. The information is old, outdated, or otherwise currently incorrect. We are keeping the page for historical reasons only. **Do not** rely on the information in this article.


The maria/5.3-gis tree on Launchpad.


Basic information about the existing spatial features can be found in the
[Geographic Features](README.md) section of the Knowlegebase. The
[Spatial Extensions page of the MySQL manual](https://dev.mysql.com/doc/refman/5.6/en/spatial-extensions.html)
also applies to MariaDB.


The [maria/5.3-gis tree](https://code.launchpad.net/~maria-captains/maria/5.3-gis), contains recent code improving the spatial functionality in MariaDB.


MySQL operates on spatial data based on the OpenGIS standards, particularly the
[OpenGIS SFS](https://www.opengeospatial.org/standards/sfs) (Simple feature
access, SQL option).


Initial support was based on version 05-134 of the standard. MariaDB implements
a subset of the 'SQL with Geometry Types' environment proposed by the OGC. And
the SQL environment was extended with a set of geometry types.


Now we have started to implement the newer 06-104r4 standard.


MariaDB supports spatial extensions to operate on spatial features.
These features are available for Aria, MyISAM, InnoDB, NDB, and ARCHIVE tables.


For spatial columns, Aria and MyISAM supports both SPATIAL and non-SPATIAL
indexes. Other storage engines support non-SPATIAL indexes.


The most recent changes in the code are aimed at meeting the OpenGIS
requirements. One thing missing in the present version is that the functions
which check spatial relations don't consider the actual shape of an object,
instead they operate only on their bounding rectangles. These legacy functions
have been left as they are, and new, properly-working functions are named with
an '`ST_`' prefix, in accordance with the last OpenGIS requirements. Also,
operations over geometry features were added.


The list of new functions:


Spatial operators. They produce new geometries.



| Name | Description |
| --- | --- |
| Name | Description |
| ST_UNION(A, B) | union of A and B |
| ST_INTERSECTION(A, B) | intersection of A and B |
| ST_SYMDIFFERENCE(A, B) | symdifference, notintersecting parts of A and B |
| ST_BUFFER(A, radius) | returns the shape of the area that lies in 'radius' distance from the shape A. |

Predicates, return boolean result of the relationship

| Name | Description |
| --- | --- |
| Name | Description |
| ST_INTERSECTS(A, B) | if A and B have an intersection |
| ST_CROSSES(A, B) | if A and B cross |
| ST_EQUAL(A, B) | if A nad B are equal |
| ST_WITHIN(A, B) | if A lies within B |
| ST_CONTAINS(A,B) | if B lies within A |
| ST_DISJOINT(A,B) | if A and B have no intersection |
| ST_TOUCHES(A,B) | if A touches B |



Geometry metadata views:



| GEOMETRY_COLUMNS | fields: |  |  |  |  |  |  |  |  |  |  |  | SPATIAL_REF_SYS | fields: |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GEOMETRY_COLUMNS | this table describes the available feature tables and their Geometry properties |
| fields: | F_TABLE_CATALOG VARCHAR(200) NOT NULL, |
|  | F_TABLE_SCHEMA VARCHAR(200) NOT NULL, |
|  | F_TABLE_NAME VARCHAR(200) NOT NULL, |
|  | F_GEOMETRY_COLUMN VARCHAR(200) NOT NULL, |
|  | G_TABLE_CATALOG VARCHAR(200) NOT NULL, |
|  | G_TABLE_SCHEMA VARCHAR(200) NOT NULL, |
|  | G_TABLE_NAME VARCHAR(200) NOT NULL, |
|  | STORAGE_TYPE INTEGER, |
|  | GEOMETRY_TYPE INTEGER, |
|  | COORD_DIMENSION INTEGER, |
|  | MAX_PPR INTEGER, |
|  | SRID INTEGER NOT NULL |
|  |  |
|  |  |
| SPATIAL_REF_SYS | this table describes the coordinate system and transformations for Geometry |
| fields: | SRID INTEGER NOT NULL PRIMARY KEY, |
|  | AUTH_NAME VARCHAR(200), |
|  | AUTH_SRID INTEGER, |
|  | SRTEXT TEXT |




CC BY-SA / Gnu FDL

