
# MLineFromWKB

## Syntax


```
MLineFromWKB(wkb[,srid])
MultiLineStringFromWKB(wkb[,srid])
```

## Description


Constructs a [MULTILINESTRING](../geometry-constructors/multilinestring.md) value using its [WKB](well-known-binary-wkb-format.md) representation and [SRID](../geometry-properties/st_srid.md).


`<code>MLineFromWKB()</code>` and `<code>MultiLineStringFromWKB()</code>` are synonyms.


## Examples


```
SET @g = ST_AsBinary(MLineFromText('MULTILINESTRING((10 48,10 21,10 0),(16 0,16 23,16 48))'));

SELECT ST_AsText(MLineFromWKB(@g));
+--------------------------------------------------------+
| ST_AsText(MLineFromWKB(@g))                            |
+--------------------------------------------------------+
| MULTILINESTRING((10 48,10 21,10 0),(16 0,16 23,16 48)) |
+--------------------------------------------------------+
```
