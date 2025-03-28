# MySQL/MariaDB Spatial Support Matrix

This table shows when different spatial features were introduced into MySQL and MariaDB.

| My | MDB | x | MBR | d | * | - |
| --- | --- | --- | --- | --- | --- | --- |
| My | MySQL |
| MDB | MariaDB |
| x | This feature is supported. |
| MBR | This feature is present, but operates on the Minimum Bounding Rectangle instead of the actual shape. |
| d | This feature is present, but has been deprecated and will be removed in a future version. |
| * | This feature is present, but may not work the way you expect. |
| - | This feature is not supported. |

| | My 5.4.2 | My 5.5 | My 5.6.1 | My 5.7.4 | My 5.7.5 | My 5.7.6 | MDB 5.1 | MDB 5.3.3 | MDB 10.1.2 | MDB 10.2 | | My 5.4.2 | My 5.5 | My 5.6.1 | My 5.7.4 | My 5.7.5 | My 5.7.6 | MDB 5.1 | MDB 5.3.3 | MDB 10.1.2 | MDB 10.2 | | My 5.4.2 | My 5.5 | My 5.6.1 | My 5.7.4 | My 5.7.5 | My 5.7.6 | MDB 5.1 | MDB 5.3.3 | MDB 10.1.2 | MDB 10.2 | | My 5.4.2 | My 5.5 | My 5.6.1 | My 5.7.4 | My 5.7.5 | My 5.7.6 | MDB 5.1 | MDB 5.3.3 | MDB 10.1.2 | MDB 10.2 | | My 5.4.2 | My 5.5 | My 5.6.1 | My 5.7.4 | My 5.7.5 | My 5.7.6 | MDB 5.1 | MDB 5.3.3 | MDB 10.1.2 | MDB 10.2 | | My 5.4.2 | My 5.5 | My 5.6.1 | My 5.7.4 | My 5.7.5 | My 5.7.6 | MDB 5.1 | MDB 5.3.3 | MDB 10.1.2 | MDB 10.2 | [ST_Envelope](geometry-properties/st_envelope.md) | [ST_Equals](/en/st_equals/) | [ST_ExteriorRing](polygon-properties/st_exteriorring.md) | ST_GeoHash | [ST_GeomCollFromText](wkt/st_geomcollfromtext.md) | [ST_GeomCollFromWKB](wkb/st_geomcollfromwkb.md) | [ST_GeometryCollectionFromText](wkt/st_geomcollfromtext.md) | [ST_GeometryCollectionFromWKB](wkb/st_geomcollfromwkb.md) | [ST_GeometryFromText](wkt/st_geomfromtext.md) | [ST_GeometryFromWKB](wkb/st_geomfromwkb.md) | [ST_GeometryN](geometry-properties/st_geometryn.md) | [ST_GeometryType](geometry-properties/st_geometrytype.md) | [ST_GeomFromGeoJSON](geojson/st_geomfromgeojson.md) | [ST_GeomFromText](wkt/st_geomfromtext.md) | [ST_GeomFromWKB](wkb/st_geomfromwkb.md) | [ST_InteriorRingN](polygon-properties/st_interiorringn.md) | [ST_Intersection](geometry-constructors/st_intersection.md) | [ST_Intersects](/en/st_intersects/) | | My 5.4.2 | My 5.5 | My 5.6.1 | My 5.7.4 | My 5.7.5 | My 5.7.6 | MDB 5.1 | MDB 5.3.3 | MDB 10.1.2 | MDB 10.2 | [ST_IsClosed](geometry-properties/st_isclosed.md) | [ST_IsEmpty](geometry-properties/st_isempty.md) | [ST_IsRing](geometry-properties/st_isring.md) | [ST_IsSimple](geometry-properties/st_issimple.md) | ST_IsValid | ST_LatFromGeoHash | [ST_Length](geometry-relations/st_length.md) | [ST_LineFromText](wkt/st_linefromtext.md) | [ST_LineFromWKB](wkb/st_linefromwkb.md) | [ST_LineStringFromText](wkt/st_linefromtext.md) | [ST_LineStringFromWKB](wkb/st_linefromwkb.md) | ST_LongFromGeoHash | [ST_NumGeometries](geometry-properties/st_numgeometries.md) | [ST_NumInteriorRings](polygon-properties/st_numinteriorrings.md) | [ST_NumPoints](linestring-properties/st_numpoints.md) | [ST_Overlaps](/en/st_overlaps/) | ST_PointFromGeoHash | [ST_PointFromText](wkt/st_pointfromtext.md) | [ST_PointFromWKB](wkb/st_pointfromwkb.md) | [ST_PointOnSurface](geometry-constructors/st_pointonsurface.md) | | My 5.4.2 | My 5.5 | My 5.6.1 | My 5.7.4 | My 5.7.5 | My 5.7.6 | MDB 5.1 | MDB 5.3.3 | MDB 10.1.2 | MDB 10.2 | [ST_PointN](linestring-properties/st_pointn.md) | [ST_PolyFromText](wkt/st_polyfromtext.md) | [ST_PolyFromWKB](wkb/st_polyfromwkb.md) | [ST_PolygonFromText](wkt/st_polyfromtext.md) | [ST_PolygonFromWKB](wkb/st_polyfromwkb.md) | [ST_Relate](geometry-properties/st_relate.md) | ST_Simplify | [ST_SRID](geometry-properties/st_srid.md) | [ST_StartPoint](linestring-properties/st_startpoint.md) | [ST_SymDifference](geometry-constructors/st_symdifference.md) | [ST_Touches](/en/st_touches/) | [ST_Union](geometry-constructors/st_union.md) | ST_Validate | [ST_Within](/en/st_within/) | [ST_X](point-properties/st_x.md) | [ST_Y](point-properties/st_y.md) | [StartPoint](linestring-properties/st_startpoint.md) | [Touches](geometry-relations/touches.md) | [Within](geometry-relations/within.md) | [X](point-properties/st_x.md) | | My 5.4.2 | My 5.5 | My 5.6.1 | My 5.7.4 | My 5.7.5 | My 5.7.6 | MDB 5.1 | MDB 5.3.3 | MDB 10.1.2 | MDB 10.2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | My 5.4.2 | My 5.5 | My 5.6.1 | My 5.7.4 | My 5.7.5 | My 5.7.6 | MDB 5.1 | MDB 5.3.3 | MDB 10.1.2 | MDB 10.2 |
| InnoDB Spatial Indexes | - | - | - | - | x | x | - | - | - | x |
| [MyISAM Spatial Indexes](spatial-index.md) | x | x | x | x | x | x | x | x | x | x |
| [Aria Spatial Indexes](spatial-index.md) | - | - | - | - | - | - | x | x | x | x |
| [Area](polygon-properties/st_area.md) | x | x | x | x | x | d | x | x | x | x |
| [AsBinary](wkb/st_asbinary.md) | x | x | x | x | x | d | x | x | x | x |
| [AsText](wkt/st_astext.md) | x | x | x | x | x | d | x | x | x | x |
| [AsWKB](wkb/st_asbinary.md) | x | x | x | x | x | d | x | x | x | x |
| [AsWKT](wkt/st_astext.md) | x | x | x | x | x | d | x | x | x | x |
| [Boundary](geometry-properties/st_boundary.md) | - | - | - | - | - | - | - | - | x | x |
| [Buffer](geometry-constructors/st_buffer.md) | - | - | x | x | x | d | x | x | x | x |
| [Centroid](polygon-properties/st_centroid.md) | - | x | x | x | x | d | x | x | x | x |
| [Contains](geometry-relations/contains.md) | MBR | MBR | MBR | MBR | MBR | d | MBR | MBR | MBR | MBR |
| [ConvexHull](geometry-constructors/st_convexhull.md) | - | - | - | - | x | d | - | - | x | x |
| [Crosses](/en/st_crosses/) | MBR | x | x | x | x | d | MBR | MBR | MBR | MBR |
| [Dimension](geometry-properties/st_dimension.md) | x | x | x | x | x | d | x | x | x | x |
| [Disjoint](geometry-relations/disjoint.md) | MBR | MBR | MBR | MBR | MBR | d | MBR | MBR | MBR | MBR |
| Distance | MBR | - | - | x | x | d | - | - | - | - |
| [EndPoint](linestring-properties/st_endpoint.md) | x | x | x | x | x | d | x | x | x | x |
| [Envelope](geometry-properties/st_envelope.md) | x | x | x | x | x | d | x | x | x | x |
| [Equals](geometry-relations/equals.md) | MBR | MBR | MBR | MBR | MBR | d | MBR | MBR | MBR | MBR |
| | My 5.4.2 | My 5.5 | My 5.6.1 | My 5.7.4 | My 5.7.5 | My 5.7.6 | MDB 5.1 | MDB 5.3.3 | MDB 10.1.2 | MDB 10.2 |
| [ExteriorRing](polygon-properties/st_exteriorring.md) | x | x | x | x | x | d | x | x | x | x |
| [GeomCollFromText](wkt/st_geomcollfromtext.md) | x | x | x | x | x | d | x | x | x | x |
| [GeomCollFromWKB](wkb/st_geomcollfromwkb.md) | x | x | x | x | x | d | x | x | x | x |
| [GeometryCollection](wkb/geometrycollectionfromwkb.md) | x | x | x | x | x | x | x | x | x | x |
| [GeometryCollectionFromText](wkt/st_geomcollfromtext.md) | x | x | x | x | x | d | x | x | x | x |
| [GeometryCollectionFromWKB](wkb/st_geomcollfromwkb.md) | x | x | x | x | x | d | x | x | x | x |
| [GeometryFromText](wkt/st_geomfromtext.md) | x | x | x | x | x | d | x | x | x | x |
| [GeometryFromWKB](wkb/st_geomfromwkb.md) | x | x | x | x | x | d | x | x | x | x |
| [GeometryN](geometry-properties/st_geometryn.md) | x | x | x | x | x | d | x | x | x | x |
| [GeometryType](geometry-properties/st_geometrytype.md) | x | x | x | x | x | d | x | x | x | x |
| [GeomFromText](wkt/st_geomfromtext.md) | x | x | x | x | x | d | x | x | x | x |
| [GeomFromWKB](wkb/st_geomfromwkb.md) | x | x | x | x | x | d | x | x | x | x |
| [GLength](linestring-properties/glength.md) | x | x | x | x | x | d | x | x | x | x |
| [InteriorRingN](polygon-properties/st_interiorringn.md) | x | x | x | x | x | d | x | x | x | x |
| [Intersects](geometry-relations/intersects.md) | MBR | MBR | MBR | MBR | MBR | d | MBR | MBR | MBR | MBR |
| [IsClosed](geometry-properties/st_isclosed.md) | x | x | x | x | x | d | x | x | x | x |
| [IsEmpty](geometry-properties/st_isempty.md) | - | * | * | * | * | d | x | x | x | x |
| [IsRing](geometry-properties/st_isring.md) | - | - | - | - | - | - | - | - | x | x |
| [IsSimple](geometry-properties/st_issimple.md) | - | * | * | x | x | d | - | x | x | x |
| [LineFromText](wkt/st_linefromtext.md) | x | x | x | x | x | d | x | x | x | x |
| | My 5.4.2 | My 5.5 | My 5.6.1 | My 5.7.4 | My 5.7.5 | My 5.7.6 | MDB 5.1 | MDB 5.3.3 | MDB 10.1.2 | MDB 10.2 |
| [LineFromWKB](wkb/st_linefromwkb.md) | x | x | x | x | x | d | x | x | x | x |
| [LineString](wkb/linestringfromwkb.md) | x | x | x | x | x | x | x | x | x | x |
| [LineStringFromText](wkt/st_linefromtext.md) | x | x | x | x | x | d | x | x | x | x |
| [LineStringFromWKB](wkb/st_linefromwkb.md) | x | x | x | x | x | d | x | x | x | x |
| [MBRContains](mbr-minimum-bounding-rectangle/mbrcontains.md) | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR |
| MBRCoveredBy | - | - | - | MBR | MBR | MBR | - | - | - | - |
| [MBRDisjoint](mbr-minimum-bounding-rectangle/mbrdisjoint.md) | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR |
| [MBREqual](mbr-minimum-bounding-rectangle/mbrequal.md) | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR |
| [MBREquals](geometry-relations/equals.md) | - | - | - | MBR | MBR | MBR | - | - | - | MBR |
| [MBRIntersects](mbr-minimum-bounding-rectangle/mbrintersects.md) | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR |
| [MBROverlaps](mbr-minimum-bounding-rectangle/mbroverlaps.md) | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR |
| [MBRTouches](mbr-minimum-bounding-rectangle/mbrtouches.md) | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR |
| [MBRWithin](mbr-minimum-bounding-rectangle/mbrwithin.md) | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR | MBR |
| [MLineFromText](wkt/mlinefromtext.md) | x | x | x | x | x | d | x | x | x | x |
| [MLineFromWKB](/en/linefromwkb/) | x | x | x | x | x | d | x | x | x | x |
| [MPointFromText](wkt/mpointfromtext.md) | x | x | x | x | x | d | x | x | x | x |
| [MPointFromWKB](wkb/mpointfromwkb.md) | x | x | x | x | x | d | x | x | x | x |
| [MPolyFromText](wkt/mpolyfromtext.md) | x | x | x | x | x | d | x | x | x | x |
| [MPolyFromWKB](wkb/mpolyfromwkb.md) | x | x | x | x | x | d | x | x | x | x |
| [MultiLineString](wkb/multilinestringfromwkb.md) | x | x | x | x | x | x | x | x | x | x |
| | My 5.4.2 | My 5.5 | My 5.6.1 | My 5.7.4 | My 5.7.5 | My 5.7.6 | MDB 5.1 | MDB 5.3.3 | MDB 10.1.2 | MDB 10.2 |
| [MultiLineStringFromText](wkt/mlinefromtext.md) | x | x | x | x | x | d | x | x | x | x |
| [MultiLineStringFromWKB](wkb/mlinefromwkb.md) | x | x | x | x | x | d | x | x | x | x |
| [MultiPoint](wkb/multipointfromwkb.md) | x | x | x | x | x | x | x | x | x | x |
| [MultiPointFromText](wkt/mpointfromtext.md) | x | x | x | x | x | d | x | x | x | x |
| [MultiPointFromWKB](wkb/mpointfromwkb.md) | x | x | x | x | x | d | x | x | x | x |
| [MultiPolygon](wkb/multipolygonfromwkb.md) | x | x | x | x | x | x | x | x | x | x |
| [MultiPolygonFromText](wkt/mpolyfromtext.md) | x | x | x | x | x | d | x | x | x | x |
| [MultiPolygonFromWKB](wkb/mpolyfromwkb.md) | x | x | x | x | x | d | x | x | x | x |
| [NumGeometries](geometry-properties/st_numgeometries.md) | x | x | x | x | x | d | x | x | x | x |
| [NumInteriorRings](polygon-properties/st_numinteriorrings.md) | x | x | x | x | x | d | x | x | x | x |
| [NumPoints](linestring-properties/st_numpoints.md) | x | x | x | x | x | d | x | x | x | x |
| [Overlaps](geometry-relations/overlaps.md) | MBR | MBR | MBR | MBR | MBR | d | MBR | MBR | MBR | MBR |
| [Point](point-properties/point-properties-y.md) | x | x | x | x | x | x | x | x | x | x |
| [PointFromText](wkt/st_pointfromtext.md) | x | x | x | x | x | d | x | x | x | x |
| [PointFromWKB](wkb/st_pointfromwkb.md) | x | x | x | x | x | d | x | x | x | x |
| [PointOnSurface](geometry-constructors/st_pointonsurface.md) | - | - | - | - | - | - | - | - | x | x |
| [PointN](linestring-properties/st_pointn.md) | x | x | x | x | x | d | x | x | x | x |
| [PolyFromText](wkt/st_polyfromtext.md) | x | x | x | x | x | d | x | x | x | x |
| [PolyFromWKB](wkb/st_polyfromwkb.md) | x | x | x | x | x | d | x | x | x | x |
| [Polygon](wkb/polygonfromwkb.md) | x | x | x | x | x | x | x | x | x | x |
| | My 5.4.2 | My 5.5 | My 5.6.1 | My 5.7.4 | My 5.7.5 | My 5.7.6 | MDB 5.1 | MDB 5.3.3 | MDB 10.1.2 | MDB 10.2 |
| [PolygonFromText](wkt/st_polyfromtext.md) | x | x | x | x | x | d | x | x | x | x |
| [PolygonFromWKB](wkb/st_polyfromwkb.md) | x | x | x | x | x | d | x | x | x | x |
| [SRID](/en/srid/) | x | x | x | x | x | d | x | x | x | x |
| [ST_Area](polygon-properties/st_area.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_AsBinary](wkb/st_asbinary.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_AsGeoJSON](geojson/geojson-st_asgeojson.md) | - | - | - | x | x | x | - | - | - | x |
| [ST_AsText](wkt/st_astext.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_AsWKB](wkb/st_asbinary.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_AsWKT](wkt/st_astext.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_Boundary](geometry-properties/st_boundary.md) | - | - | - | - | - | - | - | - | x | x |
| [ST_Buffer](geometry-constructors/st_buffer.md) | - | - | x | x | x | x | - | x | x | x |
| ST_Buffer_Strategy | - | - | - | x | x | x | - | - | - | - |
| [ST_Centroid](polygon-properties/st_centroid.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_Contains](/en/st_contains/) | - | - | x | x | x | x | - | x | x | x |
| [ST_ConvexHull](geometry-constructors/st_convexhull.md) | - | - | - | - | x | x | - | - | x | x |
| [ST_Crosses](/en/st_crosses/) | - | - | x | x | x | x | - | x | x | x |
| [ST_Difference](geometry-relations/st_difference.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_Dimension](geometry-properties/st_dimension.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_Disjoint](geometry-relations/st_disjoint.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_Distance](geometry-relations/st_distance_sphere.md) | - | - | x | x | x | x | - | x | x | x |
| | My 5.4.2 | My 5.5 | My 5.6.1 | My 5.7.4 | My 5.7.5 | My 5.7.6 | MDB 5.1 | MDB 5.3.3 | MDB 10.1.2 | MDB 10.2 |
| ST_Distance_Sphere | - | - | - | - | - | x | - | - | - | - |
| [ST_EndPoint](linestring-properties/st_endpoint.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_Envelope](geometry-properties/st_envelope.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_Equals](/en/st_equals/) | - | - | x | x | x | x | - | x | x | x |
| [ST_ExteriorRing](polygon-properties/st_exteriorring.md) | - | - | x | x | x | x | - | x | x | x |
| ST_GeoHash | - | - | - | - | x | x | - | - | - | - |
| [ST_GeomCollFromText](wkt/st_geomcollfromtext.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_GeomCollFromWKB](wkb/st_geomcollfromwkb.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_GeometryCollectionFromText](wkt/st_geomcollfromtext.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_GeometryCollectionFromWKB](wkb/st_geomcollfromwkb.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_GeometryFromText](wkt/st_geomfromtext.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_GeometryFromWKB](wkb/st_geomfromwkb.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_GeometryN](geometry-properties/st_geometryn.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_GeometryType](geometry-properties/st_geometrytype.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_GeomFromGeoJSON](geojson/st_geomfromgeojson.md) | - | - | - | - | x | x | - | - | - | x |
| [ST_GeomFromText](wkt/st_geomfromtext.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_GeomFromWKB](wkb/st_geomfromwkb.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_InteriorRingN](polygon-properties/st_interiorringn.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_Intersection](geometry-constructors/st_intersection.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_Intersects](/en/st_intersects/) | - | - | x | x | x | x | - | x | x | x |
| | My 5.4.2 | My 5.5 | My 5.6.1 | My 5.7.4 | My 5.7.5 | My 5.7.6 | MDB 5.1 | MDB 5.3.3 | MDB 10.1.2 | MDB 10.2 |
| [ST_IsClosed](geometry-properties/st_isclosed.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_IsEmpty](geometry-properties/st_isempty.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_IsRing](geometry-properties/st_isring.md) | - | - | - | - | - | - | - | - | x | x |
| [ST_IsSimple](geometry-properties/st_issimple.md) | - | - | x | x | x | x | - | x | x | x |
| ST_IsValid | - | - | - | - | - | x | - | - | - | - |
| ST_LatFromGeoHash | - | - | - | - | x | x | - | - | - | - |
| [ST_Length](geometry-relations/st_length.md) | - | - | - | - | - | x | - | x | x | x |
| [ST_LineFromText](wkt/st_linefromtext.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_LineFromWKB](wkb/st_linefromwkb.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_LineStringFromText](wkt/st_linefromtext.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_LineStringFromWKB](wkb/st_linefromwkb.md) | - | - | x | x | x | x | - | x | x | x |
| ST_LongFromGeoHash | - | - | - | - | x | x | - | - | - | - |
| [ST_NumGeometries](geometry-properties/st_numgeometries.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_NumInteriorRings](polygon-properties/st_numinteriorrings.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_NumPoints](linestring-properties/st_numpoints.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_Overlaps](/en/st_overlaps/) | - | - | x | x | x | x | - | x | x | x |
| ST_PointFromGeoHash | - | - | - | - | x | x | - | - | - | - |
| [ST_PointFromText](wkt/st_pointfromtext.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_PointFromWKB](wkb/st_pointfromwkb.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_PointOnSurface](geometry-constructors/st_pointonsurface.md) | - | - | - | - | - | - | - | - | x | x |
| | My 5.4.2 | My 5.5 | My 5.6.1 | My 5.7.4 | My 5.7.5 | My 5.7.6 | MDB 5.1 | MDB 5.3.3 | MDB 10.1.2 | MDB 10.2 |
| [ST_PointN](linestring-properties/st_pointn.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_PolyFromText](wkt/st_polyfromtext.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_PolyFromWKB](wkb/st_polyfromwkb.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_PolygonFromText](wkt/st_polyfromtext.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_PolygonFromWKB](wkb/st_polyfromwkb.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_Relate](geometry-properties/st_relate.md) | - | - | - | - | - | - | - | - | x | x |
| ST_Simplify | - | - | - | - | - | x | - | - | - | - |
| [ST_SRID](geometry-properties/st_srid.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_StartPoint](linestring-properties/st_startpoint.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_SymDifference](geometry-constructors/st_symdifference.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_Touches](/en/st_touches/) | - | - | x | x | x | x | - | x | x | x |
| [ST_Union](geometry-constructors/st_union.md) | - | - | x | x | x | x | - | x | x | x |
| ST_Validate | - | - | - | - | - | x | - | - | - | - |
| [ST_Within](/en/st_within/) | - | - | x | x | x | x | - | x | x | x |
| [ST_X](point-properties/st_x.md) | - | - | x | x | x | x | - | x | x | x |
| [ST_Y](point-properties/st_y.md) | - | - | x | x | x | x | - | x | x | x |
| [StartPoint](linestring-properties/st_startpoint.md) | x | x | x | x | x | d | x | x | x | x |
| [Touches](geometry-relations/touches.md) | MBR | x | x | x | x | d | MBR | MBR | MBR | MBR |
| [Within](geometry-relations/within.md) | MBR | MBR | MBR | MBR | MBR | d | MBR | MBR | MBR | MBR |
| [X](point-properties/st_x.md) | x | x | x | x | x | d | x | x | x | x |
| [Y](point-properties/st_y.md) | x | x | x | x | x | d | x | x | x | x |
| | My 5.4.2 | My 5.5 | My 5.6.1 | My 5.7.4 | My 5.7.5 | My 5.7.6 | MDB 5.1 | MDB 5.3.3 | MDB 10.1.2 | MDB 10.2 |