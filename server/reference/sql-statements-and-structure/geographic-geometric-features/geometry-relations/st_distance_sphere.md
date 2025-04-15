
# ST_DISTANCE_SPHERE


##### MariaDB starting with [10.5.10](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10510-release-notes.md)
`<code>ST_DISTANCE_SPHERE</code>` was introduced in [MariaDB 10.2.38](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-2-series/mariadb-10238-release-notes.md), [MariaDB 10.3.29](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-3-series/mariadb-10329-release-notes.md), [MariaDB 10.4.19](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-4-series/mariadb-10419-release-notes.md) and [MariaDB 10.5.10](../../../../../release-notes/mariadb-community-server/release-notes-mariadb-10-5-series/mariadb-10510-release-notes.md). 


## Syntax


```
ST_DISTANCE_SPHERE(g1,g2,[r])
```

## Description


Returns the spherical distance in meters between two geometries (point or multipoint) on a sphere. The optional radius *r* is in meters, must be positive, and defaults to the Earth's radius (6370986 meters) if not specified. If either of the two geometries are not valid, NULL is returned.


## Example


```
set @zenica   = ST_GeomFromText('POINT(17.907743 44.203438)');
set @sarajevo = ST_GeomFromText('POINT(18.413076 43.856258)');
SELECT ST_Distance_Sphere(@zenica, @sarajevo);
+----------------------------------------+
| ST_Distance_Sphere(@zenica, @sarajevo) |
+----------------------------------------+
|                      55878.59337591705 |
+----------------------------------------+

SELECT ST_Distance_Sphere(@zenica, @sarajevo, 6370986);
+-------------------------------------------------+
| ST_Distance_Sphere(@zenica, @sarajevo, 6370986) |
+-------------------------------------------------+
|                               55878.59337591705 |
+-------------------------------------------------+

SELECT ST_Distance_Sphere(@zenica, @sarajevo, 200);    
+---------------------------------------------+
| ST_Distance_Sphere(@zenica, @sarajevo, 200) |
+---------------------------------------------+
|                           1.754158410516584 |
+---------------------------------------------+
```
