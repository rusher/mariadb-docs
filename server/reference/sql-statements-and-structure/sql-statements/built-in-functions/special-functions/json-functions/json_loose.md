# JSON_LOOSE

#

# Syntax

```
JSON_LOOSE(json_doc)
```

#

# Description

Adds spaces to a JSON document to make it look more readable.

#

# Example

```
SET @j = '{ "A":1,"B":[2,3]}';

SELECT JSON_LOOSE(@j), @j;
+-----------------------+--------------------+
| JSON_LOOSE(@j) | @j |
+-----------------------+--------------------+
| {"A": 1, "B": [2, 3]} | { "A":1,"B":[2,3]} |
+-----------------------+--------------------+
```