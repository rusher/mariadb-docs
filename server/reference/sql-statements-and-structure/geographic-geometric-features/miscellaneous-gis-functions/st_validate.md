
# ST_Validate


##### MariaDB starting with [11.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md)
ST_Validate was added in [MariaDB 11.8](../../../../../release-notes/mariadb-community-server/what-is-mariadb-118.md).


## Syntax


```
ST_Validate(g)
```

## Description


The function checks that a given geometry is compliant with the Well-Known Binary (WKB) format and Spatial Reference System Identifier (SRID) syntax, and is geometrically valid.


It returns the geometry if it's valid, or NULL if not.


The function is useful to filter out invalid geometry data.


## Examples


A [POINT](../geometry-constructors/point.md) requires both x and y co-ordinates:


```
SELECT ST_ASTEXT(ST_VALIDATE(ST_GeomFromText('POINT(1 0)')));          
+-------------------------------------------------------+
| ST_ASTEXT(ST_VALIDATE(ST_GeomFromText('POINT(1 0)'))) |
+-------------------------------------------------------+
| POINT(1 0)                                            |
+-------------------------------------------------------+

SELECT ST_ASTEXT(ST_VALIDATE(ST_GeomFromText('POINT(1)')));  
+-----------------------------------------------------+
| ST_ASTEXT(ST_VALIDATE(ST_GeomFromText('POINT(1)'))) |
+-----------------------------------------------------+
| NULL                                                |
+-----------------------------------------------------+
```

## See Also


* [Geometry Constructors](../geometry-constructors/README.md)
* [ST_AsText](../wkt/st_astext.md)

