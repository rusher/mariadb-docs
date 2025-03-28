# JSON_COMPACT

#

# Syntax

```
JSON_COMPACT(json_doc)
```

#

# Description

Removes all unnecessary spaces so the json document is as short as possible.

#

# Example

```
SET @j = '{ "A": 1, "B": [2, 3]}';

SELECT JSON_COMPACT(@j), @j;
+-------------------+------------------------+
| JSON_COMPACT(@j) | @j |
+-------------------+------------------------+
| {"A":1,"B":[2,3]} | { "A": 1, "B": [2, 3]} |
+-------------------+------------------------+
```

#

# See Also

* [JSON video tutorial](https://www.youtube.com/watch?v=sLE7jPETp8g) covering JSON_COMPACT.