# last\_insert\_grn\_id

## Syntax

```
last_insert_grn_id()
```

## Description

`last_insert_grn_id` is a [user-defined function](../../../../server-usage/user-defined-functions/) (UDF) included with the [Mroonga storage engine](../). It returns the unique Groonga id of the last-inserted record. See [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md) for details on creating this UDF if required.

## Examples

```sql
SELECT last_insert_grn_id();
+----------------------+
| last_insert_grn_id() |
+----------------------+
|                    3 |
+----------------------+
```

## See Also

* [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
