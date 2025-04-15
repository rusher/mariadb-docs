# mroonga_escape

#

# Syntax

```
mroonga_escape (string [,special_characters])
```

* `string` - required parameter specifying the text you want to escape
* `special_characters` - optional parameter specifying the characters to escape

#

# Description

`mroonga_escape` is a [user-defined function](../../../../server-usage/programming-customizing-mariadb/user-defined-functions/user-defined-functions-calling-sequences.md) (UDF) included with the [Mroonga storage engine](../mroonga-status-variables.md), used for escaping a string. See [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md) for details on creating this UDF if required.

If no `special_characters` parameter is provided, by default `+-<>*()":` are escaped.

Returns the escaped string.

#

# Example

```
SELECT mroonga_escape("+-<>~*()\"\:");
'\\+\\-\\<\\>\\~\\*\\(\\)\\"\\:
```

#

# See Also

* [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md)