
# last_insert_grn_id

## Syntax


```
last_insert_grn_id()
```


## Description


`last_insert_grn_id` is a [user-defined function](../../../../server-usage/programming-customizing-mariadb/user-defined-functions/user-defined-functions-security.md) (UDF) included with the [Mroonga storage engine](mroonga_snippet_html.md). It returns the unique Groonga id of the last-inserted record. See [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md) for details on creating this UDF if required.


## Examples


```
SELECT last_insert_grn_id();
+----------------------+
| last_insert_grn_id() |
+----------------------+
|                    3 |
+----------------------+
```

## See Also


* [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md)

