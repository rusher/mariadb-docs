
# mroonga_snippet

## Syntax


```
mroonga_snippet document,
                max_length,
                max_count,
                encoding,
                skip_leading_spaces,
                html_escape,
                snippet_prefix,
                snippet_suffix,
                word1, word1_prefix, word1_suffix
                ...
                [wordN wordN_prefix wordN_suffix]
```


## Description


`<code>mroonga_snippet</code>` is a [user-defined function](../../../../server-usage/programming-customizing-mariadb/user-defined-functions/user-defined-functions-security.md) (UDF) included with the [Mroonga storage engine](mroonga_snippet_html.md). It provides a keyword with surrounding text, or the keyword in context. See [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md) for details on creating this UDF if required.


The required parameters include:


* `<code>document</code>` - Column name or string value.
* `<code>max_length</code>` - Maximum length of the snippet, in bytes.
* `<code>max_count</code>` - Maximum snippet elements (N word).
* `<code>encoding</code>` - Encoding of the document, for example `<code>cp932_japanese_ci</code>`
* `<code>skip_leading_spaces</code>` - `<code>1</code>` to skip leading spaces, `<code>0</code>` to not skip.
* `<code>html_escape</code>` = `<code>1</code>` to enable HTML espape, `<code>0</code>` to disable.
* `<code>prefix</code>` - Snippet start text.
* `<code>suffix</code>` - Snippet end text.


The optional parameters include:


* `<code>wordN</code>` - A word.
* `<code>wordN_prefix</code>` - wordN start text.
* `<code>wordN_suffix</code>` - wordN end text


It can be used in both storage and wrapper mode.


Returns the snippet string.


## Example


```

```

## See Also


* [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md)

