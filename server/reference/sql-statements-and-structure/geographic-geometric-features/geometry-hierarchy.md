
# Geometry Hierarchy

## Description


Geometry is the base class. It is an abstract class. The instantiable
subclasses of Geometry are restricted to zero-, one-, and
two-dimensional geometric objects that exist in two-dimensional
coordinate space. All instantiable geometry classes are defined so
that valid instances of a geometry class are topologically closed
(that is, all defined geometries include their boundary).


The base Geometry class has subclasses for Point, Curve, Surface, and
GeometryCollection:


* [Point](geometry-constructors/point.md) represents zero-dimensional objects.
* Curve represents one-dimensional objects, and has subclass [LineString](geometry-constructors/linestring.md), with sub-subclasses Line and LinearRing.
* Surface is designed for two-dimensional objects and has subclass [Polygon](geometry-constructors/polygon.md).
* [GeometryCollection](geometry-constructors/geometrycollection.md) has specialized zero-, one-, and two-dimensional collection classes named [MultiPoint](geometry-constructors/multipoint.md), [MultiLineString](geometry-constructors/multilinestring.md), and [MultiPolygon](geometry-constructors/multipolygon.md) for modeling geometries corresponding to collections of Points, LineStrings, and Polygons, respectively. MultiCurve and MultiSurface are introduced as abstract superclasses that generalize the collection interfaces to handle Curves and Surfaces.


Geometry, Curve, Surface, MultiCurve, and MultiSurface are defined as
non-instantiable classes. They define a common set of methods for
their subclasses and are included for extensibility.


[Point](point-properties/README.md), [LineString](linestring-properties/README.md), [Polygon](polygon-properties/README.md), [GeometryCollection](geometry-constructors/geometrycollection.md), [MultiPoint](geometry-constructors/multipoint.md),
[MultiLineString](geometry-constructors/multilinestring.md), and [MultiPolygon](geometry-constructors/multipolygon.md) are instantiable classes.

