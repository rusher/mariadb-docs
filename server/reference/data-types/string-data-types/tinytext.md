# TINYTEXT

#

# Syntax

```
TINYTEXT [CHARACTER SET charset_name] [COLLATE collation_name]
```

#

# Description

A [TEXT](text.md) column with a maximum length of 255 (`28 - 1`) characters. The effective maximum length is less if the value contains multi-byte characters. Each TINYTEXT value is stored using a one-byte length prefix that indicates the number of bytes in the value.

#

# See Also

* [TEXT](text.md)
* [BLOB and TEXT Data Types](blob-and-text-data-types.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)