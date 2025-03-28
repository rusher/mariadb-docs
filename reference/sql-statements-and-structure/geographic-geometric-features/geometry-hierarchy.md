# Geometry Hierarchy

#

# Description

Geometry is the base class. It is an abstract class. The instantiable
subclasses of Geometry are restricted to zero-, one-, and
two-dimensional geometric objects that exist in two-dimensional
coordinate space. All instantiable geometry classes are defined so
that valid instances of a geometry class are topologically closed
(that is, all defined geometries include their boundary).

The base Geometry class has subclasses for Point, Curve, Surface, and
GeometryCollection:

* [Point](point-properties/point-properties-y.md) represents zero-dimensional objects.
* Curve represents one-dimensional objects, and has subclass [LineString](wkb/linestringfromwkb.md), with sub-subclasses Line and LinearRing.
* Surface is designed for two-dimensional objects and has subclass [Polygon](wkb/polygonfromwkb.md).
* [GeometryCollection](wkb/geometrycollectionfromwkb.md) has specialized zero-, one-, and two-dimensional collection classes named [MultiPoint](wkb/multipointfromwkb.md), [MultiLineString](wkb/multilinestringfromwkb.md), and [MultiPolygon](wkb/multipolygonfromwkb.md) for modeling geometries corresponding to collections of Points, LineStrings, and Polygons, respectively. MultiCurve and MultiSurface are introduced as abstract superclasses that generalize the collection interfaces to handle Curves and Surfaces.

Geometry, Curve, Surface, MultiCurve, and MultiSurface are defined as
non-instantiable classes. They define a common set of methods for
their subclasses and are included for extensibility.

[Point](point-properties/point-properties-y.md), [LineString](linestring-properties/linestring-properties-numpoints.md), [Polygon](polygon-properties/polygon-properties-interiorringn.md), [GeometryCollection](wkb/geometrycollectionfromwkb.md), [MultiPoint](wkb/multipointfromwkb.md),
[MultiLineString](wkb/multilinestringfromwkb.md), and [MultiPolygon](wkb/multipolygonfromwkb.md) are instantiable classes.