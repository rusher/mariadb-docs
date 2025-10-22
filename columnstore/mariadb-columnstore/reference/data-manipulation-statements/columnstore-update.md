# ColumnStore UPDATE

The `UPDATE` statement changes data stored in rows.

## Syntax

### Single-Table Syntax

```sql
UPDATE  table_reference 
  SET col1={expr1|DEFAULT} [,col2={expr2|DEFAULT}] ...
  [WHERE where_condition]
  [ORDER BY ...]
  [LIMIT row_count]
```

### Multiple-Table Syntax

```sql
UPDATE table_references
    SET col1={expr1|DEFAULT} [, col2={expr2|DEFAULT}] ...
    [WHERE where_condition]
```

{% hint style="info" %}
Only **one** table can be updated from the table list in `table_reference`.\
However, multiple columns can be updated.
{% endhint %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
