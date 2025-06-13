# COLLATION

## Syntax

```
COLLATION(str)
```

## Description

Returns the collation of the string argument. If `str` is not a string, it is considered as a binary string (so the function returns 'binary'). This applies to `NULL`, too. The return value is a string in the utf8 [character set](../../../data-types/string-data-types/character-sets/).

See [Character Sets and Collations](../../../data-types/string-data-types/character-sets/).

## Examples

```
SELECT COLLATION('abc');
+-------------------+
| COLLATION('abc')  |
+-------------------+
| latin1_swedish_ci |
+-------------------+

SELECT COLLATION(_utf8'abc');
+-----------------------+
| COLLATION(_utf8'abc') |
+-----------------------+
| utf8_general_ci       |
+-----------------------+
```

## See Also

* [String literals](../../../sql-structure/sql-language-structure/string-literals.md)
* [CAST()](../../string-functions/cast.md)
* [CONVERT()](../../string-functions/convert.md)

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
