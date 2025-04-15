
# Boolean Literals

In MariaDB, `<code>FALSE</code>` is a synonym of 0 and `<code>TRUE</code>` is a synonym of 1. These constants are case insensitive, so `<code>TRUE</code>`, `<code>True</code>`, and `<code>true</code>` are equivalent.


These terms are not synonyms of 0 and 1 when used with the `<code>[IS](../geographic-geometric-features/geometry-properties/isclosed.md)</code>` operator. So, for example, `<code>10 IS TRUE</code>` returns 1, while `<code>10 = TRUE</code>` returns 0 (because 1 != 10).


The `<code>IS</code>` operator accepts a third constant exists: `<code>UNKNOWN</code>`. It is always a synonym of [NULL](../../data-types/null-values.md).


`<code>TRUE</code>` and `<code>FALSE</code>` are [reserved words](reserved-words.md), while `<code>UNKNOWN</code>` is not.


## See Also


* [BOOLEAN](../../data-types/data-types-numeric-data-types/boolean.md) type

