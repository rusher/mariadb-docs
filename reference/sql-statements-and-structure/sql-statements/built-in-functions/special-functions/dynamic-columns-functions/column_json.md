# COLUMN_JSON

#

# Syntax

```
COLUMN_JSON(dyncol_blob)
```

#

# Description

Returns a JSON representation of data in `dyncol_blob`. Can also be used to display nested columns. See [dynamic columns](../../../../nosql/dynamic-columns-api.md) for more information.

#

# Example

```
select item_name, COLUMN_JSON(dynamic_cols) from assets;
+-----------------+----------------------------------------+
| item_name | COLUMN_JSON(dynamic_cols) |
+-----------------+----------------------------------------+
| MariaDB T-shirt | {"size":"XL","color":"blue"} |
| Thinkpad Laptop | {"color":"black","warranty":"3 years"} |
+-----------------+----------------------------------------+
```

Limitation: `COLUMN_JSON` will decode nested dynamic columns at a nesting level of not more than 10 levels deep. Dynamic columns that are nested deeper than 10 levels will be shown as BINARY string, without encoding.