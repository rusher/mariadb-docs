
# ST_ISEMPTY

## Syntax


```
ST_IsEmpty(g)
IsEmpty(g)
```

## Description


IsEmpty is a function defined by the OpenGIS specification, but is not fully implemented by MariaDB or MySQL.


Since MariaDB and MySQL do not support GIS EMPTY values such as POINT EMPTY, as implemented it simply returns `<code>1</code>` if the geometry value *`<code>g</code>`* is invalid, `<code>0</code>` if it is valid, and `<code>NULL</code>` if the argument is `<code>NULL</code>`.


`<code>ST_IsEmpty()</code>` and `<code>IsEmpty()</code>` are synonyms.

