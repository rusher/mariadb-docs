# version\_major

## Syntax

```
sys.version_major()
```

## Description

`version_major` is a [stored function](../../../../../../server-usage/stored-routines/stored-functions/) available with the [Sys Schema](../).

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

* [version\_minor](version_minor.md)
* [version\_patch](version_patch.md)

CC BY-SA / Gnu FDL
