
# ST_AsGeoJSON

## Syntax


```
ST_AsGeoJSON(g[, max_decimals[, options]])
```

## Description


Returns the given geometry *g* as a GeoJSON element. The optional *max_decimals* limits the maximum number of decimals displayed.


The optional *options* flag can be set to `1` to add a bounding box to the output.


## Examples


```
SELECT ST_AsGeoJSON(ST_GeomFromText('POINT(5.3 7.2)'));
+-------------------------------------------------+
| ST_AsGeoJSON(ST_GeomFromText('POINT(5.3 7.2)')) |
+-------------------------------------------------+
| {"type": "Point", "coordinates": [5.3, 7.2]}    |
+-------------------------------------------------+
```

## See Also


* [ST_GeomFromGeoJSON](st_geomfromgeojson.md)


CC BY-SA / Gnu FDL

