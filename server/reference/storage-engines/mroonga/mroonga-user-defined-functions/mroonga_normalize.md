
# mroonga_normalize

## Syntax


```
mroonga_normalize(string[, normalizer_name])
```


## Description


`<code>mroonga_normalize</code>` is a [user-defined function](../../../../server-usage/programming-customizing-mariadb/user-defined-functions/user-defined-functions-security.md) (UDF) included with the [Mroonga storage engine](mroonga_snippet_html.md). It uses Groonga's normalizer to normalize text. See [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md) for details on creating this UDF if required.


Given a string, returns the normalized text.


See the [Groonga Normalizer Reference](https://groonga.org/docs/reference/normalizers.html) for details on the Groonga normalizers. The default if no normalizer is provided is `<code>NormalizerAuto</code>`.


## Examples


```
SELECT mroonga_normalize("ABぃ㍑");
+-------------------------------+
| mroonga_normalize("ABぃ㍑")   |
+-------------------------------+
| abぃリットル                  |
+-------------------------------+
```

## See Also


* [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md)

