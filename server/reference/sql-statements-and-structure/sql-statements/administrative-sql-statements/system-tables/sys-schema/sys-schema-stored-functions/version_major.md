
# version_major

## Syntax


```
sys.version_major()
```

## Description


`version_major` is a [stored function](../../../../../../../server-usage/programming-customizing-mariadb/stored-routines/stored-functions/README.md) available with the [Sys Schema](../README.md).


It returns the MariaDB Server major release version.


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


* [version_minor](version_minor.md)
* [version_patch](version_patch.md)


CC BY-SA / Gnu FDL

