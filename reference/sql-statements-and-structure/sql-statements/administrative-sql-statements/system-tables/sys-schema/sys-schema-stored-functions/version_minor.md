# version_minor

#

# Syntax

```
sys.version_minor()
```

#

# Description

`version_minor` is a [stored function](/en/stored-functions/) available with the [Sys Schema](../sys-schema-sys_config-table.md).

It returns the MariaDB Server minor release version.

#

# Examples

```
SELECT VERSION(),
 sys.version_major() AS major, 
 sys.version_minor() AS minor,
 sys.version_patch() AS patch;
+----------------+-------+-------+-------+
| VERSION() | major | minor | patch |
+----------------+-------+-------+-------+
| 10.8.2-MariaDB | 10 | 8 | 2 |
+----------------+-------+-------+-------+
```

#

# See Also

* [version_major](version_major.md)
* [version_patch](version_patch.md)