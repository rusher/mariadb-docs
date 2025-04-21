
# version_patch

## Syntax


```
sys.version_patch()
```

## Description


`version_patch` is a [stored function](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) available with the [Sys Schema](../README.md).


It returns the MariaDB Server patch release version.


## Examples


```
SELECT VERSION(),
 sys.version_major() AS major, 
 sys.version_minor() AS minor,
 sys.version_patch() AS patch;
+----------------+-------+-------+-------+
| VERSION()      | major | minor | patch |
+----------------+-------+-------+-------+
| 10.8.2-MariaDB |    10 |     8 |     2 |
+----------------+-------+-------+-------+
```

## See Also


* [version_major](version_major.md)
* [version_minor](version_minor.md)

