
# GIS features in 5.3.3

Basic information about the existing spatial features can be found in the
[Geographic Features](README.md) section of the Knowlegebase. The
[Spatial Extensions page of the MySQL manual](https://dev.mysql.com/doc/refman/5.6/en/spatial-extensions.html)
also applies to MariaDB.


The [MariaDB 5.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/mariadb-533-release-notes) release , contains code improving
the spatial functionality in MariaDB.


MySQL operates on spatial data based on the OpenGIS standards, particularly the
[OpenGIS SFS](https://www.opengeospatial.org/standards/sfs) (Simple feature
access, SQL option).


Initial support was based on version 05-134 of the standard. MariaDB implements
a subset of the 'SQL with Geometry Types' environment proposed by the OGC. And
the SQL environment was extended with a set of geometry types.


MariaDB supports spatial extensions to operate on spatial features.
These features are available for [Aria](../../storage-engines/aria/README.md), [MyISAM](../../storage-engines/myisam-storage-engine/README.md), [InnoDB](../../storage-engines/innodb/README.md), NDB, and [ARCHIVE](../../storage-engines/archive/README.md) tables.


For spatial columns, Aria and MyISAM supports both [SPATIAL](spatial-index.md) and non-SPATIAL
indexes. Other storage engines support non-SPATIAL indexes.


The most recent changes in the code are aimed at meeting the OpenGIS
requirements. One thing missed in previous versions is that the functions
which check spatial relations didn't consider the actual shape of an object,
instead they operate only on their bounding rectangles. These legacy functions
have been left as they are and new, properly-working functions are named with
an '`ST_`' prefix, in accordance with the latest OpenGIS requirements. Also,
operations over geometry features were added.


The list of new functions:


Spatial operators. They produce new geometries.



| Name | Description |
| --- | --- |
| Name | Description |
| [ST_UNION(A, B)](geometry-constructors/st_union.md) | union of A and B |
| [ST_INTERSECTION(A, B)](geometry-constructors/st_intersection.md) | intersection of A and B |
| [ST_SYMDIFFERENCE(A, B)](geometry-constructors/st_symdifference.md) | symdifference, notintersecting parts of A and B |
| [ST_BUFFER(A, radius)](geometry-constructors/st_buffer.md) | returns the shape of the area that lies in 'radius' distance from the shape A. |

Predicates, return boolean result of the relationship

| Name | Description |
| --- | --- |
| Name | Description |
| [ST_INTERSECTS(A, B)](geometry-relations/st-intersects.md) | if A and B have an intersection |
| [ST_CROSSES(A, B)](geometry-relations/st-crosses.md) | if A and B cross |
| [ST_EQUALS(A, B)](geometry-relations/st-equals.md) | if A and B are equal |
| [ST_WITHIN(A, B)](geometry-relations/st-within.md) | if A lies within B |
| [ST_CONTAINS(A,B)](geometry-relations/st-contains.md) | if B lies within A |
| [ST_DISJOINT(A,B)](geometry-relations/st_disjoint.md) | if A and B have no intersection |
| [ST_TOUCHES(A,B)](geometry-relations/st-touches.md) | if A touches B |




CC BY-SA / Gnu FDL

