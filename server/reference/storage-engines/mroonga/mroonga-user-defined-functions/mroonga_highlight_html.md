
# mroonga_highlight_html

## Syntax


```
mroonga_highlight_html(text[[, query AS query]])

mroonga_highlight_html(text[[, keyword1, ..., keywordN]])
```


## Description


`mroonga_highlight_html` is a [user-defined function](../../../../server-usage/programming-customizing-mariadb/user-defined-functions/README.md) (UDF) included with the [Mroonga storage engine](../README.md). It highlights the specified keywords in the target text. See [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md) for details on creating this UDF if required.


The optional parameter can either be one or more *keywords*, or a Groonga *query*.


The function highlights the specified keywords in the target text by surrounding each keyword with `<span class="keyword">...</span>`, and escaping special HTML characters such as `<` and `>`.


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

Highlighting the words `MariaDB` and `Mroonga` in a given text:


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


CC BY-SA / Gnu FDL

