# ST\_AsGeoJSON

## Syntax

```sql
ST_AsGeoJSON(g[, max_decimals[, options]])
```

## Description

Returns the given geometry _g_ as a GeoJSON element. The optional _max\_decimals_ limits the maximum number of decimals displayed.

The optional _options_ flag can be set to `1` to add a bounding box to the output.

## Examples

```sql
SELECT ST_AsGeoJSON(ST_GeomFromText('POINT(5.3 7.2)'));
+-------------------------------------------------+
| ST_AsGeoJSON(ST_GeomFromText('POINT(5.3 7.2)')) |
+-------------------------------------------------+
| {"type": "Point", "coordinates": [5.3, 7.2]}    |
+-------------------------------------------------+
```

## See Also

* [ST\_GeomFromGeoJSON](st_geomfromgeojson.md)

CC BY-SA / Gnu FDL
