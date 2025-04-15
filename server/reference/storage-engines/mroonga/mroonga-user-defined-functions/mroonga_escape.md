
# mroonga_escape


## Syntax


```
mroonga_escape (string [,special_characters])
```

* `<code>string</code>` - required parameter specifying the text you want to escape
* `<code>special_characters</code>` - optional parameter specifying the characters to escape


## Description


`<code>mroonga_escape</code>` is a [user-defined function](../../../../server-usage/programming-customizing-mariadb/user-defined-functions/user-defined-functions-security.md) (UDF) included with the [Mroonga storage engine](mroonga_snippet_html.md), used for escaping a string. See [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md) for details on creating this UDF if required.


If no `<code>special_characters</code>` parameter is provided, by default `<code>+-<>*()":</code>` are escaped.


Returns the escaped string.


## Example


```
SELECT mroonga_escape("+-<>~*()\"\:");
'\\+\\-\\<\\>\\~\\*\\(\\)\\"\\:
```

## See Also


* [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md)

