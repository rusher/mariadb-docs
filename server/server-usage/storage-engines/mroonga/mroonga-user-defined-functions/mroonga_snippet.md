# mroonga\_snippet

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

`mroonga_snippet` is a [user-defined function](../../../../server-usage/user-defined-functions/) (UDF) included with the [Mroonga storage engine](../). It provides a keyword with surrounding text, or the keyword in context. See [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md) for details on creating this UDF if required.

The required parameters include:

* `document` - Column name or string value.
* `max_length` - Maximum length of the snippet, in bytes.
* `max_count` - Maximum snippet elements (N word).
* `encoding` - Encoding of the document, for example `cp932_japanese_ci`
* `skip_leading_spaces` - `1` to skip leading spaces, `0` to not skip.
* `html_escape` = `1` to enable HTML espape, `0` to disable.
* `prefix` - Snippet start text.
* `suffix` - Snippet end text.

The optional parameters include:

* `wordN` - A word.
* `wordN_prefix` - wordN start text.
* `wordN_suffix` - wordN end text

It can be used in both storage and wrapper mode.

Returns the snippet string.

## Example

```
```

## See Also

* [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md)

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
