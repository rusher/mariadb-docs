
# MPointFromWKB

## Syntax


```
MPointFromWKB(wkb[,srid])
MultiPointFromWKB(wkb[,srid])
```

## Description


Constructs a [MULTIPOINT](../geometry-constructors/multipoint.md) value using its [WKB](well-known-binary-wkb-format.md) representation and [SRID](../geometry-properties/st_srid.md).


`<code>MPointFromWKB()</code>` and `<code>MultiPointFromWKB()</code>` are synonyms.


## Examples


```
SET @g = ST_AsBinary(MPointFromText('MultiPoint( 1 1, 2 2, 5 3, 7 2, 9 3, 8 4, 6 6, 6 9, 4 9, 1 5 )'));

SELECT ST_AsText(MPointFromWKB(@g));
+-----------------------------------------------------+
| ST_AsText(MPointFromWKB(@g))                        |
+-----------------------------------------------------+
| MULTIPOINT(1 1,2 2,5 3,7 2,9 3,8 4,6 6,6 9,4 9,1 5) |
+-----------------------------------------------------+
```
