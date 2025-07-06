# ST\_GeomFromGeoJSON

## Syntax

```sql
ST_GeomFromGeoJSON(g[, option])
```

## Description

Given a GeoJSON input _g_, returns a geometry object. The _option_ specifies what to do if _g_ contains geometries with coordinate dimensions higher than 2.

| Option | Description                                                                                      |
| ------ | ------------------------------------------------------------------------------------------------ |
| Option | Description                                                                                      |
| 1      | Return an error (the default)                                                                    |
| 2 - 4  | The document is accepted, but the coordinates for higher coordinate dimensions are stripped off. |

## Examples

```sql
SET @j = '{ "type": "Point", "coordinates": [5.3, 15.0]}';

SELECT ST_AsText(ST_GeomFromGeoJSON(@j));
+-----------------------------------+
| ST_AsText(ST_GeomFromGeoJSON(@j)) |
+-----------------------------------+
| POINT(5.3 15)                     |
+-----------------------------------+
```

## See Also

* [ST\_AsGeoJSON](geojson-st_asgeojson.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
