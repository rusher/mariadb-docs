
# mroonga_highlight_html

## Syntax


```
mroonga_highlight_html(text[[, query AS query]])

mroonga_highlight_html(text[[, keyword1, ..., keywordN]])
```


## Description


`<code>mroonga_highlight_html</code>` is a [user-defined function](../../../../server-usage/programming-customizing-mariadb/user-defined-functions/user-defined-functions-security.md) (UDF) included with the [Mroonga storage engine](mroonga_snippet_html.md). It highlights the specified keywords in the target text. See [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md) for details on creating this UDF if required.


The optional parameter can either be one or more *keywords*, or a Groonga *query*.


The function highlights the specified keywords in the target text by surrounding each keyword with `<code><span class="keyword">...</span></code>`, and escaping special HTML characters such as `<code><</code>` and `<code>></code>`.


Returns highlighted HTML.


## Examples


```
SELECT mroonga_highlight_html('<p>MariaDB includes the Mroonga storage engine</p>.') 
  AS highlighted_html;
+-----------------------------------------------------------------+
| highlighted_html                                                |
+-----------------------------------------------------------------+
| &lt;p&gt;MariaDB includes the Mroonga storage engine&lt;/p&gt;. |
+-----------------------------------------------------------------+
```

Highlighting the words `<code>MariaDB</code>` and `<code>Mroonga</code>` in a given text:


```
SELECT mroonga_highlight_html('MariaDB includes the Mroonga storage engine.', 'MariaDB', 'Mroonga') 
  AS highlighted_html;
+--------------------------------------------------------------------------------------------------------+
| highlighted_html                                                                                       |
+--------------------------------------------------------------------------------------------------------+
| <span class="keyword">MariaDB</span> includes the <span class="keyword">Mroonga</span> storage engine. |
+--------------------------------------------------------------------------------------------------------+
```

The same outcome, formulated as a Groonga query:


```
SELECT mroonga_highlight_html('MariaDB includes the Mroonga storage engine.', 'MariaDB OR Mroonga' 
  AS query) AS highlighted_text;
+--------------------------------------------------------------------------------------------------------+
| highlighted_text                                                                                       |
+--------------------------------------------------------------------------------------------------------+
| <span class="keyword">MariaDB</span> includes the <span class="keyword">Mroonga</span> storage engine. |
+--------------------------------------------------------------------------------------------------------+
```

## See Also


* [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md)

